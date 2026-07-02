# Global Configuration — Chapman University Economist

## User Profile

- **Institution:** Chapman University
- **Role:** Economist (researcher + teacher)
- **Tools:** LaTeX/MiKTeX (Windows), Stata, R, Python, MATLAB, Julia
- **Primary language:** English

## Master Resource Files

| File | Purpose |
|------|---------|
| `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_Academic.md` | Academic prose rules (the *surface* layer — removes AI tells) — load before editing any paper |
| `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_EconCraft.md` | Positive craft layer (flow, rhythm, voice, intuition-first, number-argument) — load alongside the academic guide when writing/refining/polishing prose |
| `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\econ_prose_exemplars.md` | Verified real exemplar passages of good economics prose, organized by craft move |
| `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_Email.md` | Email style guide |
| `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\master_catalogue.md` | Cross-project session log |

## Working Directory Layout

```
C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\
  Research\      ← one subfolder per research paper
  Teaching\      ← one subfolder per course
  Work\          ← department and administrative tasks
  Others\        ← ad hoc tasks, paper briefs, misc
  Claude Master\ ← shared resource files
```

## Central Research Data Repository

All shared raw datasets live in **`D:\0. Research Data\`**, organized into 13 numbered categories: 1. Firm · 2. Survey & Household · 3. Environment & Climate · 4. Innovation & Patents · 5. Administration & Public Finance · 6. Government Behavior · 7. Health & Medical · 8. GIS, Maps & Land · 9. Macro & Regional Statistics · 10. Agriculture & Rural · 11. History & Culture · 12. Text & NLP · 13. Transport & Infrastructure.

- **The index ("menu") is `D:\0. Research Data\DATA_CATALOGUE.md`.** When the user asks you to find, locate, or use a dataset, **read that catalogue first** — it maps every topic / unit level → dataset → exact folder path.
- **Reference data in place** via its absolute path. **Never copy a raw dataset into a project folder** (that is what bloats the drive). Save only derived/cleaned extracts inside the project, and record the source path in the project's code.
- Folders use clean English names; the original Chinese names and the old→new crosswalk live in the catalogue and in `D:\0. Research Data\_ORGANIZATION\rename_log.csv`.

## Two-Folder LaTeX Workflow (Research Projects)

Every research project has **two** LaTeX locations:

1. **`latex\`** — local working folder (never pushed to GitHub)
   - `paper_skeleton.tex` ← **skeleton-driven development file (load full rules: `~/.claude/rules/paper-skeleton.md`)**
   - `figures\` ← programs save figure outputs here
   - `tables\` ← programs save table outputs here
   - `ClaudeAnswer.tex` ← AI equation scratch pad (always overwrite, never push)

2. **`[project-name-repo]\`** — GitHub/Overleaf folder (pushed to GitHub → Overleaf sync)
   - `main.tex`, `reference.bib`, style files, `figures\`, `tables\`

**Skeleton-driven development:** every research project uses `latex\paper_skeleton.tex` as the single source of truth for the paper-in-progress. It contains the full section structure, auto-numbered `\todo{}` / `\decision{}` / `\openq{}` markers, and embedded results. See `~/.claude/rules/paper-skeleton.md` for the full system.
**Editing the paper:** work in `latex\paper_skeleton.tex` during development; migrate stabilized sections to `[project-name-repo]\main.tex` late in the project.
**Program outputs:** programs save to `latex\figures\` and `latex\tables\`
**Before sharing:** run `/sync-to-github` to copy figures/tables to the repo folder, then commit

## Starting a New Research Project

When the user creates a new folder under `Research\`:
1. Copy `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\ClaudeFiles\Research Project Template\` into the new folder.
2. The template includes a pre-wired `latex\paper_skeleton.tex` with skeleton-driven development (color markers, TOC, standard 8-section outline).
3. Fill in project title and authors in the skeleton; compile once to confirm it renders.
4. From then on, all results, decisions, and open questions live in the skeleton.

---

## Universal Rules

### Research reproducibility & provenance (PRIORITY)
Applies to every research project. Three non-negotiables:
1. **Every number has provenance.** Each number in a paper is either *computed* (written by a saved generator script that reads canonical raw data; `tables/*.tex` and `figures/*` are build artifacts, never hand-edited) or *cited* (traced to a specific source, verified against the document). Never type a computed result into prose or a table file. Never use experimental/robustness data vintages for main results.
2. **Verify by RE-EXECUTION, not re-derivation.** To check a number, run the program that produces it and diff. Never hand-derive a number and call a mismatch "wrong" — a mismatch usually means your derivation is incomplete. Keep "no generator found" / "I haven't located the generator" / "re-ran X, matches or not" distinct; only the last licenses a correctness verdict, and an "integrity problem" claim requires it.
3. **A code-derived pipeline manifest.** Each project keeps `PIPELINE.md` at its root — programs in build order from raw data to final results, each with inputs and outputs — **generated by a script** (not hand-maintained, so it cannot drift), plus a provenance audit that flags any table/figure with no generator. Re-run both before any `/sync-to-github` or submission. Reference implementations live in `Research\Water and Crop\program\` (`build_pipeline.py`, `audit_provenance.py`); copy and adapt them when a project lacks them.

### LaTeX
- Never reference content by line number — use section name + paragraph opening words.
- To locate text: give PDF page number, section, and opening words of paragraph.
- Before answering about page/equation/figure/table numbers: check the compiled PDF first. Never guess from source.
- Compile LaTeX immediately after every edit. Do not wait to be asked.
- Close PDFs before recompiling — MiKTeX cannot overwrite locked files.
- Default compiler: `pdflatex`. Three-pass compile + bibtex when bibliography present.
- Compile order when appendix is a separate file: appendix first, then main, then main again.
- **Never end a heading argument with a period** — applies to `\section{}`, `\subsection{}`, `\subsubsection{}`, `\paragraph{}`, `\subparagraph{}`, and `\caption{}`. House styles (including the `paper.sty` used across these research projects) auto-append a period to run-in `\paragraph` headings via `\titleformat{\paragraph}[runin]{...}[.]`; a manual trailing period then renders as a doubled `..`. Write `\paragraph{The setting}`, never `\paragraph{The setting.}`. (Italic run-in leads typed by hand as `\emph{Worked example.}` are not headings and keep their period.)

### Table and figure captions (AER/RES format)
- **Tables:** caption (short title) **above** the tabular, notes **below** in `\footnotesize` after `\end{tabular}`, on a separate line, starting with `\textit{Notes:}`.
- **Figures:** caption (short title) **below** the graphic, notes **below the caption on a separate line** in `\footnotesize`, starting with `\textit{Notes:}`.
- `\caption{...}` is a short title only (≤15 words). All explanatory material goes in the Notes block.
- Wrap the Notes block in `\parbox{\linewidth}{\footnotesize\textit{Notes:} ...}` so it is **left-aligned and full-width**. A bare `{\footnotesize ...}` group inherits the table/figure `\centering` and renders the notes centered, which is wrong.
- See `~/.claude/rules/table-figure-format.md` for the full pattern and rationale. This applies to every research project under `Research\`.

### Math in chat responses
When a response contains `$` or `$$` math AND the project has a `latex\` folder:
→ Compile the full answer in `latex\ClaudeAnswer.tex`, render to PDF, tell user the PDF is ready.
→ Always overwrite previous ClaudeAnswer.tex (each answer is self-contained).
→ Use minimal `\documentclass{article}` with the answer text and equations.

### Bibliography
- NEVER add papers to a `.bib` file unless the user explicitly says to cite them.
- A PDF in `literature\` does not mean it should be cited.
- When characterizing a cited paper: verify what it actually says before writing the description.

### Academic writing
Load `AI_Writing_Guide_Academic.md` before making any substantive edits to paper prose.
Key rules from that guide (do not wait to load the file for these):
- No equations in abstracts.
- No "near-nominal" — use actual numbers.
- No boldface in running text.
- No bullet points in main text body.
- "et al." for 3+ authors in running text.

When **writing, drafting, refining, or polishing** prose (not just removing tells), also load the *positive* craft layer `AI_Writing_Guide_EconCraft.md` and the `econ_prose_exemplars.md` library, and apply them — or run the `econ-craft` skill, which loads both guides plus the exemplars and applies the craft in place. The `econ-craft-reminder` UserPromptSubmit hook auto-injects this guidance when it detects a writing intent inside the 0.AI workspace. The academic guide stays authoritative on every surface conflict; the craft guide only adds the positive layer.

### Manuscript track-changes (revision marks)
Every substantive manuscript edit is a **visible revision**: deletions struck through in red via `\del{...}` (use `\delx{...}` when the span contains `\cite`/`\ref`/math, which break `\sout`), additions in green via `\add{...}`. Track every content edit, even one word; keep inter-word spaces *outside* the macros. Pure apparatus (notation/equation refactors, label renames, whitespace) stays silent. On **"clean"**, drop every `\del`/`\delx` and its content but **keep** the green `\add` wrappers; only on an explicit **"final clean" / "flatten"** unwrap `\add` to plain black text. Ensure the canonical macros are in the manuscript preamble (add them if absent). See `~/.claude/rules/manuscript-track-changes.md` for the macro block and the full pattern.

### Stata
- Batch mode: `-e` flag, NEVER `/e`.
- Log file is created in CWD, not the do-file directory.
- Keep do-files in CRLF line endings (use `unix2dos` if needed).
- Use `if <fail> { di as err "..."; error 9 }` — never `assert ..., msg()`.
- Run Stata directly without asking user; always run in `sandbox\` unless production explicitly requested.
- Export CSV snapshots to `log\` at key data steps for debugging.

### MATLAB
- NEVER start MATLAB. The user runs it manually.

### Python
- Default: `python` command. Use Python 3.12 for tasks requiring PyMuPDF (fitz).
- To read PDF highlights/annotations: use PyMuPDF via Python 3.12.

### Plan-first
For any non-trivial task (touches >1 file, unclear scope, or estimated >30 min):
1. Enter plan mode before writing anything.
2. Save plan to `quality_reports\plans\YYYY-MM-DD_description.md`.
3. Present to user and wait for approval.
4. Only execute after approval.
