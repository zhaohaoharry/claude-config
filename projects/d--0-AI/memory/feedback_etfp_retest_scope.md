---
name: feedback-etfp-retest-scope
description: ETFP re-tests after the sample fix - symmetric cleaning and transition rules stay fixed; test bounds, FE, IV set, trim symmetry on F0 and F3, few trims and thresholds
metadata:
  type: feedback
---

When re-testing earlier ETFP experiments on the fixed sample (tw95l), keep the symmetric cleaning rules and the transition rules as they are. Test only the bounds, FE, IV set and trim symmetry, with a small number of trims and transition thresholds, and on ladder steps F0 and F3 first.

**Why:** user, 2026-11-07: many earlier decisions are not to be changed, and the grid should stay small.

**How to apply:** propose a short list of cells before running. Related: [[feedback_etfp_trim_order]], [[feedback_etfp_ladder_drops_everywhere]].
