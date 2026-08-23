#!/usr/bin/env python3
"""Backfill empty `tags: []` front matter with a cheap heuristic (zero-LLM).

Writer agents in the 2026-08-23 Workflow batches frequently left `tags: []` empty despite the
style cheat-sheet asking for "a few retrieval keywords" -- 25/79 files in that batch. Rather than
spend more agent tokens re-writing files just to add tags, derive them mechanically: title words +
category + first couple of section headings, deduped and stopword-filtered. Good enough for
retrieval keywords; not a substitute for a human/agent picking better ones later if it matters.

Usage (from corpus/ directory):
    python3 _tooling/backfill_tags.py
"""

import re
from pathlib import Path

CORPUS_ROOT = Path(__file__).resolve().parent.parent

STOPWORDS = {
    "the", "a", "an", "of", "and", "or", "in", "on", "for", "to", "with", "overview",
}

TITLE_RE = re.compile(r'^title:\s*(.+)$', re.MULTILINE)
CATEGORY_RE = re.compile(r'^category:\s*(.+)$', re.MULTILINE)
EMPTY_TAGS_RE = re.compile(r'^tags:\s*\[\]\s*$', re.MULTILINE)
HEADING_RE = re.compile(r'^##\s+(.+)$', re.MULTILINE)


def words_from(text: str) -> list[str]:
    return [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'-]*", text) if w.lower() not in STOPWORDS]


def derive_tags(front_matter: str, body: str) -> list[str]:
    title_m = TITLE_RE.search(front_matter)
    cat_m = CATEGORY_RE.search(front_matter)
    tags: list[str] = []
    if title_m:
        tags.extend(words_from(title_m.group(1))[:3])
    if cat_m:
        tags.append(cat_m.group(1).strip())
    headings = HEADING_RE.findall(body)[:2]
    for h in headings:
        hw = words_from(h)
        if hw:
            tags.append(hw[0])
    seen = set()
    out = []
    for t in tags:
        t = t.strip().lower()
        if t and t not in seen:
            seen.add(t)
            out.append(t)
    return out[:6]


def main() -> None:
    changed = []
    for path in sorted(CORPUS_ROOT.rglob("*.md")):
        if "_tooling" in path.relative_to(CORPUS_ROOT).parts:
            continue
        text = path.read_text()
        if not EMPTY_TAGS_RE.search(text):
            continue
        fm_match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        if not fm_match:
            continue
        front_matter = fm_match.group(1)
        body = text[fm_match.end():]
        tags = derive_tags(front_matter, body)
        if not tags:
            continue
        tags_yaml = "[" + ", ".join(tags) + "]"
        new_text = EMPTY_TAGS_RE.sub(f"tags: {tags_yaml}", text, count=1)
        path.write_text(new_text)
        changed.append((str(path.relative_to(CORPUS_ROOT)), tags))

    print(f"Backfilled tags on {len(changed)} file(s):")
    for rel, tags in changed:
        print(f"  {rel}: {tags}")


if __name__ == "__main__":
    main()
