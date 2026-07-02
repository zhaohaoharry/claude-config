---
name: ownership-analysis-dropped
description: "Ownership / shared-farm-network analysis was CUT from the Water and Crop paper long ago; never use owner_id or networks, never mention ownership, archive all ownership code"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

The Water and Crop paper is the structural water/crop-choice model. The shared-farm-ownership / networked-ownership reduced-form analysis (the old "+10pp static network premium" headline) was **dropped from the paper long ago**. Never use `owner_id`, owner networks, "shared ownership", or any ownership variable in any analysis, and never mention ownership in prose, plans, or recommendations. Any ownership/network code must be **archived** to `program/archive/`. The crop acreage source is the owner-free `crop_plot_WD.dta`; `crop_plot_owner_WD.dta` and `data_prepare.do`'s owner merge are retired (not kept "for owner_id").

Ownership/network code to archive (confirm exact set with user before moving): `T003_rebuild_network.py`, `CVP_Share_Farm.do`, `WD_owner_network.do`, `improve_owner_matching*.py`, `RF_stylized_facts.py` (network-premium reduced form). KEEP structural/descriptive exhibits that merely shared the old data path (e.g. `RF_transition_table.py`, repointed).

**Why:** decided long ago but never written to memory, and the dead code still lives in the repo, so every fresh search resurfaces it as if live — this caused repeated wrong proposals to keep ownership.
**How to apply:** treat any `owner_id`/network consumer as an archive candidate, not a live dependency; never propose keeping ownership for any reason. Links [[fallow_handling_settled]], [[decision_id_v2_vs_fine_impact]].
