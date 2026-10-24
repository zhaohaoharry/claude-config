#!/usr/bin/env python3
"""
Data-integrity guard hook.

PostToolUse hook (matcher "Edit|Write"). After code is written to a .py, .do, .ado, .R, .jl or
.ipynb file, it scans the NEW text for operations that lose rows or hide unmatched merges without
a count: bare dropna(), merges without validate=/indicator, inner joins, Stata keep(match) and
nogenerate merges, drop-if-missing, na.omit(). Each hit is surfaced as context with a pointer to
~/.claude/rules/data-integrity.md, so the agent adds a ledger line or a reason before moving on.

It does not block the edit. A line is exempt when it already logs to the ledger (sf_step,
sf_merge, led.step, led.merge) or carries the marker `integrity-ok` in a comment, for drops the
user has approved.

Quiet when nothing is found. ENABLED=False disables it without touching settings.json.
Fail-safe: any error exits 0.

Hook Event: PostToolUse
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ENABLED = True
MAX_HITS = 8
EXEMPT = re.compile(r"integrity-ok|sf_step|sf_merge|led\.step|led\.merge|Ledger\(")

PY = [
    (re.compile(r"how\s*=\s*['\"]inner['\"]"), "inner merge silently drops unmatched rows"),
]
# Python calls whose arguments can span lines: (call regex, required argument, reason).
PY_CALLS = [
    (re.compile(r"\.dropna\("), "subset", "dropna() without subset= drops rows missing anything"),
    (re.compile(r"\.merge\("), "validate", "merge without validate= (cardinality unchecked)"),
]
STATA = [
    (re.compile(r"\bmerge\b[^\n]*keep\(\s*(match|3)\s*\)"), "merge keep(match) discards unmatched rows"),
    (re.compile(r"\bmerge\b[^\n]*\bnogen(erate)?\b"), "merge nogenerate hides the _merge counts"),
    (re.compile(r"\bdrop\s+if\s+missing\("), "drop if missing() without a ledger count"),
    (re.compile(r"\bkeep\s+if\s+!\s*missing\("), "keep if !missing() without a ledger count"),
    (re.compile(r"\bdrop\s+if\s+_merge\s*[!=]=\s*\d"), "drops merge results without logging them"),
]
R = [
    (re.compile(r"\bna\.omit\("), "na.omit() drops every row with any missing value"),
    (re.compile(r"\bdrop_na\(\s*\)"), "bare drop_na()"),
    (re.compile(r"\binner_join\("), "inner_join silently drops unmatched rows"),
]
JL = [
    (re.compile(r"\bdropmissing!?\(\s*\w+\s*\)"), "dropmissing on the whole frame"),
    (re.compile(r"\binnerjoin\("), "innerjoin silently drops unmatched rows"),
]
RULES = {".py": PY, ".ipynb": PY, ".do": STATA, ".ado": STATA, ".r": R, ".jl": JL}


def new_text(tool_input: dict) -> str:
    if "content" in tool_input:
        return tool_input.get("content") or ""
    if "new_string" in tool_input:
        return tool_input.get("new_string") or ""
    edits = tool_input.get("edits") or []
    return "\n".join(e.get("new_string", "") for e in edits)


def call_args(text: str, start: int) -> str:
    """Return the argument text of a call whose '(' ends at `start`, across lines."""
    depth, i = 1, start
    while i < len(text) and depth:
        depth += {"(": 1, ")": -1}.get(text[i], 0)
        i += 1
    return text[start:i - 1]


def scan_calls(text: str) -> list[str]:
    hits = []
    for pat, needed, why in PY_CALLS:
        for m in pat.finditer(text):
            line_start = text.rfind("\n", 0, m.start()) + 1
            line_end = text.find("\n", m.end())
            line = text[line_start:line_end if line_end >= 0 else len(text)]
            if EXEMPT.search(line) or line.strip().startswith("#"):
                continue
            if needed not in call_args(text, m.end()):
                hits.append(f"  {line.strip()[:110]}  <- {why}")
    return hits


def scan(text: str, rules) -> list[str]:
    hits = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or EXEMPT.search(line):
            continue
        if stripped.startswith(("#", "*", "//")):
            continue
        for pat, why in rules:
            if pat.search(line):
                hits.append(f"  {stripped[:110]}  <- {why}")
                break
        if len(hits) >= MAX_HITS:
            break
    return hits


def main() -> int:
    if not ENABLED:
        return 0
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, ValueError):
        return 0
    tool_input = data.get("tool_input") or {}
    path = tool_input.get("file_path", "") or ""
    rules = RULES.get(Path(path).suffix.lower())
    if not rules:
        return 0
    text = new_text(tool_input)
    hits = scan(text, rules)
    if rules is PY:
        hits = (hits + scan_calls(text))[:MAX_HITS]
    if not hits:
        return 0
    context = (
        f"[data-guard] {Path(path).name}: these lines can lose rows or hide unmatched merges "
        "without a count:\n" + "\n".join(hits) +
        "\nPer ~/.claude/rules/data-integrity.md, log each to the sample-flow ledger (rows in/out "
        "and the reason; helpers in skills/data-cleaning/tools/), diagnose merges, and stop if a "
        "step drops >5% of rows or leaves >5% of the master unmatched. If the user already approved "
        "a drop, mark the line with an `integrity-ok` comment."
    )
    json.dump({"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                      "additionalContext": context}}, sys.stdout)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
