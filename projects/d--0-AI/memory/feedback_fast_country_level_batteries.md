---
name: fast-country-level-batteries
description: "Keep multi-estimator DiD batteries fast - trended dCDH and TWFE only by default, parallel Stata instances per window"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-09-05T03:04:10.709Z
---

For country-level (or other small-panel) staggered-DiD batteries, do not run the full seven-estimator set by default. Keep BJS, TWFE, TWFE with unit trends, dCDH with `trends_lin`, and Sun-Abraham; drop the untrended dCDH and the detrended Callaway-Sant'Anna sensitivity unless asked. Split the run by window (or sample) into separate Stata batch instances launched in parallel, each writing its own results file, and concatenate afterwards.

**Why:** On 2026-09-05 the Carbon Pricing Policy country battery (148 cells x 7 estimators) took about two hours on a two-core Stata licence even though each cell is only ~4,000 country-years: `did_multiplegt_dyn` (run twice) and `csdid` with RIFs cost 10-20 s each per cell. The user asked that this be avoided in future.

**How to apply:** In programs like `44_country_panel_estimators.do`, take the window as an `args` parameter, default the estimator list to the five above, and launch one `StataMP-64.exe -e do ... <window>` per window in the background. Add the slow estimators only as an explicit option.
