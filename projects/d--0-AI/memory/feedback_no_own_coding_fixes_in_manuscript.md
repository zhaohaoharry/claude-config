---
name: feedback-no-own-coding-fixes-in-manuscript
description: Never describe fixes to our own code or mapping in a manuscript; fold them into the build so the code is right in one pass
metadata:
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-11-18T01:57:25.832Z
---

A manuscript never mentions correcting our own coding or mapping errors (said by the user 2026-11-11, Carbon Pricing
Policy, about the keyword-table fixes to coverage: "we should never mention fixing our own coding error, that is stupid").
Only corrections to the source data are reported, in the form "we cross-check X reported by [source] against [document]
and resolve the ambiguities; Appendix Y reports them".

Also no before-and-after comparisons for source-data corrections (same day): the paper states each correction and its
source, and never reports the uncorrected numbers or estimates, nor argues that results are unchanged. The user: a
correction is justified because it is the right step, not because the result does not change. Do not propose or run
re-estimations on the uncorrected data for the paper.

This covers response letters too (2026-11-18, after I added a letter bullet explaining the counterfactual coverage
fix): a change we make ourselves in the code is not explained anywhere, neither in the paper nor in the letter, unless
someone finds the issue and asks; then we answer that inquiry only. "We don't answer to ourselves."

**Why:** the code is supposed to be right; a paper that narrates its own bug fixes looks careless and the reader learns
nothing from it.

**How to apply:** before writing a "correction" into a paper, check whether the defect is in the source or in our own
build (who wrote the table or mapping that was wrong). If ours, delete every mention (text, appendix table, counts) and
restructure the code so one builder produces the right result directly, instead of a wrong file plus a patch script
(the user: "that is weird"). Verify the one-pass build reproduces the patched output cell by cell before switching
readers. Related: [[feedback_no_footprints_of_abandoned_designs]], [[feedback_no_process_narration]].
