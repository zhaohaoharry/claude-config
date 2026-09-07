---
name: compile-latex
description: Compile and verify the edited LaTeX document using the project compiler and proportionate incremental passes; repair introduced errors.
argument-hint: "[filename without extension, defaults to main]"
allowed-tools: ["Bash", "Read", "Glob"]
---

# Compile the edited LaTeX document

1. Resolve the actual edited document from the request and current project state. Use its root document, then `latex/paper_skeleton.tex` when it is the development source; do not default to an unrelated `main.tex`. Ask only if the target remains materially ambiguous.
2. Use the project compiler and bibliography backend. For a micro prose edit with unchanged citations, references, counters, and structure, run one LaTeX pass and inspect the log. Run BibTeX/Biber only when required and additional passes until changed references resolve. Build an external appendix first when the main document depends on it.
3. Do not ask preemptively about PDF locks. Attempt compilation and, on an actual lock, use a separate output location or handle the affected preview without closing unrelated user windows.
4. Fix ordinary errors introduced by the current edits and rebuild. Preserve unrelated content. If correction needs missing source material or a substantive user decision, explain that exact blocker while finishing independent checks.
5. Verify the fresh output, fatal errors, undefined references, and material layout warnings. Inspect rendered pages when substantive layout changed or final visual QA is required. Existing PDF presence alone is not build success.
6. Deliver the compiled artifact and actual validation status. Distinguish pre-existing warnings and incomplete verification; do not stop at suggested fixes for a routine error you can repair.
