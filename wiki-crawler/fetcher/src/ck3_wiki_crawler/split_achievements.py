"""Zero-LLM split of the cached Achievement master page into per-DLC-group files.

The wiki already groups all 188 achievements under `### <DLC name>` headings on one page
(see HANDOFF.md §4 -- this was flagged as needing a check before deciding on a per-DLC split
like HOI4 used). It does, so no LLM judgment is needed to group them: this script just slices
the cached master page by heading and wraps each slice in front matter.

Requires `_tooling/achievements-master-raw.md` to already exist (see cache_masters in
extract_reference's sibling caching step, or re-fetch with fetch_pages(["Achievement"])).

Usage:
    uv run python -m ck3_wiki_crawler.split_achievements
"""

import re
import sys
from pathlib import Path

CORPUS_ROOT = Path(__file__).resolve().parents[3] / "corpus"
MASTER_PATH = CORPUS_ROOT / "_tooling" / "achievements-master-raw.md"
OUT_DIR = CORPUS_ROOT / "09-achievements"
GAME_VERSION = "1.19"

# DLC name -> (front-matter dlc list, output slug)
GROUPS = {
    "Base game": ([], "base-game"),
    "Northern Lords": (["Northern Lords"], "northern-lords"),
    "Royal Court": (["Royal Court"], "royal-court"),
    "Fate of Iberia": (["Fate of Iberia"], "fate-of-iberia"),
    "Tours and Tournaments": (["Tours and Tournaments"], "tours-and-tournaments"),
    "Legacy of Persia": (["Legacy of Persia"], "legacy-of-persia"),
    "Legend of the Dead": (["Legends of the Dead"], "legends-of-the-dead"),
    "Roads to Power": (["Roads to Power"], "roads-to-power"),
    "Khans of the Steppe": (["Khans of the Steppe"], "khans-of-the-steppe"),
    "All Under Heaven": (["All Under Heaven"], "all-under-heaven"),
}


def front_matter(title: str, dlc: list[str], tags: list[str]) -> str:
    dlc_yaml = "[" + ", ".join(dlc) + "]"
    tags_yaml = "[" + ", ".join(tags) + "]"
    return (
        "---\n"
        f"title: {title}\n"
        "category: achievements\n"
        f"tags: {tags_yaml}\n"
        f'game_version: "{GAME_VERSION}"\n'
        f"dlc: {dlc_yaml}\n"
        "sources:\n"
        "  - https://ck3.paradoxwikis.com/Achievement\n"
        "---\n\n"
    )


def run() -> None:
    if not MASTER_PATH.exists():
        print(f"Missing {MASTER_PATH} -- fetch it first (see extract_reference / cache step).", file=sys.stderr)
        raise SystemExit(1)

    text = MASTER_PATH.read_text()

    intro_match = re.search(r"\A(.*?)## List of achievements\n(.*?)\n### ", text, re.DOTALL)
    if not intro_match:
        print("Could not find expected '## List of achievements' / first '### ' heading -- wiki structure may have changed.", file=sys.stderr)
        raise SystemExit(1)
    page_intro = intro_match.group(1).strip()
    list_notes = intro_match.group(2).strip()

    sections = re.split(r"\n### ", text)[1:]  # drop the preamble chunk

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest_lines = []
    written = []

    for section in sections:
        heading, _, body = section.partition("\n")
        heading = heading.strip()
        body = re.sub(r"\n## References\b.*\Z", "", body, flags=re.DOTALL).strip()

        if heading not in GROUPS:
            print(f"  WARNING: unrecognized DLC heading '{heading}' -- skipped, add it to GROUPS.", file=sys.stderr)
            continue

        dlc, slug = GROUPS[heading]
        out_path = OUT_DIR / f"achievements-{slug}.md"
        content = front_matter(f"Achievements ({heading})", dlc, ["achievements", slug]) + body + "\n"
        out_path.write_text(content)
        n_bytes = len(content.encode())
        rel = f"09-achievements/achievements-{slug}.md"
        manifest_lines.append(f"{rel}\tAchievements ({heading})\t{n_bytes}\tAchievement\n")
        written.append((heading, rel, n_bytes))
        print(f"  wrote {rel} ({n_bytes} bytes)", file=sys.stderr)

    index_lines = [
        "---",
        "title: Achievements (index)",
        "category: achievements",
        "tags: [achievements, index]",
        f'game_version: "{GAME_VERSION}"',
        "dlc: []",
        "sources:",
        "  - https://ck3.paradoxwikis.com/Achievement",
        "---",
        "",
        page_intro,
        "",
        "## Notes",
        "",
        list_notes,
        "",
        "## Achievement groups",
        "",
    ]
    for heading, rel, _ in written:
        fname = Path(rel).name
        index_lines.append(f"- [{heading}]({fname})")
    index_content = "\n".join(index_lines) + "\n"
    (OUT_DIR / "_index.md").write_text(index_content)
    n_bytes = len(index_content.encode())
    manifest_lines.append(f"09-achievements/_index.md\tAchievements (index)\t{n_bytes}\tAchievement\n")
    print(f"  wrote 09-achievements/_index.md ({n_bytes} bytes)", file=sys.stderr)

    with (CORPUS_ROOT / "_tooling" / "manifest.tsv").open("a") as f:
        f.writelines(manifest_lines)
    print(f"Appended {len(manifest_lines)} line(s) to manifest.tsv", file=sys.stderr)


if __name__ == "__main__":
    run()
