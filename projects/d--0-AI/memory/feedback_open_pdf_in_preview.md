---
name: feedback-open-pdf-in-preview
description: "After generating or rebuilding any PDF, open it in the VS Code preview automatically with `code -r <path>`"
metadata:
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-10-27T02:39:02.616Z
---

Every time a new or rebuilt PDF is produced (compiled answers, review documents, manuscripts, figures), open it in the VS Code preview right away with `code -r "<absolute path>.pdf"`. The tomoki1207.pdf and LaTeX Workshop extensions render it in an editor tab.

**Why:** the user checks every PDF by eye and asked (2026-10-27) for it to open automatically, without having to ask.

**How to apply:** run the open command as the last step after a successful compile. Skip it only when the build failed. Related: [[feedback_permission_prompts]].
