---
name: feedback-dropbox-shared-folders
description: Never delete or alter anything already in the Dropbox root — those folders are shared with collaborators
metadata:
  node_type: memory
  type: feedback
  originSessionId: 0a73e471-ad5d-46a8-9221-27dd2d33c900
  modified: 2026-10-15T07:23:10.761Z
---

Never delete, move, or alter folders that are already in the user's Dropbox root (`D:\Dropbox`, the live personal Pro account). They are **shared folders with collaborators**, not local clutter — including leftovers at the old root `C:\Users\haozh\Dropbox` after the folder move of 2026-10-15. Only touch what this setup created, such as `D:\Dropbox\AI`.

**Why:** a deletion inside a shared Dropbox folder propagates to everyone it is shared with, so a wrong guess about "remnants" reaches other people's machines. The user also manages per-machine sync themselves (those folders are already excluded from sync on the laptop H2), so an unsynced or duplicated-looking folder is a deliberate setting, not a mistake to clean up.

**How to apply:** report what is there and leave it alone; do not offer to tidy the Dropbox root. Ask before any write inside it outside `AI\`. See [[scalable_computing_2026_10]] for what this setup legitimately owns there.
