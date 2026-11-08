---
name: feedback_letter_update_format
description: "When the user asks for a letter update, report three lists by comment number - done to check, can be updated now, still waiting on runs"
metadata:
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-11-07T03:35:16.977Z
---

When the user asks for a response-letter update, answer with three lists by comment number: (1) comments done and ready for them to check, (2) what can be updated now with no run, (3) what is still running and which comments wait on it, with expected time.

**Why:** user, 2026-11-07: "when I aks for letter update, you tell me what comments are done, what can be updated, and what are running so I have a clear idea what to look while waiting for runs".

**How to apply:** build the lists from the live letter, PDF date and queue state, not from memory. A comment counts as done only if the compiled PDF shows it; say so when text is edited but the PDF is not rebuilt. Applies to response letters in any project.
