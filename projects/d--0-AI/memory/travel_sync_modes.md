---
name: travel-sync-modes
description: "Travel sync folders are built on request per trip, in two flavours — presentation (LaTeX + results only) or working (plus program and current data)"
metadata:
  node_type: memory
  type: project
  originSessionId: 0a73e471-ad5d-46a8-9221-27dd2d33c900
  modified: 2026-10-15T10:35:26.281Z
---

The user travels with HMac and wants a travel copy prepared **only when a trip is actually being prepared** — not decided in advance, since a trip may be months away. When they say they are preparing to travel, ask which kind of trip and which project.

**Presentation trip:** they only need to build slides. Copy LaTeX sources, `figures\`, `tables\`, the `.bib`, the compiled PDF and any beamer files. No code, no data.

**Working trip:** they intend to run analysis or refine a design away from LaoZhao — the Double Clinching Auction experiment design is the example they gave. Copy the LaTeX material plus the program folder and the specific current data that work needs, at its latest vintage, not the whole `data\` tree.

**Why it matters:** the failure mode is a stale data vintage copied to HMac, edited there, and merged back over newer work. Confirm the vintage is current before copying, record what was copied, and set `TRAVEL_ACTIVE.md` to HMac at handover.

Destination is `D:\Dropbox\AI\Travel\<project>\`, under the rules in `~/.claude/rules/machines-and-sync.md`. See [[machine_names]] and [[feedback_dropbox_shared_folders]].
