---
name: deferred-vfi-v0-warmstart
description: "DECIDED 2026-08-10: after bootstrap completes, add V0 warm start to solve_vfi + engine, run VFI to true 1e-4; NO re-run; expect benign ~0.01% diffs on next re-execution"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
  modified: 2026-08-10T02:08:22.666Z
---

The engine's `V_warm` never reaches `solve_vfi` (no `V0` argument exists); it only cuts the iteration budget from 200 to 30, and those 30-iteration calls restart from V=0 and exit unconverged (successive diff ~9.5e-2 vs the stated 1e-4). Appendix E describes a true warm start.

**Decision (user, 2026-08-10):** keep the Appendix E text as written, revise the code AFTER the bootstrap finishes (Windows spawn re-imports the engine per draw, so no edits mid-bootstrap), and do NOT re-run the grids.

**How to apply:**
1. After the RESTORE-AFTER-BOOTSTRAP items 1-3 (combine, table-only, macros), add `V0=None` to `solve_vfi` in `bellman_vfi.py` (init `V = V0.copy() if V0 is not None else np.zeros(...)`), pass `V` from `solve_year_equilibrium`, and drop the 30-iteration budget so every call meets tol=1e-4.
2. Measured stakes (scratchpad vfi_truncation_check.py): truncation moves CCPs ≤0.34pp, district demand 0.013%; calls cost 22ms truncated / 76ms full / ~5-12ms warm. Not worth a re-run.
3. Until the next full structural re-run, a re-execution audit reproduces committed artifacts only up to ~0.01% truncation wobble. This is EXPECTED and BENIGN, not an integrity problem. The next structural re-run absorbs it.

See [[cf-price-init-and-autarky-override]]; checklist item 5 in quality_reports/session_logs/2026-08-09_price-update-rule-fix.md.
