# Reference Workflow Consolidation

On 2026-11-15 the owner requested moving the useful reference capabilities into
[mockup-to-product](../skills/mockup-to-product/SKILL.md) and retiring
`reference-to-a-tee`. This document retains its old filename so existing links
still work. It describes the consolidation, not another reproduction workflow.

Status: content, helper/tests and callers are migrated in live/archive copies.
After migration checks, the owner approved deletion of the live reference folder
and both archived reference folders. They have been removed; the archive count
at that checkpoint was 148. Recovery copies remain local under `exports/`,
outside active skill roots. Current totals are in [CODEX_CONTEXT.md](CODEX_CONTEXT.md).

## What Moved

- Image evidence: distinguish observed, image-measured, source-measured,
  inferred and unknown claims; never invent CSS or behavior from pixels.
- Calibration: separate image/CSS coordinates, content crops and unknown scale.
- Mixed-source authority: select artifacts by surface/state and user choice,
  without automatically preferring HTML or newer modification times.
- Fair comparison: matching build, route, content, language, state and viewport.
- Complete requested scope: include below-fold/flow coverage when in scope,
  without expanding a local repair into a whole-site audit.
- The optional HTML extractor and its behavioral tests.

Read [reference evidence](../skills/mockup-to-product/references/reference-evidence.md)
for images and comparisons, and
[HTML workflow](../skills/mockup-to-product/references/html-reference-workflow.md)
only when runnable source or extraction is useful.

## What Did Not Move

The former exact-by-default mode, adaptation-as-exceptions model, mandatory
parity ledgers/tolerances and all-controls/release checklists are not defaults.
The skill starts from product/design judgment. Routine in-scope spacing,
component and responsive choices do not require approval.

Explicit user matching constraints still apply to their stated scope; do not
silently loosen them. A source image or skill invocation alone does not make
every property pixel-exact. Inspiration-only work belongs to design-direction
skills. Preserve real behavior and accessibility; a picture is not permission
to remove functionality or invent a backend.

Use `efficient-execution` for effort, `product-ux-contracts` for behavior,
`snapshot` for current visual proof, and `release-gate` when a release is
actually requested. Revisions require Before/After plus Reference when supplied;
new screens use Reference/Development. Label unavailable historical evidence.
No app capture is needed for skill-text maintenance alone.

## Names And Installation

| Entry point | Status |
| --- | --- |
| `mockup-to-product` | Canonical implementation, reference guidance, HTML helper and tests. |
| `global-mockup-to-product` | Repo-maintained global alias. |
| `claude-to-a-tee` | Retained compatibility router and legacy CLI. |
| `global-claude-to-a-tee` | Retained compatibility alias, routes directly to mockup. |
| `reference-to-a-tee`, `global-reference-to-a-tee` | Retired and removed, not compatibility wrappers. Use the mockup names. |

Install the canonical mockup folder beside any retained alias. Other skills now
route directly to mockup. Old project documents or saved prompts may still name
the retired skill: update relevant callers when encountered, without editing
unrelated projects or other chats as part of this toolkit migration.

A copy-only sync will not remove retired folders on another machine. Compare
them with the archive, preserve local differences and obtain approval before
deletion. Do not resurrect a retired skill during a later sync. Local recovery
copies belong in `exports/`, outside active skill roots and version control;
restore only after reviewing newer work and obtaining overwrite approval.

Project-specific rules remain with their project owners, including the existing
[Shane Thai context](../skills/shane-thai-new-chat/references/new-chat-context.md).
Do not turn those rules into global defaults during migration.

## HTML Helper Compatibility

The canonical command is `mockup-to-product/scripts/extract_reference.py`.
It accepts HTML only, defaults to `.design-reference`, and writes
`reference-manifest.json`, `reference-manifest.md` and
`MOCKUP_TO_PRODUCT_WORKLOG.md`. The worklog is an optional-use planning seed:
detected routes/controls/components are candidates, not required task scope.

The retained `claude-to-a-tee/scripts/extract_reference.py` forwards to that
implementation. It retains `.claude-reference` and adds both historical
`CLAUDE_TO_A_TEE_WORKLOG.md` and `REFERENCE_TO_A_TEE_WORKLOG.md` filenames for
old consumers. These filenames are compatibility outputs, not active skill names.
Existing worklog files are not overwritten; use a fresh directory for new
evidence because manifests/captures can be replaced on rerun.

Static inventory uses the Python standard library. Optional initial-state
rendering requires Python Playwright and a working browser. A requested render
that is unavailable/fails returns nonzero while retaining static inventory;
that output must not be described as rendered verification. Image files are
rejected and must be inspected visually.

## Verification

From the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills/mockup-to-product/tests -v
python3 skills/mockup-to-product/scripts/extract_reference.py --help
python3 scripts/verify_skills.py --expected-count 151
git diff --check
```

The helper suite covers static inventory, multiple inputs, rejected image/missing
inputs, render failure reporting, legacy invocation, preserved notes and a scoped
worklog. The structural verifier checks links/frontmatter/scripts. Neither proves
agent design judgment or rendered UI/UX quality. Check Codex discovery separately
after retirement; an existing chat may still have the earlier skill list in context.
At the migration checkpoint the archive contained 88 personal skills, 58 global
aliases and 2 standalone global skills (149 entrypoints with the native skill).
Later additions are recorded in [CODEX_CONTEXT.md](CODEX_CONTEXT.md).

For future instruction reviews, use these cases as acceptance examples, not a
claim that a model benchmark has been run:

| Scenario | Expected decision |
| --- | --- |
| PNG only, unknown viewport | Inspect the image; use ratios/provisional scale, not invented exact CSS or an HTML requirement. |
| Selected newer image plus older HTML | Use selected authority per surface; reuse only applicable source values/assets. |
| Desktop image plus mobile requirement | Compose and verify mobile as adaptation, not supplied mobile parity. |
| One spacing repair | Use owner, contextual comparison and touched-risk checks; no global ledger or all-controls tour. |
| Explicit exact region | Honor that constraint with adequate evidence; do not impose it on unrelated regions. |
| Full page or requested flow | Verify every requested section/step, including lower-page and relevant states. |
| Legacy prompt/CLI | Use mockup guidance and retained CLI outputs, without restoring rigid defaults. |
| Static inventory or green tests | Report helper/structure evidence only, not visual quality or release approval. |
