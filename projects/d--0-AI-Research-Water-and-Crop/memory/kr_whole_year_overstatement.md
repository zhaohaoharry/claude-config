---
name: kr_whole_year_overstatement
description: Kern River supply = whole-year Isabella outflow (no seasonal mask), overstates in-season water ~20-25%; absorbed by model, immaterial; growing-season robustness deferred pending user manuscript review
metadata:
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

OPEN/DEFERRED 2026-06-29 (Water and Crop). User asked whether KR supply is overstated because we use the
deliverable-supply for the WHOLE YEAR while irrigation is seasonal. 3-agent audit (grounded in code, NOT
re-executed) findings:

**The premise is right at raw-data level.** KR annual supply = full-calendar-year sum of daily Isabella
Dam outflow (CDEC ISB sensor 23, ×1.9835 AF/cfs-day, only `cfs>=0` filter, NO seasonal mask) —
`program/1_data/build_kern_river_allocation.py:105-112`. Off-season (Nov-Mar) share of annual outflow
averages ~22-25%, range 9% (2019) to **39% (2015, driest)**; largest exactly in the dry years that bind
(2015 39%, 2014 31%, 2021 36%). Daily file sits UNUSED in raw: `data/raw/Water supply/KernRiver/
CDEC_ISB_outflow_daily.csv` (+ storage/inflow siblings).

**But the model absorbs almost all of it:** (a) Isabella is a STORAGE reservoir (fills winter→Jun 272K AF,
drains through summer→Nov 134K) so off-season outflow is largely managed release/recharge, not deadweight
— 22-25% is an upper bound; (b) model is ANNUAL + Kern banks underground, so within-year timing is
abstracted and off-season water is still usable in-year; (c) DECISIVE: structural model does NOT consume
`SW_KR` from district_sw_supply.dta — `calibrate_water_cost.py` Stage 1.5 re-caps KR use at
min(allocation, AWMP entitlement, residual crop demand), cascading surplus away (realized KR_used ~320
kAF/yr << nominal SW_KR ~548 kAF/yr). Honest wrinkle: the demand cap binds in WET years but NOT dry years
(demand>allocation), so dry-tail overstatement isn't trimmed by the cap — saved instead by banking +
small dry-year KR volumes.

**Immaterial to results.** KR = 30.6% nominal SW but only ~14.5% of total water (SW+GW), 4.7% of bill
(cheapest at $25/AF). DECISIVE: all 8 KR-using districts have GW access (g=1); the 4 no-GW buyer districts
that drive sell-and-pump leakage (Belridge, Lost Hills, Berrenda Mesa, Tejon-Castac) have KR = exactly 0.
So a KR error is absorbed inside GW-access districts (trades 1:1 vs own pumping), can't change buyer/seller
status or move the institution×GW cross-partial. KCWA carries the uncapped flood residual but is non-ag,
dropped from estimation (`calibrate_water_cost.py:79 NON_AG_KR_USERS`).

**DEFERRED ROBUSTNESS (user reviewing manuscript first before deciding).** If wanted for referee-proofing:
rebuild KR on growing-season-only (Apr-Oct) outflow (or banking-adjusted usable volume) and re-run
`calibrate_water_cost.py → counterfactual_engine.py`, canonical files untouched (MD5-gate). No KR-scaling
env hook exists → needs a small generator edit. Whole audit was an INCIDENCE argument from committed
panels/check CSVs, NOT a re-executed sensitivity — a definitive answer requires the re-run. Related:
[[kernriver_dta_retired]], [[swp_delivery_entitlement_weighted]], [[counterfactual_results]].
