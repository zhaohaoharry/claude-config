---
name: gw_head_pgwl_and_pumping_cost
description: Current GW head = PGWL well obs (NOT C2VSim); pumping cost = 0.234*dtw with C0=0 (NOT 28.50+0.30*dtw)
metadata:
  type: project
---

Water and Crop groundwater data — the CURRENT production facts (I once mis-stated the stale ones):

- **GW head / depth-to-water (DTW):** comes from observed **PGWL** (DWR Periodic Groundwater Levels) well measurements, district-year, built by `program/1_data/build_pgwl_district_head.py`, which OVERWRITES `district_gw_head.dta`. **C2VSim is fully removed from data construction** (2026-06-20): `A7b_c2vsim_to_districts.py` is archived to `program/archive/`; `B4_counterfactuals.py` now reads district AREA from `district_area.csv` (built by `build_district_area.py` from the WD shapefile), NOT `district_aquifer_params.dta`. C2VSim survives only in `T1p3_c2vsim_gkt_validation.py` as an independent validation benchmark (not data construction).
- **Full raw-traced GW-head chain (2026-06-21):** `download_pgwl.py` (raw statewide DWR PGWL → stations.csv + measurements.csv) → `build_kern_pgwl_subset.py` (Kern subset: county filter + spatial join wells→WD polygons → `kern_measurements.parquet` + `kern_station_district_map.csv`) → `build_pgwl_district_head.py` → `district_gw_head.dta`. The subset generator was written 2026-06-21 to close a provenance gap (the two Kern files were built inline 2026-05-14 with no script); it reproduces both committed files exactly.
- **Pumping cost equation (current):** `c_gw = C0 + C1*dtw_ft`, **C0 = 0** (no fixed component), **C1 = eta = 0.234 $/AF per ft of lift** (1.0241*0.16/0.70; Hurr & Litke 1989, BPW P_elec=$0.16/kWh, CEC 70% pump efficiency); set in `A5_water_cost.py` (ETA_OVERRIDE env var can change C1). A5 EXPLICITLY overrides the cost_gw pre-baked into `district_gw_head.dta`.
- **OLD/deprecated equation (do not present as current):** `c_gw = 28.50 + 0.30*dtw_ft`. It survives in A7b's docstring and build_pgwl's cost_gw column but is overridden downstream.

Real chain: download_pgwl -> build_kern_pgwl_subset -> build_pgwl_district_head -> A5 (water cost AC_kt). See [[aquifer_elasticity_calibration]] and [[sustainable_yield_construction]].

**Why:** the user caught me presenting C2VSim head and the 28.50+0.30 cost as current; both are outdated.
**How to apply:** before describing GW head source or pumping cost in prose, the pipeline doc, or a tabnote, verify against `A5_water_cost.py` (cost) and `build_pgwl_district_head.py` (head). Do NOT trust a program's own docstring (A7b's is stale) or the auto-heuristic's I/O for data-construction programs that use `open()`/`.dat`/`.out` — re-read the actual read/write calls. [[feedback_verify_canonical_data_before_use]]
