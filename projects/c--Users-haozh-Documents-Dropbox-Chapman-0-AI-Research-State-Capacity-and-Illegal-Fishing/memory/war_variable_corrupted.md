---
name: war-variable-corrupted
description: "The `war` column in top5_analysis_panel.dta is a CORRUPTED conflict-participation measure, NOT PITF state failure; use data/clean/pitf_sf_onset_hostyear.csv instead"
metadata: 
  node_type: memory
  type: project
  originSessionId: 7a290715-e2f0-465e-aba3-b3f1b178e8dc
---

Discovered 2026-06-14. The `war` column in `data/clean/top5_analysis_panel.dta` -- used as the "PITF war" treatment in EVERY staggered-DiD script (pitf_onset in staggered_did.py, did_core.py, effort_motivation.py, etc.) -- is NOT the PITF State Failure measure the docs claim. It is a conflict-PARTICIPATION variable: it flags USA/GBR/FRA/AUS/ITA/ESP/NLD as war==1 in identical Vietnam (1965-75), Gulf (1991), and ISIS (2013-18) years (interstate/coalition involvement), and it MISSES domestic failures (Rwanda = 0 war-years despite the 1994 genocide).

The GENUINE PITF State Failure data is clean and on disk: `data/clean/pitf_all_iso.dta` (built by program/sandbox/clean_war.do from the 4 PITF Problem Set files: ethnic + revolutionary + adverse-regime-change + genocide/politicide). It correctly EXCLUDES USA/AUS/ITA/ESP and INCLUDES RWA 1990+, GBR 1971-82 (N.Ireland), etc. clean_fishing.do builds a clean `conflict` var from it (in eez_conflict.dta) -- but the separate top5 pipeline merged a different, wrong `war` column into the analysis panel.

Fix applied: rebuilt the correct onset from pitf_all_iso.dta -> `data/clean/pitf_sf_onset_hostyear.csv` (cols host_iso3, year, inc_sf, onset_sf; 81 hosts ever, 142 onsets). program/sandbox/pitf_statefailure_onset.py does the rebuild + headline re-run.

Consequence: any result keyed on the panel `war` column (incl. the +0.196** headline) used the wrong treatment. With the CORRECT measure the first-ever-onset effort effect survives (+0.206** at W0=1982, clean pretrend; +0.155 ns at 1990) -- see [[onset-did-robust]] -- but it is first-collapse-specific and the dark/illegal margin stays null [[dark-margin-null]]. ACTION: promote pitf_sf_onset into the analysis pipeline and stop using panel `war`.
