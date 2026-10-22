---
name: feedback-python-not-stata-climate
description: "Climate-similarity project uses Python (Julia for big FE fits) only; no Stata unless necessary; coauthors' Stata build is not our concern"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 03df82b9-8604-41cb-84b9-cc17e167531a
  modified: 2026-10-21T02:13:29.182Z
---

Climate similarity and supplier choice project (2026-10-21): use Python only from now on (Julia where the
high-dimensional FE estimation already runs); Stata only when genuinely necessary. Do not maintain or patch the
coauthors' Stata build.

**Why:** the user said "we dont use stata from now (only use python unless stata is necessary)" and "dont worry about coauthor".

**How to apply:** write new data steps and diagnostics in Python; don't list coauthor/Stata-build fixes as next steps.
Related: [[stata-per-machine]].
