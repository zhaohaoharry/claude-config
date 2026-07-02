#!/usr/bin/env python3
"""
Status line for Claude Code — full-dashboard layout.

Renders (segments drop out when their data is absent from stdin):

  <project> · <model> · [██░░░░░░░░] 18% · 820k left · $0.42 · 5h 24% · wk 41% · <git-branch>

stdin JSON (Claude Code statusLine command contract):
  model.display_name, cwd / workspace.current_dir,
  context_window.{used_percentage, remaining_percentage, context_window_size,
                  current_usage{input_tokens, output_tokens,
                                cache_creation_input_tokens, cache_read_input_tokens}},
  cost.total_cost_usd,
  rate_limits.{five_hour, seven_day}.used_percentage
Git branch is NOT provided by the harness, so it is computed here.

Colors: context bar/% — green <60, yellow 60–85, red >85.
        5h/wk plan usage — yellow >=60, red >=80.

Fail-safe: any error prints a minimal line and exits 0 (a crashing status
line just blanks the bar, never blocks work).

Registered in settings.json: "statusLine": {"type":"command","command":"python ..."}
"""

from __future__ import annotations

import json
import re
import subprocess
import sys

# Folders that sit directly under 0.AI; the project is the level below them.
WORKSPACE_BUCKETS = {"research", "teaching", "work", "others", "claude master"}

BAR_WIDTH = 10

RESET = "\x1b[0m"
DIM = "\x1b[2m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
RED = "\x1b[31m"

SEP = f"{DIM} · {RESET}"


def project_name(cwd: str) -> str:
    parts = [p for p in re.split(r"[\\/]+", cwd or "") if p]
    if not parts:
        return "?"
    low = [p.lower() for p in parts]
    if "0.ai" in low:
        i = low.index("0.ai")
        rest = parts[i + 1:]
        if rest:
            if rest[0].lower() in WORKSPACE_BUCKETS and len(rest) >= 2:
                return rest[1]
            return rest[0]
        return "0.AI"
    return parts[-1]


def git_branch(cwd: str) -> str | None:
    try:
        r = subprocess.run(
            ["git", "-C", cwd, "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, timeout=2,
        )
        if r.returncode == 0:
            b = r.stdout.strip()
            if b and b != "HEAD":
                return b
    except Exception:
        pass
    return None


def fmt_tokens(n: float) -> str:
    n = max(0, int(round(n)))
    if n >= 1_000_000:
        s = f"{n / 1_000_000:.1f}"
        if s.endswith(".0"):
            s = s[:-2]
        return s + "M"
    if n >= 1_000:
        return f"{round(n / 1_000)}k"
    return str(n)


def ctx_color(pct: float) -> str:
    return RED if pct > 85 else (YELLOW if pct >= 60 else GREEN)


def limit_color(pct: float) -> str:
    return RED if pct >= 80 else (YELLOW if pct >= 60 else "")


def context_segments(cw: dict) -> list[str]:
    """Bar + used % + tokens remaining, from whatever fields are available."""
    size = cw.get("context_window_size")
    pct = cw.get("used_percentage")
    if not isinstance(pct, (int, float)):
        cu = cw.get("current_usage") or {}
        used = sum(
            int(cu.get(k) or 0)
            for k in ("input_tokens", "output_tokens",
                      "cache_creation_input_tokens", "cache_read_input_tokens")
        )
        if used and isinstance(size, (int, float)) and size > 0:
            pct = used / size * 100
    if not isinstance(pct, (int, float)):
        return []
    p = max(0.0, min(100.0, float(pct)))
    col = ctx_color(p)
    filled = round(p / 100 * BAR_WIDTH)
    bar = "█" * filled + "░" * (BAR_WIDTH - filled)
    segs = [f"{col}[{bar}] {round(p)}%{RESET}"]
    if isinstance(size, (int, float)) and size > 0:
        rem = cw.get("remaining_percentage")
        if not isinstance(rem, (int, float)):
            rem = 100.0 - p
        segs.append(f"{fmt_tokens(size * rem / 100)} left")
    return segs


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    try:
        data = json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, ValueError):
        data = {}

    cwd = data.get("cwd") or (data.get("workspace") or {}).get("current_dir") or ""
    model = data.get("model") or {}
    model_name = model.get("display_name") or model.get("id") or ""

    segs = [project_name(cwd)]
    if model_name:
        segs.append(model_name)

    segs.extend(context_segments(data.get("context_window") or {}))

    cost = (data.get("cost") or {}).get("total_cost_usd")
    if isinstance(cost, (int, float)) and not isinstance(cost, bool):
        segs.append(f"${cost:.2f}" if cost < 100 else f"${cost:.0f}")

    limits = data.get("rate_limits") or {}
    for key, label in (("five_hour", "5h"), ("seven_day", "wk")):
        p = (limits.get(key) or {}).get("used_percentage")
        if isinstance(p, (int, float)):
            col = limit_color(p)
            segs.append(f"{label} {col}{round(p)}%{RESET if col else ''}")

    br = git_branch(cwd)
    if br:
        segs.append(f"{DIM}{br}{RESET}")

    sys.stdout.write(SEP.join(s for s in segs if s))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
