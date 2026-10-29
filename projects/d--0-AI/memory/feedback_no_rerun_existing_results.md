---
name: feedback-no-rerun-existing-results
description: "Before launching any estimation, check which specifications already have results and run only the missing ones; never rerun a spec as a \"check\""
metadata:
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-10-29T04:02:29.301Z
---

Before launching any estimation run, check whether the results for each specification already exist (stats folders, pooled csv) and queue only the specifications not yet run. Do not rerun an existing specification as a validation step. Validate a new engine on one partner block against the stored moments instead.

**Why:** On 2026-10-29 (Carbon Pricing Policy) I queued full-sample TWFE again inside a chain of robust estimators, even though `fix6/enact_eu` already held that exact path. The user objected to repeated runs.

**How to apply:** Before each launch, list the target specs and compare them against the existing output folders. Drop the ones that are done, and say which ones were skipped. A one-block moment comparison is the check; a full rerun is not. Related: [[feedback-fast-country-level-batteries]].
