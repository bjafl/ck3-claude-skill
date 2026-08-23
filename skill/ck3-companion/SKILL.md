---
name: ck3-companion
description: 'Answer Crusader Kings III (CK3) gameplay questions grounded in a patch-1.19 vanilla reference, not general knowledge. Trigger on CK3 terminology even when the user doesn''t say "CK3" or "Crusader Kings": crown authority, vassals and factions, succession laws (primogeniture, gavelkind, confederate partition), government types (feudal, tribal, clan, theocracy) and converting between them, schemes and intrigue, councils, religion, faith, doctrine, tenets, culture, traditions, warfare, casus belli, decisions, artifacts, dynasties, DLC content, and any of the 188 achievements. Also covers "what should I focus on" strategy questions for a given government, culture, or religion, and beginner strategy. Ground exact numbers, requirements, and mechanics in bundled data rather than guessing. Skip: Steam pricing, other Paradox games (EU4, HOI4, Stellaris, Victoria 3), real medieval history, CK3 mods, unrelated PC troubleshooting.'
---

## Overview

Reference data for Crusader Kings III, built from `ck3.paradoxwikis.com` and rewritten dense and
factual for lookup by an LLM. Ground precise answers (exact numbers, mechanics, requirements) in
this data instead of general knowledge, which is prone to inventing plausible-sounding but wrong
specifics for a niche strategy game — especially achievement names/requirements and exact stat
values.

## When to Use

- A CK3-specific gameplay question: mechanics, strategy, or "how do I..."
- An achievement question ("how do I get X")
- A request for exact numbers/requirements (law effects, building costs, artifact stats)
- The user names the skill explicitly ("use the ck3-companion skill...")

Don't use for: pricing/store questions, other games, real history, CK3 mods, or unrelated
troubleshooting — see the description's skip list above.

## How Reference Data Is Organized

Only this file's frontmatter (name + description) loads by default. The `references/` files below
load on demand, one at a time, when actually needed for a specific question — this is why the
corpus can be broad without costing context on unrelated questions. Check `references/INDEX.md`
first for topic-level routing before reading a file blind.

| Directory | Contents |
|---|---|
| `00-meta/` | DLC index, patch history, glossary, FAQ/QNA, game rules |
| `01-character-mechanics/` | Attributes, traits, lifestyles, artifacts (mechanics), hooks, activities, dynasty |
| `02-realm-and-succession/` | Titles, government types, laws, succession, council, court |
| `03-religion-and-culture/` | Faiths, doctrines, tenets, culture, traditions, innovations |
| `04-intrigue-and-diplomacy/` | Schemes, alliances |
| `05-warfare/` | Combat, casus belli, armies, knights, duels |
| `07-rulers-and-dynasties/` | Starting-ruler bookmarks, notable-character highlights |
| `08-decisions-and-activities/` | The decisions system |
| `09-achievements/` | All 188 achievements, split into 10 files by required DLC + an index |
| `10-strategy/` | Beginner's guide |
| `11-reference/` | Pure lookup tables: buildings by type, artifact catalog, empire/kingdom lists |

### Keep reference files lean if you add to this corpus

Prefer one file per topic group over one file per item. Reference a shared/generic file for common
mechanics rather than repeating them per variant (e.g. government-type files link back to
`government-overview.md` instead of re-explaining shared concepts). Depth (a genuinely detailed
file) is fine; breadth for its own sake (many thin files covering near-duplicate ground) isn't.

## Workflow

1. Identify the topic from the user's question.
2. Check `references/INDEX.md` for which file covers it.
3. Read that file, and answer grounded in what it actually says — cite specifics (numbers,
   requirements) rather than paraphrasing vaguely.
4. If no file covers the topic, say so explicitly rather than answering from general knowledge —
   general-knowledge answers about CK3 specifics (achievement names, exact numbers) are prone to
   confident hallucination.

## Status

95 files, ~1.85 MB, game version 1.19. Vanilla CK3 only (no mod content). Build history and known
data-quality notes: `references/README.md` and the project's `LEDGER.md`.
