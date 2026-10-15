---
name: onset-did-robust
description: "Final consolidated empirical picture — first-collapse state failure raises foreign fishing PRESSURE (modest, effort) but NOT the dark/illegal margin"
metadata: 
  node_type: memory
  type: project
  originSessionId: 7a290715-e2f0-465e-aba3-b3f1b178e8dc
---

Consolidated 2026-06-14 after: fixing the [[war-variable-corrupted]] treatment, a long-panel buffer grid, a directly-observed GFW month+year + SAR workflow, and 3 adversarial verifiers (all numbers reproduced to the digit). Reports: `quality_reports/onset_verification_2026-06-14.md` + its UPDATEs; `quality_reports/onset_buffer_grid_2026-06-14.csv`. Scripts: pitf_statefailure_onset.py, onset_buffer_grid.py, onset_disentangle.py, staggered_did_corrected.py.

**EFFORT (pressure) — holds, but narrow.** With the CORRECT genuine-PITF state-failure onset, a state's FIRST-EVER descent into state-failure war raises total foreign fishing effort (Watson): CS = +0.206** at W0=1982 (clean pretrend 0.48); +0.155 ns at 1990 (borderline pretrend). The GFW monthly within-host event-study echoes it: delayed +0.37 (p=0.069), emerging ~9 months post-onset. It is FIRST-COLLAPSE-specific: the peace-buffer "any-onset" estimand (which counts recidivist re-onsets) is null (the ~20 recidivists average to ~0). Disentangle (onset_disentangle.py) proved it's the estimand, not last_treat or the buffer mechanics. Intensive (hours) margin; entry null. Annual GFW panel is null (underpowered, failing pretrends). So: a modest, first-collapse PRESSURE effect, post-UNCLOS.

**DARK / ILLEGAL margin — robustly NULL across every data system.** Watson dark effort negative everywhere; SAU unreported insignificant (one weak 1990 window only); GFW undocumented effort = pre-trend failure (elevated BEFORE onset, no break); GFW going-dark/AIS-disabling = precise null (17k events, tight SEs, OLS+Poisson+coastal/inland); SAR dark-fishing = scale artifact only (dies in share/PPML; total detections also rise). The originally-assumed "weak state -> illegal/dark fishing" channel is NOT in the data.

**1970 pre-UNCLOS placebo:** consistent with the EEZ mechanism but UNDERPOWERED, not discriminating (every buffer window is null, so no pre/post contrast). Do not present as affirmative support. (Earlier I over-stated it as a clean placebo — retracted.)

**Paper implication.** Lead with "conflict -> foreign fishing PRESSURE" (first-collapse, modest), and report the dark/illegal margin as a TESTED-AND-NULL question -- itself a contribution given the field assumes the opposite, and it is tested directly against Sentinel-1 dark-vessel detections + AIS-disabling. This sharpens [[disentangle-findings]]: the SAR dark-vessel pull does NOT rescue an illegality claim. Open: promote pitf_sf_onset + the first-ever-onset spec into staggered_did.py; consider a state-failure-only recode robustness; theory motivation for the first-collapse asymmetry.
