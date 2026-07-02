# CRITICAL: Math in Chat Responses

This rule applies to ALL projects that have a `latex\` folder.

**NEVER display raw LaTeX math (`$...$` or `$$...$$`) in chat text.**

When a response would contain math equations:
1. Create `latex\answers\` folder if it does not exist.
2. Write the full answer (text + equations) into a **descriptively named file** under `latex\answers\`, e.g. `latex\answers\answer_mobius_triple.tex`. Use short, informative names — no dates or timestamps.
3. Use `\documentclass{article}` with `amsmath,amssymb,amsthm`.
4. Compile with `pdflatex -interaction=nonstopmode <filename>.tex` (two passes for cross-references).
5. Tell the user: "The compiled answer is in `latex/answers/<filename>.pdf`."

**Never overwrite a previous answer file.** Each answer is a separate file that persists.

**No exceptions.** Even short inline formulas like `$x_i^*$` are unreadable in the terminal. Compile everything.

If the response is ONLY creating/editing a `.tex` file (not explaining math in chat), this rule does not apply — the equations live in the file itself.
