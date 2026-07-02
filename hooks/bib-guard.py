#!/usr/bin/env python3
"""
Bib-guard hook.

PreToolUse hook (matcher "Edit|Write"). When the file being edited is a
.bib bibliography, it surfaces the user's standing rule at the exact moment
it matters: never add references unless explicitly asked, and verify every
entry actually exists and is characterized accurately.

MODE = "remind"  -> injects a non-blocking reminder (default).
MODE = "ask"     -> forces a confirmation prompt before any .bib edit.

Fail-safe: any error exits 0 so the edit is never blocked by a hook bug.

Hook Event: PreToolUse
"""

from __future__ import annotations

import json
import sys

MODE = "remind"  # "remind" (soft) or "ask" (require confirmation)

REASON = (
    "This is a .bib file. House rule: do NOT add references unless the user "
    "explicitly asked you to cite them (a PDF in literature/ is not a request). "
    "For any entry you do touch, verify it actually exists and that the paper "
    "is characterized accurately. Prefer bib-validate before adding."
)


def is_bib(path: str) -> bool:
    return bool(path) and path.lower().rstrip().endswith(".bib")


def main() -> int:
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, ValueError):
        return 0

    path = (data.get("tool_input") or {}).get("file_path", "") or ""
    if not is_bib(path):
        return 0

    if MODE == "ask":
        out = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": REASON,
            }
        }
    else:
        out = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": REASON,
            }
        }
    json.dump(out, sys.stdout)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
