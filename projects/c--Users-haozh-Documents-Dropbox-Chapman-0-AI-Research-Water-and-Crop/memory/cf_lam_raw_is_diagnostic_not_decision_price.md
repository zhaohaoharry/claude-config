---
name: cf-lam-raw-is-diagnostic-not-decision-price
description: "In cf_district_year_outcomes.csv, LAM_raw is a marginal-price DIAGNOSTIC that never reaches the Bellman; the decision price is MC_bellman (blend + one-way shadows), welfare uses AC_welfare"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
  modified: 2026-08-09T09:18:24.076Z
---

In `results/cf_district_year_outcomes.csv` the three price columns mean different things and I have twice mischaracterized the model by using the wrong one:

- **LAM_raw** = the allocator's internal marginal price (`lam_kt`). The engine comment (~line 1157 of `counterfactual_engine.py`) says it is "retained as a marginal-price diagnostic (LAM_kt) but no longer reaches the Bellman."
- **MC_bellman** = the decision price actually fed to the Bellman under production `CF_PRICING_RULE` (blended average cost + one-way scarcity shadows). This is what demand responds to.
- **AC_welfare** = realized floored average cost used in the welfare ledger.

**Why:** Under the adopted uniform pool closure ([[counterfactual-results]], POOL_CORNER="uniform"), in rationed years (centralized × cap × drought) EVERY pool trader's decision price is floored at the ONE common scarcity price, including districts with cap headroom and cheap pumping (Devils Den 2013: LAM_raw=$7, MC_bellman=$207). Cap slack arises because demand at the common price falls below the cap, not because those districts are priced at c_g.

**How to apply:** Never characterize what price "sets demand" or "prices a district" from LAM_raw. Use MC_bellman for decision-price claims, AC_welfare for welfare claims.

**Superseded 2026-08-09 (corner fix promoted):** the "do not reintroduce a per-district case equation" line above is withdrawn. A district with cheap pumping and a slack cap now gets a per-(district,omega) bisection price between its blend and the common P, and Appendix C carries `tab:cent_cap_positions` stating the three positions (no aquifer access, D(p*) >= cap, D(p*) < cap). The common p* still prices every rationed pool trader; the corner is the third row only.
