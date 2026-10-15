---
name: deferred-repoint-8cat-revenue-cost
description: "Water and Crop: DEFERRED repoint — A10 + B1d (step2_ccp/step3_euler) still read the ARCHIVED 9-cat crop_revenue/crop_cost/crop_water; switch them to crop_revenue_8cat.dta / crop_cost_8cat_panel.dta / 8-cat water (crop_category_summary.csv) when next working on those programs"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

When next working on `A10_build_mle_sample.py`, `B1d_step3_euler.py`, the estimation sample, or the structural rerun,
**do this repoint** (deferred 2026-06-22; the old 9-cat files are archived under `data/archive/old_9cat_20260622/`, so
these programs currently FileNotFound). The user asked me to remember and do it then.

**1. `program/1_data/A10_build_mle_sample.py`** (crop REVENUE):
- Change the read `crop_revenue_9cat.dta` -> **`crop_revenue_8cat.dta`**. Same schema (`cat, year, rev_per_acre`), so
  the `columns=["cat","year","rev_per_acre"]` read and the `pivot(index="year", columns="cat", ...)` still work —
  but it now yields `R_c1..R_c8` (8 cats), not R_c9.
- Update `keep_cols` `[f"R_c{c}" for c in range(1, 10)]` -> `range(1, 9)`.

**2. `program/2_structural/B1d_step3_euler.py`** (crop COST):
- Change the read `crop_cost_9cat_panel.dta` -> **`crop_cost_8cat_panel.dta`**. **Column rename:** the old file had
  `crop_cat`; the NEW 8-cat panel uses **`cat`** (to match the revenue panel). Update the read/merge key accordingly.
- Cost panel is now 8 categories (1-8), fallow = cat 8 = 0.

**3. WATER side — `A10_build_mle_sample.py` + `program/2_structural/B1d_step2_ccp.py`** (crop WATER): both read the
now-ARCHIVED `crop_water_9cat.dta` (archived 2026-06-23 at the user's direction — the 8-cat acre-weighted water
requirement already exists in `crop_category_summary.csv`, e.g. Nuts 3.26 / Tree fruit 3.47 / … AF/acre). Repoint them
to the 8-cat water: read `water_req` per `cat` from `crop_category_summary.csv` (D1, `build_crop_concordance.py`), or
build a small `crop_water_8cat.dta` from it. The old generator `program/1_data/compute_water_9cat.py` (D20) is
superseded by D1 — archive/retire it at the same repoint.

**4. `program/1_data/A_data_construction_batch.py`** — TASK 1 (crop revenue) is flagged SUPERSEDED; **remove it** at
this repoint (it still writes the archived `crop_revenue_9cat.dta`). Keeps only the aquifer-influence output.

**Why:** the canonical crop revenue is now `build_crop_revenue_8cat.py` and cost is `build_crop_cost_8cat.py` (8-cat
construct); the old 9-cat data and generators are archived. Until the consumers are repointed the estimation can't run.
**How to apply:** make the filename/column/cat-count edits above, then re-run A10 / B1d_step3_euler and confirm they
produce R_c1..R_c8 / 8-cat cost. Relates to [[crop_concordance_8cat]].
