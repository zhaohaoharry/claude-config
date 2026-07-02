---
name: Auto-open generated PDFs in VS Code
description: After compiling any answer/equation PDF the user is meant to read, open it in VS Code immediately using Start-Process from PowerShell.
type: feedback
originSessionId: 78ced47c-e9ad-4b4d-84b1-a497ab260cb9
---
After successfully compiling a `.tex` file to PDF for the user to read, immediately open the resulting PDF in VS Code. Do not wait for the user to ask.

**Why:** The user wants to read the PDF without manually navigating to it in the file tree. They explicitly told me on 2026-05-05: "after you generate the pdf, directly open it in vs code."

**How to apply (Windows):**
- Use the PowerShell tool: `code -r "<absolute-pdf-path>"`. The `-r` flag reuses the user's active VS Code window. Reusing the window matters because:
  1. The PDF preview extension (`tomoki1207.pdf`) lives in the active workspace; a fresh VS Code instance launched via `Start-Process` may not load it and the PDF opens as raw binary instead of the preview.
  2. The user's active workspace context is preserved.
- Do NOT use `Start-Process code -ArgumentList "<path>"`. The user told me on 2026-06-03: "the pdf does not open correctly. and I only need the pdf to open in vs preview." The Start-Process variant launches a separate VS Code instance that may not render PDFs in preview mode.
- Do NOT use `code <pdf>` from the Bash tool — in this environment it resolves to a Node.js runner that tries to execute the PDF as JavaScript and fails with `SyntaxError: Unexpected token '%'` (the PDF header).
- Fallback if `code -r` is unavailable: `cmd /c code -r "<absolute-pdf-path>"`.

**Scope of "auto-open":**
- Yes, auto-open: answer files in `latex/answers/*.pdf`, `latex/ClaudeAnswer.pdf`, and paper PDFs the user explicitly asks me to view or share — but only the FIRST time, to get it on screen.
- No, do not (re-)open: routine paper recompiles (`paper_publication.pdf`, `paper_skeleton.pdf`) after every small edit — that would flood VS Code with tabs.
- **Once a PDF is already open in the VS Code preview, just recompile — the preview auto-refreshes on file change. Do NOT call any open command again.** The user said on 2026-06-20, while iterating on `program/PIPELINE_manual.pdf`: "no need to open in pdf reader later. I already open it in the vs preview. so when you recompile, it updates automatically." So during an iterative build-and-recompile loop, open once (or not at all if they already have it open), then only recompile on each subsequent edit.

**PDF preview note:** Native VS Code shows PDFs as binary files. The user may have or want the `tomoki1207.pdf` extension for inline PDF rendering. If they ever say "the PDF won't render" or "I just see binary," flag the extension as the fix.
