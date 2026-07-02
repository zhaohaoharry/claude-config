---
name: kernriver_dta_retired
description: "KernRiver.dta retired pipeline-wide; KR rights from kr_first_point_rights.csv, allocation from kern_river_allocation.dta; allocator runs before supply panel"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

Since 2026-06-21, the old `KernRiver.dta` (stale KR_rights: Buena Vista 158K, Kern-Tulare 23K, Bakersfield blank) is **retired** — no live program uses it. KR provenance is now split cleanly:

- **Rights / priority** → `program/1_data/kr_first_point_rights.csv` (sourced, cited in `KR_RIGHTS_SOURCES.md`).
- **District-year allocation** → `kern_river_allocation.dta` (priority-cascade off the CSV; see [[counterfactual_results]] / [[settled_cf_rules]]).

**Data-prep order (changed):** D3 `WD_month.do` (roster) → **D4 `build_kern_river_allocation.py` (allocator)** → **D5 `build_district_sw_supply.py`** → D6 `A_data_construction_batch.py`. D3 stays first because the allocator reads `Kern_WD.dta`.

Key code facts after the refactor:
- `build_district_sw_supply.py` sets `SW_KR = KR_allocation_af` directly (merge on agencyname+year) and writes the FINAL `district_sw_supply.dta` (incl. `connected_SWP/CVP/KR`, consumed by `A5_water_cost.py`). Dead `AWMP`/`kr_allocation` columns dropped.
- `A_data_construction_batch.py` **TASK 4 removed** — it no longer touches `district_sw_supply` (no more D6 `SW_KR` overwrite).
- `WD_month.do` gets priority from the CSV (`kr_priority.dta`); kept the `isabella` sheet → `KernRiver_year/month.dta` (CDEC hydrology for the legacy Stata `WD_month`/`WD_year` panels). Isabella for the allocation comes from `CDEC_ISB_outflow_daily.csv`, NOT KernRiver_year.
- `data_all_other.do` is a dead draft (errors at line 130 `dfdfd`); it still nominally saves `KernRiver.dta` but is never run.

Refactor is **structure-only / numerically identical** to post-KR-correction production (final SW_KR unchanged). Not yet rerun as of 2026-06-21 — user reruns the full chain after finishing the pipeline. Verify with a before/after diff on `district_sw_supply.dta`.
