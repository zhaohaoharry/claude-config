---
name: reference-ai-share-folder
description: "Phone share folders: Nutstore D:\\AI_share is preferred (syncing again since 2026-10-16); D:\\Dropbox\\AI\\AI_share is the fallback. Copy PDF results there when asked to send them"
metadata:
  node_type: memory
  type: reference
  originSessionId: a92848a1-ac62-4dd2-9e7f-f902cdbb3c6e
  modified: 2026-10-16T07:42:08.481Z
---

When the user asks to send/share PDF results "to the share folder", "AI_share" or "to my phone", copy the compiled PDF(s) (copy, never move; the project copy stays the source of truth) with a descriptive filename.

**Preference (user, 2026-10-16): Nutstore first.** Put files in `D:\AI_share` (a Nutstore/坚果云 sync root). If Nutstore is not syncing, use `D:\Dropbox\AI\AI_share` (Dropbox app on the phone) instead. Check before relying on Nutstore: the client log `%APPDATA%\Nutstore\logs\Nutstore.Client.Wpf.log` prints "SyncRoot connected for D:\AI_share" when it is live.

History: Nutstore stalled on 2026-10-15 because the 0.AI migration removed the local folders of six other Nutstore roots, which pauses all syncing; Dropbox `D:\Dropbox\AI\AI_share` was used in the meantime. On 2026-10-16 15:39 the client restarted and reconnected all seven roots, D:\AI_share included. Only result PDFs and documents go to either folder, never data (see [[feedback_dropbox_shared_folders]]). The SendUserFile tool also works from the phone, but PDFs sent as attachments did not open there; images did.
