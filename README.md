# ck3-claude-skill

A Claude Code / claude.ai skill that answers Crusader Kings III gameplay
questions from a curated, version-tagged wiki corpus instead of the model's
(often stale) training data.

**Status:** Initial build complete (August 2026). Corpus covers vanilla CK3
1.19; the skill is packaged and usable. No ongoing content updates.

## Why

CK3 is a niche, frequently patched strategy game, and general model
knowledge tends to invent plausible-but-wrong specifics: achievement
requirements, law effects, building stats. This project scrapes the
community wiki once, distills it into a lean reference corpus, and packages
it as a skill so Claude looks things up instead of guessing.

It is a sibling of [hoi4-claude-skill](https://github.com/bjafl/hoi4-claude-skill)
and reuses the same scrape → distill → package pipeline, with changes aimed
at cutting the token cost of the distill phase.

## Layout

```
skill/                       the shipped Claude skill
  ck3-companion/             SKILL.md + references/ (copied from wiki-crawler/corpus/)
  ck3-companion.skill        packaged upload for claude.ai (~600 KB)
  ck3-companion-workspace/   trigger eval set + description-optimization logs

wiki-crawler/                build pipeline that produces the corpus
  fetcher/                   Python/Playwright fetcher (ck3_wiki_crawler) for
                             ck3.paradoxwikis.com
  corpus/                    staging corpus: distilled, front-mattered markdown
                             (see corpus/README.md and corpus/INDEX.md)
  corpus/_tooling/           style guide, manifest checks, zero-LLM extractors,
                             batch-writing workflow scripts

HANDOFF.md                   background, methodology and design rationale
LEDGER.md                    build log, status per category, known caveats
```

The corpus in `wiki-crawler/corpus/` is the **build/staging** copy; the skill
under `skill/ck3-companion/references/` is the **shipped** copy. Fix content
issues in the corpus and re-copy — don't hand-edit the shipped copy.

## Using the skill

- **Claude Code**: point it at `skill/ck3-companion/` (contains `SKILL.md`)
  as a project or personal skill. This repo already links it under
  `.claude/skills/ck3-companion`.
- **claude.ai**: upload `skill/ck3-companion.skill` directly.

Autonomous triggering is imperfect (description optimization topped out
well below full recall), so naming the skill explicitly ("use the
ck3-companion skill…") is the reliable way to invoke it. See
`skill/ck3-companion/SKILL.md` for the routing table and reference-file
conventions.

## Rebuilding the corpus

1. `wiki-crawler/fetcher/` fetches wiki pages through headless Chromium
   (the `uv`-managed environment is defined in its `pyproject.toml`):

   ```bash
   cd wiki-crawler/fetcher
   uv sync
   uv run python -m ck3_wiki_crawler.fetch "Page title" "Another page"
   ```

2. Pages are turned into `wiki-crawler/corpus/<category>/` files following
   `corpus/_tooling/STYLE.md`, using one of three approaches per page:
   zero-LLM extraction for table-shaped pages (`extract_reference.py`,
   `split_achievements.py`), batched LLM rewrites via the scripts in
   `_tooling/workflow-scripts/`, or individual rewrites for pages that need
   more judgment.
3. `_tooling/check_corpus.py` and `_tooling/regen_manifest.py` verify the
   manifest against what's on disk.
4. Finished categories are copied into
   `skill/ck3-companion/references/<same category>/`.

Current corpus: 95 files, ~1.9 MB, game version 1.19 unless a file's front
matter says otherwise. Ten categories (meta, character mechanics, realm and
succession, religion and culture, intrigue, warfare, rulers and dynasties,
decisions, all 188 achievements, strategy, reference tables). Known gaps:
mod content and per-county/duchy lists are deliberately excluded, the
intrigue and strategy categories are thin, and the FAQ is based on a
pre-launch source with outdated sections flagged. See
`wiki-crawler/corpus/README.md` and `LEDGER.md` for details.

## Attribution

Content derived from the [Crusader Kings III Wiki](https://ck3.paradoxwikis.com),
published under Creative Commons Attribution-ShareAlike (CC BY-SA 3.0).
Game data is factual; prose has been rewritten and condensed. The corpus
and packaged skill are adaptations and remain under CC BY-SA — retain
attribution and the same license if you redistribute.

Crusader Kings III is a trademark of Paradox Interactive. This project is
not affiliated with or endorsed by Paradox.
