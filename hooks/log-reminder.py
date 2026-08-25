#!/usr/bin/env python3
"""
Session Log Reminder Hook

Stop hook: after THRESHOLD responses without a session log update,
blocks Claude and prompts it to update the log.

Hook Event: Stop
"""

from __future__ import annotations

import json
import os
import sys
import hashlib
from pathlib import Path
from datetime import datetime

THRESHOLD = 15


def get_state_dir() -> Path:
    import os
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    if not project_dir:
        state_dir = Path.home() / ".claude" / "sessions" / "default"
    else:
        project_hash = hashlib.md5(project_dir.encode()).hexdigest()[:8]
        state_dir = Path.home() / ".claude" / "sessions" / project_hash
    state_dir.mkdir(parents=True, exist_ok=True)
    return state_dir


def get_project_dir():
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        hook_input = {}

    if hook_input.get("stop_hook_active", False):
        sys.exit(0)

    return hook_input.get("cwd", ""), hook_input


def load_state(state_path: Path) -> dict:
    try:
        return json.loads(state_path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {"counter": 0, "last_mtime": 0.0, "reminded": False, "no_log_reminded": False}


def save_state(state_path: Path, state: dict):
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state))


def find_latest_log(*start_dirs: str) -> tuple[Path | None, float]:
    """Walk up from each start dir looking for quality_reports/session_logs.

    Takes several starting points because the shell's cwd drifts: a single
    `cd ~/.claude` to run git leaves cwd outside the project, and walking up
    from there finds nothing, which used to report "no session log exists"
    and block the turn even when the log was sitting in the project root.
    CLAUDE_PROJECT_DIR is checked first because it does not drift.
    """
    seen: set[Path] = set()
    for start in start_dirs:
        if not start:
            continue
        d = Path(start)
        for base in [d, *d.parents]:
            if base in seen:
                continue
            seen.add(base)
            log_dir = base / "quality_reports" / "session_logs"
            if log_dir.is_dir():
                md_files = list(log_dir.glob("*.md"))
                if md_files:
                    latest = max(md_files, key=lambda f: f.stat().st_mtime)
                    return latest, latest.stat().st_mtime
    return None, 0.0


def main():
    project_dir, hook_input = get_project_dir()
    env_project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    if not project_dir and not env_project_dir:
        sys.exit(0)

    state_path = get_state_dir() / "log-reminder-state.json"
    state = load_state(state_path)

    # Env var first: it points at the project root and does not follow the shell.
    latest_log, current_mtime = find_latest_log(env_project_dir, project_dir)
    today = datetime.now().strftime("%Y-%m-%d")

    if latest_log is None:
        if not state.get("no_log_reminded", False):
            state["no_log_reminded"] = True
            save_state(state_path, state)
            output = {
                "decision": "block",
                "reason": (
                    f"No session log exists yet. Create one at "
                    f"quality_reports/session_logs/{today}_description.md "
                    f"before continuing. Include the current goal and key context."
                ),
            }
            json.dump(output, sys.stdout)
        sys.exit(0)

    if current_mtime != state["last_mtime"]:
        state = {"counter": 0, "last_mtime": current_mtime, "reminded": False, "no_log_reminded": False}
        save_state(state_path, state)
        sys.exit(0)

    state["counter"] += 1

    if state["counter"] >= THRESHOLD and not state["reminded"]:
        state["reminded"] = True
        save_state(state_path, state)
        output = {
            "decision": "block",
            "reason": (
                f"SESSION LOG REMINDER: {state['counter']} responses without "
                f"updating the session log. Append your recent progress to "
                f"{latest_log.name}."
            ),
        }
        json.dump(output, sys.stdout)
        sys.exit(0)

    save_state(state_path, state)
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.exit(0)
