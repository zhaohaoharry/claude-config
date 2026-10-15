---
name: data-v2-suffix-is-experimental-not-canonical
description: The _v2 suffix on DATA files (mle_sample_v2, district_water_cost_v2) is an EXPERIMENTAL variant, NOT canonical and NOT the manuscript v1/v2 distinction; production uses the non-suffixed panels
metadata:
  type: project
---

**Use the non-suffixed data panels.** The canonical production inputs are `data/clean/mle_sample.dta` and `data/clean/district_water_cost.dta` (NO `_v2`). Every real estimation step reads these: A10 panel build, Stage 1.5 allocation (B1d_step1p5), CCP/Euler estimation (B1d_step2/3/4), B0 calibrations, B4 counterfactuals. Verified 2026-06-16 by grepping the pipeline.

**The `_v2` data files are one-off sandbox experiments, NOT canonical:**
- `mle_sample_v2.dta` = `mle_sample.dta` with the water-cost regressor `AC_kt` swapped for `AC_farmer` (farmer-side vs district-side cost concept); built by `B1h_lp_ac_reestimation.py`. `crop_cat`/`year`/`dot_id` are BYTE-IDENTICAL to canonical (0 mismatches / 1,078,001 rows) — only the cost column differs.
- `district_water_cost_v2.dta` = `AC_kt` recomputed under a revised Kern River allocation (`apply_kr_v2_propagate.py`); this also shifts `SW_KR`/`SW_total` in 77 of 632 district-years (its `dtw_ft` is also corrupted, max 1086 ft vs canonical 580).

**This is NOT the manuscript v1-vs-v2 distinction.** Manuscript v1/v2 differ in welfare-calculation method (a writeup-level choice); the user's current choice is v1. The data `_v2` suffix is a data-build experiment (alt price concept / KR build). Faint cousin only: HANDOFF flags an open "MC-vs-AC price concept" decision and AC_farmer explores it — but the suffix ≠ the manuscript number.

**Correction applied 2026-06-16:** Figure 2 (`draw_fig_sf1_v2.py`) and the 2017-fill robustness (`robustness_2017_fill.py`) had been built on the `_v2` panels by mistake. Re-pointed both to canonical. Consequences: SW decline 42%→**40%**, manuscript prose updated; summary table `tab_sumstats_district.tex` Panel B SW rows refreshed (Total SW max 915→988, sd 79→81; Kern River max 901→974, sd 67→70; means unchanged 58/21/18/20). Robustness composition UNCHANGED (crop_cat identical). See [[fig2_perennial_water_2017_artifact]].
