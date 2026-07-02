---
name: open-pdf-in-vscode-preview
description: "Always open compiled PDFs in the VSCode preview tab, never the system PDF reader."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0670748a-1e4c-4d37-8faa-a08ba44cb59c
---

When the user asks to open or reopen a PDF, open it in the VSCode preview tab with `code -r "<file>"`, never with `Start-Process` / the system default PDF reader.

**Why:** The user works inside the VSCode editor and wants the PDF rendered in an in-editor preview tab next to the source, not popped out in an external app like Adobe. The system reader is also more prone to file-lock issues that block recompiles.

**How to apply:** Use `code -r "<path-to-pdf>"` (reuse window) from Bash. Do not call `Start-Process`/`Invoke-Item` on a PDF. After a successful compile, this is how to surface the result. Related: keep the PDF closed in any external app before recompiling so MiKTeX can overwrite it.
