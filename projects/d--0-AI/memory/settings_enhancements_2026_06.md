---
name: settings-enhancements-2026-06
description: "Settings/automation added 2026-06-07 — deny rules, encoding env, status line, bib-guard/latex-autocheck/session-start hooks, Zotero MCP"
metadata: 
  node_type: memory
  type: project
  originSessionId: 20d1a03d-3473-4e85-9554-c7ff2c743ac0
---

Configured 2026-06-07 in `~/.claude/settings.json` (backup: `~/.claude/settings.backup-2026-06-07.json`). These change runtime behavior, so future sessions should know they exist.

**permissions.deny (hard blocks, override allow):** `Edit/Write(**/data/raw/**)` makes raw data read-only to the file tools; `Bash(rm -rf*)`, `Bash(git reset --hard*)`, `Bash(git push --force*)`, `Bash(git clean -f*)` are refused; `Read(**/.env)` blocked. If a destructive op is genuinely needed, the deny rule must be removed first (use Python shutil/os for cleanup instead, e.g. removing throwaway dirs). The allow-list was also cleaned (~90 → 42 entries; junk/one-offs removed, broad allows kept, `PowerShell(Start-Process code*)` added).

**env:** `PYTHONIOENCODING=utf-8`, `PYTHONUTF8=1` set for every command — stop hand-prefixing these; Windows cp1252 Unicode crashes are fixed globally.

**statusLine:** `~/.claude/statusline.py` — upgraded 2026-06-11 to a full dashboard: `project · model · [██░░] ctx% · Nk left · $cost · 5h N% · wk N% · git-branch`. Context bar/% colored green <60 / yellow 60–85 / red >85; 5h/wk plan-usage segments only appear when the harness sends `rate_limits` (subscription plans); every segment drops out gracefully when its field is absent. Fail-safe exit 0. **Terminal CLI only** — the VS Code extension chat panel does not render custom status lines (verified 2026-06-11; script works, panel ignores it). In the extension, point the user to `/context`, `/cost`, and the built-in context indicator instead; don't re-attempt a chat-panel status bar via hooks (hook stdout isn't rendered there either).

**New hooks (Python, fail-safe exit 0):**
- `hooks/bib-guard.py` (PreToolUse, Edit|Write) — on `.bib` edits injects the "don't add citations unless asked; verify each" rule. MODE="remind" (flip to "ask" for a hard confirm).
- `hooks/latex-autocheck.py` (PostToolUse, Edit|Write) — after editing `paper_skeleton.tex`/`main.tex`, runs a pdflatex `-draftmode` error check into a throwaway `.autobuild/` dir (never touches the real PDF, so no MiKTeX file-lock clash) and reports errors only. It is an error CHECKER, not a PDF builder; still compile normally to refresh the PDF. Disable via `ENABLED=False` at top.
- `hooks/session-start-resume.py` (SessionStart) — injects the active (non-completed) plan + paper_skeleton marker counts on session open/resume.

**Zotero MCP (item pending user activation):** `zotero-mcp-server` pip-installed (`zotero-mcp.EXE serve`). NOT yet registered — `~/.claude/register-zotero-mcp.py` adds it to `~/.claude.json` user scope (run with Claude Code CLOSED to avoid the app clobbering the file; `--remove` to undo). User must also enable Zotero 7 local API (Edit > Settings > Advanced) and keep Zotero running. Local mode (ZOTERO_LOCAL=true), no API key. Note the prompt-injection surface of library content.

Related: [[econ_craft_system]] (the UserPromptSubmit econ-craft hook), [[project_setup]].
