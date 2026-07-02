#!/usr/bin/env python3
"""
LaTeX auto-checker hook.

PostToolUse hook (matcher "Edit|Write"). After an edit to paper_skeleton.tex
or main.tex, it runs a fast pdflatex *draftmode* pass into a throwaway
.autobuild/ aux directory and surfaces any compile errors as context.

Why draftmode + aux dir: it does NOT write a PDF, so it never fights a PDF
the user has open in a viewer (the classic MiKTeX "cannot overwrite locked
file" problem on Windows). This is an error CHECKER, not a PDF builder; the
user still runs a real compile to refresh the PDF they read.

Quiet on success. ENABLED=False disables it without touching settings.json.
Fail-safe: any error exits 0.

Hook Event: PostToolUse
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ENABLED = True
WATCH_NAMES = {"paper_skeleton.tex", "main.tex"}
TIMEOUT_SEC = 90
MAX_ERR_LINES = 6


def collect_errors(log_text: str) -> list[str]:
    errs = []
    lines = log_text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("!"):
            snippet = line.strip()
            # include the line-number pointer that often follows ("l.123 ...")
            for j in range(i + 1, min(i + 4, len(lines))):
                if lines[j].startswith("l."):
                    snippet += "  " + lines[j].strip()
                    break
            errs.append(snippet)
        if len(errs) >= MAX_ERR_LINES:
            break
    return errs


def main() -> int:
    if not ENABLED:
        return 0
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, ValueError):
        return 0

    path = (data.get("tool_input") or {}).get("file_path", "") or ""
    if not path:
        return 0
    tex = Path(path)
    if tex.name.lower() not in WATCH_NAMES or not tex.is_file():
        return 0

    workdir = tex.parent
    aux = workdir / ".autobuild"
    try:
        aux.mkdir(exist_ok=True)
    except OSError:
        return 0

    try:
        proc = subprocess.run(
            [
                "pdflatex", "-draftmode", "-interaction=nonstopmode",
                "-halt-on-error", f"-output-directory={aux}", tex.name,
            ],
            cwd=str(workdir), capture_output=True, text=True,
            encoding="utf-8", errors="ignore", timeout=TIMEOUT_SEC,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        return 0

    if proc.returncode == 0:
        return 0  # compiles clean, stay silent

    log_file = aux / (tex.stem + ".log")
    log_text = ""
    try:
        log_text = log_file.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        log_text = proc.stdout or ""

    errs = collect_errors(log_text)
    if not errs:
        return 0

    context = (
        f"[latex-autocheck] {tex.name} fails to compile after this edit "
        f"(draftmode error check). First errors:\n" + "\n".join(errs) +
        "\nFix these before relying on the PDF. (This check did not touch the "
        "real PDF; run a normal compile to refresh it.)"
    )
    out = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
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
