---
name: feedback-minimal-track-changes
description: "Track changes must mark only the changed token (number/word), never repeat the whole sentence"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a92848a1-ac62-4dd2-9e7f-f902cdbb3c6e
  modified: 2026-09-01T03:47:04.115Z
---

When making tracked manuscript edits (\del/\add), mark the smallest changed span only. If a number changes, track just the number (`$\sigma = {}$\del{2.763}\add{2.90}`); if a word changes, track just the word. Full-sentence del/add pairs only when the sentence's claim itself changed.

**Why:** The user (2026-09-01, ETFP Z1 update) saw whole sentences repeated in red+green just to change one number and called it out hard ("this should be a general rule for track changes!!"). Duplicated text buries the actual change.

**How to apply:** Full rule with math-mode patterns is in [[manuscript-track-changes]] rule file `~/.claude/rules/manuscript-track-changes.md` (Minimal-span rule section). For numbers inside inline math, close math before the number: `$x = {}$\del{old}\add{new}`.
