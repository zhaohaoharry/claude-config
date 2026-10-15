---
name: cf-price-init-and-autarky-override
description: "CF solver: zero price init + autarky ratchet floor restricted to no-GW and cap-binding districts; certified by price==blend on unrationed GW district-years"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
  modified: 2026-08-09T09:18:39.872Z
---

The counterfactual solver's decision-price loop has two settings that were wrong until 2026-08-09 and are now certified.

- **Initialization.** `AC_curr = np.zeros(...)` at cold start (year t0 only; later years warm-start from the previous year's converged panel). The old `max(c_gw, 50)` start sat ABOVE equilibrium for cheap-pumping districts and pinned them there forever.
- **Autarky override.** The ratchet floor (`decision = max(decision, standing)`) applies only to `~gw_access | (cap-binding & gw_access)`. It used to be all-True under autarky, which floored districts that emit no quantity signal.

**Why:** an unrationed groundwater district always meets demand by pumping, so neither the excess-demand nor the excess-supply branch ever fires for it. With a floor, nothing can pull its price back down, so a bad start or a stale drought-year price persists. Rationed districts self-correct from any start, which is why the floor is still needed for them (their blend is an average cost over a fixed endowment and never responds to a shortage).

**How to apply:** the acceptance test is `MC_bellman == AC_welfare` on unrationed GW-access district-years in `autarky_open` (0 of 425 above $1, max $0.015). `baseline_open` is the negative control and always passed, which is what proved the damped two-sided update was fine and localized the bug to the override. Cap cells legitimately fail this test on cap-binding rows.

**Impact when fixed:** leakage 2.07 -> 1.28 MAF, autarky net at sigma=1000 +$585M -> +$88M, crossover $717 -> $931, autarky tax $65 -> $150, autarky cap x 0.103 -> 0.16. Other cells moved little; centralized_cap +$32M. See [[counterfactual-results]] and [[cf-lam-raw-is-diagnostic-not-decision-price]].
