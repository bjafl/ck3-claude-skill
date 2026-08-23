// Workflow script template for batch-writing one corpus category via Haiku writer agents.
// See HANDOFF.md §5 for the rationale (batch N pages/agent, inline style rules, no example-file
// reads after the first wave). NOT auto-run by anything -- this is staged for when the user gives
// explicit go-ahead to invoke the Workflow tool (see LEDGER.md). To use:
//   1. Build the `args` payload with `_tooling/build_workflow_args.py <workitems-file.json>`
//      (prints ready-to-paste JSON: items, styleCheatsheet, categoryDir, fetcherDir).
//   2. Call the Workflow tool with `scriptPath` pointing at this file and that `args` payload.
//   3. Keep the run's scriptPath + Run ID -- if a batch fails partway (session limits are a known
//      HOI4-build failure mode, see HANDOFF.md §6), resume with `resumeFromRunId` rather than
//      re-running from scratch; already-completed batches replay from cache.
//
// This script is plain JS run by the Workflow tool's own runtime -- it has no filesystem access,
// which is why the caller must pre-load everything (item list, cheat-sheet text) into `args`.

export const meta = {
  name: 'ck3-batch-write-category',
  description: 'Batch-write CK3 corpus files for one category from a work-item list',
  phases: [{ title: 'Write' }],
}

function chunk(arr, size) {
  const out = []
  for (let i = 0; i < arr.length; i += size) out.push(arr.slice(i, i + size))
  return out
}

const BATCH_SCHEMA = {
  type: 'object',
  properties: {
    files: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          path: { type: 'string' },
          title: { type: 'string' },
          bytes: { type: 'number' },
        },
        required: ['path', 'title', 'bytes'],
      },
    },
    issues: { type: 'string', description: 'Anything that needs a human look, or empty string' },
  },
  required: ['files', 'issues'],
}

phase('Write')

const items = args.items
const styleCheatsheet = args.styleCheatsheet
const categoryDir = args.categoryDir
const fetcherDir = args.fetcherDir
const batchSize = args.batchSize || 6
const model = args.model || 'claude-haiku-4-5-20251001'

const batches = chunk(items, batchSize)
log(`${items.length} items -> ${batches.length} batch(es) of up to ${batchSize}`)

const results = await pipeline(
  batches,
  (batch, _item, idx) => {
    const titlesJson = JSON.stringify(batch.map((b) => b.title))
    const fileList = batch
      .map((b) => `- "${b.title}" -> ${categoryDir}/${b.output} (tags: ${JSON.stringify(b.tags || [])}, dlc: ${JSON.stringify(b.dlc || [])})`)
      .join('\n')

    const prompt = `You are writing CK3 companion-skill reference files for the "${categoryDir}" category.
This is a one-shot batch: write all ${batch.length} files, then report back. Do not ask
clarifying questions -- if a page redirects or is missing, note it in "issues" and skip it.

STYLE RULES (follow exactly, do not deviate):
${styleCheatsheet}

Step 1 -- fetch all pages in one call (run from ${fetcherDir}):
  cd ${fetcherDir} && uv run python -c "import sys; sys.path.insert(0,'src'); from ck3_wiki_crawler.fetch import fetch_pages; print(fetch_pages(${titlesJson}))"

Step 2 -- for each page, write one file (corpus root is ${fetcherDir}/../corpus/; the category
directory may not exist yet, create it with mkdir -p if needed):
${fileList}

Step 3 -- append one manifest line per file you wrote to ${fetcherDir}/../corpus/_tooling/manifest.tsv
using the printf command from the style rules (use >>, never rewrite the file).

Report back the files you wrote (path relative to corpus/, title, byte count) and anything that
needs a human look (missing page, ambiguous redirect, content that didn't fit the expected shape).`

    return agent(prompt, {
      schema: BATCH_SCHEMA,
      model,
      phase: 'Write',
      label: `batch-${idx + 1}`,
    })
  }
)

const allFiles = results.filter(Boolean).flatMap((r) => r.files)
const allIssues = results.filter(Boolean).flatMap((r) => (r.issues ? [r.issues] : []))
log(`Wrote ${allFiles.length} files across ${batches.length} batch(es); ${allIssues.length} batch(es) flagged issues`)

return { files: allFiles, issues: allIssues }
