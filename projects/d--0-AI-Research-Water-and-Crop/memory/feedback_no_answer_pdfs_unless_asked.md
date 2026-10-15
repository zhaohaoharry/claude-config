---
name: feedback-no-answer-pdfs-unless-asked
description: Do not auto-generate answer/equation PDFs to deliberate; answer in the chatbox and apply the fix directly. Only make a PDF when explicitly asked.
metadata:
  type: feedback
---

Default to answering in the chatbox and applying the fix directly. Do **not** keep generating `latex/answers/answer_*.pdf` notes to lay out options or explain math — the user finds the PDF proliferation noisy. Only compile an answer PDF when the user explicitly asks for one.

**Why:** This supersedes the global `~/.claude/rules/math-compilation.md` auto-PDF behavior for this user. The user wants decisiveness: a concise chat answer plus the actual edit, not a deliberation artifact each turn. Stated 2026-06-17, alongside "clean up the answers."

**How to apply:** When a fix is clear, just explain it briefly in chat and make the edit. When there is a real choice, present the options in chat (prose/short table), recommend one, and apply on confirmation — without a PDF. Keep the chat math light (words over raw `$...$` where possible). Periodically clean stale `latex/answers/answer_*` scratch files. Related: [[feedback_evaluate_prose_before_showing]]. Applies across all research projects.
