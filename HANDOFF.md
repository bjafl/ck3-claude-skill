# CK3 Companion Skill — Handoff

Sibling project to `../hoi4-claude-skill`, which built a Claude skill for Hearts of Iron IV using a
scrape → distill → condense → package pipeline. This project applies the same proven methodology to
Crusader Kings III, with specific improvements to cut the token cost of the crawl/distill phase,
which ran noticeably heavier than it needed to on the HOI4 build.

**Read this whole document before starting.** It's written so a fresh agent with no other context
can pick up the work and make good decisions immediately, not just follow steps blindly. This file
holds background, design rationale, and methodology — it's meant to stay stable. For **current
status, what's done, and what's planned next, see `LEDGER.md`** instead; that file is the living
tracker and changes every session.

---

## 1. What this project starts with

- `wiki-crawler/fetcher/` — a working Playwright-based crawler, ported from HOI4's `hoi_wiki_crawler`
  and renamed to `ck3_wiki_crawler`. Headless Chromium passes `ck3.paradoxwikis.com`'s Fastly "Client
  Challenge" exactly like it does on the HOI4 wiki (same hosting platform) — confirmed by loading
  `WIKI_ENTRY_URL` and getting a real page title ("CK3 Wiki"), not the challenge page. `uv sync` +
  import both work. No separate `playwright install` needed — the Chromium binary cache is shared
  across projects at `~/.cache/ms-playwright`, not per-venv, and it was already installed while
  building the HOI4 project.
- `wiki-crawler/corpus/_tooling/STYLE.md` — ported and adapted from HOI4's version. Same authoring
  rules (front matter schema, number-fidelity, condensing, cross-linking), CK3-specific examples
  swapped in.
- `.gitignore` copied (covers `.venv/`, `__pycache__/`).

See `LEDGER.md` for what's been built on top of this since (corpus content, category progress).

---

## 2. Why this project exists as a separate repo, not a folder in hoi4-claude-skill

Decided when starting this: the crawler *tool* is the only genuinely reusable part (confirmed by
how easily it ported — rename the package, swap one URL, done). The corpus and skill content are
100% game-specific and share nothing. `hoi4-claude-skill` as a repo name doesn't fit a second
unrelated game either. If a third Paradox game skill gets built later, consider whether a genuinely
shared crawler *package* (published once, imported by each game's project) is worth the overhead at
that point — for two games it wasn't.

---

## 3. Wiki recon done so far (verify further before committing to a plan)

```
WIKI_ENTRY_URL = "https://ck3.paradoxwikis.com/Crusader_Kings_III_Wiki"   # confirmed live
```

`Category:DLC` members (11, same category-naming convention as HOI4's wiki):
All Under Heaven, By God Alone, Coronations, Fate of Iberia, Friends and Foes, Khans of the Steppe,
Legacy of Persia, Legends of the Dead, Medieval Monuments, Northern Lords, Roads to Power,
Royal Court (DLC), Silk & Silver, Tours and Tournaments, Wandering Nobles, Wards and Wardens
(plus the general `Downloadable content` overview page — 17 total, matching HOI4's pattern almost
exactly).

Current patch (confirmed via the homepage's "Game history" section, check it again if a lot of time
has passed since this was written): **1.19** (latest micro-patch 1.19.0.6, released 2026-05-25). By
God Alone is an announced-but-unreleased DLC (2026-09-30) — don't write content for it yet, and don't
count it in DLC totals. Use `game_version: "1.19"` in front matter until this changes.

§4 below has the confirmed real category taxonomy (replacing the original hypothesis). Two gotchas
found along the way, both important for every future batch:

1. **The wiki hosts several total-conversion mods as regular content**, not just the vanilla game:
   `CK3AGOT`, `RICE`, `Rajas of Asia`, `The Fallen Eagle`, `Realms in Exile`, `Lotr:RiE`, `Way of
   Kings`, `When the World Stopped Making Sense`, `DATAW`, `WCGOA` all showed up as top-level
   categories in a full `allcategories` dump. **Never fetch/write content from these** — this corpus
   is vanilla CK3 only. If a `search_titles` or `category_members` result includes a page that looks
   mod-specific (unfamiliar faith/culture/mechanic names, especially fantasy/setting-specific ones),
   verify it isn't one of these before using it.
2. **Some "list" pages are enormous generated dumps, not hand-written wiki content** — `List of
   counties` alone is 689 KB (3,476 individual counties, scripted from game data). This is far too
   granular for a companion skill and must not be crawled/condensed 1:1. If a category needs county-
   level detail at all, keep it to a tiny curated/summarized subset (e.g. "notable capitals") rather
   than reproducing the list. Check page size with a quick `fetch_pages` call before committing a
   category to using a page like this as a source.

---

## 4. Category taxonomy — confirmed against the real wiki

The original hypothesis below turned out mostly right at the theme level but wrong on the details —
CK3's own `Category:*` structure is flatter and more scattered than HOI4's. Real MediaWiki categories
found via a full `action=query&list=allcategories` dump plus `category_members` spot-checks on the
vanilla-relevant ones:

`Category:Character` (26: Activity, Alliance, Artifacts, Artifact modifiers, Attributes, Court,
Culture, Dynasty, Family, Form of address, Hooks, Interactions, Interesting characters, Knight,
Lifestyle, Modifiers, Nickname, Prisoner, Resources, Ruler Designer, Schemes, Traditions, Traits,
Travel, …), `Category:Realm` (19: Barony, Building, Council, County, Court, Domicile, Government,
Great projects, Knight, Laws, Power sharing, Prisoner, Royal court, Situation, Stories, Struggles,
Subjects, Succession, Titles), `Category:Religion` (11: Abrahamic/Dharmic/Pagan/Sinitic faiths,
Doctrines, Faith, Great holy war weights, Holy sites, Holy war, Tenet), `Category:Governments` (16
distinct types + hub), `Category:Laws` (Authority laws, Laws, Succession laws), `Category:War`
(Alliance, Army, Casus belli, Hired forces, Warfare, Duel), `Category:Buildings` (9 sub-lists:
Castle/County/Duchy/Economic/Military/Special/Temple/Temple Citadel/Tribe buildings),
`Category:Decisions` (Adventurer/Character/Ruler decisions), `Category:Domiciles` (Administrative
estate, Camp, Celestial estate, Manor, Nomadic capital), `Category:DLC` (17, matches original recon),
`Category:Patches` (39 — do **not** crawl all of these, see below), `Category:Lists` (Interesting
characters, Keyboard shortcuts, List of counties/duchies/kingdoms/empires — see §3's warning on
`List of counties`), `Category:Guides` (FAQ, **Jargon** = the glossary, QNA, Tutorial videos),
`Category:Walkthroughs` (2 long narrative let's-plays — low compression value, likely skip or fold
one line into `strategy`). Separately, big single-page reference/hub content exists outside any
tidy category: `Traits` (103 KB), `Achievement` (148 KB, 188 achievements in one page — check
whether it's already grouped by DLC before deciding on a per-DLC-file split like HOI4 used),
`Innovation` (50 KB), and a `Mechanics` hub page that links out to ~30+ per-topic detail pages (the
closest CK3 equivalent of HOI4's `01-mechanics`).

Revised category list (numbering still gappy/renumberable on purpose). For which of these have
actually been built out, see `LEDGER.md`.

**Taxonomy correction, applied 2026-08-23**: the original hypothesis had a separate
`06-court-and-council` category. Dropped — the wiki's own navbox groups Council/Court with the
rest of Realm & Governance (see `Mechanics` hub page, cached at
`wiki-crawler/corpus/_tooling/mechanics-hub-master-raw.md`), and there's no source-side content
split that would justify keeping them apart. Council and Court live in `02-realm-and-succession`.
Numbers 07 onward were **not** renumbered down to fill the gap — corpus directories already exist
under the original numbers (`07-rulers-and-dynasties`, `08-decisions-and-activities`, etc.) and
renumbering after content exists isn't worth the churn.

| # | Category | Confirmed content |
|---|---|---|
| 00 | `meta` | DLC index, patch history (summarized, not all 39 pages), Jargon glossary, FAQ/QNA, Bookmarks/game rules |
| 01 | `character-mechanics` | Attributes, Traits, Lifestyle, Interactions, Family, Dynasty, Ruler Designer, Prisoner, Hooks, Travel, Resources, Modifiers, Artifacts (mechanics), Activities |
| 02 | `realm-and-succession` | Titles (Barony/County/Duchy/Kingdom/Empire), **Council, Court** (folded in from the dropped 06), Domicile, Government (16 types), Great projects, Power sharing, Royal court, Situation, Stories, Struggles, Subjects, Succession, Laws |
| 03 | `religion-and-culture` | Faiths (Abrahamic/Dharmic/Pagan/Sinitic), Doctrines, Tenet, Holy sites, Holy war, Culture, Innovation, Traditions, Form of Address |
| 04 | `intrigue-and-diplomacy` | Schemes, Alliance — genuinely thin; Faction/Secret/Marriage content folds into Subjects/Hooks/Interactions in other categories rather than having dedicated pages |
| 05 | `warfare` | Army, Casus belli, Hired forces, Warfare, Duel, Knights |
| ~~06~~ | ~~`court-and-council`~~ | **dropped, folded into 02** — see correction above |
| 07 | `rulers-and-dynasties` | Bookmarks, curated Interesting-characters highlights (source page is 334 KB — see §3-style granularity warning, don't reproduce in full) |
| 08 | `decisions-and-activities` | Decisions hub, Adventurer/Character/Ruler decisions |
| 09 | `achievements` | Per-DLC-group files + index, from the single `Achievement` page (188 total, confirmed exact match) |
| 10 | `strategy` | Beginner's guide; the 2 known Walkthroughs stay excluded (low compression value), cross-referenced by name only |
| 11 | `reference` | Building lists (9 sub-lists), Innovations list, Artifacts catalog, List of kingdoms/empires — zero-LLM scripted where the source page was clean tables (§5.5), a real writer pass where it wasn't (e.g. Artifacts, which was 29% prose) |

---

## 5. Token-minimization strategy for the crawl/distill phase

This is the part explicitly asked for. The HOI4 build worked and produced a genuinely good skill
(validated: 100% vs 33% eval pass rate against a no-skill baseline — see
`../hoi4-claude-skill/skill/hoi4-companion-workspace/iteration-1/benchmark.md` for the numbers), but
the pipeline spent more tokens than it needed to. Here's what to change.

### 5.1 The fetch step was already free — keep it that way

`fetch_pages()`/`search_titles()`/`category_members()` are pure Playwright automation, zero LLM
tokens. This was correct in HOI4 and stays correct here. **Do not** be tempted to have an agent
"read and interpret" a fetched page directly from the browser — always go through the script first,
hand the agent already-fetched markdown text.

### 5.2 The real cost: ~250 separate agent spawns, each paying fixed overhead

HOI4's corpus has 250 files, built mostly as one-agent-per-file (via `Workflow`'s `pipeline()`).
Each spawn re-paid a fixed cost regardless of how small the actual output was:
- Its own system prompt / tool-schema overhead (unavoidable per spawn, but avoidable *in count*)
- A `Read STYLE.md` tool call — full ~90-line file, every single time
- Often a "skim this example file for tone" `Read` call too
- The fetch step itself
- The actual writing (the one part that's genuinely irreducible — see 5.3)
- A `wc -c` + `printf` manifest-append step

For a country file that's only 4-6 KB of eventual output, the fixed overhead was a large fraction of
the total agent cost. Concretely:

1. **Inline the style rules into the prompt text instead of a `Read STYLE.md` call.** Don't make
   every agent spend a tool round-trip loading the same ~90-line file. Write a condensed "rules
   cheat-sheet" (5-10 lines covering: front matter schema, keep-numbers-exact, strip icons/navbox,
   cross-link, don't invent, manifest-append command) and paste it directly into each generated
   prompt. Full `STYLE.md` still exists as the source of truth for a human/future agent to read once
   when *designing* the pipeline — just don't make every *writer* agent re-read it.

2. **Batch multiple files per agent instead of one-agent-per-file**, especially for small, uniform
   content (country-style profiles, per-DLC achievement groups). Have one agent handle a cluster of
   5-10 related pages in one continuous session: fetch all of them (batched fetch calls), write all
   the output files, append all the manifest lines, return one structured result covering the whole
   batch. This amortizes the fixed per-spawn overhead across more output. The tradeoff is slightly
   messier structured-output tracking (one JSON array of `{filename, bytes, ...}` per agent instead
   of one object) — worth it for anything where individual files are small.

3. **Drop the "skim an example file" step after the first wave.** In HOI4 it was included in nearly
   every prompt "for tone calibration." Once a category's pattern is established (after ~5-10 files
   look right), stop asking later agents to read a full example file — either embed a 3-4 line
   inline snippet directly in the prompt, or drop it entirely and rely on the inlined style rules.

4. **Push more mechanical cleanup into the fetch script, not the writer agent.** `h2md()` in
   `fetch.py` already strips icons/navboxes/edit-sections at the HTML level (cheap, deterministic,
   zero tokens). If a consistent additional cruft pattern shows up during CK3 content review (e.g. a
   specific "External links" heading format, a specific broken-template signature), add it to the JS
   regex/selector list in `fetch.py` rather than telling every future writer agent to notice and
   strip it by hand. Port improvements back to `hoi4-claude-skill`'s `fetch.py` too if they'd help
   there (see the comment left in `fetch.py` here).

### 5.3 What's NOT reducible — don't try to script away prose judgment

Compressing wiki prose to ~half length while keeping 100% of the data, deciding what's worth its own
file vs folding into a shared one, flagging contradictions, writing `**Inferred:**` strategy
synthesis — this needs an LLM. Don't attempt to template/regex this away; it's where the skill's
actual value comes from (confirmed by the eval: baseline-without-skill answers were either vague or
outright hallucinated, e.g. inventing achievement names that don't exist).

### 5.4 Reuse the "fetch shared master page once" pattern aggressively

For any category with a hub/list page (HOI4's `Countries` master stats table, `Achievements` master
list), fetch it **once**, save it to `_tooling/<name>-master-raw.md`, and have every writer agent
`grep`/`sed` its own section out of that saved file instead of re-fetching the same large page N
times. This alone avoided ~80 redundant fetches in the achievements category. Look for CK3
equivalents early — a full character/dynasty list, a full building/innovation list, etc.

### 5.5 For purely tabular reference pages, skip the LLM entirely

Some wiki pages are already a clean table with nothing to compress or judge (a trait list, a
building-cost list). For these, write a small dedicated script — no agent at all — that: fetches the
page, runs it through the existing table-to-markdown conversion, wraps it in the standard front
matter, writes the file. This is the single biggest remaining lever if CK3's reference-list pages
(traits, artifacts, buildings, innovations — CK3 wikis tend to have a lot of these) turn out to be
clean tables, which is likely. Check this early: pull one or two candidate pages with `fetch_pages`
and look at how tabular vs prose-heavy they actually are before deciding whether a category needs an
agent at all.

### 5.6 Model choice

Haiku was used for every writer agent in HOI4 and validated as sufficient — the eval (100% vs 33%
pass rate against baseline) was run against Haiku-written content, not a stronger model. Default to
Haiku here too; only escalate a specific category to a stronger model if an early spot-check shows a
real quality problem (e.g. a category needing unusually subtle judgment).

### 5.7 Concurrency (wall-clock, not token cost, but worth carrying over)

This host has 4 CPUs. The `Workflow` tool's internal concurrency cap is `min(16, CPUs - 2)`, so a
single `Workflow` call here only runs 2 agents at a time. The fix used in HOI4: split a large batch
into 3-4 chunks and launch them as **separate parallel `Workflow` invocations** (each independently
capped at 2) rather than one big one — got ~8x real concurrency instead of 2x. Not a token saving,
but cuts wall-clock a lot; do this again for any batch bigger than ~15-20 items.

---

## 6. Other important lessons from the HOI4 build (not just token-related)

- **claude.ai only accepts "Skills"** (a `SKILL.md` + `references/` folder, zipped), not full Claude
  Code "Plugins" (marketplace.json, hooks, MCP servers). Don't build plugin infrastructure for this.
- **Progressive disclosure is what makes a 250+ file corpus cheap to ship.** Only the skill's
  frontmatter (name + description) sits in context by default; the body loads when the skill
  triggers; `references/` files load only when actually read for a specific question. This is why
  the corpus can be large — just keep individual files reasonably scoped and the routing table (an
  `INDEX.md`, see HOI4's) accurate.
- **Skill autonomous-triggering has a real ceiling.** Even after running skill-creator's full
  description-optimization loop (5 iterations), HOI4's skill topped out around 62% raw accuracy on a
  held-out test set — short, casual-sounding questions (even ones that literally say "hoi4") often
  don't trigger a specialized skill because Claude judges it can probably answer from general
  knowledge alone. This is inherent to the trigger mechanism, not something description wording
  alone fully fixes. The practical mitigation: users can explicitly name the skill in their prompt
  ("use the ck3-companion skill...") to bypass the autonomous judgment entirely.
- **The description-optimization script's own "best" pick can be noisy on a small eval set.**
  `scripts/run_loop.py`'s literal `best_description` field is selected by a majority-vote-per-query
  metric on a small held-out set (8 items in HOI4's case) — it picked the *original* description over
  one with a clearly better trend in the raw per-run numbers (54%→62% test accuracy across
  iterations, precision steady at 100%). If this happens again, trust the raw-run trend over the
  literal `best_description` field rather than assuming the script's pick is definitely best — but
  do sanity-check the description qualitatively (it should read as clear and correctly scoped, not
  just "whatever scored highest by one noisy metric").
- **Session usage limits can interrupt a long batch mid-run** — hit this hard in HOI4 (several
  `Workflow` batches failed partway through with "You've hit your session limit"). Recovery was
  trivial because of `Workflow`'s caching: relaunch with the *same* `scriptPath` + `resumeFromRunId`
  + same `args`, and every already-completed agent replays from cache instantly — only the failed
  ones actually rerun. **Always keep the `scriptPath` and `Run ID` from each `Workflow` launch
  result** so a resume is possible without resending the whole script.
- **Check for redundancy across categories before fetching.** HOI4 found 3 planned reference-list
  categories were already fully covered by content written earlier in the build (a Factions list
  already in the diplomacy mechanics file, a scientists roster already in the special-projects file,
  an operations/operatives list already in the espionage file) and dropped them rather than
  re-fetching duplicates. Do the equivalent check for CK3 before committing to §4's category list.
- **Manifest and cross-link hygiene needs an explicit pass, not just hoping agents get it right.**
  Concurrent/retried writer agents produced a handful of stale/duplicate `manifest.tsv` lines and
  ~16 broken relative cross-links across 250 files in HOI4 (typos, wrong `../` depth, one dangling
  reference to content that got folded elsewhere). A simple Python script (regex for `[text](path)`,
  `os.path.exists` check) catches all of this cheaply — run it as a normal step at the end of each
  category, not just once at the very end of the whole build.
- **`.claude/skills/<name>` should be a symlink into `skill/<name>/`**, not a duplicate copy, once
  this project has an actual skill directory — keeps local Claude Code testing in sync with the
  canonical location automatically. (`hoi4-claude-skill` already does this for its own skill and for
  an unrelated installed skill — same pattern, safe to reuse.)
- **Git discipline**: even solo, stage files by explicit name (never `git add -A`/`.`), and check
  `git status --porcelain` before and after staging in case another session is touching the same
  checkout — see `hoi4-claude-skill`'s CLAUDE.md-driven habit of invoking the
  `concurrent-git-commit-safety` skill before every commit.

---

## 7. Suggested workflow, first steps through completion

1. Explore the CK3 wiki's real category structure (`category_members`/`search_titles`) before
   touching §4's taxonomy — confirm or correct it. (Already done once — see §4 — but re-verify if
   picking this up much later, the wiki changes with patches.)
2. Confirm the actual current game patch version — don't blindly trust §3's snapshot if a lot of
   time has passed.
3. Pick one small category and run a **pilot batch of 5-10 files** using the token-minimized
   approach from §5 (inlined rules, batched agents, no example-file read after the first couple) —
   check output quality before scaling to the full corpus. Cheap insurance against building 250
   files on a broken pattern. Check `LEDGER.md` first — this may already be done for at least one
   category.
4. Once a category's pattern is validated, scale it up the same way HOI4 did: build a work-item
   list (JSON), write one `Workflow` script per category (or a few categories at a time), split into
   parallel chunks per §5.7, launch, verify, repeat. **Get explicit user go-ahead before invoking
   `Workflow`** — multi-agent orchestration needs an explicit opt-in in this harness (the user
   saying so in their own words, or an "ultracode" trigger), it isn't implied by this handoff
   document alone.
5. Follow the same finishing pass HOI4 used at the end: cross-link scan, `README.md`/`INDEX.md`
   with routing hints, copy into `skill/ck3-companion/references/`, eval pass via `skill-creator`,
   description-optimization loop, package via `scripts.package_skill`.

Update `LEDGER.md` as you go — status per category, decisions made, anything a future session
would otherwise have to rediscover. Keep this file (`HANDOFF.md`) itself stable; only edit it for
genuine corrections to background facts or methodology, not for status updates.

Good luck — the hard part (proving the crawler works against Paradox's bot protection, and proving
the whole scrape→skill pipeline actually produces something measurably better than no skill at all)
is already done once, in the sibling project. This one should go faster.
