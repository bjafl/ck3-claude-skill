# CK3 Companion Corpus

Build complete (initial pass). 95 files, ~1.85 MB, scraped and rewritten from
`ck3.paradoxwikis.com`, game version 1.19.

## Layout

```
00-meta/                    6 files   — DLC index, patch history, glossary, FAQ/QNA, game rules
01-character-mechanics/    13 files   — attributes, traits, lifestyle, artifacts, hooks, etc.
02-realm-and-succession/   24 files   — titles, government types, laws, succession, council/court
03-religion-and-culture/   14 files   — faiths, doctrines, tenets, culture, traditions
04-intrigue-and-diplomacy/  2 files   — schemes, alliances (genuinely thin category)
05-warfare/                 6 files   — combat, casus belli, armies, knights, duels
07-rulers-and-dynasties/    2 files   — bookmarks, curated notable-character highlights
08-decisions-and-activities/4 files   — the decisions system
09-achievements/           11 files   — all 188 achievements, split by required DLC + index
10-strategy/                1 file    — beginner's guide
11-reference/               12 files  — pure lookup tables: buildings, artifacts, empire/kingdom lists
```

See `INDEX.md` for topic-level routing ("a question about X → read file Y").

Numbering has a gap at 06 on purpose — see `HANDOFF.md` §4: a planned `06-court-and-council`
category was dropped and folded into `02-realm-and-succession` once real wiki exploration showed
no source-side split justified it. Numbers weren't renumbered down afterward since content already
existed under the original numbers.

## File contract

Every file starts with YAML front matter:
```yaml
---
title: <Topic name>
category: <bare category name, e.g. "realm-and-succession", not the numbered directory>
tags: [a, few, retrieval, keywords]
game_version: "1.19"
dlc: [<DLC name(s) required, or [] for base game>]
sources: [https://ck3.paradoxwikis.com/<Page_Title>, ...]
---
```
Full authoring rules: `_tooling/STYLE.md`. Condensed cheat-sheet used by writer agents:
`_tooling/style-cheatsheet.md`.

## How this was built

Mix of three approaches, chosen per source page (see `HANDOFF.md` §5 for the full rationale):

- **Zero-LLM extraction** (`_tooling/extract_reference.py`, `_tooling/split_achievements.py`) for
  pages that were already clean tables or pre-grouped by the wiki itself — most of
  `09-achievements` and `11-reference`.
- **Batch-written by Haiku via `Workflow`** (`_tooling/workflow-scripts/batch-write-category.js`,
  work-item lists in `_tooling/workitems/`) for everything else, 6 pages per agent batch, style
  rules inlined into the prompt rather than read from disk per agent.
- **Individually dispatched agent rewrites** for a couple of files that needed more judgment than
  a batch write could give (`00-meta/faq.md`'s outdated-content flagging,
  `11-reference/artifacts-list.md`'s prose-heavy source page).

## Known data quality notes

- `00-meta/faq.md`'s source is Paradox's 2020 pre-launch developer FAQ. Several sections are
  flagged `⚠️` as likely superseded by later patches/DLC (the scheme/intrigue rework, cultural
  traditions replacing the described innovation system, etc.) rather than stated as current fact.
- `07-rulers-and-dynasties/interesting-characters.md` is a curated ~20-30 character subset of the
  wiki's 334 KB full roster, not a complete reproduction — see that file's own note.
- `List of counties`/`List of duchies` (the wiki's own generated per-holding dumps, hundreds of KB
  each) were deliberately excluded as too granular for this skill — see `HANDOFF.md` §3.
- Mod-specific wiki content (CK3AGOT, RICE, Rajas of Asia, The Fallen Eagle, and others) was
  deliberately excluded — this corpus is vanilla CK3 only.
- Full verification history, including the manifest-corruption and duplicate-file issues found and
  fixed across 3 build rounds, is in `LEDGER.md`.

## Attribution

Content adapted from the [CK3 Wiki](https://ck3.paradoxwikis.com), a community-maintained
resource. Rewritten and condensed, not reproduced verbatim, per the file contract above.
