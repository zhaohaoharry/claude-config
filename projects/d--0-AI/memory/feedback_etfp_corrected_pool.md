---
name: feedback_etfp_corrected_pool
description: ETFP runs always use the corrected trim pool (mode sc), never the old std pool
metadata:
  type: feedback
---

Every ETFP estimation runs on the corrected trim pool, mode sc in 331_gmmtrim_unit.py: all rows with e stay in the pool, single-firm-year firms included, and the under-30 cell test counts only rows with e. Never run or queue a std or sa unit, including restarts and bootstrap units.

**Why:** the user, 2026-11-07: "Always run corrected pool never the old pool." The old pool lost single-firm-year rows through a dropna on firm-FE residuals that the trim does not use.

**How to apply:** before packing any unit, confirm the trim mode field is sc. Do not report std results as candidates; rerun on sc if one is still needed. The gt and gl modes are separate requested designs with their own pool, not the old pool. Related: [[feedback_etfp_ladder_drops_everywhere]], [[feedback_etfp_retest_scope]].
