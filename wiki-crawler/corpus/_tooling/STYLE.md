# Knowledge-base authoring rules (all writers follow these)

Adapted from the hoi4-claude-skill project's STYLE.md — same structure, ported to CK3. See
`../../../HANDOFF.md` for why these rules exist and what worked/didn't in the HOI4 build.

The audience is **an LLM agent** that will be asked things like "I'm playing a count in the HRE,
what should I focus on?", "how does the scheme success chance work?", "how do I get the achievement
for X?". Docs must be dense, scannable, and factual. No fluff, no marketing, no "this wiki is
community maintained" boilerplate.

## Language
English. All game terms exactly as they appear in-game (trait names, law names, title names,
building/innovation names).

## Every file starts with YAML front matter

```yaml
---
title: <Topic name>
category: <matches its numbered directory, e.g. mechanics>
tags: [a, few, retrieval, keywords]
game_version: "<current patch, e.g. 1.15>"
dlc: [<DLC name(s) required, or [] for base game>]
sources:
  - https://ck3.paradoxwikis.com/<Page_Title>
---
```

- `dlc:` lists DLC required for the content described (`[]` if base game).
- `game_version:` — take from the wiki page's version banner if present, else the current patch
  (confirm what that is before starting a batch — don't hardcode a guess).
- `sources:` — every wiki page URL you drew on. Required.

Follow the front matter with a 2–4 sentence **Summary** section, then the body.

## Body rules

1. **Keep the numbers.** Stat tables, modifier values, costs, requirements, formulas — reproduce
   these as markdown tables. They are the whole point. Never round, never "approximately".
2. **Rewrite the prose.** Do not paste wiki paragraphs. Compress explanation into your own tight
   sentences and bullets. Aim for roughly half the wiki's word count on prose while keeping 100%
   of the data.
3. **Strip icon noise.** The extractor leaves markers like `[Piety.png]`, `[Prowess]`. Delete them,
   or fold them into the term (`[Prowess]prowess` → `prowess`). Never leave bare `.png` text in a
   table cell.
4. **Delete navigation cruft.** Navbox tables, "External guides", "References" link lists, and edit
   links at the tail of a page — drop them.
5. **Mark DLC gating inline** whenever a mechanic, decision, or building requires DLC:
   `(requires Tours & Tournaments)`.
6. **Flag uncertainty.** If the wiki is self-contradictory, outdated, or the page carries an
   "outdated" banner, add `> ⚠️ Wiki flags this section as potentially outdated (last verified
   patch X).`
7. **Cross-link** with relative paths: `See [Schemes](../01-mechanics/intrigue-and-schemes.md)`.
8. **Do not invent.** If you don't have the data, write `_Not covered on the wiki._` rather than
   guessing. Strategy advice you infer must be labelled `**Inferred:**`.
9. Headings: file starts at `##` (the `title:` in front matter is the H1). Never emit `#`.
10. Long files are fine — don't truncate to save space. But see HANDOFF.md's condensing guidance
    before deciding a topic needs its own file at all versus folding into a shared one.

## File naming
`lowercase-with-hyphens.md`. Category-specific naming conventions (e.g. how to name per-dynasty,
per-culture, or per-religion files, if those categories end up existing) should be decided and
written down here once the corpus's actual category structure is settled — see HANDOFF.md's
"open questions" section, this hasn't been decided yet for CK3.

## When you finish
Append one line per file you wrote to `_tooling/manifest.tsv` (path relative to the
`wiki-crawler/corpus/` knowledge-base root — do not hardcode an absolute path, it will
differ per environment/session):

```
printf '%s\t%s\t%s\t%s\n' "<relpath>" "<title>" "<bytes>" "<comma,separated,source,pages>" >> _tooling/manifest.tsv
```

(Use `>>` — many agents append concurrently. One `printf` per file, never rewrite the file.)
