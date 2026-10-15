---
name: word-com-pdf-export-visible
description: Word docx→PDF via COM hangs with Visible=$false on this machine; use Visible=$true
metadata: 
  node_type: memory
  type: reference
  originSessionId: 45dc5155-e6a9-4f38-9aa5-dbf9e0b22af2
---

On this Windows machine, exporting a .docx to PDF through Word COM (`ExportAsFixedFormat($pdf,17)`) **hangs indefinitely at high CPU when the Word instance is `Visible=$false`** — even for a trivial one-line document. `Documents.Open` and `ComputeStatistics` still work hidden; only the PDF export path hangs (likely an invisible app-level modal). Killing/retrying does not help; it is not content-, font-, or equation-related.

**Fix:** create the Word.Application with `$w.Visible=$true`, then `ExportAsFixedFormat`. Wrap in a `Start-Job` + `Wait-Job -Timeout 120` so a hang is recoverable, and `Stop-Process -Force` any leftover WINWORD afterward. The visible window flashes briefly but the export completes in seconds.

Secondary gotcha: a **network default printer** (e.g. "HP DJ Plus 6000 ... (网络)") can also stall Word's pagination; switching the default to "Microsoft Print to PDF" before export and restoring it after avoids that. Restore the user's original default printer when done.

Used by the 北社科 / grant-proposal build pipeline (`build_lyn.py`, `build_v2.py`) and any LaTeX-adjacent Word task. PowerShell COM only — LibreOffice (`soffice`) is not installed here.
