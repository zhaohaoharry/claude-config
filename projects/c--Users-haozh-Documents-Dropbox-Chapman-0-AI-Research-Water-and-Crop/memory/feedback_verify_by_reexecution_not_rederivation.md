---
name: feedback_verify_by_reexecution_not_rederivation
description: "To check whether a computed number is correct, RE-RUN its generating program and diff — never hand-derive it and call a mismatch \"wrong\". Provenance gap ≠ correctness error; \"I can't reproduce it\" ≠ \"it is wrong\"."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

How to verify any number in a paper, and the failure mode to never repeat. Worked example: on 2026-06-18 I wrongly declared `tab_cf_iv.tex` "unverifiable / traces to nothing / possibly wrong" and raised it as a second integrity problem. The numbers were CORRECT. I had hand-reconstructed them from an intermediate JSON with my own formula (omitting the `entropy/|β_W|` term), got the wrong answer, and trusted my reconstruction over the artifact. Running the real generator `program/sandbox/T1p3_iv_welfare_matrix.py` reproduced every cell exactly.

**The rule: verify by RE-EXECUTION, not RE-DERIVATION.**
- To check a computed number, find and RUN the program that produces it, then diff its output against the artifact. That is the only basis for saying "correct" or "stale/wrong".
- NEVER hand-re-derive a result from intermediate files and declare the artifact wrong because your derivation disagrees. A mismatch has three causes — (a) the artifact is stale, (b) the data changed, (c) YOUR derivation is wrong — and (c) is usually the most likely, because the computation lives in a program precisely because it is not trivial to redo from memory.

**Separate provenance from correctness — they are independent questions.**
- Provenance: "Does a saved generator write this artifact?" Answered by `program/audit_provenance.py`. A "no" is a real gap to fix.
- Correctness: "Is the number right?" Answered only by running the generator. A number can FAIL provenance (hand-transcribed) yet be perfectly correct. Do not let an orphan flag contaminate the correctness judgment.

**Three claim-states, never collapsed:**
1. "No saved generator found" — a provenance fact (audit output).
2. "I have not located/run the generator" — uncertainty about MY search, NOT about the artifact. Default here when unsure.
3. "Re-ran program X; output matches / does not match" — the ONLY basis for a correctness verdict.
Before escalating "this number is wrong" or "integrity problem", state 3 must hold (an actual run showing the mismatch). Alarming claims need a HIGHER evidence bar, not a lower one.

**Mandatory search before concluding "can't verify":** grep programs that WRITE the artifact; if none, grep programs that READ its source/result file (the consumer); search session transcripts for how it was produced. Only after these come up empty is the status "provenance UNLOCATED" — and that is a gap to fix, never a numeric-error claim.

**Guard against anchoring:** a prior finding (e.g. one table was genuinely wrong) is not evidence about the next artifact. Treat each as independent and demand the same re-execution standard.

**Re-executing IN PLACE can destroy a correct artifact — back up or redirect first.** A generator can be STALE or WRONG (renamed inputs, changed format) so that re-running it OVERWRITES a committed artifact that was correct but no longer reproduced. Before re-running a generator that writes a committed `tables/`/`figures/` file to "verify" it, first copy the committed file aside (or redirect the generator's output to a scratch path) and DIFF, rather than letting it clobber the original. Worked failure (2026-06-19, Water and Crop): re-running `build_sf2_transition_matrices.py` to check Table 1's `N=240{,}432` overwrote the correct committed `sf2_transition_matrices.tex` with a wrong vintage (`N=124{,}503`, different format) because the script reads `crop_plot_all.dta` while the committed table came from `crop_plot_owner_WD.dta` via an older generator. Restored from the synced repo copy. Lesson is twofold: (a) protect the artifact before re-running; (b) a NAMED generator that does not REPRODUCE the artifact is an orphan-by-reproduction that `audit_provenance.py` misses — only re-execution catches it (logged in project `DECISIONS.md`).

This composes with [[feedback_every_number_has_provenance]]: once every number has a generator, verification is always just "re-run + diff", and the re-derivation temptation disappears. See [[project_table2_provenance_rebuild]] for the worked case.
