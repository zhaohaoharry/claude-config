---
name: project_final_rerun_covid_rule
description: Final rerun done 2026-10-25 with HDF_COVID_RULE=none and HDF_W_MENU=quality as defaults; June-Dec robustness variant
metadata:
  node_type: memory
  type: project
  originSessionId: 8e8d7e67-cb4d-47e2-8455-bc143574e324
  modified: 2026-10-24T20:02:56.730Z
---

The final rerun was done on 2026-10-24/25 with the specification the user set: all disease labels kept (config default
COVID_RULE="none", because Haodf relabelled diseases at the end of May 2020), June–December consultations as a robustness
variant (data/variants/covid_jundec), and the offline value W_od from doctor quality only (W_MENU="quality").

**Why:** the user asked that any rerun use this specification; label-based dropping selected different patients before and after the relabelling.

**How to apply:** do not switch the defaults back. Still open after the rerun: facility controls need province totals of beds and
physicians (county-yearbook data are wrong for municipalities), and no bootstrap until the user reviews. Details in the plan
quality_reports/plans/2026-10-20_online_estimation_rebuild.md. Related: [[feedback_report_only_what_serves_argument]].
