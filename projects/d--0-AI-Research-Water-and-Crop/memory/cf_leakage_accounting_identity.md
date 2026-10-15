---
name: cf-leakage-accounting-identity
description: "Leakage is NOT the traded volume; every CF cell shares the same 33.5 MAF surface endowment (bought==sold by construction, no out-of-county water); autarky strands 1.2 MAF"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
  modified: 2026-08-10T04:01:35.362Z
---

Leakage = county GW pumping under bilateral trade minus county GW pumping under autarky. It is the sellers' refill response, **not** the traded volume and not the buyers' extra consumption.

**There is no out-of-county water anywhere in the allocation.** In `calibrate_water_cost.run_year`, `SWP_sold = flows.sum(axis=1)` and `SWP_bought = flows.sum(axis=0)` come from the same LP flow matrix, so within-county bought == sold identically (observed panel `AC_kt_baseline.csv`: 0.887 MAF each side over 25 years). Never explain a consumption gap as imports.

**Every CF cell shares one endowment.** Settled rule R1/M1: `inputs["baseline_SW_kt"]` = each district's own allocation that it used or sold under the simulated baseline (`SWP_kept + SWP_sold + CVP_used + KR_used`), which excludes water bought in and excludes forfeited/unused Table A. County total **33.913 MAF**, identical across all nine cells (printed as the `[M1] Per-district endowment` line in every run log; do NOT infer it from bilateral SW use).

**Canonical county balance (post-2026-08-09 engine, MAF over 1998-2022):**

| | SW endowment | SW used | stranded | GW pumped | consumed |
|---|---|---|---|---|---|
| bilateral | 33.913 | 33.508 | 0.405 | 22.829 | 56.337 |
| autarky | 33.913 | 32.308 | 1.605 | 21.551 | 53.859 |
| difference | 0 | 1.200 | 1.200 | **1.278 = leakage** | 2.478 |

Bilateral strands 0.405 MAF of its own endowment, NOT zero. What trade recovers is the 1.200 MAF *difference* in stranding, not the whole autarky shortfall.

Trade raises consumption through **two** channels: it puts 1.200 MAF of otherwise-stranded surface water to use, and it induces 1.278 MAF of extra pumping. Only the second is leakage.

**Why autarky strands 1.200 MAF.** The four no-GW districts cannot move water across space and the model has no carryover, so in wet years their decision price sits at their own delivery rate (Belridge 1998: price 78.3 vs blend 78.0 — unrationed, holding more than it wants) while in drought years they are rationed at a scarcity shadow (Belridge 2015/2022: 636). Summed over the horizon they consume less than they hold and the surplus is forfeited.

See [[cf-price-init-and-autarky-override]] (the fix moved leakage 2.07 -> 1.28 MAF entirely through the autarky benchmark; bilateral and centralized cells are bit-identical) and [[counterfactual-results]].
