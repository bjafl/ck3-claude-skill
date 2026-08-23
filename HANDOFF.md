# CK3 Companion Skill — Handoff

Sibling project to `../hoi-claude-skill`, which built a Claude skill for Hearts of Iron IV using a
scrape → distill → condense → package pipeline. This project applies the same proven methodology to
Crusader Kings III, with specific improvements to cut the token cost of the crawl/distill phase,
which ran noticeably heavier than it needed to on the HOI4 build.

**Read this whole document before starting.** It's written so a fresh agent with no other context
can pick up the work and make good decisions immediately, not just follow steps blindly.

---

## 1. What's already done in this project

- `wiki-crawler/fetcher/` — a working Playwright-based crawler, ported from HOI4's `hoi_wiki_crawler`
  and renamed to `ck3_wiki_crawler`. **Verified working today**: headless Chromium passes
  `ck3.paradoxwikis.com`'s Fastly "Client Challenge" exactly like it does on the HOI4 wiki (same
  hosting platform), confirmed by loading `WIKI_ENTRY_URL` and getting a real page title ("CK3
  Wiki"), not the challenge page. `uv sync` + import both work. No separate `playwright install`
  needed — the Chromium binary cache is shared across projects at `~/.cache/ms-playwright`, not
  per-venv, and it was already installed while building the HOI4 project.
- `wiki-crawler/corpus/_tooling/STYLE.md` — ported and adapted from HOI4's version. Same authoring
  rules (front matter schema, number-fidelity, condensing, cross-linking), CK3-specific examples
  swapped in. **Not yet finalized** — see §4, the category/naming sections have open TODOs pending
  the taxonomy decision.
- `.gitignore` copied (covers `.venv/`, `__pycache__/`).
- Quick recon done (see §3) confirming `Category:DLC` exists with the same naming convention as
  HOI4's wiki, and roughly what patch versions exist.

**Not started**: `wiki-crawler/corpus/`'s actual content (only `_tooling/` exists), `skill/`
(completely empty), git init/commit for this project.

---

## 2. Why this project exists as a separate repo, not a folder in hoi-claude-skill

Decided when starting this: the crawler *tool* is the only genuinely reusable part (confirmed by
how easily it ported — rename the package, swap one URL, done). The corpus and skill content are
100% game-specific and share nothing. `hoi-claude-skill` as a repo name doesn't fit a second
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

Highest patch number surfaced by a `search_titles("patch notes")` call: **Patch 1.19.X** — treat
this as a lower bound, not a confirmed "current version." Confirm the actual current patch before
starting real content work (check the wiki's own homepage or a `Patches` hub page), and use that
number as `game_version` in every file's front matter, matching the convention STYLE.md documents.

**Not yet explored**: the wiki's actual category taxonomy for game mechanics content (the
equivalent of HOI4's `Category:National focus trees`). Do this — via `search_titles`/
`category_members`, same tools used above — before finalizing §4's category structure.

---

## 4. Draft category taxonomy (hypothesis — verify, don't assume)

This is my best guess based on CK3's actual game systems, by analogy to how HOI4's 10 categories
were organized around *that* game's systems. It is very likely wrong in the details and should be
corrected once real wiki exploration happens — CK3 doesn't have "focus trees" or "naval warfare" the
way HOI4 does; it has character-, dynasty-, and realm-centric systems instead.

| # | Category | Rough content | HOI4 analog |
|---|---|---|---|
| 00 | `meta` | Game overview, DLC index, patch history, glossary, console commands, hotkeys | same |
| 01 | `character-mechanics` | Traits, stress, lifestyles, education, health/aging, death | `01-mechanics` (partial) |
| 02 | `realm-and-succession` | Crown authority, council, laws, succession types (partition/primogeniture/elective/etc.), titles, de jure | `01-mechanics` (partial) |
| 03 | `religion-and-culture` | Faiths, doctrines, piety, holy wars, culture, innovations, hybridization | new — no HOI4 equivalent |
| 04 | `intrigue-and-diplomacy` | Schemes, secrets, alliances, marriages, factions, vassalization | `01-mechanics` (diplomacy part) + new |
| 05 | `warfare` | Levies, men-at-arms, combat resolution, sieges, commanders/knights | `02-land-warfare`+`04-naval-warfare` combined (CK3 land warfare only, no separate naval/air the way HOI4 has) |
| 06 | `court-and-council` | Court positions, councilors, guests, hybrid CK3-specific systems | new |
| 07 | `rulers-and-dynasties` | Notable bookmark/start characters, dynasties, historical figures | `05-countries` analog |
| 08 | `decisions-and-activities` | Decisions, activities, major choice trees | `06-focus-trees` analog (structurally different — CK3 doesn't have a tech-tree-shaped focus system) |
| 09 | `achievements` | Same pattern as HOI4: per-DLC-group files + index | same |
| 10 | `strategy` | Playstyle guides, synthesis — mostly `**Inferred:**`, low fetch volume | `08-strategy` |
| 11 | `reference` | Trait list, building list, innovation list, artifact list, etc. — prime candidates for the zero-LLM scripted path, see §5.5 | `09-reference` |

Numbering intentionally left gappy/renumberable — finalize the real list only after wiki exploration,
then lock in the numbering and update this table and STYLE.md's file-naming section together.

---

## 5. Token-minimization strategy for the crawl/distill phase

This is the part explicitly asked for. The HOI4 build worked and produced a genuinely good skill
(validated: 100% vs 33% eval pass rate against a no-skill baseline — see
`../hoi-claude-skill/skill/hoi4-companion-workspace/iteration-1/benchmark.md` for the numbers), but
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
   strip it by hand. Port improvements back to `hoi-claude-skill`'s `fetch.py` too if they'd help
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
  canonical location automatically. (`hoi-claude-skill` already does this for its own skill and for
  an unrelated installed skill — same pattern, safe to reuse.)
- **Git discipline**: even solo, stage files by explicit name (never `git add -A`/`.`), and check
  `git status --porcelain` before and after staging in case another session is touching the same
  checkout — see `hoi-claude-skill`'s CLAUDE.md-driven habit of invoking the
  `concurrent-git-commit-safety` skill before every commit.

---

## 7. Suggested first steps

1. Explore the CK3 wiki's real category structure (`category_members`/`search_titles`, same tools
   already proven working above) before touching §4's draft taxonomy — confirm or correct it.
2. Confirm the actual current game patch version (don't rely on the "1.19.X" lower bound from §3).
3. Pick one small category and run a **pilot batch of 5-10 files** using the token-minimized
   approach from §5 (inlined rules, batched agents, no example-file read after the first couple) —
   check output quality before scaling to the full corpus. This is cheap insurance against building
   250 files on a broken pattern.
4. Once a category's pattern is validated, scale it up the same way HOI4 did: build a work-item
   list (JSON), write one `Workflow` script per category (or a few categories at a time), split into
   parallel chunks per §5.7, launch, verify, repeat.
5. Follow the same finishing pass HOI4 used at the end: cross-link scan, `README.md`/`INDEX.md`
   with routing hints, copy into `skill/ck3-companion/references/`, eval pass via `skill-creator`,
   description-optimization loop, package via `scripts.package_skill`.

Good luck — the hard part (proving the crawler works against Paradox's bot protection, and proving
the whole scrape→skill pipeline actually produces something measurably better than no skill at all)
is already done once, in the sibling project. This one should go faster.
