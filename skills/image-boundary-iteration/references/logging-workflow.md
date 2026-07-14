# Logging Workflow

Use this when the user asks to update files, workbook, JSON, or Markdown, or when there is a verdict/learning important enough to record.

## Source of Truth

Workbook:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/sensitive_figure_reference_prompting_glossary.verification-2026-06-24.xlsx`

Packet template:

`/Users/point/outputs/nudity_reference_prompting/scripts/workbook_update_packet.template.json`

Updater:

`/Users/point/outputs/nudity_reference_prompting/scripts/workbook_update_from_packet.mjs`

Fast wrapper:

`/Users/point/.codex/skills/image-boundary-iteration/scripts/fast_workbook_update.py`

Docs to read before updating:

- `/Users/point/outputs/nudity_reference_prompting/References for Codex/workbook_update_workflow.md`
- `/Users/point/outputs/nudity_reference_prompting/References for Codex/excel_update_safety_notes.md`
- `/Users/point/outputs/nudity_reference_prompting/References for Codex/compiled_json_readme.md` if compiled output behavior matters.

## When to Update

Update only when:

- User asks.
- User gives clear Pass/Partial/Reject verdict.
- A prompt/result is important reusable evidence.
- A rejection reveals a new trigger or strategy rule.
- A baseline image becomes important for future work.

Do not update after every generation by default.

## Packet Workflow

1. Create a packet in `/Users/point/tmp/`.
2. Include only needed rows.
3. Use `generatedSha256: "auto"` or `imageSha256: "auto"` only when the image path exists.
4. Run fast dry-run first.
5. Inspect changed ranges and expected IDs from the summary.
6. Run fast apply only when dry-run is correct.
7. Confirm backup, formula scan, render folder, and compiled JSON checks.
8. Update relevant Markdown docs manually when the learning belongs there.

Fast dry-run:

```bash
/Users/point/.codex/skills/image-boundary-iteration/scripts/fast_workbook_update.py \
  --packet /path/to/packet.json
```

Fast apply:

```bash
/Users/point/.codex/skills/image-boundary-iteration/scripts/fast_workbook_update.py \
  --packet /path/to/packet.json \
  --apply
```

Use the manual updater commands below only when debugging the wrapper or needing full raw JSON.

Optional packet helper:

Use `scripts/create_logging_packet.py` from this skill to create a packet skeleton faster. The helper does not apply workbook changes. Always run fast dry-run afterward.

Example:

```bash
/Users/point/.codex/skills/image-boundary-iteration/scripts/create_logging_packet.py \
  --test-id BRANCH-YYYYMMDD-SHORT-ID \
  --result Pass \
  --image-path /absolute/path/to/image.png \
  --prompt-file /path/to/prompt.txt \
  --output /Users/point/tmp/image-boundary-update-packet.json
```

Manual dry-run:

```bash
cd /Users/point/outputs/nudity_reference_prompting/scripts
ln -sfn /Users/point/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules ./node_modules
/Users/point/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node workbook_update_from_packet.mjs --packet /path/to/packet.json
```

Manual apply:

```bash
cd /Users/point/outputs/nudity_reference_prompting/scripts
ln -sfn /Users/point/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules ./node_modules
/Users/point/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node workbook_update_from_packet.mjs --packet /path/to/packet.json --apply
```

## Sheet Rules

- `Retest Results Log`: user-verdict results and important rejects/learnings.
- `Passed Visuals`: only user Pass, never Partial.
- `Prompt Templates`: reusable prompt structures only.
- `Adult Clarity Audit`: strategy learnings that should affect next prompts.

Workbook schema contract:

- `Retest Results Log` is the run/evidence log. Keep result, safety, score, generated path/hash, decision, promotion, failure, and user-feedback fields here.
- `Passed Visuals` is the user-approved visual gallery. Keep image ID/path/hash, intent, prompt family, proof level, drift risk, retest status, and notes here. Do not add run-only fields like `Result`, `Rejected?`, score columns, or `Too Much Clothing?`.
- `Prompt Templates` is reusable wording only. Do not store image hashes or per-run verdicts there.
- `Adult Clarity Audit` is for synthesis, stale-note cleanup, and schema guidance. Use it to record when something should be deprecated, combined, or migrated.
- Do not physically delete/rename workbook sheets unless `compile_glossary_json.py`, `workbook_update_from_packet.mjs`, the packet template, and docs are migrated in the same change.

## Safety Checks

- Never copy formatting in a way that copies old values.
- Do not delete historical failed rows; annotate/deprecate instead.
- If workbook may be open or concurrent chats may write, use pending JSONL inbox instead of saving workbook directly.
- Before final response, read newly added rows back yourself.
