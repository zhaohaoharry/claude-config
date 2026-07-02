---
name: All empirical output must use real data, never fake numbers
description: Every table, figure, and welfare calculation must come from runnable code on real data — no placeholder or simulated numbers unless explicitly marked as simulation with real inputs
type: feedback
---

All empirical work — tables, figures, welfare numbers, calibration results — must be produced from code that runs on the actual project data. The user must be able to run the code and verify every number.

**Why:** The user needs to check accuracy personally. Fake or placeholder numbers erode trust and waste time.

**How to apply:** 
- Never hardcode regression coefficients, summary statistics, or welfare numbers in .tex files. Always generate them from code.
- If a simulation or calibration is involved, it must use real data as inputs (e.g., real reduced-form estimates, real catch data for calibration).
- If code cannot run because data is missing, flag it explicitly rather than inserting placeholder values.
- This rule applies to ALL research projects, not just this one.
