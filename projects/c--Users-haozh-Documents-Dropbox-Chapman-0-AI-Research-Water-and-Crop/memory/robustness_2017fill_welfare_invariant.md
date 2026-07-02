---
name: robustness-2017fill-welfare-invariant
description: The 2017 permit-aware fill, run end-to-end through an ISOLATED pipeline to the 3x3 welfare matrix, leaves the welfare matrix unchanged except AC_mean of the 3 bilateral-trade cells
metadata:
  type: project
---

Robustness check done 2026-06-16 (user request, fully isolated, production untouched). Repaired the
spurious 2017 land-use-vintage fallow gap with a permit-aware carry-forward fill and re-ran the WHOLE
pipeline (dot_panel + crop_plot_owner_WD → A5 → Stage 1.5 → A10 → CCP → Euler → OLS → B0 → B4 two-task).

**Result: the 3×3 welfare matrix is invariant to the fill.** Across all 9 cells × ~30 fields the ONLY
changes are `AC_mean` (mean realized water cost) of the three bilateral-trade cells: baseline_open
78.40→81.71, baseline_tax 110.61→112.68, baseline_cap 82.06→82.62 $/AF. Everything else is bit-identical:
baseline GW 30.867 MAF, ΔW at every σ, ΔGW, taus (40.9/102.7/104.8), caps (4.7/16.6/9.0%), crossover σ
(888/1279/555/474), crop-acreage shifts.

**Why:** B4 forward-simulates crop choice from the 1998 anchor (never ingests observed 2017 crops). The
fill's routes into B4 — β_W 0.0011815→0.0011830 (0.13%; VERIFIED loaded by isolated load_all, no leak) and
a one-year cost-panel change — don't move the supply-constrained equilibrium FS/GW. Only the diagnostic
AC_mean (direct read of the filled cost panel) rises with the +157k AF 2017 demand.

**Upstream the fill DID change things:** Channel B 876 bracketed permits → +61,201 acres → A5 2017 demand
+157,316 AF → Stage 1.5 2017 GW pump +137,312 AF. Channel A 214 strict-same-permit dots (2017 fallow
29.04→28.65% in mle_sample). Conservative literal "same permit" (PMT_SITE 2016==2018) fills ~29% of the
2017 demand gap; a looser "same-field" reading (fixed 300m dot bracketed by crops) would fill more — NOT
yet run. PMT_SITE embeds year/crop coding for ~34% of dots, so literal equality undercounts.

Isolated artifacts under `data/temp/robustness_2017fill/`, `results/robustness_2017fill/`,
`latex/robustness_2017fill/`; runners `program/sandbox/robustness_2017fill/00-09_*.py`; results writeup
`quality_reports/2026-06-16_2017fill_isolated_rerun_results.md`. Related: [[fig2_perennial_water_2017_artifact]],
[[data_v2_suffix_is_experimental_not_canonical]], [[settled_cf_rules]].
