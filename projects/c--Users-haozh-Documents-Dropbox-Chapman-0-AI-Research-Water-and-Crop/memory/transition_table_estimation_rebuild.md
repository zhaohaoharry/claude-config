---
name: transition_table_estimation_rebuild
description: "Water-and-Crop Table 3 (tab:transitions / sf2_transition_matrices.tex) is built by program/3_exhibits/RF_transition_table.py from the DE-OVERLAPPED 8-cat plot_panel.dta minus KCWA (same 234,491 plot-decisions as Table 2 Panel A), acre-weighted; drought split from SWP_allocation_year.dta. Decoupled from the stale 9-cat mle_sample."
metadata:
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

**CURRENT (2026-06-23 rebuild).** Table 3 is built from the **de-overlapped 8-category reconstructed plot
panel**, not the structural estimation sample. Same decoupling logic as Table 2 Panel A (see
[[project_table2_provenance_rebuild]]): the transition matrix is a property of the reconstructed plots; water
conditions don't change it, so it needn't wait for the structural rerun on the de-overlapped 8-cat data (which
the user drives). `mle_sample.dta` is still **stale 9-cat** (crop_cat 1–9, pre-de-overlap).

**Generator:** `program/3_exhibits/RF_transition_table.py` (moved from `program/sandbox/`) reads
`plot_panel.dta` (drop the wholesale Kern County Water Agency) + `SWP_allocation_year.dta`, and writes
`latex/tables/sf2_transition_matrices.tex`. Each plot-decision row carries `crop_cat` + `crop_cat_lag` (0 NaN),
so one transition per row. Super-types on the **8-cat construct**: Perennial = crop_cat 1–3, Annual = 4–7,
Fallow = 8 (was 1–4 / 5–8 / 9). Acre-weighted by `plot_acres`. Drought = statewide SWP final allocation
≤ 0.40 (11 years: 2001, 2008–09, 2012–15, 2018, 2020–22).

**Numbers (current):** N = **234,491** plot-decisions = Table 2 Panel A's universe (538 district-years × mean
436 plots; non-drought 132,810 + drought 101,681). Perennial persistence **98–99%** (98.5/99.0). Annual
persistence **~94%** (94.4/94.1) — up from the old ~90% because the de-overlap removed double-counted annual
permits (Veg −41%, Grain −39%). Fallow re-entry **59→36%** (non-drought 59.1, drought 35.7), the lost re-entry
going entirely to extended fallow. PIPELINE_manual Exhibit 6; audit 0 orphans; compiles 81 pp.

**Manuscript prose (tracked):** Fact 2 + tabnotes say "234,491 plot-decisions of the reconstructed plot panel",
"about 94%", "59% re-entry to 36%", and the 8-cat crop grouping; edited inside the pending green `\add` wrappers.

**History.** 2026-06-19 first rebuild read the OLD 9-cat `mle_sample.dta` + `AC_kt_baseline.csv`, mirrored
`B1d_step2_ccp.py`'s sample (acres>0 + water-cost inner join) to make N=230,339 match the estimator. That tie to
the estimator was dropped on 2026-06-23 when the table was decoupled to `plot_panel` for the de-overlap. Old
`build_sf2_transition_matrices.py` (read `crop_plot_all.dta`) archived. See
[[feedback_verify_by_reexecution_not_rederivation]], [[overlap_resolution_deoverlap]],
[[crop_concordance_8cat]], [[decision_id_v2_vs_fine_impact]].
