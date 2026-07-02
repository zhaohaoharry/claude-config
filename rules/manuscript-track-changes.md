# Manuscript Track-Changes (Revision Marks)

Universal rule for **all** research projects under `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Research\`.

Every substantive edit to a manuscript is made as a **visible revision**: deletions are struck through in red, additions are shown in green. The author reviews the marked-up PDF, then asks to "clean" (accept deletions, keep additions highlighted) or "final clean" (flatten to a publication copy). One source file carries the marks; the views differ only by how the macros render.

## The macros (ensure these are in the manuscript preamble or the project `.sty`)

If a manuscript does not already define them, add this block to the preamble. These are the canonical, tested definitions.

```latex
\usepackage[normalem]{ulem}                 % \sout without underlining \emph
\definecolor{delred}{RGB}{178,34,34}
\definecolor{addgreen}{RGB}{34,139,34}
\newcommand{\del}[1]{{\color{delred}\sout{#1}}}                                  % deletion: red strikethrough
\newcommand{\delx}[1]{{\color{delred}\textsuperscript{\textsc{[del]}}#1}}        % citation-safe deletion (no \sout)
\newcommand{\add}[1]{{\color{addgreen}#1}}                                       % addition: green
\newcommand{\addblock}[1]{\begingroup\color{addgreen}#1\endgroup}               % block-level addition
```

## How to edit

- **Track every content edit, even one word.** Replacing text reads `\del{old text}\add{new text}`. Deleting reads `\del{...}`. Inserting reads `\add{...}`. The author wants to see exactly what changed.
- **`\del` vs `\delx`.** `\del` wraps its argument in `\sout`, which **breaks on `\cite`, `\ref`, and most display math**. If the deleted span contains a citation, cross-reference, or inline math command, use `\delx` instead (it tags `[DEL]` and skips the strikethrough). Never put `\cite`/`\ref` inside `\del`.
- **Spacing gotcha.** A leading space *inside* `\add{ X}` is swallowed at render, so `word.\add{ Next}` prints as `word.Next`. Put inter-word spaces **outside** the macro: `word. \add{Next}`. Trailing spaces inside are preserved. Do **not** add a space between a `\del{old}\add{new}` replacement pair.
- **What is tracked vs silent.** Prose and content (sentences, numbers, claims, captions) are always tracked. Pure mechanical apparatus is silent (no marks): symbol/equation refactors, notation swaps, label/`\ref` renames, whitespace, and anything inside math where `\sout` would break or obscure rather than clarify. When a silent apparatus change is non-trivial, note it in the chat reply rather than the source.

## "clean" — accept deletions, keep additions green

When the author says **"clean"** or **"clean up"** a section or the draft:
- **Remove** every `\del{...}` and `\delx{...}` along with its content (the deletions are accepted).
- **Keep** every `\add{...}` / `\addblock{...}` wrapper intact, so the additions stay **green**.

The result still compiles with the tracked preamble and shows, in green, everything that was added since the last clean. This is the normal review checkpoint. It does **not** flatten to black.

## "final clean" / "flatten" — publication copy

Only on an explicit **"final clean"**, **"flatten"**, or "make it black":
- Remove `\del`/`\delx` and their content.
- **Unwrap** `\add`/`\addblock`: keep the added text but drop the wrapper so it renders as normal black text.

The fastest way to produce a flattened PDF without touching the marked-up source is the **macro-redefinition twin**: copy the file (or `\input` a shared body) and redefine the macros so the marks disappear.

```latex
\newcommand{\del}[1]{}        % deletion vanishes
\newcommand{\delx}[1]{}       % deletion vanishes
\newcommand{\add}[1]{#1}      % addition becomes plain black text
\newcommand{\addblock}[1]{#1}
```

Keep the marked-up working file as the single source of truth; the clean/flattened file is derived.

## Discipline

- Compile after every tracked edit and confirm it still builds (`\sout` over an unexpected `\cite`/math is the usual failure).
- Before showing an edit, self-check that spaces sit outside the macros and that no `\cite`/`\ref` is trapped inside `\del`.
- The marked-up file is never the version shared with co-authors or journals; share the clean or flattened copy.
