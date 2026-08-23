# Work-item lists

One JSON file per corpus category, `<NN>-<name>.json`, each a flat array of:
```json
{ "title": "<exact wiki page title>", "output": "<slug>.md", "notes": "<optional>" }
```
`title` is the exact MediaWiki page title (spaces, not underscores; redirects resolve
automatically since fetch.py always passes `redirects=1`). `output` is the suggested corpus
filename (not the full path — the category directory is implied by the JSON filename). These
are **planning lists**, not yet verified page-by-page for size/tabularity/prose-vs-table split —
treat each `notes` field's warning seriously before batching.

Status: built from real `category_members`/`allcategories` recon done 2026-08-23 (see LEDGER.md)
plus the `Mechanics` hub page's own navbox (cached at `_tooling/mechanics-hub-master-raw.md`,
lines 71-85 — the wiki's own canonical grouping, more complete than the on-page table above it).

**Taxonomy correction found while building these lists**: the wiki's own navbox groups Council,
Court, Power sharing, Subjects, Succession, Government, Laws, Decisions, Titles, Barony, County,
Buildings, Royal court, Domiciles, and Great projects all under one "Realm & Governance" bucket —
there's no wiki-side split matching HANDOFF.md §4's separate `06-court-and-council` category.
Recommendation: fold 06 into 02 (`realm-and-succession`) rather than force a split the source
material doesn't have. Not yet applied to HANDOFF.md §4 — flagging here for a deliberate decision
rather than silently changing the taxonomy again this session.

Categories not listed here yet (07-rulers-and-dynasties, 08-decisions-and-activities,
10-strategy) still need their own `category_members`/hub-page exploration before a work-item list
can be built — don't guess page titles for these, verify first (see HANDOFF.md §7 step 1).

`04-intrigue-and-diplomacy.json` is **known incomplete** — only Schemes and Alliance are
confirmed real titles. Factions, secrets, and vassalization-interaction pages weren't confirmed
during this session's recon; run `search_titles("faction")` / `search_titles("secret")` etc.
before treating that category as ready to batch.
