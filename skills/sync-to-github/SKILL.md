---
name: sync-to-github
description: Sync figures and tables referenced by your tex files into the GitHub/Overleaf repo folder, then commit and push. Only copies files actually used in the paper — not every file in latex/.
argument-hint: "[optional commit message]"
allowed-tools: ["Bash", "Glob", "Read", "Write"]
---

# Sync to GitHub/Overleaf — Smart Pipeline

Copy only the figures and tables **actually referenced** in your tex files into the repo folder, then commit and push to GitHub.

## Background

Tex files (main.tex, appendix.tex, beamer slides, response letters, cover letters) live directly in the repo folder and are already tracked by git — no copying needed for them.

Programs produce many figures and tables locally in `latex\figures\` and `latex\tables\`, but only a subset are used in the paper. This skill scans your tex files and copies only the referenced ones.

---

## Steps

### 1. Find the GitHub repo folder
Look for a subfolder containing a `.git` directory. If multiple exist, ask user which one.

### 2. Identify tex files to scan
List all `.tex` files in the repo folder (main.tex, appendix.tex, beamer files, response letters, cover letters, etc.). Show the list to the user and confirm before proceeding.

### 3. Parse all tex files for figure and table references

**Figures** — scan for:
```
\includegraphics[...]{filename}
\includegraphics{filename}
```
Extract `filename` from each. If no extension given, try `.pdf`, `.png`, `.eps`, `.jpg` in that order.

**Tables** — scan for:
```
\input{tables/filename}
\input{filename}
\include{filename}
```
Extract filenames that resolve to files in `latex\tables\`.

Collect the full deduplicated list of referenced figure and table files.

### 4. Report what was found
```
Figures referenced in tex files (N total):
  - fig1.pdf
  - fig2.pdf
  ...

Tables referenced in tex files (M total):
  - table1.tex
  - table2.tex
  ...
```

### 5. Copy only referenced files

For each referenced figure:
```bash
cp "latex/figures/[filename]" "[repo-folder]/figures/[filename]"
```
If a referenced file is NOT found in `latex/figures/`: flag it as missing (do not stop — continue with the others).

For each referenced table:
```bash
cp "latex/tables/[filename]" "[repo-folder]/tables/[filename]"
```
Same: flag missing files but continue.

### 6. Check for changes
```bash
cd "[repo-folder]"
git status
```
If nothing to commit: report "Nothing to push — repo is already up to date." and stop.

### 7. Determine commit message
- If `$ARGUMENTS` provided: use it
- Otherwise: auto-generate (e.g., "Update figures and tables" or list changed files)
- Show message to user before committing

### 8. Commit and push
```bash
cd "[repo-folder]"
git add .
git commit -m "[commit message]"
git push
```

### 9. Final report
```
✓ Pushed to GitHub
  Figures synced:  N
  Tables synced:   M
  Files changed:   K (in git)
  ⚠ Missing locally (referenced but not in latex/): [list if any]

  Overleaf: Menu → GitHub → Pull from GitHub
```

---

## What this skill does NOT touch
- Files already in the repo folder (`main.tex`, `appendix.tex`, etc.) — git handles those
- Anything in `data\`, `program\`, `literature\` — stays local forever
- Figures/tables in `latex\` that are not referenced by any tex file — stays local

---

## Troubleshooting

### Push rejected (remote has changes)
```bash
cd "[repo-folder]"
git pull
```
Then retry `/sync-to-github`.

### Referenced figure not found locally
The tex file references a figure that doesn't exist yet in `latex\figures\`. Either the program hasn't generated it yet, or the filename in the tex file doesn't match. The skill will flag it — fix the mismatch or generate the figure first.

### First push from this machine (credentials)
Windows Credential Manager handles this. On first push, a browser window will ask you to log in to GitHub once. After that it's stored permanently. If using a token: GitHub → Settings → Developer Settings → Personal Access Tokens.
