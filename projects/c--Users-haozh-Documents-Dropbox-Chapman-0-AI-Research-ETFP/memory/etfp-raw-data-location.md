---
name: etfp-raw-data-location
description: "Where the readable raw ASIE/CESD data for ETFP lives (E: drive), and which Dropbox copies are unreadable online-only placeholders"
metadata: 
  node_type: memory
  type: project
  originSessionId: c3dae0d6-96ef-491d-953c-724c0ebc0469
---

For the ETFP (China industrial cleanup) project, the **readable** raw micro-data lives on the **E: drive**, not the C: Dropbox path:

- `E:\Dropbox (Chapman)\1. Research Projects\TradeAndEmission\data\ASIE\cleaned\` — harmonized firm-level ASIE Stata files `qy00.dta`–`qy13.dta` with **consistent English columns** (`output_asie`, `vadded`, `employment`, `sales`, `org_code`, `year`). Use these for ASIE aggregates — the raw `qy*.dta` one level up have wildly inconsistent cross-year schemas (2000 Chinese names, 2004 census-year gaps, 2008 coded `B0xx` names).
- `E:\Dropbox (Chapman)\1. Research Projects\TradeAndEmission\CESD\cesd2000.xlsx`–`cesd2008.xlsx` (some `.csv`) — clean CESD with English columns (`org_code`, `year`, `output`, `so2_emis`, ...). **`so2_emis` is in kg.**

Caveats found in the data:
- ASIE `cleaned/qy04.dta` has `output_asie`/`vadded` = NaN (2004 economic-census year); `qy08.dta` has `vadded` = NaN.
- The naive full-sample aggregate is contaminated by ASIE **sample expansion** (above-scale firms 163k→411k, 2000→2008) and a **2006 CESD coverage break** (`so2_nonmiss` drops while row count jumps). Use a **balanced panel** (firms present every year) for coverage-consistent aggregates.

What is NOT readable in this environment (Dropbox Smart-Sync online-only placeholders — fail Errno 22 / BadZipFile even with sandbox disabled): everything under `C:\Users\haozh\Dropbox\TradeAndEmission\data\` except the materialized files, including `ASIE.zip`, `CESD.zip`, and `cleaned\CESD-ASIE-CUST-firmLevel-noInterp.dta`. The 4.5GB `cleaned\CESD-ASIE-CUST-noInterp.dta` (C:) IS readable but has duplicated customs rows. Estimation output `cleaned\clean_tech_TCZ.dta` (C:) is readable. See [[etfp-motivation-aggregate-numbers]].
