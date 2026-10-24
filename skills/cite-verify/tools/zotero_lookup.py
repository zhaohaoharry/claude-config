"""Look up papers in the local Zotero library: abstract, PDF path, and Better BibTeX cite key.

Copies zotero.sqlite AND zotero.sqlite-wal to a temp folder first (a copy without the WAL is
stale), then queries read-only. Prints JSON, one record per match.

    python zotero_lookup.py --doi 10.1093/qje/qjt031
    python zotero_lookup.py --author Hsieh --year 2009
    python zotero_lookup.py --title "misallocation and manufacturing TFP"
    python zotero_lookup.py --citekey hsieh2009misallocation
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sqlite3
import sys
import tempfile
from pathlib import Path

ZOTERO = Path(os.path.expanduser("~/Zotero"))


def snapshot(name: str) -> Path | None:
    src = ZOTERO / name
    if not src.exists():
        return None
    d = Path(tempfile.mkdtemp(prefix="zotq_"))
    shutil.copy(src, d / name)
    wal = ZOTERO / (name + "-wal")
    if wal.exists():
        shutil.copy(wal, d / (name + "-wal"))
    return d / name


def field(c, item_id: int, name: str) -> str | None:
    row = c.execute(
        "SELECT v.value FROM itemData d JOIN fields f ON d.fieldID=f.fieldID "
        "JOIN itemDataValues v ON d.valueID=v.valueID WHERE d.itemID=? AND f.fieldName=?",
        (item_id, name)).fetchone()
    return row[0] if row else None


def creators(c, item_id: int) -> list[str]:
    return [r[0] for r in c.execute(
        "SELECT cr.lastName FROM itemCreators ic JOIN creators cr ON ic.creatorID=cr.creatorID "
        "WHERE ic.itemID=? ORDER BY ic.orderIndex", (item_id,))]


def pdfs(c, item_id: int) -> list[str]:
    out = []
    for key, path in c.execute(
            "SELECT i.key, a.path FROM itemAttachments a JOIN items i ON a.itemID=i.itemID "
            "WHERE a.parentItemID=? AND a.contentType='application/pdf'", (item_id,)):
        if path and path.startswith("storage:"):
            out.append(str(ZOTERO / "storage" / key / path[len("storage:"):]))
        elif path:
            out.append(path)
    return out


def find(c, args) -> list[int]:
    base = ("SELECT DISTINCT d.itemID FROM itemData d JOIN fields f ON d.fieldID=f.fieldID "
            "JOIN itemDataValues v ON d.valueID=v.valueID "
            "WHERE d.itemID NOT IN (SELECT itemID FROM deletedItems) AND ")
    if args.doi:
        return [r[0] for r in c.execute(base + "f.fieldName='DOI' AND lower(v.value)=lower(?)",
                                        (args.doi.strip(),))]
    if args.title:
        return [r[0] for r in c.execute(base + "f.fieldName='title' AND lower(v.value) LIKE ?",
                                        (f"%{args.title.lower()}%",))]
    if args.author:
        ids = [r[0] for r in c.execute(
            "SELECT DISTINCT ic.itemID FROM itemCreators ic JOIN creators cr "
            "ON ic.creatorID=cr.creatorID WHERE lower(cr.lastName) LIKE ? "
            "AND ic.itemID NOT IN (SELECT itemID FROM deletedItems)",
            (f"%{args.author.lower()}%",))]
        if args.year:
            ids = [i for i in ids if (field(c, i, "date") or "").startswith(str(args.year))]
        return ids
    return []


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--doi")
    ap.add_argument("--title")
    ap.add_argument("--author")
    ap.add_argument("--year")
    ap.add_argument("--citekey")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")  # titles carry ligatures; Windows consoles default to GBK

    db = snapshot("zotero.sqlite")
    if db is None:
        print(json.dumps({"error": f"no zotero.sqlite under {ZOTERO}"}))
        return
    c = sqlite3.connect(f"file:{db}?mode=ro", uri=True)

    keymap = {}
    bbt = snapshot("better-bibtex.sqlite") or snapshot("better-bibtex-search.sqlite")
    if bbt:
        try:
            b = sqlite3.connect(f"file:{bbt}?mode=ro", uri=True)
            keymap = {r[0]: r[1] for r in b.execute("SELECT itemID, citekey FROM citekeys")}
        except sqlite3.Error:
            keymap = {}

    if args.citekey:
        ids = [i for i, k in keymap.items() if k == args.citekey]
    else:
        ids = find(c, args)

    out = [{
        "itemID": i,
        "citekey": keymap.get(i),
        "authors": creators(c, i),
        "year": (field(c, i, "date") or "")[:4],
        "title": field(c, i, "title"),
        "journal": field(c, i, "publicationTitle"),
        "doi": field(c, i, "DOI"),
        "abstract": field(c, i, "abstractNote"),
        "pdfs": pdfs(c, i),
    } for i in ids]
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
