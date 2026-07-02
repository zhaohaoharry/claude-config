---
name: Settled Counterfactual Rules (Water and Crop B4)
description: Rules that are FROZEN for the B4 counterfactual design. Do NOT change unless the user explicitly asks. The user has gotten frustrated when these are inadvertently broken while making other edits.
type: feedback
originSessionId: 78ced47c-e9ad-4b4d-84b1-a497ab260cb9
---
**FROZEN RULES — DO NOT CHANGE without explicit user request.**

**Why:** The user has been iterating on B4 counterfactual design across many turns. Each rule below is a deliberate decision they've made. When implementing a new fix, change ONLY the targeted rule; leave the others alone. The user has had to repeat themselves multiple times when I bundled unrelated changes.

**How to apply:** Before any edit to `program/sandbox/B4_counterfactuals.py`, check this list. If a proposed edit affects a rule below, STOP and confirm with the user.

## Settled rules

### R1 (REVISED 2026-05-10) — SW supply primitive per district = baseline B4 simulator output

In all CFs (CF1/CF2/CF3/CF4), each district's per-district SW endowment per year is `scen_base["SW_kt"][k, t]` — the baseline B4 simulator's actual SW delivery to district k year t. Sum across districts and years = 34.38 MAF (the same total SW use as baseline welfare reference).

Implementation: after `scen_base = run_scenario("Baseline", ...)` in `main()`, store `inputs["baseline_SW_kt"] = scen_base["SW_kt"]`. Modify `_own_sw_endowments(year, canon, inputs)` to read this when present and return per-district SW_owned from it. own_cost weight comes from panel proportions (`CVP_used × CVP_PRICE + KR_used × KR_PRICE + (SWP_kept + SWP_sold) × p_SWP_y) / total`).

Baseline B4 itself uses panel-attested forfeit-adjusted via run_year (rule R7 unchanged); _own_sw_endowments fallback path still returns panel forfeit-adjusted for legacy callers.

### R2 (NOW REDUNDANT) — Aggregate SW supply cap

Aggregate cap = sum of R1 per-district endowments = 34.38 MAF (ties to baseline B4 SW use by construction). The previous `supply_total_override = baseline_pool_supply_t` plumbing remains as a defensive guard but is mathematically redundant when R1 is set from baseline simulator output.

When the Walrasian pool is structurally short at all discrete λ values (balance < 0), DO NOT ration. Instead, raise λ to a scarcity-priced value above max($c_g$); the outer AC* loop drives demand down via Bellman until pool clears at the new equilibrium price.

### R3 — GW SGMA cap calibration

`gw_cap_sgma[k] = (1 - rho) × scen_base["GW_kt"].mean(axis=1)[k]` with `rho = 0.16`. Anchored at *simulator* baseline pumping (not panel). Per-district average across years (constant per district). Non-GW districts capped at 0.

### R4 — Autarky (CF1)

`alloc_autarky` uses `_own_sw_endowments` directly. **No CVP redistribution to formal Friant–Kern contractors.** Each district consumes own panel-attested supply, no inter-district SW trade. The five-formal-contractor pro-rata rule was removed earlier; do not reintroduce it.

### R5 — Buyer mask under CF3

CF3 uses `alloc_all_sw_pool` with `buyer_mask = (g == 0)` (only non-GW districts can buy from the pool). GW districts can sell but not buy, matching the bilateral-LP institutional restriction. CF4 has no buyer mask (all districts trade).

### R6 — Endogenous Walrasian pricing in CF2/CF3/CF4

In all three centralized regimes, the SW price λ\* is endogenous (Walrasian market clearing via bisection over $c_g$ values), with the partial-buyer mechanism for fine-grained clearing when balance > 0 at the bisection-found λ. Baseline and CF1 use externally calibrated prices (passive farmer); CF2/CF3/CF4 are scarcity-priced.

### R7 — Baseline B4 supply input (overrides for run_year)

`alloc_baseline` calls `run_year` with overrides:
- `swp_ent_override` with `E_k = SWP_kept + SWP_sold` (panel)
- `kr_override` with `KR_alloc = KR_used` (panel)
- `Q_deliv_SWP_override = sum(swp_eff)` per year

So baseline B4 also operates on the same forfeit-adjusted supply primitive as the CFs.

### R8 (NEW 2026-05-12) — Welfare formula = W3 (decision price ≠ welfare-ledger price)

Two prices per district-year, two distinct uses; no re-optimization in welfare.

- **Decision price `MC_bellman`** = converged Bellman input (the shadow). In `alloc_all_sw_pool` it's per-district: c_gw for unconstrained GW sellers (c_gw < λ AND GW_pumped < cap), λ for buyers and constrained sellers. Outer-loop shortage bumps apply to non-traders. This drives the CCP via the Bellman.
- **Welfare-ledger AC `AC_welfare`** = `max(0, bill / consumed)` per district-year. The rebate term `max(0, −bill)` captures cash inflow when bill < 0.

Welfare formula:
```
v_realized(c, s, k, t) = α_{s,c} + α_{k,c} + β_R π_c − β_W W_c · AC_welfare[k, t]
W[s, k, t]             = Σ_c CCP[c, s, k, ω_t] · v_realized(c, s, k, t)     # choice-consistent expected payoff
FS_iv                  = Σ_{plot, year} W[s_p, k_p, t] · A_p / |β_W|
FS_rebate              = Σ_{k, t} max(0, −bill[k, t])
FS_total               = FS_iv + FS_rebate
```

Notice: NOT an inclusive value `log Σ exp` — it's `Σ_c CCP × v_c`. The CCP comes from Bellman at MC_bellman (shadow); the per-crop payoff is evaluated at AC_welfare (realized cost). Water cost enters welfare exactly once via `AC_welfare`.

**Why R8 matters.** Prior W1 (Bellman PV-V) and W2 (static IV at MC_bellman + unfloored bill) both double-counted water cost when MC_bellman ≠ realized AC (i.e., in centralized cap-binding years where pool λ is high but actual cost paid is low). W3 separates the two prices cleanly.

Implementation anchor: `B4_counterfactuals.py` lines 519–546 (per-district MC_bellman), 936–966 (AC_welfare, rebate, MC_bellman_kt save), 952–1003 (W3 welfare aggregation).

## When changing rules

If a new fix proposal would change one of R1–R8, EXPLICITLY flag it to the user before implementing. Don't bundle.
