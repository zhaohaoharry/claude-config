---
name: Stage 1.5 baseline water-allocation design
description: Locked baseline structural design (2026-04-25): drops network and tau, adds Stage 1.5 institutional water allocation; supersedes the 2026-04-24 "no LP, uniform price" pivot.
type: project
originSessionId: 8c3deae3-4980-49d5-aefe-33158566f878
---
The headline structural baseline has 22 parameters (NOT 23): beta_W, beta_R, 8 alpha_c,
8 F_est, 4 F_rem. Network channel gamma_N is dropped from the headline payoff and
moved to robustness (CF1). Transaction cost tau remains dropped (no bilateral data
to identify it).

**Stage 1.5** sits between the original Stage 1 (SWP price specs) and Stage 2 (CCP
first stage). It produces `data/clean/AC_kt_baseline.csv` — a district-year panel of
average water cost AC_kt that becomes the structural regressor for Stages 2-4.

**Algorithm (deterministic institutional, NOT optimization):**
1. CVP delivery consumed by each district up to demand.
2. KR cascade: tier 1->4 by priority, unused cascades down (capped by AWMP).
3. SWP entitlement: pro-rata `a_t * E_k`. Each district uses own SWP first.
4. GW districts pump for own residual; never buy SWP.
5. Non-GW deficit districts buy from sellers via transportation LP minimizing
   total trade-distance. Seller's reservation: max(P_Option3, cost_GW) for GW
   sellers; P_Option3 for non-GW. GW sellers can sell up to full SWP allocation
   (replacing with own GW pumping).
6. Bill = sum of source-level costs for water actually consumed. Sales revenue is
   NOT netted — accrues to WD as institutional revenue, not farmer cost.

**Pricing:** Own-SWP at Option 1 (Bulletin 132 cost-recovery, ~$48-292/AF).
Inter-district transactions at Option 3 (calibrated market, ~$128-1106/AF) or
seller's cost_GW (whichever is higher). Both columns from
`SWP_KernAg_three_prices.csv`.

**Output validation (2026-04-25 run):**
- 575 ag district-years (4 non-GW + 21 GW); Bakersfield + KCWA flagged is_ag=0
- Water balance exact for ag districts (FP noise only)
- AC range: $15-$1076/AF; GW median $69, non-GW median $260, drought p99 $1063
- Correlation AC_nonGW vs (1-a_t) = 0.92
- 207 inter-district trades; drought-year revenue ~$28-100M per year

**Why:** This replaces both the τ-joint-identification proposal (Apr 23) and the
no-LP uniform-price simplification (Apr 24). The Stage 1.5 algorithm uses observed
KR/CVP/GW data plus a calibrated SWP price to fill in the missing piece —
within-Kern SWP allocation across the 13 KCWA member units.

**How to apply:** AC_kt_baseline.csv is the input regressor for Stage 2 CCP and
Stage 3 Euler-equation construction. Don't recompute AC from Bulletin 132 directly.
Don't use the legacy `district_water_cost.dta::AC_kt` — that's deprecated.
