---
name: verify-code
description: Independently verify research code that implements a method — a custom estimator, a GMM/SMM objective, a structural model solver, a simulation, a bootstrap, or a data pipeline whose numbers reach a paper. Separates the code from its validation with information barriers (adapted from StatsClaw, Qin and Xu 2026): a planner writes isolated implementation, test and simulation specs, a tester that never sees the code checks known-truth cases at fixed tolerances, a simulator designs the data-generating process from theory alone, and a reviewer audits tolerance integrity and convergence. Use before trusting AI-written code for results, after porting code between languages, or when a referee-facing number comes from custom code. Not for packaged commands with standard diagnostics (that is econometrics-playbook) or for derivations on paper (that is model-derivation).
argument-hint: "[path to the code, plus the method source: paper PDF, derivation .tex, or a one-line description]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "Agent"]
---

# verify-code — the code that produces a number must not be the code that checks it

Adapted from StatsClaw (Tianzhu Qin and Yiqing Xu, arXiv 2604.04871, MIT licence,
github.com/statsclaw/statsclaw). Its central rule: **the process that generates code must never be
the same process that validates it.** In their interflex Python port, an independent review found
six bugs in code that already passed every test, two of them silent (a bootstrap branch that quietly
returned delta-method standard errors, and an HC1 sandwich with wrong operator precedence). Tests
written by the agent that wrote the code test what that agent understood, so they share its
misreadings.

**Input:** `$ARGUMENTS` — the code (existing, or to be written) and the source that defines what it
should do. Work in `program\sandbox\verify_<name>\` unless the user names another location. All
artifacts below are written there; keep them, they are the audit trail.

## Roles and what each may see

| Role | Who | Sees | Never sees |
|---|---|---|---|
| Planner | you, the main session | everything: the method source, the code, the data layout | — |
| Builder | subagent (only when code must be written or fixed) | `spec.md` | `test-spec.md`, `sim-spec.md` |
| Tester | fresh subagent | `test-spec.md`, the code's public interface (how to call it) | `spec.md`, `sim-spec.md`, the code's source |
| Simulator | fresh subagent (estimators only) | `sim-spec.md`, the call interface | `spec.md`, `test-spec.md`, the source |
| Reviewer | fresh subagent | all artifacts and the code | — |

Isolation is enforced by what each subagent prompt contains: paste in only that role's spec and
the interface, never paths to the other specs, never the conversation, never your account of what
the code is meant to do. Tell the tester and simulator explicitly not to open the source files. A
subagent that writes code gets `isolation: "worktree"` when the project is a git repository.

## Steps

1. **Comprehension record (gate).** Before any spec, write `comprehension.md` answering in
   writing:
   1. The requirement restated in one paragraph without looking at the source.
   2. Every formula written out from memory with each term explained, then compared with the
      source; discrepancies listed.
   3. Symbols, terms or concepts that cannot be defined precisely.
   4. Steps that would need a judgment call the source does not support.
   5. Why the method works: the statistical or economic intuition.
   6. Assumptions the source relies on without stating them.

   Verdict: `FULLY UNDERSTOOD`, `UNDERSTOOD WITH ASSUMPTIONS` (each assumption listed), or
   `UNSPECIFIABLE`. Resolve what the source, the project files and the conversation can resolve.
   Ask the user only about a gap that would change the code, with concrete options ("HC1, HC2 or
   clustered by firm?"), at most three rounds. Do not proceed on `UNSPECIFIABLE`.

2. **Write the isolated specs.** Each must be sufficient on its own.
   - `spec.md` (builder): notation, numbered algorithm steps, input validation, output contract,
     numerical constraints. No test cases, no expected outputs.
   - `test-spec.md` (tester): behavioral contract; scenarios with exact inputs or seeded
     generators, expected values or properties, and a **fixed tolerance for every numerical
     comparison**; edge cases (singular, collinear, empty, one cluster, all-missing column);
     invariants (symmetry, scale equivariance, known closed forms); benchmarks (a packaged
     command, a published table, an analytic special case). For any data pipeline it also states
     the expected N at each stage and the coverage of each key variable, derived from the raw files
     and the sample definition, so the tester can rebuild them independently
     (`~/.claude/rules/data-integrity.md`). No algorithm steps, no internal function names.
   - `sim-spec.md` (simulator, estimators only): the DGP with true parameter values, error and
     covariate distributions, the scenario grid (sample sizes at least N = 200, 1,000, 5,000),
     replications per cell, metrics, acceptance criteria, and the seed rule. The estimator appears
     only as a call interface. Long grids go to ScalableComputing (`~/.claude/rules/scalable-computing.md`).
   - Cross-check before dispatch: every contract in `test-spec.md` maps to a step in `spec.md`;
     nothing from one spec leaked into another.

3. **Build or freeze the code.** If code must be written or fixed, dispatch the builder with
   `spec.md` only. If it exists, record its git commit or file hashes in `comprehension.md` so the
   tested version is unambiguous.

4. **Test and simulate in parallel.** Dispatch the tester and (for estimators) the simulator in one
   message, each with its spec and the interface only. Each writes and runs its own harness in
   `verify_<name>\tester\` or `verify_<name>\simulator\` and returns:
   - Tester: `audit.md` with a per-test result table (one row per metric per scenario: expected,
     actual, tolerance used, pass/fail) and the exact commands run with their output.
   - Simulator: `simulation.md` with the metrics table — bias and its Monte Carlo standard error,
     RMSE and its log-log slope in N, coverage of nominal 95% intervals, the ratio of mean reported
     SE to the empirical SD, rejection rate under the null, and the failure rate.

5. **Review.** Dispatch the reviewer with every artifact and the code. It checks, and issues
   `PASS`, `PASS WITH NOTE` or `STOP` with the step and the role to route back to:
   - **Isolation:** no artifact of one pipeline cites another's spec; the tester's harness does
     not import internals.
   - **Convergence:** both pipelines agree. Flag false confidence: code and tests passing under
     different readings of the method. Complete overlap between the builder's own unit tests and
     the tester's scenarios signals an isolation breach; zero overlap signals a spec gap.
   - **Tolerance integrity (never skipped):** every tolerance in `audit.md` equals the one in
     `test-spec.md`. Any widening is a STOP. So are assertions removed or commented out, failures
     swallowed by `try`/`except` or Stata `capture` without a return-code check, fewer replications
     or a smaller N than specified, seeds changed without a stated reason, and scenarios silently
     absent from the audit.
   - **Simulation against theory:** bias shrinks toward zero as N grows, RMSE falls at roughly
     the √N rate, coverage approaches 95%, the SE ratio approaches 1. Coverage landing exactly on
     nominal in every cell, or passes that only barely clear a threshold, are investigated rather
     than accepted.
   - **Coverage of the code:** every changed function has a correctness assertion, not only a
     "runs without error" check.
   - **Before/after table:** for a change to existing code, a table of the key outputs before and
     after, with any change explained.

6. **Fix and re-run.** On STOP, route to the named role, fix, and re-run the affected pipeline and
   the review. At most three rounds per problem, then report to the user what still fails and why.

7. **Report.** Save `verify_<name>\review.md` and give the user: the verdict, the bugs found (with
   the scenario that caught each), the tolerance table, the simulation table, and anything still
   unverified. Every number quoted comes from a harness that ran.

## Lightweight mode

For a short function or a one-off script, steps 1, 2 and 5 may be collapsed into one comprehension
record, one test spec and one reviewer pass, and the simulator skipped. The tester stays isolated
from the source in every mode; that separation is the point of the skill.

## Important

- **The planner never grades its own work.** You may write specs and dispatch; the verdict comes
  from the reviewer subagent, which receives the artifacts and not your summary of them.
- **Tolerances are fixed before anyone runs anything** and never loosened afterwards. A test that
  only passes at a wider tolerance is a failing test.
- **Verification is empirical, not a proof.** A misunderstanding shared by all specs passes all
  pipelines; this is why the comprehension record is the step to read closely. Say so in the
  report when the method source was thin.
- **Never present unrun checks as passed.** If a harness could not run (missing package, no data,
  no licence), report the check as not run.
- **Raw data stays in place** (`D:\0. Research Data\`, referenced by path); harnesses write only to
  the `verify_<name>\` folder.
- Provenance: a result that passed review still enters the paper only through its generator script
  and `PIPELINE.md`; `review.md` is evidence about that script, not a substitute for it.
