---
name: Citation management rule (all projects)
description: When citing any paper in an output file (tex, pdf, md), download it to literature/ and wire it through the bib
type: feedback
originSessionId: 989f0ece-2b64-4612-953b-46deb8ca9663
---
**Rule.** For every paper cited in any output file of any project (LaTeX, markdown, PDF), I must:
1. Find the most recent version online — the published version if the paper is published, otherwise the latest working-paper/NBER/SSRN version.
2. Download the PDF to the project's `literature/` folder.
3. Name the file `Author-Year-Journal-Paper Title.pdf` (e.g., `Colmer-Martin-Muuls-Wagner-2025-ReStud-Does Pricing Carbon Mitigate Climate Change.pdf`). For multi-author papers, concatenate author surnames with hyphens; drop diacritics from filenames.
4. Add a proper BibTeX entry to the project's `reference.bib`.
5. Replace any free-text citation in the tex file with a `\cite{...}` command that resolves against the bib.

**Why:** Hao wants verified primary-source PDFs on hand during research (not just citation strings he has to chase), wants consistent naming so PDFs sort by author, and wants the tex to compile with a proper bibliography rather than inline text.

**How to apply:**
- Any time I write or edit a tex/pdf/md output file that cites papers, before finalizing I check: does every citation have (i) a PDF in `literature/`, (ii) a bib entry, (iii) a `\cite{}` in the tex?
- When a citation is first introduced (either newly written or in a literature review), download the paper the same turn — do not defer.
- If the PDF is behind a paywall and no open version exists, flag that to Hao and put a placeholder note in the filename (e.g., `PAYWALLED-Author-Year-...pdf`) rather than skipping.
- Prefer the journal published version over NBER/SSRN working paper when both exist, unless the working paper is substantially more recent (within ~1 year of publication).
- Bib keys should be stable across projects: `authorSurnameYearKeyword` (lowercase, camelCase). Reuse existing keys in `reference.bib` if already present; do not duplicate.
