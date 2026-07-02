# Plan-First Workflow

For any non-trivial task, enter plan mode before writing or editing files.

## When to Plan

**Always plan when:**
- Task touches more than 1 file
- Scope is ambiguous or high-level ("improve the paper", "analyze the data")
- Estimated time > 30 minutes
- Multiple valid interpretations exist

**Skip planning for:**
- Clear single-file edits ("fix typo on page 3")
- Running a specific command the user specified
- Compiling LaTeX

## The Protocol

1. **Enter Plan Mode** — use `EnterPlanMode`
2. **Clarify if needed** — for ambiguous/complex tasks, ask 3-5 focused questions before planning (use `AskUserQuestion`)
3. **Draft the plan** — what changes, which files, in what order, verification steps
4. **Save to disk** — write to `quality_reports\plans\YYYY-MM-DD_short-description.md`
5. **Present to user** — wait for approval
6. **Exit plan mode** — only after approval
7. **Execute** — implement, then verify output

## Plan File Format

```markdown
# Plan: [Short Description]
**Date:** YYYY-MM-DD
**Status:** DRAFT | APPROVED | COMPLETED

## Goal
[What we're trying to achieve]

## Steps
- [ ] Step 1
- [ ] Step 2
- [ ] Step 3

## Files to Modify
- `path/to/file` — what changes

## Verification
- [ ] How to confirm the task succeeded
```

## Context Survival

Plans saved to disk survive context compression. Before compression:
1. Ensure the active plan is saved to `quality_reports\plans\`
2. Ensure the session log is current
3. Ensure MEMORY.md has any `[LEARN]` entries from this session

After compression, first message: "Resuming after compression. Reading most recent plan and git log."
