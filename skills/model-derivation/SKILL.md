---
name: model-derivation
description: Derive and verify an economic model's results step by step — first-order conditions, equilibrium characterization, closed forms, comparative statics and their signs — with every non-trivial step checked by units, limiting cases and a numeric or symbolic computation in Python, and the key steps re-derived blind by a fresh subagent that sees only the model setup. Use when solving a model, checking a derivation in a draft or appendix, or signing a comparative static before it goes into a paper. Pairs with theory-model, which decides whether a model is needed and what result it must deliver; this skill derives and verifies it. Not for choosing an estimator (econometrics-playbook) or verifying code (verify-code).
argument-hint: "[model description, or path to a .tex/.pdf containing the model or derivation] [--verify for an existing derivation]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "Agent"]
---

# model-derivation — derive every step, check every step that can be wrong

Adapted from `solving-model` in amatray/claude-skills-public (MIT) and the comprehension gate in
StatsClaw (Qin and Xu 2026). Their external GPT "oracle" is replaced by a fresh Claude subagent, so
no outside subscription is needed and nothing leaves the machine. The checkpoint after every phase
is dropped: the skill runs through and stops only when a check fails or a substantive modeling
choice is the user's to make.

**Input:** a verbal model, a `.tex`/`.pdf` with the model, or (`--verify`) an existing derivation.
Work in the project's `latex\answers\derivation_<name>\` (create it), so the result compiles under
the math-compilation rule and never reaches the manuscript unasked. Back up any file before
overwriting it (`.bak`).

## Phase 1 — Setup and comprehension

1. Write `model_setup.tex` (a fragment, no preamble): environment in prose; timing if dynamic;
   agents, preferences, technology, constraints, market structure, information, equilibrium
   concept; numbered assumptions (`\paragraph{Assumption A1}`, no trailing period); every
   optimization problem in a labelled `align`. Elements the source leaves open get the canonical
   choice from the literature, stated as an assumption with its source, never silently.
2. Write `comprehension.md`: the target result restated in one sentence without notation; every
   symbol with type, domain and the equation that first uses it; assumptions the source relies on
   without stating; the economic intuition for why the target result should hold; any choice the
   source does not settle. If a choice would change the result, ask the user with concrete options.
   Otherwise state it as an assumption and continue.
3. Notation audit: no letter carries two meanings; every symbol is introduced in the paragraph of
   the equation that first uses it (Personal guide 3.1b).

## Phase 2 — Derivation

Write `derivation.tex`, one algebraic operation per step:

```latex
\paragraph{Step 4: Substitute $\lambda$ from Step 3 into the capital FOC} % VERIFY
\textit{Operation:} replace $\lambda$ in \eqref{eq:foc_k} using \eqref{eq:foc_b}.
\begin{align}
  ... \label{eq:step4}
\end{align}
```

- Every substitution names its source step. Substeps (4a, 4b) for anything longer than one line.
- Never "it can be shown", "clearly", "obviously", "trivially", "by inspection", "straightforward
  algebra yields", "it follows that". Writing one of these is the signal to split the step.
- Flag `% VERIFY` on: sign or inequality claims; simplifications beyond collecting terms; the
  envelope theorem, implicit function theorem, Leibniz rule, Kuhn-Tucker; concavity, existence
  and uniqueness; limits; any case split (binding vs slack constraint).
- If the derivation needs an assumption the setup lacks (a missing non-negativity constraint, a
  missing market-clearing condition), amend `model_setup.tex` and say so in the report.

## Phase 3 — Verification

Follow `references/verification-protocol.md`. For every `% VERIFY` step run three local checks:

- **A. Units:** both sides carry the same units or the same homogeneity degree.
- **B. Limiting cases:** the result behaves as economic logic requires at boundary values
  (constraint slack, friction to zero, elasticity to one or infinity, one agent type).
- **C. Computation, in Python, never in-context arithmetic:** a SymPy check of the step
  (`simplify(lhs - rhs) == 0`, a derivative, a solve), and a numeric spot-check at two or three
  parameter vectors drawn from the protocol's tables, with endogenous variables solved
  consistently first.

Then the **blind re-derivation**: dispatch a fresh subagent with `model_setup.tex` and a list of at
most five claims ("starting from A1-A3, the FOC for k is ..."), and **never** `derivation.tex`. It
derives each claim from first principles and returns AGREE, DISAGREE (with the divergence step and
both paths), or AGREE WITH IMPLICIT ASSUMPTIONS. Pick the claims that carry the paper: the
equilibrium condition, the key closed form, and every sign that will be reported. Several batches
are fine.

**Halt rule:** any failed check or DISAGREE stops the run. Present the step, the failing check and
both derivations side by side, find which is wrong (re-run SymPy on the disputed step), correct
`derivation.tex`, and re-run all checks on the corrected step and every step that uses it.

Write `verification_log.tex`: one row per flagged step with Units | Limits | SymPy | Numeric |
Blind re-derivation (`NOT SELECTED` where not sent), and the overall verdict.

## Phase 4 — Comparative statics

For each parameter-outcome pair the paper needs: differentiate (implicit function theorem or
directly), show every step, state the sign and the condition under which it holds, and give the
mechanism in one sentence whose subject is the economic cause, not the equation. Verify each sign
with SymPy and on a numeric grid of parameter values, and send the signs to the blind subagent with
the equilibrium conditions. A sign that depends on parameters is reported as conditional with the
sufficient condition, never forced. Summary table in `comparative_statics.tex` (booktabs; caption
above, notes below in a `\parbox{\linewidth}{\footnotesize\textit{Notes:} ...}`).

## Phase 5 — Assemble and compile

`full_model.tex` (`\documentclass{article}`, amsmath, amssymb, amsthm, booktabs) inputs the four
fragments plus an appendix with the parameter values used in the numeric checks and a log of each
blind re-derivation batch (claims sent, verdicts). The SymPy and numeric scripts are saved next to
it (`checks.py`) so every check can be re-run. Compile with `pdflatex` in that folder and fix
errors.

## Report

Give the PDF path, the number of steps and flagged steps, which checks ran and passed, every halt
and how it was resolved, the comparative statics with their conditions, and any step still
unverified. Hand off: `theory-model` (if the result does not match the estimate the paper needs),
`econ-craft` (to write the model section, intuition before notation), `verify-code` (if the model
is then solved or estimated numerically).

## Important

- A sign that has not passed SymPy, the numeric grid and the blind re-derivation is reported as
  unverified, never as a result.
- The blind subagent never sees the derivation, the conversation, or the answer you expect.
- Do not invent mechanisms or assumptions to make a sign come out; report the conflict instead.
- Nothing from this folder goes into a manuscript unless the user asks; when it does, the
  manuscript track-changes rule applies.
