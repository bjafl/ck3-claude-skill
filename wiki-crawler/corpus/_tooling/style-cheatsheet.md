# Style cheat-sheet (paste this into writer-agent prompts verbatim — do not have agents `Read STYLE.md`)

Front matter every file needs:
```yaml
---
title: <Topic name>
category: <matches its numbered directory>
tags: [a, few, keywords]
game_version: "1.19"
dlc: [<DLC name(s) required, or [] for base game>]
sources: [https://ck3.paradoxwikis.com/<Page_Title>, ...]
---
```
Then a 2-4 sentence Summary, then the body starting at `##` (never `#`).

Rules: (1) Keep every number/stat/table exactly as-is, never round. (2) Rewrite prose in your own
words, aim for ~half the wiki's word count, keep 100% of the data. (3) Delete any leftover
`[Something.png]`-style bracket noise. (4) Delete navboxes/breadcrumb link lists/"External links".
(5) Mark DLC gating inline: `(requires Tours & Tournaments)`. (6) If the wiki is self-contradictory
or flags a section outdated, add `> ⚠️ Wiki flags this as potentially outdated.` (7) Cross-link with
relative paths: `See [Schemes](../04-intrigue-and-diplomacy/schemes.md)`. (8) Don't invent — write
`_Not covered on the wiki._` rather than guess; label inferred strategy `**Inferred:**`. (9) Long
files are fine, don't truncate to save space — truncating a stat table to save space is a bug, not
an optimization. (10) File names: `lowercase-with-hyphens.md`.

When done, append one line per file to `_tooling/manifest.tsv` (path relative to `corpus/`):
```
printf '%s\t%s\t%s\t%s\n' "<relpath>" "<title>" "<bytes>" "<comma,separated,source,pages>" >> _tooling/manifest.tsv
```
Use `>>`, never rewrite the file — other agents may be appending concurrently.
