# ck3-wiki-crawler

Playwright-driven fetcher for `ck3.paradoxwikis.com`. Adapted from the
`hoi-claude-skill` project's `hoi_wiki_crawler` — see `../../HANDOFF.md` at
the repo root for full context on why this exists and how it was used there.

## Why not just `requests`/`pymediawiki`?

The wiki sits behind a Fastly "Client Challenge" (a JS proof-of-work gate)
that blocks plain HTTP clients entirely — confirmed on both hoi4.paradoxwikis.com
and ck3.paradoxwikis.com. A real browser passes it automatically because it
can execute the JS; this module drives headless Chromium via Playwright to
load the wiki once (passing the challenge), then uses the page's own
same-origin `fetch()` to call the MediaWiki API directly.

## Usage

```bash
uv run python -m ck3_wiki_crawler.fetch "Some page title" "Another page"
```

Prints one `===== PAGE: <title> =====` block per page to stdout, HTML
converted to markdown. Also exposes `search_titles(query)` and
`category_members(category)` for looking up exact page titles before
dispatching writer agents — see `fetch.py`'s docstrings.
