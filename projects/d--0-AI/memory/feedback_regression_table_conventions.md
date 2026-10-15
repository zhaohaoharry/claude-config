---
name: regression-table-conventions
description: "User's rules for regression tables — one regression per panel-column, explicit FE indicator rows, DDD must control all double interactions"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 366d52e4-00c4-455f-b6b6-aa97d4559cd9
  modified: 2026-08-22T03:54:03.020Z
---

Rules for regression tables in research papers/memos (stated 2026-08-21,
Carbon Pricing Policy project):

1. **Each panel presents one regression design.** Never stack rows from
   different regressions (different FE structures/designs) inside one
   panel. Columns within a panel may be separate regressions (standard
   columns-as-specifications), but a panel must be one design.
2. **Every panel/table must show the fixed effects controlled** (and
   other key controls) — as explicit indicator rows in the table body
   (e.g. "Pair FE: Yes / Year FE: Yes / Pair$\times$year FE: --"), not
   only buried in notes.
3. **DDD discipline:** in any triple-difference, ALL double-interaction
   terms must be controlled — either explicitly or absorbed by fixed
   effects — and the table/notes must make clear which FE absorbs which
   interaction. (User caught a missing basket$\times$year FE in a
   pair$\times$year DDD this way.)

**Why:** journal-standard legibility; a referee must be able to read the
identifying variation off the table. **How to apply:** when building any
multi-panel regression table, one design per panel, add FE rows to every
panel, and for DDD verify the full double-interaction checklist before
running.
