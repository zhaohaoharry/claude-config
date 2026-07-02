---
name: lag-state-split-in-decision-id
description: "Water and Crop: perennial maturity (young/mature/other) is a per-dot lag_state folded into decision_id_fine; mixed parcels SPLIT not collapse; missing t-2 = mature"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

Since 2026-06-22, the plot decision key carries perennial maturity. `create_sampling_dots.py` (D1) computes
per dot a `crop_cat_lag2` (= `crop_cat_lag` shifted one more consecutive year within `dot_id`) and a
`lag_state ∈ {young, mature, other}`, and `decision_id_fine = PMT_SITE × year × crop_cat_lag × district ×
lag_state` (decision_id_broad gains it too). `build_plot_panel.py` (D2) reads `crop_cat_lag2`/`lag_state` from
D1 (no longer recomputes) and carries `lag_state` through the collapse.

**lag_state rule:** annual/fallow lag → `other`; perennial lag with t-2 missing OR == lag → `mature` (missing
t-2, e.g. 1998, is **left-censored to mature**, per paper §7.3); perennial lag with a different t-2 → `young`.
This reproduces the 13-state field state `s_idx_13` (mature perennials 0–3, annual/fallow 4–8, young perennials
9–12) as a function of (crop_cat_lag, lag_state).

**SETTLED — do not revisit:** mixed parcels (dots partly young, partly mature) are **SPLIT** into a young plot
and a mature plot, NOT collapsed to mature. Decided after diagnostic (`program/sandbox/diag_mixed_lagstate.py`):
only ~2% of perennial cells are mixed (+0.9% decisions to split), but collapse-to-mature would mislabel ~15% of
all young acreage (young is just 2.9% of perennial acreage), on the planting margin the state exists to capture.
Splitting is near-free because the estimator is acre-weighted.

**Why:** the old `decision_id_fine` keyed only on the t-1 crop, so it pooled young+mature perennials and the
collapse picked the plot's state by an arbitrary `"first"`. Folding lag_state in makes every cell a single clean
field state and the `"first"` carry exact.

**Downstream still to repoint (user drives, not done):** A5 (`A5_water_cost.py`), A10
(`A10_build_mle_sample.py`), B1d (`B1d_step2_ccp.py`) collapse on `decision_id_fine` and will now produce split
cells; B1d's own `crop_cat_lag2`/`s_idx_13` recompute becomes redundant-but-consistent and could read
`lag_state`. Full structural rerun needed; estimates will move (perennial values / switching costs). Relates to
[[notation_convention_model]], [[feedback_focused_scope_not_cascade]].
