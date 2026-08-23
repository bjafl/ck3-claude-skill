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
| 00 | `meta` | **done** | 6/6 items. `faq.md` needs a follow-up re-pass — see session log, real content-quality issue not just hygiene |
| 01 | `character-mechanics` | **substantially done** | 13/14 items (Family correctly skipped — disambiguation page, no content) |
| 02 | `realm-and-succession` | **substantially done** | 24 files: 6 from the by-hand Government pilot + 18 from the Workflow batch |
| 03 | `religion-and-culture` | **done** | all 14 items written |
| 04 | `intrigue-and-diplomacy` | **done** | 2 items — genuinely thin category, confirmed via search (Faction/Secret/Marriage all fold into other files) |
| 05 | `warfare` | **done** | 6 items (Situations deduped into 02, see below) |
| 06 | `court-and-council` | **merged into 02** | see taxonomy correction above |
| 07 | `rulers-and-dynasties` | **done** | Bookmarks + curated Interesting-characters highlights (source page is 334 KB, condensed to ~18 KB) |
| 08 | `decisions-and-activities` | **done** | Decisions hub + 3 decision-type pages |
| 09 | `achievements` | **done** | 10 DLC-group files + index, built via `split_achievements.py` (zero-LLM — wiki already groups achievements by `### DLC` heading) |
| 10 | `strategy` | **done** | Beginner's guide (Walkthroughs stay excluded, cross-referenced by name only) |
| 11 | `reference` | **in progress** | 11/12 zero-LLM candidates done (9 building sub-lists, list-of-kingdoms, list-of-empires). Artifacts list flagged as NOT a clean zero-LLM candidate (29% prose) — needs a writer pass instead. |

`skill/` directory: still empty. `wiki-crawler/corpus/_tooling/manifest.tsv`: 94 entries, all
verified consistent (`_tooling/check_corpus.py` — no duplicates, no dangling references, every
corpus `.md` file accounted for, regenerated from disk ground truth via `_tooling/regen_manifest.py`
each round rather than trusting accumulated appends — see session log for why).

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

All 12 categories now have content (11/12 fully, `reference` at 11/12 zero-LLM items with the
Artifacts list still open). What's left:

1. **`faq.md` needs a real re-pass** — see session log, it's still close-to-verbatim in its
   remaining ~30 sections despite the marketing-section strip. Best done as its own small Workflow/
   agent job with an explicit "compress and flag outdated content" instruction, not a quick hand-fix.
2. **Artifacts list** (`11-reference`) — the last zero-LLM candidate, flagged as NOT actually clean
   (29% prose) — needs a real writer pass instead of `extract_reference.py`.
3. **Decide the 06-into-02 taxonomy fold-in for real** (update `HANDOFF.md` §4) — still only a
   flagged note in `_tooling/workitems/README.md`, never formally applied.
4. **`01-character-mechanics/traits-overview.md`** covers all of Traits in one file — the original
   work-item note guessed it would need splitting into several; it didn't, per a spot-check. Revisit
   only if it turns out too large in practice for the skill's retrieval needs.
5. Once content is believed complete: run `check_corpus.py` one more time, then move to HANDOFF §7
   step 5 — cross-link scan (partially covered by check_corpus.py already), `README.md`/`INDEX.md`
   with routing hints, copy into `skill/ck3-companion/references/`, eval pass via `skill-creator`,
   description-optimization loop, package via `scripts.package_skill`.

`build_workflow_args.py` + `batch-write-category.js` (now supporting per-item `dir` overrides for
combined/thin-category runs) are proven across 2 rounds and 8 Workflow invocations — safe to reuse
as-is for future batches (the Artifacts writer pass, a faq.md re-pass, etc.).

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

**Committed 2026-08-23**: commit `488b628`, 105 files changed. Working tree clean after.

**2026-08-23, same session, round 2**: user asked to finish the remaining work-item lists then run
4 more parallel Workflow batches. Explored the real wiki for the 3 unexplored categories plus
completed 04's list:

- **04-intrigue-and-diplomacy**: confirmed genuinely thin — Schemes and Alliance are the only real
  dedicated pages; Faction/Secret/Marriage all fold into other already-covered pages (Subjects,
  Hooks, Interactions respectively per search results). List stays at 2 items.
- **07-rulers-and-dynasties**: `Bookmarks` (51 KB, real content, 8 start-date recommendations) and
  `Interesting characters` — the latter is **334 KB**, a per-start-date roster hitting the same
  granularity trap as `List of counties` (HANDOFF §3). Work item explicitly instructs picking
  ~20-30 notable/achievement-relevant characters rather than reproducing the full list.
  `Ruler Designer` already covered in 01, not duplicated here.
- **08-decisions-and-activities**: `Category:Decisions` confirmed — Decisions hub + Adventurer/
  Character/Ruler decisions (4 items). `Activity`/`Activities` already covered in 01, not
  duplicated.
- **10-strategy**: `Beginner's guide` (27 KB, real content) is the only solid candidate; the 2
  known Walkthroughs stay excluded per the existing low-value judgment, just cross-referenced by
  name.

Since 04 and 07 were both very thin (2 items each), combined them into one Workflow run using a
new `dir` field on work items (`batch-write-category.js` updated to take `item.dir` as an
override, falling back to the run's `categoryDir` — backward compatible with all earlier runs) so
one Workflow call can write into two different category directories. This kept the total at
exactly 4 parallel Workflow invocations as asked, covering all 5 remaining categories:

| Categories | Items | Task ID | Run ID |
|---|---|---|---|
| 00-meta | 6 | `woafslwas` | `wf_e1503d75-b1e` |
| 08-decisions-and-activities | 4 | `wc42kojq5` | `wf_89d12216-41f` |
| 10-strategy | 1 | `wevnuikgm` | `wf_ad87245a-eab` |
| 04-intrigue-and-diplomacy + 07-rulers-and-dynasties | 4 | `wr09ogj8k` | `wf_637e617d-0a4` |

New work-item files: `_tooling/workitems/08-decisions-and-activities.json`,
`_tooling/workitems/10-strategy.json`, `_tooling/workitems/04-and-07-combined.json`.

**Results, all 4 landed**: 15 new files, corpus went from 79 → 94. Same "missing StructuredOutput"
failure mode hit 2 of the 4 runs (00-meta's single 6-item batch, and interestingly *not* the other
3) — same recovery as before: the files were correctly written to disk regardless, only the
workflow's own aggregated JSON came back empty for that one. Post-batch hygiene pass found:

- **Same `category:` numbering bug recurred** across all 4 new directories (`category:
  00-meta` instead of `category: meta`, etc.) — same `sed` fix as round 1. Worth revisiting the
  style cheat-sheet wording if this keeps recurring; it's now happened in both rounds despite the
  cheat-sheet's own front-matter example showing the bare form.
- **All 6 files in the 00-meta batch had empty `tags: []`** (the same batch that hit the
  StructuredOutput failure — plausibly related, though not confirmed causally). Fixed with
  `backfill_tags.py`, same as round 1.
- **3 broken cross-links** in `decisions-overview.md` — the agent guessed at paths for content it
  hadn't actually seen (`../02-realm-and-succession/adventurers.md` — no such file, meant the
  Adventurer government section of `government-overview.md`; `./activities.md` — assumed same-
  directory, actually lives in `01-character-mechanics/`; `../03-character-development/lifestyle.md`
  — invented a category name that doesn't exist, actually `01-character-mechanics/lifestyle.md`).
  Fixed by hand. **Lesson for future batches**: agents cross-linking to content from *other*
  categories they didn't write this run are guessing at paths — consider passing a short index of
  already-known corpus paths into the prompt for categories with heavy cross-category linking.
- **`faq.md` was a real content-quality problem, not just hygiene**: the source wiki page is
  Paradox's 2020 pre-launch community FAQ. The agent fetched and kept the entire page almost
  verbatim (133 KB), including ~210 lines of pure 2020 marketing/pre-order/release-logistics
  content (pricing in USD, "PURCHASE NOW!", GeForce Now availability) that has zero value for a
  current player and violates STYLE.md rule 2 (rewrite/compress, don't paste). This wasn't caught
  by my own work-item note either — I hadn't previewed the page before assigning it. Fixed the
  worst of it by hand: stripped the marketing section entirely (down to 122 KB) and added an
  explicit `> ⚠️` banner noting the remaining ~30 sections are pre-launch dev commentary and may be
  outdated. **Not fully fixed** — the remaining sections are still close-to-verbatim Q&A, not
  compressed to ~half length per STYLE.md rule 2. Flagged as a follow-up: this file genuinely needs
  a real writer-agent re-pass (fetch fresh, rewrite with explicit outdated-content judgment per
  section), not something to rush through by hand.
- **`interesting-characters.md` curation was genuinely good** — the 334 KB source page was
  condensed into a well-organized ~18 KB highlights file (curated subset by start date/region,
  tight 2-4 sentence entries with real hooks), exactly what the work item asked for instead of
  reproducing the full roster.
- **`qna.md` vs `faq.md` overlap check (flagged in the work item) turned out to be a non-issue** —
  different real sources (QNA = community Discord Q&A, FAQ = dev pre-launch commentary), kept as
  separate files correctly.

Post-fix state: `check_corpus.py` clean (94 files, no broken links, no manifest issues, no empty
tags).

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
