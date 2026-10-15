---
name: fallow-handling-settled
description: "Fallow handling in the structural sample is SETTLED — drop zero-acre/no-permit fallow pixel-years, NO inheritance (the decision_id_fine convention); never re-ask"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

A pixel-year with no permit (fallow) carries no acreage and drops out of the acre-weighted estimation sample. There is **no exit-injection, no forward-fill of acreage into fallow years, and no inheritance** of a prior crop year's acreage. This is the `decision_id_fine` convention, and the manuscript appendix `app:plot_reconstruction` was rewritten to match it. The alternative (the `decision_id_v2` exit-inject + forward-fill inheritance) was tested and **rejected** for overstating fallow. See [[decision_id_v2_vs_fine_impact]].

**Why:** a permanent exit from the permit records is not idle cropland (the parcel may convert to housing or higher-value use), and a multi-year gap is not continuous fallow; the no-inheritance rule is the conservative, defensible choice.
**How to apply:** never re-ask how to handle fallow; never reintroduce inheritance or exit-injection. This is independent of the district-split work (which concerns non-fallow parcels straddling districts).
