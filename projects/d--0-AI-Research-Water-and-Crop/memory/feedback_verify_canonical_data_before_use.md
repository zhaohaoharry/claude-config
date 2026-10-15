---
name: feedback-verify-canonical-data-before-use
description: Before using a data/results file, verify it is the CANONICAL one the production pipeline reads; never infer canonical-ness from a filename suffix (_v2/_final/_new) or newest mtime
metadata:
  node_type: memory
  type: feedback
---

Before reaching for any data or results file, confirm it is the canonical input the production pipeline actually consumes. Do NOT infer canonical-ness from the filename (a `_v2`/`_final`/`_new` suffix) or from the newest modification time.

**Why:** In research repos, experimental forks sit right next to production files with confident-sounding suffixes. On Water and Crop the `_v2` data panels (`mle_sample_v2.dta`, `district_water_cost_v2.dta`) were one-off experiments, while the canonical files the estimation reads have NO suffix and were actually newer. I used `_v2` by habit for Figure 2 and a robustness check and had to redo them (SW decline 42%→40%, summary-table SW rows refreshed). The "newer/`_v2` = better" heuristic was exactly backwards.

**How to apply:** (1) Check the project's data manifest first — on Water and Crop that is `HANDOFF.json` `data.clean`, which lists the canonical files. (2) Or grep the production scripts for which file they `read_stata`/`read_csv`. (3) Only then use it. One cheap verification beats a whole session of downstream rework. Project-specific facts: [[data_v2_suffix_is_experimental_not_canonical]]. Applies across all research projects.
