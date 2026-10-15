---
name: Referee Service project setup
description: Working folder for all referee reports the user writes for economics journals; cloned GitHub repo lives inside it
type: project
originSessionId: 45d31b7e-be99-4a56-ba23-bd40b087896a
---
The folder `c:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Work\Referee Service\` is the user's hub for **all referee reports for economics journals**.

The GitHub repo `zhaohaoharry/Referee_Report` is cloned into the subfolder `Referee_Report\`. It contains one `.tex` file per report (e.g., `JEEM D24-00823.tex`, `JEEM-D-25-01438.tex`, `MS-SUS-2025-05438.tex`), shared style files (`paper.sty`, `appendix_online.sty`, `bibliography.bst`), and `reference.bib`.

**Why:** The user manages referee reports as a single corpus rather than per-paper folders — shared bib and style files, one repo, one place to look.

## Workflow for a new referee assignment

1. User drops the paper PDF (named with the manuscript ID, e.g., `JEEM-D-26-00394.pdf`) in `Referee Service\` root.
2. Create a per-paper working folder `Referee Service\[manuscript-id]\` (e.g., `JEEM-D-26-00394\`).
3. Copy `paper.sty`, `appendix_online.sty`, `bibliography.bst`, and `reference.bib` from `Referee_Report\` into the working folder.
4. Move the paper PDF into the working folder.
5. Draft the report as `[manuscript-id]_report.tex` inside the working folder (the `_report` suffix is critical — otherwise the pdflatex output `[manuscript-id].pdf` will overwrite the paper PDF, which has the same base name). Compile to PDF there.
6. **When the report is finalized:** move only the `.tex` file to `Referee_Report\` (the existing reports there use the bare manuscript-id name, e.g., `JEEM-D-26-00394.tex` — rename the file when moving) and commit/push, which syncs to Overleaf. The working folder stays local with the paper PDF and any scratch files.

## Report style conventions (from existing reports)

- `\documentclass[letterpaper,11pt,leqno]{article}`, `\usepackage{paper}`, `\bibliographystyle{bibliography}`.
- Title: `\title{\Large Referee Report on [Manuscript ID]}` (or `Report on ...` — both have been used).
- `\textbf{Manuscript Title:}` line under the title.
- `\section*{Summary}` with three paragraphs: (1) what the paper does, (2) what is timely/valuable, (3) major reservations.
- `\subsection*{Main Comments}` with `\subsection*{N. Title}` for each main point, using `itemize` for sub-bullets.
- `\subsection*{Minor Comments}` with `\begin{enumerate}` and bold lead-ins.
- Inline author-year citations (e.g., ``Sanders and Barreca, 2022''), no `\cite{}` — bibliography is commented out.
- Compile with `pdflatex -interaction=nonstopmode`, two passes.

**How to apply:** When the user assigns a new referee report, follow the workflow above before drafting. New reports get a new `.tex` file in `Referee_Report\` once finalized, following the journal-code + manuscript-ID naming pattern.
