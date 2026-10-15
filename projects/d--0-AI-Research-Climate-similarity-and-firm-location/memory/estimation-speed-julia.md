---
name: estimation-speed-julia
description: "For HDFE Poisson / conditional-logit on this project's large choice panel, Julia GLFixedEffectModels is ~17x faster than the 2-core Stata license; pyfixest is the Python fallback"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 50884341-1a39-409e-91a0-02b4e86a8c41
---

**The heavy conditional-logit / Poisson-HDFE estimation should move OFF Stata.** Benchmarked head-to-head 2026-06-12 on this project's data (full choice panel, `establish ~ z_cli_dis_7bio + ln_distance + fe(decision_id) + fe(scity_sind_yid)`, two-way clustered centroid+decision_id). Root cause of Stata's slowness: **StataMP here is licensed for only 2 cores on a 20-core machine.**

| Tool | full-sample fit | McFadden 5.4M | coef |
|------|------|------|------|
| Stata ppmlhdfe (2-core) | ~50 min | ~min | −0.0177577 (baseline) |
| pyfixest fepois (Py, 20-core) | >20 min | 56.9s | matches |
| **Julia GLFixedEffectModels** | **171s (2.85 min)** | **7.9s** | EXACT to 7 dp |

**Julia GLFixedEffectModels.jl is the winner — ~17x over Stata, ~7x over pyfixest, exact coefficient match.** (This OVERTURNED the reputation-based prior that Julia's GLM-FE is immature/not-worth-it; measuring corrected it. FixedEffectModels' LSMR demeaner is just fast.)

**Setup already done (this machine):** Julia 1.12.6 at `C:\Users\haozh\AppData\Local\Programs\julia-1.12.6` (installed alongside the old 1.9.4, non-destructive; 1.12 caches precompile so the first-use tax is paid once). Packages in the `@bench` shared project: `GLFixedEffectModels, DataFrames, Arrow, GLM, Vcov`. Run: `"<julia-1.12.6>/bin/julia.exe" --project=@bench -t auto script.jl`. API: `nlreg(df, @formula(y ~ x + fe(id1) + fe(id2)), Poisson(), LogLink(), Vcov.cluster(:c1,:c2))`.

**Workflow that makes it fast:** (1) export the slim Stata panel to **Arrow** once (`pandas df.to_feather`) — loads in 0.2–4s vs 15s for .dta; `data/temp/sim_panel6.arrow` (full) and `sim_panel_mcf.arrow` (McFadden 30-sampled, 5.4M) already built by `program/sandbox/export_arrow.py` / `export_mcf_arrow.py`. (2) Develop on the **McFadden-sampled** file (consistent under IIA) → seconds per spec; reserve the full panel for final tables. Bench scripts: `program/sandbox/bench_julia_*.jl`, `bench_pyfixest*.py`. Full writeup: `quality_reports/2026-06-12_estimation_speed_benchmark.md`.

**Bonus:** Julia/pyfixest use a different demeaner than ppmlhdfe, so they should run the **country-FE conditional LOGIT that Stata's IRLS reproducibly hung on** (see [[run-programs-background-bash]]) — recovering the logit, not just the reghdfe LPM proxy. Caveats: pyfixest is the zero-setup Python fallback (coauthor's stack) but ~7x slower; for pure LINEAR/LPM specs `FixedEffectModels.jl` (the linear parent) is even faster than the GLM version. Always validate a migrated spec reproduces the Stata coefficient (all did).
