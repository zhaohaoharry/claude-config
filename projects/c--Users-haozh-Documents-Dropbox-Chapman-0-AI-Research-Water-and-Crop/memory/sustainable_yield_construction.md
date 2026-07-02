---
name: Sustainable yield construction (CF2/CF3 SGMA cap)
description: Pro-rata SY_k = (1-rho)*avg_pump_k with rho=16% from BPW2024 + WEF2024; observed water-balance and C2VSim methods rejected as primary.
type: project
originSessionId: 8c3deae3-4980-49d5-aefe-33158566f878
---
Per-district sustainable yield SY_k for CF2 (SGMA cap) and CF3 (combined) is constructed by **uniform pro-rata reduction calibrated to published Kern Subbasin overdraft**. Script: `program/sandbox/B0_construct_sustainable_yield.py`. Output: `data/clean/district_sustainable_yield.csv` (21 GW-pumping districts).

**Primary (binding) — Method A:** `SY_k = (1 - rho) * avg_baseline_pumping_k` with `rho = 0.16`. Source: Kern Subbasin overdraft ~274,000 AF/yr (Water Education Foundation 2024) against 1998-2022 baseline aggregate pumping 1,745,454 AF/yr → 15.7%, rounded to 16%. Corroborated by Burlig-Preonas-Woerman 2024/2026 (NBER WP 28706 / Haas WP 349): 16.7% average pumping reduction needed across overdrafted CA basins (their sample includes Kern). Implied aggregate overdraft 279,273 AF/yr matches WEF 274k within rounding. Cap binds for 20 of 21 districts.

**Why pro-rata:** matches the form most Kern GSAs adopted in 2020/2025 GSP submissions; clean policy interpretation of SGMA's basin-level sustainability requirement (each district contributes proportionally to historic share of basin extraction); aggregate matches published numbers; immune to bank-stabilization measurement bias that plagued the per-district water-balance approach.

**Method B (alternative for robustness column, not primary):** observed water-balance, `SY_k^B = avg_pump_k - max(0, b_k*S_k*A_k)` with floor at avg pumping for passive small pumpers. Reported as `sustainable_yield_method_b_af` in CSV. Gives only 1.6% aggregate overdraft because Semitropic, Cawelo show bank-stabilized heads.

**Method C (NOT a cap, sanity reference only):** C2VSim `R_k_af_yr` from `district_aquifer_params.dta`. Zone-aggregated, attributed identically to all districts sharing `dominant_zone` (Bakersfield, Kern Delta, Tehachapi all show R_k = 350,096 because they share zone 20). Sigma R_k = 5.6 MAF/yr is implausible. Kept as `c2vsim_zone_recharge_af` for reference. **Do NOT use as the cap.**

**How to apply:** When implementing B4_counterfactuals.py CF2/CF3, read `sustainable_yield_af` column for the binding per-district cap and `cumulative_cap_af` for the 25-year cumulative budget (= SY_k * 25). Skeleton §7.5 paragraph "Construction of SY_k" (label `sec:cf_sy_construction`) has the formal definition matching the script. Robustness rho values flagged in skeleton openq: {0.10, 0.20, 0.25}; not implemented yet.

**Bib entries added:** `WaterEducationFoundation2024` and `KernSubbasinGSP2025` in `latex/model_refs.bib`. `BurligPreonasWoerman2026` was already there.
