---
name: crop-concordance-8cat
description: "Water and Crop: crop categories rebuilt to 8 water+revenue-grounded categories via auditable concordance (program/1_data/crop_comm_concordance.csv); replaces buggy hardcoded classify_crop"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

Since 2026-06-22 the crop categories are an **auditable COMM->category concordance grounded in water use + revenue**,
replacing the hardcoded keyword `classify_crop()` in `create_sampling_dots.py` (which had bugs: PEACH/PEAR->veg via "PEA",
GRAPEFRUIT->grape, SUGARBEET/tangelo/pecan->fallow, ~767k ac leaked to Fallow).

**8 categories (down from 9):** 1 Nuts (almond+pistachio MERGED+walnut+pecan), 2 Tree fruit (citrus+deciduous fruit),
3 Grapes & berries (grapes+blueberry+caneberries), 4 Cotton & field, 5 Alfalfa & pasture, 6 Grain, 7 Vegetables
(incl flowers/nursery), 8 Fallow (uncultivated only). Field crops split among 4/5/6 by water (mid/high/low). Almond &
pistachio merged (tightest water+revenue pair). Strawberry->veg (annual), kiwi->tree fruit, flowers NOT a 9th category
(0.4% of cropland). See DECISIONS.md 2026-06-22 for the full rule set.

**Pipeline (restructured 2026-06-22, DATA side RUN):** D1 `build_crop_concordance.py` (NEW) reads the COMM list +
acreage DIRECTLY from the raw crop polygons (data/raw/gis/kern{year}.shp, attribute-only via pyogrio; it is the FIRST
step so it must NOT depend on the derived crop_plot_WD), then builds the concordance + per-category primitives (`data/clean/crop_comm_concordance.csv` 366 COMM; `crop_category_summary.csv` = per-cat
acre-weighted water + value range). D2 `create_sampling_dots.py` (was D1) now READS the concordance for `crop_cat`
(keyword classify_crop retired; fallow=8; perennial mask = cats 1,2,3). D3 `build_plot_panel.py` (was D2). Reran
D1->D2->D3: 8-cat dot_panel/plot_panel, acreage conserved 19,933,637; shares Nuts 32.2, Cotton&field 12.7,
Grapes&berries 12.4, Tree fruit 9.5, Veg 9.4, Alfalfa 8.8, Grain 7.7, Fallow 7.2. Table 1 generator
`program/3_exhibits/draw_tab1_crop_categories.py` (D1 summary + D3 plot_panel) -> `latex/tables/tab_crop_categories.tex`.
PIPELINE_manual.tex renumbered (concordance D1, dots D2, plotpanel D3) + Table 1 exhibit after Fig 1. Manuscript
`tab:crop_categories` switched from hand-typed 9-cat to generated 8-cat \input; Data-section prose tracked (367 labels,
"eight" categories). Audit scripts still in `program/sandbox/crop_concordance_audit/`.

**Crop revenue + cost rebuilt on 8-cat (2026-06-22, DATA side RUN):** NEW standalone generators
`program/1_data/build_crop_revenue_8cat.py` -> `data/clean/crop_revenue_8cat.dta` (acreage-weighted rev/acre from
prices.xlsx + nass_{2017-2022}; crops assigned to the 8 cats by keyword rules implementing the concordance — note it
does NOT read crop_comm_concordance.csv; aggregate/total rows dropped, pasture/rangeland excluded; audit
sandbox/log/crop_revenue_8cat_assignment.csv) and `build_crop_cost_8cat.py` -> `data/clean/crop_cost_8cat_panel.dta`
(per-cat UC ANR anchors on the 8 cats, NASS-Prices-Paid-indexed, fallow=0). Both are BETTER than the prior canonical
(batch TASK 1, which silently dropped 2020, lost alfalfa 2017-20, double-counted aggregates, doubled 2012). The OLD
9-cat data + generators ARCHIVED (data/archive/old_9cat_20260622/; program/archive/...STALE/SUPERSEDED); batch TASK 1
flagged SUPERSEDED in-code (still writes the old crop_revenue_9cat.dta until removed at repoint). PIPELINE_manual.tex:
new `\dgroup{Miscellaneous data: crop revenue \& cost}` after D13 (cropreven + cropcost), old `rev` step removed.

**STILL PENDING (user drives — structural rerun):** A5/A10/B1d/B4 still expect old 9-cat conventions (s_idx 13; field
state now 11). **A10 reads the now-archived crop_revenue_9cat.dta and B1d_step3_euler reads the now-archived
crop_cost_9cat_panel.dta -> BOTH FileNotFound until repointed to crop_revenue_8cat.dta / crop_cost_8cat_panel.dta**
(A10 pivot cat 1-9 -> 1-8, R_c1..R_c8). Manuscript model/results sweep: category-name refs (almonds/pistachios ->
nuts), "eight productive crops" -> seven, param taxonomy, all structural magnitudes change with the rerun. Relates to
[[lag_state_split_in_decision_id]].
