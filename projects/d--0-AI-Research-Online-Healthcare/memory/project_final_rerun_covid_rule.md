---
name: project-final-rerun-covid-rule
description: The final full rerun must use the no-label-drop COVID rule (HDF_COVID_RULE=none) plus a June-December robustness column
metadata:
  node_type: memory
  type: project
  originSessionId: 8e8d7e67-cb4d-47e2-8455-bc143574e324
  modified: 2026-10-22T07:37:02.242Z
---

On 2026-10-22 the user decided that the final rerun (done once, after all checks, before the bootstrap) uses `HDF_COVID_RULE=none`: keep all disease labels instead of dropping pneumonia/cough/fever before May 2020. Add a June-December robustness column (`HDF_COVID_RULE=jun_dec`). Also (2026-10-23, decision D7) set `HDF_W_MENU=quality` as the default so the offline value W_od uses doctor quality only, without online format effects and prices.

**Why:** Haodf relabelled diseases at the end of May 2020, so the old rule selected by label inconsistently over time; estimates barely change (second decimal).

**How to apply:** Before the final rerun, follow the "Pending final rerun" checklist in quality_reports/plans/2026-10-20_online_estimation_rebuild.md (change the config default, run the whole pipeline, never rerun s12 alone on a changed sample). Bootstrap stays deferred until the user reviews the rerun ([[feedback-report-only-what-serves-argument]] for how results are written up).
