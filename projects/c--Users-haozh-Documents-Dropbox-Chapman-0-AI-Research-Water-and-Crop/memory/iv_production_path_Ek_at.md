---
name: iv-production-path-Ek-at
description: "Water and Crop: the ONE live structural water-cost IV is T1p3_stage4_robust_table_v2.py (z = E_k(1998)/A_k × a_t, no leave-one-out); two wrong variants (share×delivery T1p6, LOO v1) archived 2026-06-22"
metadata:
  type: project
---

The production structural water-cost IV is **`program/sandbox/T1p3_stage4_robust_table_v2.py`**, which writes
`latex/tables/tab_beta_W_robust.tex` (read by `manuscript_v1.tex`). It uses the shift-share instrument
`z_{k,t} = (E_k(1998) / A_k) × a_t` — 1998-fixed SWP entitlement per acre × statewide allocation **rate**
(`ENT_BASE_YEAR=1998`, `z_dec = (e_dec/a_dec)*alloc_dec`). **Leave-one-out is RETIRED**: under year FE it is an
exact linear function of the endogenous regressor (partial F 3.6e6 = mechanical collinearity, not strength). Text
and code agree.

**Two wrong IV variants were archived 2026-06-22 (user: "archive them, they are just wrong").** Do NOT re-read them
to check the IV, and do NOT let them trigger a code/prose mismatch flag — they are dead:
- `T1p6_iv_betaW.py` (now `program/archive/T1p6_iv_betaW_WRONG_share_x_delivery_20260622.py`): built
  `Z1 = (E_k/Σ E_l) × Q_deliv` (entitlement share × statewide *delivery quantity*), which collapses to a district's
  actual delivery — the construction the user rejected. This file misled an earlier mismatch flag.
- `T1p3_stage4_robust_table.py` v1 (now `..._v1_SUPERSEDED_by_v2_20260622.py`): spec (3) was the leave-one-out 2SLS;
  superseded by the v2 above.

To verify the IV, RE-RUN the v2 generator (never re-derive from a sandbox file). Relates to
[[feedback_verify_by_reexecution_not_rederivation]] and [[swp_delivery_entitlement_weighted]].
