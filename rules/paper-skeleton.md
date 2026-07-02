# Paper Skeleton — Standard Research Project Workflow

Every research project in `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Research\` uses a **paper skeleton** as the single source of truth for what the paper *will be*, before and during writing. This replaces scattered drafts, side notes, and ad-hoc result files.

## What the Skeleton Is

A single LaTeX file: `latex\paper_skeleton.tex` (compiles to `paper_skeleton.pdf`).

- Contains the **full paper structure** (all sections, from Introduction to Conclusion) from day one, even when most sections are empty.
- Uses **three auto-numbered markers** to track the state of every piece of content:
  - `\todo{...}` — red, for pending tasks and placeholders
  - `\decision{...}` — blue, for choices that have been made (with rationale)
  - `\openq{...}` — orange, for unresolved questions
- Embeds **produced results as they arrive**: tables, figures, equations, numbers — each in its intended section.
- Ends with two collector sections: **Resolved Decisions** and **Open Questions Log**.

The skeleton is not a scratchpad. It is the paper, viewed at whatever stage it currently occupies.

## Why It Exists

- The user can read the compiled PDF and see the whole project in one place: what is known, what is decided, what is pending.
- New sessions can resume from the skeleton without re-reading sprawling drafts, notes, or code outputs.
- Results are organized by their eventual paper section, not by the date they were produced.
- The TOC gives a single-glance view of progress.

## When a New Research Project Is Created

If the user creates a new folder under `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Research\`:

1. Copy `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\ClaudeFiles\Research Project Template\` into the project folder.
2. The template already contains `latex\paper_skeleton.tex` with the skeleton system pre-wired (graphicx, color markers, TOC, standard section outline).
3. Fill in the title, authors, and any known research question in the skeleton's first TODO.
4. Compile once to confirm the skeleton renders: `pdflatex -interaction=nonstopmode paper_skeleton.tex`.

## How to Work With the Skeleton

### Adding new content
- A new result is produced → embed the table or figure in the appropriate section of the skeleton, with a one-paragraph caption explaining what it shows. Don't leave results floating in `program\sandbox\log\` alone.
- A modeling or specification choice is made → write `\decision{[brief rationale]}` inline at the point in the paper where it applies. It will be auto-numbered D1, D2, etc.
- An unresolved question arises → write `\openq{[question]}` inline. Auto-numbered Q1, Q2, etc.
- A task is identified but not done → write `\todo{[task]}` inline. Auto-numbered T1, T2, etc.

### Resolving markers
- When a TODO is done: delete the `\todo{...}` wrapper, replace with the actual content.
- When a question is resolved: convert the `\openq{...}` into a `\decision{...}` at the same location, recording the answer and rationale.
- Keep the **Resolved Decisions** list at the end of the skeleton as a running audit trail — append a one-line summary of each decision as it is finalized.

### Embedding results
- Tables produced by scripts should go to `latex\tables\*.tex` and be included via `\input{tables/xxx.tex}` or inlined in the skeleton if small.
- Figures go to `latex\figures\*.pdf` and are included via `\includegraphics[width=...]{figures/xxx.pdf}`.
- Every table/figure in the skeleton must have a caption explaining its role in the paper's argument — not just what it plots.

### Compiling
- Compile the skeleton after every substantive edit.
- The skeleton should always produce a valid PDF — never commit a version that doesn't compile.

## Skeleton vs. Final Paper

- The **skeleton** lives in `latex\paper_skeleton.tex` and stays colorful and marker-laden throughout the project.
- The **final paper** lives in `[project-name-repo]\main.tex` (the GitHub/Overleaf folder) and is created by copying stabilized sections out of the skeleton and removing the color markers.
- Late in the project, sections migrate from skeleton → final paper one at a time. The skeleton can keep the marked-up versions for ongoing revision.

## Session Workflow

- **Session start**: read `paper_skeleton.pdf` (or the .tex if the PDF isn't current) to recover context. This is faster and more structured than reading `HANDOFF.json` + scattered session logs.
- **Session end**: ensure the skeleton reflects all work done — new results embedded, decisions logged, todos updated. The skeleton is the handoff.

## Skeleton Template Location

Template: `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\ClaudeFiles\Research Project Template\latex\paper_skeleton.tex`

Every new research project starts from this file.
