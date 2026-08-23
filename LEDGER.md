# CK3 Companion Skill — Ledger

Living status tracker for this project: what's done, what's in progress, what's next, and the
decisions made along the way. Updated every session. For background, methodology, and design
rationale (why this project exists, the token-minimization strategy, lessons carried over from
`hoi4-claude-skill`), see `HANDOFF.md` instead — that file stays stable; this one changes constantly.

---

## Current status by category

Taxonomy reference: see `HANDOFF.md` §4. **Taxonomy correction found 2026-08-23**: fold
`06-court-and-council` into `02-realm-and-succession` — the wiki's own navbox groups Council/Court
with Realm & Governance, there's no source-side split matching a separate category. Not yet applied
to `HANDOFF.md` §4 itself; flagged in `_tooling/workitems/README.md` pending a deliberate pass.

| # | Category | Status | Notes |
|---|---|---|---|
| 00 | `meta` | not started | work-item list ready (`_tooling/workitems/00-meta.json`) |
| 01 | `character-mechanics` | **substantially done** | 13/14 items (Family correctly skipped — disambiguation page, no content) |
| 02 | `realm-and-succession` | **substantially done** | 24 files: 6 from the by-hand Government pilot + 18 from the Workflow batch |
| 03 | `religion-and-culture` | **done** | all 14 items written |
| 04 | `intrigue-and-diplomacy` | not started | work-item list **incomplete** — only 2 confirmed titles, see workitems/README.md |
| 05 | `warfare` | **done** | 6 items (Situations deduped into 02, see below) |
| 06 | `court-and-council` | **merged into 02** | see taxonomy correction above |
| 07 | `rulers-and-dynasties` | not started | **no work-item list yet** — category_members not explored |
| 08 | `decisions-and-activities` | not started | **no work-item list yet** — category_members not explored |
| 09 | `achievements` | **done** | 10 DLC-group files + index, built via `split_achievements.py` (zero-LLM — wiki already groups achievements by `### DLC` heading) |
| 10 | `strategy` | not started | **no work-item list yet** |
| 11 | `reference` | **in progress** | 11/12 zero-LLM candidates done (9 building sub-lists, list-of-kingdoms, list-of-empires). Artifacts list flagged as NOT a clean zero-LLM candidate (29% prose) — needs a writer pass instead. |

`skill/` directory: still empty. `wiki-crawler/corpus/_tooling/manifest.tsv`: 79 entries, all
verified consistent (`_tooling/check_corpus.py` — no duplicates, no dangling references, every
corpus `.md` file accounted for, regenerated from disk ground truth 2026-08-23 after a batch of 4
concurrent Workflow runs corrupted the append-only version — see session log for what happened and
`_tooling/regen_manifest.py` for the fix/recovery tool).

---

## Scaling infrastructure built 2026-08-23

In response to a gap analysis (see session log below) of what was missing to scale `Workflow`-driven
batches with minimized token use per `HANDOFF.md` §5. All of the below is built and verified; none
of it requires `Workflow` itself to have been invoked yet.

- **`fetch.py` icon-noise fix** — raw filename artifacts like `[Holding castle.png]` (alt text that's
  just a leaked image filename) are now dropped entirely at the JS extraction layer instead of
  surviving into fetched markdown for every future writer (agent or script) to notice and strip by
  hand. Verified: `Castle buildings` fetch went from `[Holding castle.png] Castle holdings` to clean
  `Castle holdings`. Meaningful alt text (e.g. `[Roads to Power]`) is untouched.
- **`_tooling/style-cheatsheet.md`** — the condensed 5-10 line style-rules block from HANDOFF.md §5.2
  point 1, ready to paste into writer-agent prompts instead of a `Read STYLE.md` call per agent.
- **`ck3_wiki_crawler.extract_reference`** — zero-LLM extraction for tabular reference pages (§5.5).
  Fetches a page, strips breadcrumb-nav lines and the trailing navbox "References" section, wraps in
  front matter, writes the file, appends manifest. Run on 11 pages so far (9 building sub-lists +
  list-of-kingdoms + list-of-empires), all clean on inspection.
- **`ck3_wiki_crawler.split_achievements`** — zero-LLM split of the cached `Achievement` master page
  (188 achievements) into 10 per-DLC-group files + an index, by the wiki's own `### <DLC>` headings.
  No LLM judgment needed since the wiki already did the grouping.
- **Master-page cache** (§5.4) — `Achievement` (147 KB), `Mechanics` hub (2.7 KB, has the wiki's own
  canonical topic grouping — more complete than its on-page table), `Innovation` (47 KB), `Traits`
  (97 KB) all fetched once and cached to `_tooling/*-master-raw.md`.
- **Work-item lists** (`_tooling/workitems/*.json`) — real page titles (not guessed) for categories
  00, 01, 02 (remainder), 03, 04 (partial), 05, 11. See per-category notes above for what's still
  missing (07, 08, 10 need their own `category_members` exploration first).
- **`_tooling/check_corpus.py`** — link-checker + manifest-hygiene script (HANDOFF.md §6). Checks
  relative cross-links resolve, manifest has no duplicates/malformed lines/missing-file references,
  every corpus `.md` file is manifest-accounted-for. Run clean except the 2 known forward-references
  from the pilot batch (`subjects.md`, `resources.md` — expected until those files exist).
- **`_tooling/workflow-scripts/batch-write-category.js`** + **`_tooling/build_workflow_args.py`** —
  the actual `Workflow` script for batch-writing a category (pipeline of Haiku agents, one per
  6-item batch, style cheat-sheet inlined into each prompt) plus a helper that assembles the
  script's `args` payload from a work-item file (items + cheat-sheet text + paths — the script has
  no filesystem access, everything must be pre-loaded). **Staged, not run** — invoking the actual
  `Workflow` tool still needs your explicit go-ahead in this session; writing/staging the script
  itself doesn't require that.

---

## Next planned step

Infrastructure gaps from the last session are closed (see above). What's left before a full-scale
build:
1. **Your explicit go-ahead to invoke `Workflow`** — still not given; this is the one item on the
   original gap list that isn't a script/tooling problem.
2. Fill the 3 missing work-item lists (07-rulers-and-dynasties, 08-decisions-and-activities,
   10-strategy) via `category_members`/`search_titles` before batching those.
3. Complete 04-intrigue-and-diplomacy's work-item list (currently only 2 of an unknown-but-larger
   set of real titles confirmed).
4. Decide the 06-into-02 taxonomy fold-in for real (update `HANDOFF.md` §4), rather than leaving it
   as a flagged note.

Once (1) happens: run `build_workflow_args.py` on a work-item file, invoke `Workflow` with
`batch-write-category.js` + that args payload, verify output quality on the first batch before
launching the rest, chunk into parallel `Workflow` calls per HANDOFF §5.7 for anything past ~15-20
items. `02-realm-and-succession`'s remaining 18 items are the natural first real batch (list ready,
category partially validated already by the by-hand pilot).

**2026-08-23, later same session**: user gave the go-ahead and asked for 4 parallel Workflow runs.
Launched via `batch-write-category.js` (Haiku, batchSize 6) on the 4 categories with the most
complete work-item lists — keep these Run IDs for resume if a batch fails partway (HANDOFF §6, a
known HOI4 failure mode was hitting session usage limits mid-batch):

| Category | Task ID | Run ID |
|---|---|---|
| 01-character-mechanics | `wt3uv6bm6` | `wf_1f4d95a1-c34` |
| 02-realm-and-succession | `wle17rohg` | `wf_6f4948ed-03b` |
| 03-religion-and-culture | `wyvgej6ae` | `wf_bac7d25a-ce6` |
| 05-warfare | `w073fg1z3` | `wf_6f52226a-5c8` |

`scriptPath` for all 4: `wiki-crawler/corpus/_tooling/workflow-scripts/batch-write-category.js`.

**Results, all 4 landed**: 52 new files, corpus went from 28 → 80 (then 79 after dedup, see below).
No agent errors, but real issues surfaced on inspection — exactly why HANDOFF §6 calls for an
explicit hygiene pass rather than trusting agents:

- **Manifest got badly mangled** by concurrent appends across 4 simultaneous workflows: one
  batch's shell command dropped the `/` (and a letter) when building its path, e.g.
  `01-character-mechanicshooks.md` instead of `01-character-mechanics/hooks.md`; several lines
  were duplicated across retries; one had a garbled 4th field. **The actual files on disk were
  always correct** — only the manifest log was corrupted. Fix: wrote `_tooling/regen_manifest.py`,
  which rebuilds manifest.tsv from scratch by reading every corpus file's own front matter rather
  than trusting accumulated appends. Now the standard recovery tool if this happens again.
- **One batch (01-character-mechanics) silently lost its structured report** — the agent did the
  real work (fetched, wrote 6 files, appended manifest lines) but never called the required
  StructuredOutput tool, so the workflow's aggregated JSON result was missing those 6 files
  entirely even though they existed on disk. Lesson: **verify against the filesystem, not just the
  workflow's returned JSON** — the aggregate result undercounts what actually happened.
- **`Situation` got written twice** — both 02-realm-and-succession and 05-warfare had it on their
  work-item lists (flagged as a known risk in the lists themselves) and both agents wrote it
  independently. Kept the better-structured 02 copy (matches the wiki's own categorization), but
  it was missing the Royal Court DLC gating that the 05 copy had correctly caught — patched that in
  by hand, then deleted the 05 duplicate.
- **`category:` front matter was inconsistent**: all 4 new batches wrote the numbered directory
  name (`category: 02-realm-and-succession`) instead of the bare category name STYLE.md's own
  example uses (`category: realm-and-succession`, matching the earlier hand-written pilot files).
  Fixed with a `sed` pass across all 52 files.
- **26/79 files had empty `tags: []`** despite the style cheat-sheet asking for retrieval keywords.
  Rather than spend more agent tokens re-writing files just for tags, wrote
  `_tooling/backfill_tags.py` — a zero-LLM heuristic (title words + category + first 2 section
  headings) — and ran it. Good enough for retrieval; not a substitute for better tags later if
  it turns out to matter.
- **3 files had leaked wiki template-rendering errors** (`(unrecognized string "kuzarism" for
  Template:Icon)`) that the writer agents didn't catch/strip per STYLE.md rule 6 — a genuine
  wiki-side glitch, not a fetch bug. Cleaned by hand with `sed`; not yet automated since only 3
  instances were found (may be worth a regex in `fetch.py` if this recurs at scale).
- **Content quality itself, on spot-check, is good** — e.g. `traits-overview.md` condensed the
  entire 103 KB, 15-section Traits master page into one coherent 13.8 KB file with full numeric
  fidelity, better than the "probably needs splitting into multiple files" guess in its work-item
  note. `succession.md` reads dense and well-organized, DLC-gating and tips sections intact.

Post-fix state: `check_corpus.py` clean (79 files, no broken links, no manifest issues, no empty
tags). Corpus is now 79 files across 6 categories (00 not started, 04/06/07/08/10 not started or
merged, 09 and most of 11 done, 01/02/03/05 substantially built).

---

## Session log

### 2026-08-23 — recon + pilot batch

- Explored the real wiki category taxonomy (`action=query&list=allcategories` + `category_members`
  spot-checks). Confirmed current patch = 1.19 (1.19.0.6, released 2026-05-25). Folded findings into
  `HANDOFF.md` §3/§4 as reference facts (not reproduced here — see that file).
- Two gotchas found, now documented in `HANDOFF.md` §3: the wiki also hosts several total-conversion
  mods as regular categories (CK3AGOT, RICE, Rajas of Asia, The Fallen Eagle, etc.) — must stay
  excluded from this vanilla-only corpus; and `List of counties` is a 689 KB generated dump, far too
  granular to crawl 1:1.
- Ran a pilot batch by hand (no `Workflow` — that needs explicit user opt-in for multi-agent
  orchestration, not yet given) on the Government sub-topic of `02-realm-and-succession`:
  - Wrote `government-overview.md` + `government-{feudal,tribal,clan,administrative,nomadic}.md`
    (6 files, 35.6 KB), appended all 6 to `manifest.tsv`.
  - Compression: ~30-58% off raw fetched prose (most files ~40-50%), full stat-table fidelity kept
    per STYLE.md rule 1.
  - Caught and fixed one style-rule violation during writing: an early draft of
    `government-administrative.md`'s Family Attributes table dropped the level-2 tier of a 3-level
    progression "to save space" — STYLE.md rule 1 (never round/approximate numbers) + rule 10 (long
    files are fine) together forbid this; expanded back to all 3 levels before finalizing.
  - Theocracy and Republic (2 of the 16 government types) turned out to redirect to the `Government`
    hub page rather than having dedicated articles — documented only in `government-overview.md`,
    no separate file. ~10 other types (Mandala, Wanua, Celestial, Meritocratic, Meritocratic
    Khanate, Ritsuryō, Sōryō, Herder, Holy Order, Mercenary Company) also have no dedicated page —
    covered only by the overview's summary tables, flagged `_Not covered on the wiki._` per style
    rule 8.
  - Quality read: good. Recommendation was to proceed to scaling with the same approach.
- User asked to split ongoing status/planning out of `HANDOFF.md` into this file — this ledger was
  created as a result, and the progress-tracking material previously added to `HANDOFF.md` §§1/3/4/7
  and the standalone §6b was trimmed back out / moved here.
- User asked for a gap analysis of what's needed to scale `Workflow`-driven batches with minimized
  tokens. Found (by actually inspecting this repo and the `hoi4-claude-skill` sibling, not just
  reasoning from HANDOFF.md's prose): no `Workflow` script existed anywhere (HOI4's own were
  per-session and never persisted), no inlined style cheat-sheet, no zero-LLM extraction script (and
  no verification of which pages actually qualify), no master-page cache, no work-item lists, no
  link-checker (also never persisted in HOI4). Also caught a real naming bug: `HANDOFF.md` and
  several other files referred to the sibling project as `hoi-claude-skill`; its real name is
  `hoi4-claude-skill` — fixed everywhere.
- User asked to build the missing scripts and close the gaps. Did so — see "Scaling infrastructure
  built 2026-08-23" above for the full list. Along the way, ran the new zero-LLM tools for real
  rather than just building and shelving them: achievements (10 files) and 11/12 reference pages are
  now actually done, not just planned. Also found and fixed a real cruft-noise bug in `fetch.py`
  (raw `.png` filenames leaking through as fake alt text) while investigating tabularity of candidate
  reference pages — a good example of infrastructure work surfacing a fix that benefits every future
  fetch, automated or hand-written.
- Nothing committed to git yet this session — pending user confirmation.
