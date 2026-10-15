---
name: no-redundant-work
description: User dislikes redundant computation/work — reuse results already produced instead of recomputing
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 50884341-1a39-409e-91a0-02b4e86a8c41
---

When a long job is already running or results already exist, do NOT re-run or recompute things already in hand (e.g., re-estimating climate measures whose numbers are already saved). Reuse existing outputs; only compute what is genuinely missing.

**Why:** The user flagged that `stage1_results.do` was re-running the 7-BIO and annual-profile confounders-only specs I already had from `stage0e` — wasted hours on a 2-core Stata license.

**How to apply:** Before launching estimation/builds, check which outputs already exist and scope the job to only the missing pieces. While a program waits, do other useful work (e.g., manuscript) rather than duplicate runs. See [[climate-similarity-supplier-choice-project]].
