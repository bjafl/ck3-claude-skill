"""Zero-LLM extraction for purely/mostly tabular wiki reference pages.

See HANDOFF.md §5.5: some wiki pages are already clean tables with nothing worth an LLM's
judgment (a trait list, a building-cost list). This script fetches such a page, strips the
mechanical cruft an LLM writer would otherwise have to notice and remove by hand (breadcrumb
nav lists, trailing "References" navbox sections), wraps the rest in the standard STYLE.md front
matter, and writes the corpus file directly -- no agent involved, zero LLM tokens spent.

This is a MECHANICAL extract, not a distillation: unlike an LLM-written file, prose sections are
kept verbatim rather than compressed to ~half length. Use it only for pages that are already
dense/tabular (checked via §5.5's own advice: pull the page first, eyeball how tabular it is)
-- see HANDOFF.md §4 for candidates (building sub-lists, innovation/artifact lists, list of
kingdoms/empires). Do NOT use it on prose-heavy pages; STYLE.md's compression and judgment rules
still apply there and need a real writer agent.

Usage:
    uv run python -m ck3_wiki_crawler.extract_reference <jobs.json>

jobs.json is a list of job objects:
    {
      "title": "Castle buildings",       // exact wiki page title
      "output": "11-reference/buildings-castle.md",  // path relative to corpus/ root
      "category": "reference",           // front-matter category
      "tags": ["buildings", "castle"],
      "dlc": []                          // [] for base game
    }

Run from the `wiki-crawler/fetcher/` directory; writes into `../corpus/`.
"""

import json
import re
import sys
from pathlib import Path

from .fetch import fetch_pages

CORPUS_ROOT = Path(__file__).resolve().parents[3] / "corpus"
GAME_VERSION = "1.19"

_TRAILING_REFERENCES_RE = re.compile(r"\n##\s*References\b.*\Z", re.DOTALL)


def _strip_breadcrumb_nav(body: str) -> str:
    """Drop leading short, punctuation-less lines (sidebar/breadcrumb link lists)."""
    lines = body.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith("#"):
            break
        if len(line) < 60 and not re.search(r"[.!?]\s*$", line):
            i += 1
            continue
        break
    return "\n".join(lines[i:]).strip()


def _strip_trailing_references(body: str) -> str:
    return _TRAILING_REFERENCES_RE.sub("", body).strip()


def clean_body(body: str) -> str:
    body = _strip_breadcrumb_nav(body)
    body = _strip_trailing_references(body)
    return body.strip()


def wiki_url(title: str) -> str:
    return "https://ck3.paradoxwikis.com/" + title.replace(" ", "_")


def build_file(title: str, category: str, tags: list[str], dlc: list[str], body: str) -> str:
    tags_yaml = "[" + ", ".join(tags) + "]"
    dlc_yaml = "[" + ", ".join(dlc) + "]"
    front_matter = (
        "---\n"
        f"title: {title}\n"
        f"category: {category}\n"
        f"tags: {tags_yaml}\n"
        f'game_version: "{GAME_VERSION}"\n'
        f"dlc: {dlc_yaml}\n"
        f"sources:\n"
        f"  - {wiki_url(title)}\n"
        "---\n\n"
        f"Reference data for {title}, extracted mechanically from the wiki (no LLM compression --\n"
        "see HANDOFF.md §5.5). Prose below is reproduced close to verbatim; tables are exact.\n\n"
    )
    return front_matter + body + "\n"


def run(jobs_path: str) -> None:
    jobs = json.loads(Path(jobs_path).read_text())
    titles = [j["title"] for j in jobs]
    print(f"Fetching {len(titles)} page(s) in one browser session...", file=sys.stderr)
    raw = fetch_pages(titles)

    blocks: dict[str, str] = {}
    for block in raw.split("===== PAGE:")[1:]:
        title_end = block.index("=====")
        page_title = block[:title_end].strip()
        blocks[page_title] = block[title_end + 5:].strip()

    manifest_lines = []
    for job in jobs:
        title = job["title"]
        if title not in blocks:
            print(f"  SKIP {title}: not returned by fetch (redirect mismatch?)", file=sys.stderr)
            continue
        if "(ERROR" in blocks[title][:40]:
            print(f"  SKIP {title}: {blocks[title][:60]}", file=sys.stderr)
            continue

        body = clean_body(blocks[title])
        content = build_file(title, job["category"], job.get("tags", []), job.get("dlc", []), body)

        out_path = CORPUS_ROOT / job["output"]
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content)

        rel_path = job["output"]
        n_bytes = len(content.encode())
        manifest_lines.append(f"{rel_path}\t{title}\t{n_bytes}\t{title}\n")
        print(f"  wrote {rel_path} ({n_bytes} bytes)", file=sys.stderr)

    if manifest_lines:
        manifest_path = CORPUS_ROOT / "_tooling" / "manifest.tsv"
        with manifest_path.open("a") as f:
            f.writelines(manifest_lines)
        print(f"Appended {len(manifest_lines)} line(s) to manifest.tsv", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: uv run python -m ck3_wiki_crawler.extract_reference <jobs.json>", file=sys.stderr)
        raise SystemExit(1)
    run(sys.argv[1])
