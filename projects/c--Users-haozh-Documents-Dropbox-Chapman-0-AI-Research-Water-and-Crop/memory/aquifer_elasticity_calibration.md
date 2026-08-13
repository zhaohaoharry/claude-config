---
name: spatial-gw-head-elasticity-aquifer-beta-kj
description: "Calibrated spatial GW head response, CANONICAL 2026-08-12: beta_0 = -2.64e-5 ft/AF, beta_1 = 0.013/mile (53 mi half-life), joint-NLS cluster SEs; earlier 0.025/28mi and -2.57e-5 vintages are superseded."
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
  modified: 2026-08-12T04:38:21.368Z
---

The CF aquifer-update step uses a data-calibrated spatial GW head elasticity matrix `beta_kj = beta_0 * exp(-beta_1 * d_kj)`, d_kj = inter-district centroid distance in miles. Estimated from observed Δh and pumping panel via `Δh_{k,t+1} = α_k + beta_0 * Σ_j exp(-beta_1 * d_{kj}) * g_{j,t} + ε_{k,t}` (district FE, joint NLS, cluster-robust at district level).

**Canonical output:** `results/B0_aquifer_elasticity.json` (produced by `program/2_structural/calibrate_aquifer_elasticity.py`, JSON mtime 2026-07-31). Values (verified 2026-08-12 against the JSON and Table 5 / prose macros):
- `beta_0 = -2.6407e-05 ft/AF`; conditional SE 3.43e-06 (t = -7.69); **joint NLS cluster SE 1.38e-05** (the pair Table 5 reports)
- `beta_1 = 0.0130 per mile`; joint SE 0.0234
- Spatial half-life = **53 miles**; within R² = 0.11; N = 432, 18 clusters

**Supersedes** two older vintages that appear in session notes: (β₀=-2.57e-5, β₁=0.025, 28-mi half-life, 2026-05-31 log) and a 12-mile pilot. Do not cite either; the manuscript (Table 5 `tab_param_taxonomy`, prose via `\AqBeta*` macros in `prose_macros.tex`) matches the JSON above.

**SE conventions:** manuscript prose and Table 5 use the JOINT NLS cluster SEs (`se_beta_0_joint`, `se_beta_1_joint`); the conditional `se_beta_0`/t=-7.69 also lives in the JSON. `\AqBetaOneSe` (0.0183) in prose_macros is a dormant macro not used in the manuscript.

Related: [[sensitivity-analysis-8cat-production]] (β₁=0.0130 confirmed there).
