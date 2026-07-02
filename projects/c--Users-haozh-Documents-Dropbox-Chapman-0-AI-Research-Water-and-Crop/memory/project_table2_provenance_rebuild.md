---
name: project_table2_provenance_rebuild
description: Water-and-Crop Table 2 generator. 2026-06-23 — decoupled from the structural pkl, now built from plot_panel.dta (8-cat, drop KCWA); SW 73kAF / DTW 208ft corrected from stale 57k/220
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

2026-06-18 provenance work on the Water-and-Crop manuscript (`latex/manuscript_v1.tex`). Trigger: the summary-stats table (Table 2) was discovered to be **hand-built in a past session with no generator**, and stale — its Fallow row said 11,086 (25%) vs the estimation sample's true 8.7%. See the governing rule [[feedback_every_number_has_provenance]].

**Audit tool:** `program/audit_provenance.py` parses the manuscript for `\input{tables/...}` and `\includegraphics{figures/...}`, then greps `program/` for a script naming each artifact (base / full stem / leading stem before first dot). Reports ORPHANS (no generator). Result of first run: **23 of 24 artifacts mapped; 1 true orphan.**

**Table 2 — FIXED.** New generator `program/sandbox/build_tab_sumstats.py` reads ONLY canonical `results/B1d_ccp_firststage.pkl` (the frozen 22-district estimation sample, 230,339 decisions, 538 district-years) + `data/clean/district_sw_supply.dta` + `data/clean/district_water_cost.dta`. Both panels restricted to the same 538 estimation district-years. Key new numbers: Panel A 22 districts / 538 dy, Total plots 428, Total acreage 38,761, Fallow 3,387; Panel B SW 57 kAF (SWP 23/CVP 19/KR 16), depth-to-water 220 ft (N=440, 18 GW districts). Manuscript prose + tabnotes threaded to match (tracked): 58,000→57,000 AF, 217→220 ft. Note on fallow (RESOLVED 2026-06-18): Table 2's acreage-weighted Fallow = 8.7% is CORRECT — keep it. Earlier confusion (8.7% vs a "~25% land" or "~15% v2-panel" figure) is a sampling artifact, NOT a real difference and NOT an estimation drop. `create_sampling_dots.py` left-joins the union-of-ever-farmed dot grid to each year's permit polygons and labels any dot that overlays NO permit that year as fallow (lines 217-219). So ~25% of DOTS are "fallow", but 71% of those fallow dots carry null/0 acres (no permit that year) — verified: in mle_sample 71.0% of fallow dots have null/0 acres vs 0.0% of cropped dots. Acreage weighting (what Table 2 and the estimation use) gives those gap dots ~zero weight, leaving the genuine ~8.7% fallow on real permits. Do NOT report the 25% dot-count as "fallow land share" — it is a grid artifact. My earlier "drops plots without a lag" and "quarter of land idle" claims were both wrong (lags exist; the 25% is artifact). Lesson reinforces [[feedback_verify_by_reexecution_not_rederivation]].

**UPDATE 2026-06-23 — Table 2 DECOUPLED from the structural pkl.** Generator now lives at
`program/3_exhibits/build_tab_sumstats.py` (moved out of sandbox). Panel A no longer reads `B1d_ccp_firststage.pkl`;
it reads `data/clean/plot_panel.dta` directly (the reconstructed plot panel IS Panel A's crop data — the estimation
only adds water and drops the wholesale agency). Filters: drop **Kern County Water Agency** (wholesale, overlaps members);
verified `plot_panel` minus KCWA = the pkl's exact 538 (district,year) cells (0 diff). 8-cat now (CROP_LABELS Nuts/Tree
fruit/Grapes & berries/Cotton & field/Alfalfa & pasture/Grain/Vegetables/Fallow). New: 22 districts, 538 dy, 234,491
plot-decisions; Nuts largest (32.7%), perennials 54.9%. **Means CORRECTED** (the rebuilt D9 SW panel + PGWL water-cost
changed them; the prior 57k/220 were stale anticipatory numbers): SW deliveries **73 kAF** (SWP 38/CVP 19/KR 17), DTW
**208 ft** (N=440, 18 GW districts) — verified identical under both pkl-cells and plot-panel-cells. So Table 2 now
builds WITHOUT the structural rerun. Supersedes the "reads B1d_ccp_firststage.pkl / SW 57 / DTW 220" claims below.

**`tab_cf_iv.tex` — RESOLVED 2026-06-18.** The inclusive-value (logsum) welfare table (`tab:cf_iv`, appendix). The numbers were always CORRECT — my first-pass alarm was my own error: I reconstructed from `B4_two_task_results_iv.json` by hand and left out the `entropy/|β_W|` term, so I wrongly got +475/+1,605 instead of +1,843. The real computation lives in a dedicated program, **`program/sandbox/T1p3_iv_welfare_matrix.py`** (reads `results/B4_two_task_scens_iv.pkl`, computes `dW = ΔFS_det + entropy/|bW| − σ·ΔPump`). Running it reproduces all 9 cells EXACTLY (autarky-open 475 det + 1,368 entropy = 1,843) and both crossovers (autarky-vs-bilateral 888→564, autarky-vs-centralized 921→603 — all match the §sensitivity prose). The only real gap: the `.tex` had been hand-`Write`-n from the program's console output. FIX APPLIED: added a writer block to `T1p3_iv_welfare_matrix.py` that writes `latex/tables/tab_cf_iv.tex` from the same `dW()` it prints (no recompute — reads the existing pickle). Regenerated file is numerically identical to the hand-built one. **Audit now: 24 mapped, 0 orphans.** Lesson: verifying a number requires the RIGHT program; a hasty hand-reconstruction is itself an error source. The IV crossovers in prose are still hand-typed literals (not yet macro-backed) but are verified correct — candidates for the phase-2 `\newcommand` system.

Related: [[settled_cf_rules]], [[counterfactual_results]], [[key_results]].
