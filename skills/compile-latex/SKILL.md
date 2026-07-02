---
name: compile-latex
description: Compile a LaTeX paper with pdflatex (3 passes + bibtex). Use when compiling the paper after edits.
argument-hint: "[filename without extension, defaults to main]"
allowed-tools: ["Bash", "Read", "Glob"]
---

# Compile LaTeX

Compile a LaTeX document with pdflatex using 3 passes + bibtex.

## Steps

1. **Identify the file:**
   - If `$ARGUMENTS` given: use that filename (without .tex extension)
   - Default: `main`

2. **Warn about PDF lock:**
   Tell the user: "Make sure the PDF is closed before I compile — MiKTeX cannot overwrite a locked file."
   Then proceed.

3. **Find the file location:**
   - Look for `[filename].tex` in the current project
   - Likely in the GitHub repo subfolder (e.g., `Double-Clinching-Auction/`)

4. **Run 3-pass compile:**
   ```bash
   cd [directory containing the .tex file]
   pdflatex -interaction=nonstopmode [filename].tex
   bibtex [filename]
   pdflatex -interaction=nonstopmode [filename].tex
   pdflatex -interaction=nonstopmode [filename].tex
   ```

5. **Check the log:**
   - Read `[filename].log` for errors and overfull hbox warnings
   - Report: success or list errors with line context

6. **Report to user:**
   - Compiled successfully: confirm PDF created
   - Errors: show error messages with suggested fixes
   - Overfull hbox: list the worst offenders (>10pt)
