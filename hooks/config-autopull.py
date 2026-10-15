#!/usr/bin/env python3
"""
Config Auto-Pull Hook

SessionStart counterpart to config-autosync.py: pull the latest tracked
~/.claude config (CLAUDE.md, rules, skills, agents, hooks, settings, curated
memory) from the private `claude-config` GitHub repo, so a session that starts
on LaoZhao, H2 or HMac begins with whatever the other machines last pushed.

Design:
- Fire-and-forget. Never blocks session start; always exits 0.
- Fast-forward only. A pull that would merge or rebase is refused and logged,
  so a divergence is surfaced rather than silently resolved.
- Skips entirely when tracked files are dirty locally: the session end hook
  will commit and push those, and pulling first would risk a conflict.
- Never prompts for credentials (GIT_TERMINAL_PROMPT=0); offline is a no-op.
- Logs one line to ~/.claude/config-autosync.log (shared with the push hook,
  itself gitignored).

Hook Event: SessionStart
"""
from __future__ import annotations

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

CLAUDE_DIR = Path.home() / ".claude"
LOG = CLAUDE_DIR / "config-autosync.log"


def log(msg: str) -> None:
    try:
        with LOG.open("a", encoding="utf-8") as f:
            f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S}  {msg}\n")
    except Exception:
        pass


def git(args, timeout: int = 25) -> subprocess.CompletedProcess:
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    return subprocess.run(
        ["git", "-C", str(CLAUDE_DIR), *args],
        capture_output=True, text=True, timeout=timeout, env=env,
    )


def main() -> None:
    try:
        sys.stdin.read()
    except Exception:
        pass

    if not (CLAUDE_DIR / ".git").exists():
        return

    status = git(["status", "--porcelain"])
    if status.returncode != 0:
        log(f"pull skipped: git status failed ({status.stderr.strip()[:120]})")
        return
    if status.stdout.strip():
        n = len([ln for ln in status.stdout.splitlines() if ln.strip()])
        log(f"pull skipped: {n} tracked file(s) modified locally; session end will push them")
        return

    before = git(["rev-parse", "--short", "HEAD"]).stdout.strip()
    pull = git(["pull", "--ff-only", "--quiet"], timeout=40)
    after = git(["rev-parse", "--short", "HEAD"]).stdout.strip()

    if pull.returncode != 0:
        err = (pull.stderr or pull.stdout).strip().splitlines()
        log(f"pull FAILED (config unchanged): {err[0][:160] if err else 'unknown error'}")
    elif before != after:
        log(f"pulled config {before} -> {after}")
    else:
        log("config already current")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log(f"pull hook error: {type(e).__name__}: {e}")
    sys.exit(0)
