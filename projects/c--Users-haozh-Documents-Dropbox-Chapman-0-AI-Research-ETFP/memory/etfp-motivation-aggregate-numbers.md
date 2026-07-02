---
name: etfp-motivation-aggregate-numbers
description: Verified aggregate China-industry numbers used in the ETFP opening motivation (computed from raw ASIE+CESD)
metadata: 
  node_type: memory
  type: reference
  originSessionId: c3dae0d6-96ef-491d-953c-724c0ebc0469
---

Aggregate facts in the ETFP opening paragraph, computed from raw ASIE+CESD (see [[etfp-raw-data-location]]), 2000–2008:

- Above-scale industrial firms: **162,885 → 411,407** (≈163k → 411k).
- Total employment: **55.6M → 84.7M** (+52%).
- Full-sample nominal gross output: 8.6 → 48.9 trillion RMB (5.7×) — **contaminated** by sample expansion; do not quote as growth.

**Balanced CESD panel (5,225 plants present every year)** — coverage-consistent, used for Figure 1 (`Figure/decoupling_aggregate.pdf`):
- Real output: **+175%** ("more than doubled"). Deflated by NBS ex-factory PPI, chained 2008/2000 ≈ 1.25 (YoY 98.7,97.8,102.3,106.1,104.9,103.0,103.1,106.9).
- SO₂ emissions: **+12%** ("rose only modestly", hump at 2005, recedes after).
- Emission intensity (SO₂/real output): **−59%** ("close to 60 percent"). Nominal-output basis would be −67%; robust to PPI choice (−58% to −61%).
- Corroboration: China Statistical Yearbook real industrial value added ≈ 2.4× by 2008 (+140%).

Green patents (firm_patent.dta, by calendar `year`): **93 → 2,531 = 27×** ("more than 25-fold"). All patents 1,078 → 35,215 (33×).

Reproducible scripts in `program/sandbox/`: `aggregate_china_industry.py`, `balanced_aggregate.py`, `decoupling_aggregate.py`, `verify_green_patent.py`. Note: the within-firm decoupling (`decoupling.pdf`) was **rejected** by the user — motivation must use aggregate numbers, not within-firm.
