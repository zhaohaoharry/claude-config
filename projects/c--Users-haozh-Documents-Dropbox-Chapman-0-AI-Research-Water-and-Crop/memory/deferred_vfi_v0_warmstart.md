---
name: deferred-vfi-v0-warmstart
description: "EXECUTED 2026-08-10: V0 warm start in solve_vfi + BOTH engine call sites, all solves run to stated tol; unit-tested (44 vs 95 iters, same fixed point); in production since the 17.3%-target rerun"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
  modified: 2026-08-10T05:13:43.137Z
---

**EXECUTED 2026-08-10, folded into the 17.3%-target full rerun** (user's call, superseding the earlier defer-no-rerun plan). `solve_vfi` takes `V0`; BOTH engine call sites pass `V0=V` — the outer-loop site (tol=1e-4) and the final-consistent-pass site (tol=1e-5), which had also been budget-truncated at 50 cold iterations. Unit test: warm solve 44 iters vs 95 cold for a $2 price step, same fixed point (max|dCCP| 8e-6). Appendix E's warm-start sentences are now TRUE as written.

Historical defect: the engine's `V_warm` never reached `solve_vfi` (no `V0` argument existed); it only cut the iteration budget from 200 to 30, and those 30-iteration calls restarted from V=0 and exited unconverged (successive diff ~9.5e-2 vs the stated 1e-4), while Appendix E described a true warm start.

**Decision (user, 2026-08-10):** keep the Appendix E text as written, revise the code AFTER the bootstrap finishes (Windows spawn re-imports the engine per draw, so no edits mid-bootstrap), and do NOT re-run the grids.

**How to apply:**
1. After the RESTORE-AFTER-BOOTSTRAP items 1-3 (combine, table-only, macros), add `V0=None` to `solve_vfi` in `bellman_vfi.py` (init `V = V0.copy() if V0 is not None else np.zeros(...)`), pass `V` from `solve_year_equilibrium`, and drop the 30-iteration budget so every call meets tol=1e-4.
2. Measured stakes (scratchpad vfi_truncation_check.py): truncation moves CCPs ≤0.34pp, district demand 0.013%; calls cost 22ms truncated / 76ms full / ~5-12ms warm. Not worth a re-run.
3. Until the next full structural re-run, a re-execution audit reproduces committed artifacts only up to ~0.01% truncation wobble. This is EXPECTED and BENIGN, not an integrity problem. The next structural re-run absorbs it.

See [[cf-price-init-and-autarky-override]]; checklist item 5 in quality_reports/session_logs/2026-08-09_price-update-rule-fix.md.
