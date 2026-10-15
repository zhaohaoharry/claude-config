---
name: feedback-zotero-first
description: "When papers are needed, search the user's Zotero library first (copy zotero.sqlite AND -wal, query by author), then go online"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a92848a1-ac62-4dd2-9e7f-f902cdbb3c6e
  modified: 2026-10-06T02:41:59.640Z
---

Look for papers in Zotero (C:\Users\haozh\Zotero) before downloading them from the web.

**Why:** the user keeps a large Zotero library (~3,000 items) with published PDFs. On 2026-10-06 I missed ACF 2015, De Loecker 2011, GNR, Grieco–Li–Zhang and Zhang 2019, which were all there, and downloaded working papers instead. The user had to correct me.

**How to apply:**
- Copy both zotero.sqlite and zotero.sqlite-wal to the scratchpad before querying. A copy of zotero.sqlite alone is stale.
- Query by creator last name (itemCreators → creators), not only by title LIKE.
- Attachments live at storage/<key>/<file>. Check page 1, because one item can carry a supplement, a working paper and the published version.
- Go online only for what is not in Zotero.
- See [[research-data-repository]] for datasets.
