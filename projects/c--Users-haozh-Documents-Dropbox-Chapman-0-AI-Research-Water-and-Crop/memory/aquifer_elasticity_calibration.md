---
name: spatial-gw-head-elasticity-aquifer-beta-kj
description: "Calibrated spatial GW head response beta_0 = -2.57e-5 ft/AF, beta_1 = 0.025/mile (28 mi half-life), used in CF aquifer-update step. UPDATED 2026-05-31 to match production code; earlier 12-mile figure was an obsolete pilot run."
metadata: 
  node_type: memory
  type: project
  originSessionId: 6de2f577-1ca3-423f-8df3-7772a79528ba
---

The CF aquifer-update step in B4_counterfactuals.py uses a data-calibrated spatial GW head elasticity matrix `beta_kj = beta_0 * exp(-beta_1 * d_kj)` where d_kj is inter-district centroid distance in miles. Estimated from observed Δh and pumping panel.

**Script:** `program/sandbox/B0_calibrate_aquifer_elasticity.py`. **Output:** `results/B0_aquifer_elasticity.json`. **Figure:** `latex/figures/fig_aquifer_elasticity.pdf`.

**Estimating equation:** `Δh_{k,t+1} = α_k + beta_0 * Σ_j exp(-beta_1 * d_{kj}) * g_{j,t} + ε_{k,t}`. District FE α_k absorbs long-run head trend. Estimator: profile beta_1 over coarse grid + golden-section refinement; for each beta_1, beta_0 by within-FE OLS. Cluster-robust SE at district level (M=21).

**Production estimates (1998-2022 panel, N=491, M=21 districts; verified from `program/sandbox/log/B0_calibrate_aquifer_elasticity.log` on 2026-05-31):**
- `beta_0 = -2.571828e-05 ft/AF` (cluster-robust SE 3.339057e-06, t = -7.70)
- `beta_1 = 0.0250 per mile` (selected by SSR profile)
- Spatial half-life = ln(2) / 0.025 = **27.7 miles**
- Within R^2 = 0.117

**Why this differs from earlier memory:** an earlier pilot fit (β₀ = −1.32e-5, 12-mi half-life) appears in older session notes. The production simulation and Table 3 of the manuscript both use the current values above. The 12-mile estimate was from a partial run on a subset; do not cite.

**Use in B4 CF simulator:** `Δh_kt^CF = Σ_j beta_kj * (g_jt^CF - g_jt^base)`. Then `h_{k,t+1}^CF = h_{k,0}^obs + Σ_{s≤t} Δh_{k,s+1}^CF`. Then `c_k^g(h_{kt}^CF) = c_0 + c_1 * DTW_{kt}^CF` re-enters the within-year solver.

**Robustness pending (not implemented):** (a) include time FE to absorb statewide drought shocks; (b) cross-check against C2VSim Theis matrix in `aquifer_influence_matrix.dta`; (c) try alternative kernel forms (Gaussian, Matérn) instead of exponential decay.

**Skeleton:** results paragraph and Figure ref `fig:aquifer_elasticity` are in §7.4 right after eq.\ref{eq:aquifer_elasticity}.
