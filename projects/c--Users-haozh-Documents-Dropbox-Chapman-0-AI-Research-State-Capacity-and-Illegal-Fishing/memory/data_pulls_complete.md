---
name: data-pulls-complete
description: GFW/SAR/NOAA API data pulls are complete; inventory + the SAR null-tile gotcha
metadata: 
  node_type: memory
  type: project
  originSessionId: 7a290715-e2f0-465e-aba3-b3f1b178e8dc
---

As of 2026-06-14 all five raw API pulls are complete and verified in `data/clean/`:

- `gfw_eez_flag_month.csv` — observed AIS fishing effort, host-EEZ × flag × month, 2012–2020 (71,525 rows, 146 hosts)
- `gfw_gaps_events.csv` — AIS going-dark events, 2012–2020 (761,102 events; 90,668 fishing)
- `sar_eez_flag_year.csv` — Sentinel-1 SAR detections by host × year × flag, 2017–2021 (DARK/unmatched = 49.6%)
- `sar_eez_class_year.csv` — SAR detections by matched × neural class, 2017–2021 (dark-fishing lower bound = 4,848,114)
- `chl_host_month.csv` — NOAA MODIS chlorophyll-a control, host × month, 2012–2021 (147 hosts, 1470/1470 host-years)

These are the empirical backbone of the reduced form — SAR dark-vessel pull is the keystone (see [[disentangle-findings]]).

Pull scripts live in `program/sandbox/` (`gfw_pull_*.py`, `sar_pull_*.py`, `chl_pull.py`); all are resume-safe via `data/temp/*_done.json`. Token in `program/sandbox/gfw_token.txt` (valid; GFW allows only ONE concurrent 4Wings report — run GFW pulls sequentially, NOAA can run in parallel).

**Gotcha (fixed):** SAR datasets return HTTP 200 with a `null` entry for genuinely empty tiles (e.g. corner tile (-180,-90), deep Southern Ocean — zero detections). The original `return ent[0][key] if key else []` mapped `null → None`, which the loop misread as FAIL and re-attempted on every resume. Patched both SAR scripts to return `[]` on a null entry. The fishing-effort dataset returns `[]` (not null) for empty tiles, so it never had this issue. Empty corner tiles are NOT missing data — they are correctly empty.
