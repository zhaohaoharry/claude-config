#!/usr/bin/env python3
"""
Session-start resume hook.

SessionStart hook. When a session opens or resumes in a research project,
it surfaces where work was left off: the active (non-completed) plan and the
paper_skeleton marker counts, injected as context so the session resumes
without the user re-explaining.

Silent when there is no plan and no skeleton (e.g., a non-research directory).
Fail-safe: any error exits 0.

Hook Event: SessionStart
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def active_plan(project_dir: Path) -> str | None:
    plans = project_dir / "quality_reports" / "plans"
    if not plans.is_dir():
        return None
    files = sorted(plans.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
    for f in files[:5]:
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if "COMPLETED" in text.upper():
            continue
        status = "in progress"
        up = text.upper()
        if "APPROVED" in up:
            status = "approved"
        elif "DRAFT" in up:
            status = "draft"
        next_task = None
        for line in text.splitlines():
            if "- [ ]" in line:
                next_task = line.split("- [ ]", 1)[1].strip()
                break
        msg = f"active plan {f.name} ({status})"
        if next_task:
            msg += f"; next open task: {next_task}"
        return msg
    return None


def skeleton_status(project_dir: Path) -> str | None:
    skel = project_dir / "latex" / "paper_skeleton.tex"
    if not skel.is_file():
        return None
    try:
        text = skel.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None
    todo = len(re.findall(r"\\todo\b", text))
    openq = len(re.findall(r"\\openq\b", text))
    dec = len(re.findall(r"\\decision\b", text))
    return f"paper_skeleton.tex: {todo} todo, {openq} open questions, {dec} decisions"


def main() -> int:
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, ValueError):
        return 0

    cwd = data.get("cwd") or ""
    if not cwd:
        return 0
    project_dir = Path(cwd)

    bits = [b for b in (active_plan(project_dir), skeleton_status(project_dir)) if b]
    if not bits:
        return 0

    context = "[resume] Where this project stands. " + " | ".join(bits) + (
        ". Read the plan and paper_skeleton.pdf to recover full context before major work."
    )
    out = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context,
        }
    }
    json.dump(out, sys.stdout)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
