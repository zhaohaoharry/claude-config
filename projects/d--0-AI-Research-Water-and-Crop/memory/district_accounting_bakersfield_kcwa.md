---
name: district-accounting-bakersfield-kcwa
description: Verified district counts for the Water and Crop manuscript and how Bakersfield (urban) and KCWA (wholesale+ag) are handled across panels
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

Verified district accounting (v2 pipeline) for the Water and Crop manuscript, settled with the author 2026-06-15.

**The counts (all robust to v1/v2 since only membership matters):**
- 25 surface-water districts exist in the data (`district_water_cost_v2.dta`).
- **24 AGRICULTURAL districts** = the analysis universe. Bakersfield (City of) is the 25th, urban/municipal, dropped from the count.
- **Crop / MLE panel** (`mle_sample_v2.dta`) = **23** districts. Drops Bakersfield and Rag Gulch (no crop info); **INCLUDES KCWA**.
- **Water-cost panel** (excl. Bakersfield, 1998–2022) = **24** districts, **588 district-years**.
- **20 of the 24** ag districts pump groundwater. The 4 no-GW buyers: Belridge, Berrenda Mesa, Lost Hills, Tejon-Castac.
- **Depth-to-water / spatial-spillover calibration** (`B0_aquifer_elasticity.json`: β0=−2.57e-5 ft/AF, β1=0.025/mile, N=491, 21 clusters) = **21 pumping districts = the 20 ag pumpers + the City of Bakersfield**.

**Bakersfield** is non-ag (municipal) and absent from crop/structural estimation, but KEPT in two PHYSICAL inputs: (1) the Kern River cascade as a senior pre-1914 appropriative right (~163,193 AFY, `build_kern_river_allocation_v2.py`, reserved at First Point before any ag tier — uses the legal entitlement, NOT demand); (2) the aquifer-elasticity calibration (aquifer responds to all extraction regardless of land use). Documented in the manuscript via a prose footnote on the first Table A1 mention (§2.3), the Kern River appendix (`app:institution`), and §3.3 wording changed from "ag-pumping" to "pumping districts". See [[settled_cf_rules]], [[aquifer_elasticity_calibration]], [[stage1p5_baseline_design]].

**KCWA** = wholesale SWP master contractor for 14 member units, but also delivers to farms in its own improvement districts, so treated as an ag district (in the crop/water-cost panels). Footnote at first mention (§3.2, line ~188).

**RESOLVED 2026-06-18:** the structural estimation genuinely uses **22 districts** — KCWA IS dropped. Verified directly: `results/B1d_ccp_firststage.pkl` has exactly 22 districts (230,339 decisions, 538 district-years), and `data/clean/mle_sample.dta` (canonical, NO `_v2`) has 23 incl. KCWA; the single difference is Kern County Water Agency. In code, `B1d_step1p5_water_allocation.py` lists `NON_AG_KR_USERS = {Bakersfield, Kern County Water Agency}`, so KCWA is treated as a non-ag/wholesale user and excluded from the crop-choice estimation (not for size — 4 smaller districts are kept). The §3.5 data prose and Table 2 were rewritten 2026-06-18 to lead with the 22-district / 538-dy estimation sample and state KCWA's exclusion; the line-~188 footnote was reversed from "I count it among the agricultural districts" to excluding it from estimation. Ladder: 25 entities → 24 ag (−Bakersfield urban) → 23 crop panel (−Rag Gulch) → **22 estimation (−KCWA)**; 18 of the 22 pump GW; depth-to-water panel 21 = those 18 + KCWA + Rag Gulch + Bakersfield. NOTE: canonical files are `mle_sample.dta` / `district_water_cost.dta` (no `_v2`) per [[data_v2_suffix_is_experimental_not_canonical]]. See [[project_table2_provenance_rebuild]].
