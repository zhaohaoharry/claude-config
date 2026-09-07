---
name: sync-to-github
description: Sync figures and tables referenced by your tex files into the GitHub/Overleaf repo folder, then commit and push. Only copies files actually used in the paper — not every file in latex/.
argument-hint: "[optional commit message]"
allowed-tools: ["Bash", "Glob", "Read", "Write"]
---

# Sync referenced manuscript assets to GitHub/Overleaf

## Resolve the authorized target

Use the requested project, live project metadata, repository root, and remote to identify the target. Support `.git` directories and worktree `.git` files. Ask only if multiple targets remain plausible after inspection. An explicit sync-and-push request authorizes that operation for the resolved repository; a local-only request does not. Do not add a second approval for unchanged authorization.

## Prepare and validate

1. Inspect the worktree, staged changes, branch, and existing local commits. Preserve unrelated user work and record the intended file set.
2. Identify the requested document entry points and recursively resolve `\input`, `\include`, `\includegraphics`, graphics paths, and relevant bibliography dependencies. Do not treat obsolete drafts or unrelated cover letters as entry points merely because they are `.tex` files. Show the resolved list as progress, not an approval gate.
3. Copy only referenced generated assets from `latex/figures/` and `latex/tables/` to the corresponding repository paths, retaining directory structure. Do not copy raw data, secrets, or unrelated programs. Do not overwrite differing destination edits without reconciling their provenance.
4. Resolve missing references by checking source paths, valid existing repository assets, and authorized generators. Run the required project provenance checks. Continue independent preparation when one dependency is blocked. Do not hand-edit generated results or run prohibited production/MATLAB jobs.
5. Compile and inspect the target as required by the project. Fix introduced failures. Do not publish a newly broken manuscript by default; if missing evidence prevents completion, state the exact remaining issue and keep the prepared work.

## Commit and push

- Inspect `git diff` and `git diff --check`. Stage only task-related paths, never `git add .`. Preserve unrelated staged changes and exclude them from the task commit; use an isolated worktree or a carefully scoped commit where needed.
- Use the requested commit message or generate an accurate one. Showing it is informational, not another approval gate.
- A clean worktree does not imply nothing to push. Fetch the authorized remote and inspect ahead/behind state against the resolved upstream. If local commits are ahead, inspect their scope and push those covered by the request even if no new commit is needed. Ask only if existing commits introduce an unresolved scope issue.
- If behind or diverged, inspect and integrate remote changes without discarding user work, rewriting published history, or force-pushing. Resolve routine conflicts within scope and verify again. Do not blindly `git pull` and restart the whole skill.
- Use the exact target remote and branch. Reuse normal credential handling; never print or copy tokens. User login is needed only when actual authentication is missing.
- Verify the remote branch points to the intended commit after pushing. Do not claim the remote is current when it was not checked.

## Completion

Report separately: assets synchronized, manuscript validation, commit/push outcome, and any unresolved dependency. Say 'already synchronized' only after both relevant content and local/remote commit state have been verified. Transport success is not proof of manuscript completeness. Do not claim Overleaf has pulled a GitHub update unless that was actually verified.
