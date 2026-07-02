---
name: pgwl-raw-data-location
description: "Water and Crop: where the DWR PGWL groundwater-level data lives — raw statewide in data/raw/dwr_pgwl, derived Kern subset in data/clean (moved out of data/temp on 2026-06-23)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

The DWR PGWL (Periodic Groundwater Level) data was relocated on 2026-06-23 (it used to sit in `data/temp/dwr_pgwl/`,
which was wrong — disposable + Dropbox-synced bloat). Current canonical locations:

- **Raw statewide source** (immutable) → `data/raw/dwr_pgwl/`: `measurements.csv` (1.4 GB), `stations.csv` (8 MB).
  Written by `download_pgwl.py` (D11, run-once download).
- **Derived Kern subset** (analysis-ready) → `data/clean/`: `kern_measurements.parquet`,
  `kern_station_district_map.csv`. Written by `build_kern_pgwl_subset.py` (D12), read by `build_pgwl_district_head.py`
  (D13, → `district_gw_head.dta`) and sandbox `SF3_well_level_drawdown.py`.

`build_kern_pgwl_subset.py` splits its path vars: `RAW_PGWL` (data/raw/dwr_pgwl, reads) vs `CLEAN` (data/clean, writes).

**Why / open:** the user chose project `data/raw` "for now" over the central repo `D:\0. Research Data\3. Environment &
Climate\`. The 1.4 GB raw is therefore Dropbox-synced — a known bloat tradeoff that may be revisited (move to the
central D:\ repo, reference in place). The sandbox "later" cluster (`sf3_*`, `sgma_extraction.csv`,
`kern_district_year_dtw_observed.csv`) still sits in `data/temp/dwr_pgwl/`. Relates to [[gw_head_pgwl_and_pumping_cost]].
