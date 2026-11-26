---
name: feedback_open_pdf_in_vscode
description: "Open compiled answer PDFs in the VS Code preview tab, not an external PDF viewer"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2c90432b-2125-4d8b-8592-c76b411c6b5b
  modified: 2026-11-25T03:14:26.599Z
---

When showing the user a compiled PDF (e.g. latex/answers/*.pdf), open it inside VS Code (`code -r <file.pdf>`), not with Start-Process / the system viewer.

**Why:** user reads the notes in VS Code's preview (stated 2026-11-25).
**How to apply:** every time an answer PDF is produced and the user should see it.
