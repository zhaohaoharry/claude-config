---
name: Counterfactual analysis (B4) headline results
description: B4_counterfactuals.py runs 4 scenarios on Stage 4 + Stage 2 closures; CF1 dominates by FS, CF3 by aquifer benefit; sigma_calib = $51.85/AF-ft.
type: project
originSessionId: 8c3deae3-4980-49d5-aefe-33158566f878
---
`program/sandbox/B4_counterfactuals.py` runs Baseline + CF1 (all-SW market) + CF2 (SGMA cap, institutional SW) + CF3 (combined). Outputs: `results/B4_cf_results.json`, `results/B4_district_year_outcomes.csv`, `latex/tables/tab_counterfactuals.tex`, `latex/figures/fig_cf_outcomes.pdf`. Wall time ~17s. Skeleton §7 "Counterfactual Results" embeds the table and figure.

**Key implementation decisions (substantive, may need revisit):**
- **Hard annual cap, not Lagrangian cumulative.** Initial Lagrangian shadow-price approach failed because: (a) MNL beta_W=0.0007 is small, demand response too weak; (b) Stage 1.5 institutional allocator pumps GW = D - SW regardless of cgw cost; (c) non-CCP districts (3 of 25) have completely inelastic demand. Switched to hard annual cap g_kt <= SY_k = sustainable_yield_af. AC under cap inflated by scarcity multiplier D/(SW+cap) so within-year MNL response brings demand toward effective supply.
- **Field state held at observed throughout (short-run, BPW-style).** Forward-simulating field-state dynamics under CF deferred.
- **Welfare ledger via revealed-preference sigma calibration** (user-specified): sigma_calib = -DeltaFS_CF2 / sum(area * delta_dtw_CF2) = $51.85/AF-ft, so DeltaW_CF2 = 0 by construction. Apply same sigma to CF1 and CF3.

**Headline results (1998-2022, with same-SW-supply constraint AND per-district market-clearing AC bisection):**
- Baseline: cum GW = 29.5 MAF, mean AC = $123/AF
- CF1 all-SW market: cum GW = **31.0 MAF (+1.5 MAF leakage)**, AC = $67, FS = +$3.6B, head -3.5M AF-ft, ΔW = +$6.4B
- CF2 SGMA cap: cum GW = 25.3 MAF, demand drops to 54.2 MAF (4 MAF fallowing!), AC = $555, FS = -$18.4B, head -23.1M AF-ft, ΔW = $0 (calib)
- CF3 combined: cum GW = 24.7 MAF, demand drops to 52.6 MAF (5.5 MAF fallowing), AC = $735, FS = -$18.4B, head -38.6M AF-ft, ΔW = **+$12.3B (best)**

σ_calib = $796.52/AF-ft (CF2 welfare-neutral). CF3 ΔW nearly doubles CF1 ΔW: COMPLEMENTARITY confirmed.

**Same-SW-supply constraint (user-specified):** pool size per year = baseline total SW used (28.6 MAF / 25 yr = 1.146 MAF/yr), NOT institutional CVP+KR+SWP supply (which would unlock banked SWP). Without this constraint, CF1 banking-unlock dominates and CF1 GW falls below baseline — which contradicted the user's economic intuition. With the constraint, CF1 shows the textbook leakage: low-c_gw districts pump more after losing SW endowment to the pool.

**Per-district decomposition under CF1 (with same-SW constraint):**
- Leakage (low-c_gw districts pump more): +12.1 MAF over 25 yr (Kern Delta +3.2, Lost Hills +2.9, North Kern +1.8, Belridge +1.3, etc.)
- Substitution (high-c_gw districts pump less): -10.9 MAF (Wheeler Ridge -5.3, Arvin -2.3, Cawelo -2.1, Semitropic -1.1)
- Net: +1.2 MAF (small but positive)

**Surprising finding (still): market-cap substitutability, not complementarity.** ΔW_CF1 + ΔW_CF2 = $3.9B > ΔW_CF3 = $2.0B. Reason: CF3's binding cap forces inefficiently high water cost on binding districts (mean AC $159), and the additional aquifer benefit beyond CF1 is valued at σ_calib = $51.85/AF-ft which is too low to justify the FS hit. A higher σ would favor CF3.

**Stock externality non-intuition under CF1:** despite +1.0 MAF more pumping, CF1 has lower area-weighted Δh than baseline (head IMPROVED on average). This is a SPATIAL effect: pumping shifted from large-area pumpers (Wheeler Ridge, Arvin, Cawelo, Semitropic) whose local heads recover, to smaller-area pumpers (Lost Hills, Belridge) whose local heads fall. Area-weighted average dominated by the big pumpers.

**Robustness needed (flagged in skeleton openq):** (a) tighter cap shares rho ∈ {0.20, 0.25}; (b) Lagrangian formulation with cumulative budget; (c) 13-state field state per BPW; (d) Pigouvian wedge sigma sensitivity for an appendix.

**Bug pattern to remember (importing B1d_step1p5 + B1d_step2_ccp):** Both modules wrap sys.stdout at module load. Chained wrapping closes the buffer; subsequent print() raises ValueError. Workaround in B4: `sys.stdout = open(1, "w", encoding="utf-8", buffering=1, closefd=False)` AFTER the imports, and a custom log() function that writes to the freshly-reopened sys.stdout.
