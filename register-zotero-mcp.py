#!/usr/bin/env python3
"""
One-time registration of the Zotero MCP server for Claude Code (user scope).

RUN THIS WITH CLAUDE CODE CLOSED. Claude Code keeps ~/.claude.json in memory
and rewrites it on exit, so editing it while the app is open would be clobbered.

Steps it performs:
  1. Backs up ~/.claude.json.
  2. Adds an "mcpServers.zotero" entry pointing at the installed zotero-mcp
     server in local mode (ZOTERO_LOCAL=true -> talks to the running Zotero
     app on localhost:23119, no API key needed).

Before this helps you must also (in Zotero 7, one time):
  Edit -> Settings -> Advanced -> enable "Allow other applications on this
  computer to communicate with Zotero" (the local API), and keep Zotero open.

To undo: run with `--remove`, or delete the "zotero" entry under mcpServers.
"""

from __future__ import annotations

import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

CONFIG = Path.home() / ".claude.json"
FALLBACK_EXE = Path.home() / "AppData/Local/Programs/Python/Python313/Scripts/zotero-mcp.EXE"


def find_exe() -> str:
    exe = shutil.which("zotero-mcp")
    if exe:
        return exe
    if FALLBACK_EXE.exists():
        return str(FALLBACK_EXE)
    print("ERROR: zotero-mcp not found. Install it first: pip install zotero-mcp-server")
    sys.exit(1)


def main() -> int:
    remove = "--remove" in sys.argv
    if not CONFIG.exists():
        print(f"ERROR: {CONFIG} not found. Open Claude Code once, then close it, then re-run.")
        return 1

    data = json.loads(CONFIG.read_text(encoding="utf-8"))
    backup = CONFIG.with_suffix(f".json.bak-{datetime.now():%Y%m%d-%H%M%S}")
    shutil.copyfile(CONFIG, backup)
    print(f"Backed up to {backup}")

    servers = data.get("mcpServers") or {}
    if remove:
        servers.pop("zotero", None)
        data["mcpServers"] = servers
        print("Removed the 'zotero' MCP server.")
    else:
        exe = find_exe()
        servers["zotero"] = {
            "command": exe,
            "args": ["serve"],
            "env": {"ZOTERO_LOCAL": "true"},
        }
        data["mcpServers"] = servers
        print(f"Registered 'zotero' MCP server -> {exe} serve (local mode)")

    CONFIG.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\nDone. Now:")
    print("  1. In Zotero 7: Edit > Settings > Advanced > enable the local API")
    print("     (\"Allow other applications on this computer to communicate with Zotero\").")
    print("  2. Keep Zotero running, then open Claude Code and run /mcp to confirm 'zotero' is connected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
