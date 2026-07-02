---
name: fig_a4_well_level_drawdown
description: "Water-and-Crop Figure A4 (fig:sf3_well, well-level drawdown vs distance) generator is now program/3_exhibits/build_sf3_well_level.py reading derived kern_measurements.parquet (NOT the raw 1.4GB stream); panel DEDUPLICATED to 298 unique wells (was 313 well-district obs; 79 wells map to >1 district in kern_station_district_map.csv); slope -0.658, t=-3.50."
metadata:
  node_type: memory
  type: project
---

**Generator (2026-06-23).** Figure A4 (`fig:sf3_well`) — the well-level robustness companion to Figure 3 — is built
by **`program/3_exhibits/build_sf3_well_level.py`** (promoted from `program/sandbox/SF3_well_level_drawdown.py`, which
streamed the raw 1.4 GB `measurements.csv`; archived). It now reads the **derived Kern PGWL subset**
`data/clean/kern_measurements.parquet` (`gse_gwe` by well-year, from build_kern_pgwl_subset.py / \dref{pgwlsub}),
`data/clean/kern_station_district_map.csv` (well→ag-district), and the raw `data/raw/dwr_pgwl/stations.csv` for
per-well lat/lon (no derived file carries coordinates). Each point is a well's 1998--2002 → 2018--2022 mean-DTW change
vs great-circle distance to the NW no-GW cluster centroid (Belridge, Lost Hills, Berrenda Mesa). The panel is
**collapsed to one row per unique well** (2026-06-23, user: "update 313 to 298 wells. that makes more sense"): OLS
slope **−0.658 ft/mile** (SE 0.188, t=−3.50, R²=0.040, **N=298**); winsorized ±150 ft for plotting (legend "N=293",
5 dropped), fit on the full 298-well sample. Writes `latex/figures/sf3_well_level.baseline_20yr.pdf`. PIPELINE_manual
Exhibit 12.

**Repoint preserved numbers exactly** (before the dedup): `kern_measurements.parquet` is the Kern subset of the same
raw file and year is parsed from `msmt_date` the same way; old-stream vs new-parquet diffed identical (N=313, −0.694).

**Why 298 not 313 (shared-crosswalk quirk).** In `kern_station_district_map.csv`, **79 wells are mapped to >1
district** (boundary wells inside overlapping district polygons). The pre-dedup panel entered those wells twice
(313 = 313 well-district obs from 298 unique wells). The dedup keeps each well once, with NW-cluster membership =
"in any NW district." The 14 represented districts and 7 absent are unchanged by the dedup. This same map feeds the
district head panel `district_gw_head.dta`, so the duplicate mapping is a property to watch wherever
`kern_station_district_map.csv` is aggregated. See [[pgwl_raw_data_location]], [[gw_head_pgwl_and_pumping_cost]].
