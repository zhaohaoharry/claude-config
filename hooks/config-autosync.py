#!/usr/bin/env python3
"""
Config Auto-Sync Hook

SessionEnd hook: when a Claude Code session ends, commit any changes to the
tracked ~/.claude config (skills, hooks, agents, rules, settings, memory) and
push them to the private `claude-config` GitHub repo, so other machines can
pull the latest.

Design:
- Fire-and-forget. Never blocks the session exit; always exits 0.
- Acts ONLY when tracked config actually changed (respects .gitignore, so
  credentials and the 1.4 GB of transcripts/caches are never touched).
- Never prompts for credentials (GIT_TERMINAL_PROMPT=0); if the network/auth
  is unavailable the change stays committed locally and is pushed next time.
- Writes a one-line audit to ~/.claude/config-autosync.log (itself ignored,
  so it can't trigger another sync).

Hook Event: SessionEnd
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
    # Consume the hook payload on stdin (not needed, but read it cleanly).
    try:
        sys.stdin.read()
    except Exception:
        pass

    if not (CLAUDE_DIR / ".git").exists():
        return  # not a git repo yet; nothing to sync

    status = git(["status", "--porcelain"])
    if status.returncode != 0:
        log(f"status failed: {status.stderr.strip()}")
        return
    if not status.stdout.strip():
        return  # no tracked-config changes; stay silent

    changed = len(status.stdout.strip().splitlines())

    add = git(["add", "-A"])
    if add.returncode != 0:
        log(f"add failed: {add.stderr.strip()}")
        return

    msg = f"Auto-sync config ({datetime.now():%Y-%m-%d %H:%M}, {changed} file(s))"
    commit = git(["commit", "-m", msg])
    if commit.returncode != 0:
        log(f"commit failed: {(commit.stderr or commit.stdout).strip()}")
        return

    push = git(["push", "origin", "HEAD"], timeout=30)
    if push.returncode != 0:
        log(f"push FAILED (committed locally, will retry next session): "
            f"{push.stderr.strip()}")
        return

    log(f"pushed {changed} file(s): {msg}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log(f"exception: {e}")
    sys.exit(0)
