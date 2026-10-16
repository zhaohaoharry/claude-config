---
name: reference-ai-share-folder
description: "D:\\Dropbox\\AI\\AI_share is the user's phone-synced share folder (Dropbox, since 2026-10-15); copy PDF results there when asked to \"send\" them"
metadata:
  node_type: memory
  type: reference
  originSessionId: a92848a1-ac62-4dd2-9e7f-f902cdbb3c6e
  modified: 2026-10-15T14:21:35.382Z
---

Since 2026-10-15 the share folder the user reads on their phone is `D:\Dropbox\AI\AI_share` (Dropbox app on the phone). When the user asks to send/share/put PDF results "to the share folder" or "to my phone", copy the compiled PDF(s) there (copy, never move; keep the project copy as the source of truth), with a descriptive filename. Only result PDFs and documents go there, never data (see [[feedback_dropbox_shared_folders]] and the machines-and-sync rule: only `D:\Dropbox\AI\` belongs to this setup).

The old folder `D:\AI_share` is a Nutstore (坚果云) sync root; Nutstore stopped syncing on 2026-10-15 because the 0.AI migration to D:\0.AI removed the local folders of six other Nutstore roots, which pauses all syncing until they are relocated in the Nutstore window. The SendUserFile tool also works from the phone, but PDFs sent as attachments did not open there; images did.
