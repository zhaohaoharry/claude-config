# Session Logging

Track work across sessions so context is never lost.

## Three Logging Triggers

### 1. Post-Plan Log
After a plan is approved: immediately write a session log capturing goal, approach, and key context.

### 2. Incremental Logging
Append 1-3 lines whenever:
- A design or methodological decision is made
- A problem is solved
- The user corrects something or changes direction
- An approach fails (record what was tried)
Do not batch — log as it happens.

### 3. End-of-Session Log
When wrapping up: write a full session summary covering what changed, why, open questions, and next steps.

## Log File Location

```
quality_reports\session_logs\YYYY-MM-DD_description.md
```

Use the template at `ClaudeFiles\Research Project Template\templates\session-log.md`.

## Session Note (human-readable summary)

Also write a human-readable summary to:
```
session_notes\session_YYYYMMDD_HHMM_xxx.md
```
where `xxx` is a random 3-letter id (e.g., xkr, mtz).

Frontmatter:
```
---
date: YYYY-MM-DD
title: <one-line title>
tags: [TAG1, TAG2]
project: <project name>
---
```

Sections: Context / What changed / Why / Open questions / Next steps

## Project Catalogue

Append one row to `session_notes\catalogue.md` after each session:
```
| YYYY-MM-DD | filename | one-line title | tags |
```

## Master Catalogue

Append one row to `Claude Master\master_catalogue.md` after each session:
```
| YYYY-MM-DD | project name | filename | one-line title | tags |
```
