---
name: factset-naics-vintage
description: FactSet supplier_naics_4 in this project uses the NAICS 2017 vintage (needed for any HS/ISIC concordance)
metadata: 
  node_type: memory
  type: project
  originSessionId: 50884341-1a39-409e-91a0-02b4e86a8c41
---

The `supplier_naics_4` codes in the Climate-Supply-Chain data are **NAICS 2017** vintage (180 distinct 4-digit codes).

**Evidence (from `data/supplier_city_ind_first.dta`, read 2026-06-07):** the code set contains `4523` (General Merchandise Stores incl. Warehouse Clubs/Supercenters, introduced in NAICS 2017) and `5173` (consolidated Wired+Wireless Telecom Carriers, 2017), while the 2012-only `4529` and the 2012 telecom codes `5171`/`5172` are absent. Not NAICS 2022 (retail still uses 44-45 codes like 4451/4523, not the 2022 449/455/457 renumbering). Minor anomaly: `4522` appears (non-standard in 2012/2017) — handle as a one-off in any crosswalk.

**Why it matters:** any HS-to-NAICS or NAICS-to-ISIC concordance (e.g., Pierce-Schott, R `concordance` package) for the BACI shift-share instrument must be matched to NAICS 2017, or one-to-many splits are misassigned at codes that changed between vintages. 87 of the 180 codes are tradable goods (sectors 11, 21, 31-33); the other 93 are services/non-tradable with no HS line. See [[climate-similarity-supplier-choice-project]].
