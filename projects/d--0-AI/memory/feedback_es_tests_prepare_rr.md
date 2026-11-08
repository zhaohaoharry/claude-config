---
name: feedback-es-tests-prepare-rr
description: Every event-study test run must save the ES covariance and produce Rambachan-Roth (HonestDiD) breakdown values alongside the ES figure
metadata:
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-11-08T01:19:32.930Z
---

When running any event-study test (design variants, coverage lists, data fixes), always prepare the Rambachan-Roth bounds: save the event-study covariance (coef + vcov files that `program/R/honestdid_window.R` reads) and report the RM breakdown M̄ (npre 1, 3, 6) next to the ES figure and pre-trend p-values.

**Why:** On 2026-11-08 the user asked "what are their rr values" after the coverage test, and the runs had not saved the covariance, so it had to be rebuilt from block moments afterwards. "Yes when testing always prepare for rr."

**How to apply:** Build the vcov export into the test runner (Carbon Pricing: `coverage_test_20261107/export_vcov_covtest.py` pattern), run HonestDiD as part of the test, and include RR breakdowns in the result table. Related: [[feedback_always_show_es_figures]].
