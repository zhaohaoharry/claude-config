---
name: res-rejection-fact-check-2026-11
description: "RES rejected MS-39111 (Nov 2026); fact check confirmed referees on the average-cost price, Kern River allocation and several wrong inputs; rebuild plan drafted"
metadata:
  node_type: memory
  type: project
  originSessionId: f36c3e39-09db-4483-89d6-c626fc1ce2ad
  modified: 2026-11-19T02:19:50.329Z
---

RES rejected the paper (MS-39111) with two reports; state as of 2026-11-19. Supersedes the "prepare
RES submission" state in [[res-submission-package]].

Fact check of the submitted `latex/manuscript_res.tex` lives in
`quality_reports/fact_check_2026-11-19/` (six blocks + archived source PDFs); plan in
`quality_reports/plans/2026-11-19_res-rejection-evaluation-and-revision-plan.md`.

Confirmed problems (do not re-defend these):
- Average-cost decision price is contradicted by district documents: surface water is rationed pro
  rata, most growers' margin is a private well, west-side drought purchases are invoiced to
  subscribing landowners at cost. Only Arvin-Edison, North Kern, Cawelo price near average cost. The
  Kern-Tulare and Wheeler Ridge "blended/melded" quotes do not support the paper.
- Kern River: Miller-Haggin is a 1/3–2/3 proportional split above 300 cfs, not a cascade; priority
  (Shaw Decree) applies only within First Point (Kern Delta > City > North Kern); 6 of 10
  entitlements in `kr_first_point_rights.csv` mis-sourced; observed diversions exist in the City of
  Bakersfield Kern River Hydrographic Annual Reports.
- `data/clean/SWP_allocation_year.dta` has 2012 = 0.35 (DWR 65%) and 2024 = 0.10 (40%).
- `swp_transfer_price_records.csv` has transcription errors vs the board-minutes scans.
- Uncited antecedent: Knapp, Weinberg, Howitt, Posnikoff (2003, JEM), Kern County.

**Why:** the user wants every policy/institutional claim in the next version mapped to an actual
document, assembled into a policy appendix.

**How to apply:** treat the fact-check blocks as the claim register; a claim counts as verified only
with a document opened and a page cite; scan/OCR readings need a second read. Referee 2's report was
pasted in chat and may not be on disk.
