---
name: cf-decision-price-acpass
description: ADOPTED 2026-07-28 — CF decision price = district blended average cost (option B) + shadow ratchet; frozen-buyer-price bug history; guardrails; marginal rule kept as CF_PRICING_RULE=marginal sensitivity
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
  modified: 2026-07-28T03:38:53.077Z
---

Production CF pricing (counterfactual_engine.py, adopted 2026-07-28): the Bellman
decision price is the district's endogenous floored-at-0 blended average cost
(estimation's exact price concept), with the excess-demand ratchet supplying
scarcity shadows (cap-binding, autarky rationing). Districts trade/pump at the
margin inside allocators. GW access comes ONLY from the roster
(`inputs["gw_access_mask"]`, from district_sw_supply.dta GW flag) — never from
`cost_GW > 0` (hypothetical lift cost, positive for all 25 districts; that test
froze buyers at ~$50 for 25 yrs and inflated leakage to 3.25 MAF). Panel anchor
default `CF_PANEL_ANCHOR=mean` (1998 states, district acreage rescaled to sample
mean). Cycle-averaging damping (midpoint when update direction flips) cured the
drought-year blend limit cycle and cut grid runtime 80→17 min.
`CF_PRICING_RULE=marginal` re-enables the cheapest-source marginal rule, used
only for the rate-design counterfactual in sensitivity (B4_OUT_SUFFIX=_pricefix;
bilateral trade collapses to 0.04 MAF, leakage migrates to the pool +2.93).
Guardrails in run_scenario: no-GW pumps zero (hard), buyer price >= 0.8x blend
while buying (blend rule only), freeze detector for no-GW. Standing audits in
program/sandbox/leak_decomp/ (audit_marginal_prices.py, attribution_run.py).
Baseline-fit validation is tab:baseline_fit via build_baseline_fit.py — trade
0.94 vs 0.89, buyer demand −0.4%, blended cost $173 vs $171, all untargeted.
Related: [[settled-cf-rules]], [[counterfactual-results]].
