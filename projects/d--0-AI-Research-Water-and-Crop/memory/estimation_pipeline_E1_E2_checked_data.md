---
name: estimation_pipeline_E1_E2_checked_data
description: "Water-and-Crop calibration+estimation-sample data group (PIPELINE_manual Part 1, NOT Part 2 anymore): D16=calibrate_trade_price.py, D17=calibrate_water_cost.py (both still in program/2_structural/, ANALYSIS badge), D18=build_estimation_sample.py->estimation_sample.dta (NEW plot-level, 11-state, replaces dot-level A10). Part 2 now a stub for the real CCP/Euler estimation. New sample N=234,439, 21 districts (Lebec drops: D17 returns D_kt=0). Old retired chain auto-renumbered D19-D25. R1-R13."
metadata:
  node_type: memory
  type: project
---

**Pipeline restructure (2026-06-24, SUPERSEDES the E1/E2 framing below).** The two calibrations + the estimation-sample
assembly are now a **Part-1 data group "Calibration & estimation sample"** (the user's reframe: calibration + sample =
data; the real estimation is Part 2). They auto-number as data steps: **D16 = `calibrate_trade_price.py`** (was E1),
**D17 = `calibrate_water_cost.py`** (was E2), **D18 = `program/1_data/build_estimation_sample.py`** (NEW). Both
calibration .py files stay in `program/2_structural/` (B4/T1p3 import them); they keep the ANALYSIS badge but live in the
data part. All `\eref{}`→`\dref{}`. **Part 2 is now a forward-looking stub** for the actual first-stage CCP + Euler,
pointing at D18. The retired chain (batch, area, plotacre, crop, water, cost=A5, mle=A10) sits under a "Legacy data
steps (pending deletion)" banner and auto-renumbers **D19–D25** (caveat: `batch`=aquifer-influence matrix and
`area`=district area still feed the counterfactual — not blindly deletable). PIPELINE_manual compiles 21 pp.

**D18 = `build_estimation_sample.py` → `data/clean/estimation_sample.dta`.** Plot-level successor to the dot-level
`A10_build_mle_sample.py` (D25, retired). One row per plot-decision (no dot collapse — `plot_panel` D3 is already the
unit); `plot_acres` = LL weight. Carries the **11-state** field state (3 perennials×{young,mature}+4 annual+Fallow, from
`crop_cat_lag`+`lag_state`), `c_idx`, `AC_kt`(+GW,`cost_gw`) from D17, `drought`/`swp_alloc` from D4, per-year revenue
`R_c1..R_c8` (D14), cost `C_c1..C_c8` (D15), constant water `W_c1..W_c8` (D1). Mirrors the CCP's own filter
(`is_ag==1 & AC notna`, inner join). Output: **N=234,439, 21 cropping districts**. KCWA drops (wholesale); **Lebec drops
— investigated & settled**: its *entire* permit record is uncultivated rangeland (4 parcels, all raw commodity
`UNCULTIVATED AG` → cat 8 Fallow), so zero crop-water demand → no `AC_kt` → no crop-choice variation. A **legitimate
all-fallow exclusion, NOT a bug**; 21 is the settled count of districts that actually crop.

**First-stage CCP DONE on 8-cat (2026-06-24) — Part 2 E1.** `program/2_structural/B1d_step2_ccp.py` rewritten for
`N_C=8`, `N_S=11`, `PERM_MASK=[1,1,1,0,0,0,0,0]`, reading `estimation_sample.dta` (D18) directly (no dot collapse — uses
the precomputed `s_idx`/`c_idx`). Run: 234,439 plots, 21 districts, **228 params** (α_sc 77 + α_kc 147 + 4), district-crop
**R²=0.973** (168 cells), per-crop residual ≤0.06pp; φ̂=(−0.158,−0.006,+0.002,+0.048). Pickle `B1d_ccp_firststage.pkl`
now carries `district_r2`. Table exhibit `B1d_step2_ccp_table.py` made construct-agnostic (N_C/R² from pickle, dropped
hardcoded 0.9188) → `tab_stage2_estimates.tex`. Pipeline E1 added; manifest traces D18→estimator→table (fixed the
exhibit's pickle read to one-line `pickle.load(open(...))`); audit 0 orphans. Manuscript first-stage table auto-updates;
prose track-changed (446 FE 280→224/104→77/176→147; 438 22→21; 605 R² .92→.97 & 176→168 cells; 612 tabnote 176→168);
81pp.

**SECOND STAGE DONE on 8-cat (2026-06-25) — Part 2 E2.** Programs renamed (clean stage names, per user): `B1d_step2_ccp`
→`stage1_ccp`, `_table`→`stage1_ccp_table`, `B1d_step3_euler`→`stage2_euler`, `B1d_step4_ols`→`stage2_ols`; redundant
`B1d_step4_relevel_table` archived. stage2_euler/ols are construct-agnostic (read N_C/N_S/perennials/names from the
pickle→npz; young-offset = N_S−n_perennial = 8; revenue/cost repointed to crop_revenue/cost_8cat). **Artifacts ALSO renamed
(clean names):** `B1d_ccp_firststage.pkl`→`first_stage_ccp.pkl`, `B1d_ccp_diagnostics.pdf`→`first_stage_ccp_diagnostics.pdf`,
`B1d_euler_moments.npz`(+`_aux`)→`euler_moments.npz`, `B1d_dynamic_params.json`→`structural_params.json`,
`B1d_stage4_vcov.npz`→`structural_vcov.npz` (stem-replaced across all 11 production readers incl. stale B4/VFI/T1p3,
repointed path-only; build_pipeline ordering heuristic updated). Old base files deleted; ~35 suffixed B1d_* vintages in
results/ left orphaned (inert). `B1d_step5_vfi.py` program name kept (still 9-cat). Run: 225,019 plot-decisions × 7 × 5 = 7.88M moments; **β̂_W=+0.00126 (t10.2), β̂_R=+2.6e-6 (t2.4
— now weakly SIGNIFICANT, was insignificant)**; 21 clusters. `tab_structural_params.tex` regenerated. Manuscript
track-changed: β_W 0.00118→0.00126, magnitude para almonds→nuts/3.34→3.26AF/$46→$55/seven→eight & **$700 tier dropped
(max AC now ~$508)**, α summaries, dims 22×8/13×8→21×7/11×7, β_R "indistinguishable"→"significant but negligible". 81pp;
audit 0 orphans; pipeline 22pp.

**Table A3 (robustness, `tab:beta_W_robust`) DONE 8-cat (2026-06-25):** sandbox `T1p3_stage4_robust_table_v2.py` →
production `program/3_exhibits/build_tab_beta_W_robust.py`; BPW moment builder `B1d_step3_euler_bpw.py` →
`program/2_structural/stage2_euler_bpw.py` (both promoted, construct-agnostic, sandbox originals archived). β_W×10³: OLS
1.256, BPW 1.509, +c×ω 1.272, +yrFE 1.275, 2SLS 1.053; first-stage F=18.7. Added to Results pipeline R14 (Table 7→
stage1_ccp_table), R15 (Table 8→stage2_ols), R16 (Table A3→build_tab_beta_W_robust). Manuscript IV prose+tabnote
track-changed (F 18→19, IV β_W 0.97→1.05, 40→35/8→7 moment rows, 22→21 clusters). **build_pipeline.py WRITE_VERB regex
fixed** (couldn't see `open(os.path.join(TEX,"x.tex"),"w")` nested paren → tab_structural_params/Table 8 had been silently
missing from the manifest though audit was 0-orphan; now all trace).

**Auxiliary calibrations DONE 8-cat (2026-06-25) — D19-D21 + Table 5 (R17).** Promoted sandbox→2_structural:
`calibrate_aquifer_elasticity.py` (D19, repointed GW pumping to AC_kt_baseline GW_pumped+D13 dtw; β1 0.025→0.013,
half-life 28→**53mi**, β0 -2.64e-5), `calibrate_drought_transitions.py` (D20, crop-indep, unchanged), `calibrate_ar1_rev_cost.py`
(D21, 8-cat panels, +per-crop R²; 7 productive cats, ρ̄_R 0.75→**0.84**). JSON outputs keep B0_*.json names. Table 5
(`tab:param_taxonomy`) now generated by `build_tab_param_taxonomy.py` (3_exhibits) reading the 4 calib JSONs; manuscript
\input + prose track-changed. audit 27 mapped 0 orphans. **FLAG: aquifer half-life doubled 28→53mi — manuscript
"in line with literature ~28mi" sentence needs author review.**

**Bellman VFI + Table 9 DONE 8-cat (2026-06-25).** `B1d_step5_vfi.py`→`program/2_structural/bellman_vfi.py` (construct-agnostic,
reads N_C/N_S/perennials from first-stage pickle at import; young-offset 8); `B4_diagnose_baseline_ccp`(sandbox)→
`program/3_exhibits/build_tab_baseline_fit.py`. Repointed to first_stage_ccp.pkl/structural_params.json/B0_*.json.
**Fit improved: Bellman district-crop RMSE 3.09pp (was 4.94), residuals ≤0.06pp**; BVWSD 25,688 AF unchanged. Table 9
regenerated; prose updated (0.30→0.10, 4.94→3.09); R18 in Results. audit 0 orphans. B4_counterfactuals import repointed
to bellman_vfi.

**COUNTERFACTUALS MIGRATED to 8-cat + LEGACY DATA CHAIN RETIRED + B4 RENAMED + PIPELINE REORG (2026-06-25).**
CF engine 8-cat fix: crop groups `PERENN=[0,1,2,3]`→imported from bellman_vfi (perennial 0-2/annual 3-6/fallow 7), `[:, :8]`→`[:, :N_C-1]`.
**B4 → intuitive names:** `B4_counterfactuals.py`→`counterfactual_engine.py`, `B4_two_task_counterfactuals.py`→`run_counterfactuals.py`,
`B4_crop_margins_figure.py`→`build_fig_crop_margins.py`; artifacts `B4_two_task_results/scens/district_year`→`cf_results/cf_scenarios/cf_district_year_outcomes` (+_iv).
**Legacy chain ARCHIVED** to `program|data/archive/legacy_data_chain_20260625/` (READMEs): A10/mle, A5/cost, batch, build_crop_plot_WD/plotacre, compute_water_9cat, build_district_area, crop.do + 6 .dta. Repoints verified byte-identical: **area** folded into `build_kern_pgwl_subset.py` (build_district_area()); **crop** `build_crop_concordance.py` now reads raw `crop_concordance.xls`+`surftypwb15.xls` via **xlrd** (10 CalPoly label drifts don't change 8-cat output); **B4 repointed off A5 `district_water_cost.dta` → canonical `district_gw_head.dta`** = CORRECTNESS FIX (A5 carried alt dtw for 2 districts: Lebec, Tehachapi-Cummings; 33 dist-yrs, max 154ft). Adversarial workflow PASS 0 crit/major. Deferred consumer: `T1p3_eta_reestimate.py` still reads archived district_water_cost (deferred sweep).
**Pipeline reorg (user):** Part 2 renamed "Estimation and counterfactuals", **one E-step per program** in 5 subsections — First stage (stage1_ccp/Table7), Second stage (stage2_euler/stage2_ols+Table8), Water-cost robustness (stage2_euler_bpw/build_tab_beta_W_robust+TableA3), Baseline-fit (bellman_vfi/build_tab_baseline_fit+Table9), Counterfactual analysis (counterfactual_engine/run_counterfactuals=Table10+Fig7/build_fig_crop_margins=Fig6/T1p3_iv_welfare_matrix=TableA4). Estimation+CF tables MOVED OUT of Part 3; Table 5 kept (Part 3 = R1-R14 data exhibits+Table5). 25pp.
**FINAL post-repoint headline:** taxes 36/93/89; caps 3.87/14.30/10.72%; ΔW@1000 autarky-open **+795**, centralized-open **+56**(positive again, was -42 on stale dtw), centralized-tax **+2,787**(global max), centralized-cap +2,498; crossovers 751/792/1153; autarky closes **76%** of 4.22 MAF; baseline GW 22.23. IV ledger (tab_cf_iv): 1809/0/-41,2797/3922/4350,2788/3531/4044; IV crossovers 433/480. Manuscript fully track-changed (centralization sign reverted to "improves/nearly offsets"); 81pp; audit 27/0.
**DEFERRED (per user "leave bootstrap alone; update other results for now"):** (1) **bootstrap CIs** carried over
unchanged — now several point estimates fall OUTSIDE stale CIs (autarky-open +705 vs [+154,+672]; centralized-tax +2750
vs [+3231,+3678]); cross-partial "all 60 draws" claim stale. (2) **sensitivity sweep** sens_beta/eta/hydro + its prose
STILL 9-cat; `sandbox/T1p3_sensitivity_sweep.py` itself needs migration (stale central β0/β1, old module ref) + 6 variant
re-runs. (3) ~~IV ledger~~ **DONE** (tab_cf_iv + 676/737 on the repointed chain). (4) **appendix per-district decomp**
(app:cf_details tab_cf_decomp_autarky/centralized + channel prose) is hand-built inline (no generator → audit can't see
it), still 9-cat; needs a generator off `cf_district_year_outcomes.csv` — do NOT hand-transcribe. (5) ~~B4 rename~~ **DONE**.
(6) `T1p3_eta_reestimate.py` (η robustness, deferred sweep) still reads/subprocess-invokes the archived
`district_water_cost.dta`/`A5_water_cost.py` — repoint to `district_gw_head.dta` when the sweep is migrated.

---

_Below is the prior 2026-06-23 E1/E2 write-up; the E-step labels are superseded by D16/D17 above, but the
clean-names + checked-data facts still hold._

**Pipeline structure (2026-06-23).** PIPELINE_manual.tex now has three parts: Part 1 Data (D1–D22), Part 2
**Estimation** (E-steps, `\estep`/`\eref` auto-numbered), Part 3 **Results** (renamed from "Exhibits"; short-named
**R1–R12**, R not E to avoid colliding with the estimation E-steps). "Stage 1.5" was retired as misleading — the AC LP
is **E2**, "the average-cost LP"; only the filename `B1d_step1p5_water_allocation.py` keeps the legacy token.

**The verified-data boundary (user, important).** **D1–D15 are the double-checked / canonical data steps; D16–D22
are OLD programs "not supposed to be used"** (D16 batch, D17 area, D18 plotacre, D19 crop, D20 water, **D21 cost =
A5_water_cost.py**, **D22 mle = A10**). The estimation must run on D1–D15. So `district_water_cost.dta` (A5/D21) is
legacy and the AC LP must stop reading it.

**Estimation steps (clean names, DONE 2026-06-23).** **E1 = `program/2_structural/calibrate_trade_price.py`** fits
$p_t=a\,e^{b(1-a_t)}$ (a=256.74, b=1.384, reproduces old v3) reading the `in_fit` anchors from the checked
`swp_transfer_prices.csv` (D10); `compare_swp_price_options.py` applies it (now reads un-versioned
`swp_price_calibration.json`) → `SWP_KernAg_three_prices.csv`. **E2 = `program/2_structural/calibrate_water_cost.py`**
(renamed from `B1d_step1p5_water_allocation.py`) → `AC_kt_baseline.csv` + `AC_kt_heatmap.pdf` (Fig A5 / R13). Old
`calibrate_swp_price_v3.py` and `B1d_step1p5...py` are archived. B4/T1p3 importers updated to the new names.

**Design decisions (user-confirmed).**
- **GW pumping cost is NOT calibrated**: η = 0.234 \$/AF/ft is from literature (Burlig–Preonas–Woerman marginal-energy
  cost; `build_pgwl_district_head.py` C1=0.234, C0=0). Checked **D13** (`district_gw_head.dta`) already carries
  per-district-year `cost_gw`; the AC LP just uses it. No GW-cost E-step. See [[gw_head_pgwl_and_pumping_cost]].
- **Demand needs no separate program**: summed in-LP from de-overlapped `plot_panel` (D3) × per-category water
  requirement (`crop_category_summary.csv` / concordance, D1).

**Repoints DONE (2026-06-23).** Both E1 and E2 now read checked data; old AC regenerated. New demand 55.2 MAF (vs
59.1 double-counted); AC ag mean 74→72/AF, median per-cell change 0.62, ρ=0.88. See [[table_a2_sf4_trades_generator]],
[[swp_delivery_entitlement_weighted]], [[deferred_repoint_8cat_revenue_cost]].

**Downstream now STALE — must re-run on the new AC:** first-stage CCP (`B1d_step2_ccp`), Euler (`B1d_step3`),
structural results, B4 counterfactuals all used the OLD `AC_kt_baseline.csv`. Also `T1p3_eta_reestimate`'s eta-override
re-runs A5, which `calibrate_water_cost` no longer reads — that robustness path needs reworking to override η in D13.
