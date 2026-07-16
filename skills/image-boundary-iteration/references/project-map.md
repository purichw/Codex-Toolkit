# Project Map

Use these paths as current source-of-truth pointers. If a path is stale, search under `/Users/point/outputs/` and update the relevant project handoff.

## Main Paths

Project root:

`/Users/point/outputs/nudity_reference_prompting/`

Reference docs:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/`

Generated/reference assets:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/generated_assets/`

Scripts:

`/Users/point/outputs/nudity_reference_prompting/scripts/`

Skill helper scripts:

`/Users/point/.codex/skills/image-boundary-iteration/scripts/`

Additional skill snapshots:

`/Users/point/outputs/nudity_reference_prompting/skills/`

Global image-boundary live skill:

`/Users/point/.codex/skills/image-boundary/SKILL.md`

Fast workbook updater:

`/Users/point/.codex/skills/image-boundary-iteration/scripts/fast_workbook_update.py`

Pending update inbox:

`/Users/point/outputs/nudity_reference_prompting/inbox/`

Archive:

`/Users/point/outputs/nudity_reference_prompting/archive/`

## Important Files

- `new_chat_handoff_prompt.md`: current handoff and file map.
- `codex_communication_preferences.md`: how to talk to the user.
- `imagen_rejection_efficiency_notes.md`: rejection strategy learning.
- `rejection_trigger_index.md`: quick risk index, never prompt payload.
- `rpg_guy_visual_baselines.md`: accepted visual baselines and caveats.
- `watercolor_bathhouse_branch_notes_2026-07-05.md`: watercolor bathhouse branch rules, assets, rejects, and prompt direction.
- `watercolor_bathhouse_visual_baselines.md`: accepted/useful visual baselines for the watercolor bathhouse branch.
- `watercolor_genshin_trio_batch_notes_2026-07-14.md`: active watercolor fantasy trio branch notes, including PV-082 water north-star, PV-083 safe bedroom base, and PV-084 bedroom editorial-crop north-star.
- `design_polishing_playbook.md`: quality-restoration workflow for accepted boundary images; use before further boundary pushes when faces, hands, linework, water, or texture start breaking.
- `moonlit_celestial_fountain_branch_notes_2026-07-05.md`: moonlit fountain branch rules, assets, rejects, and prompt direction.
- `moonlit_celestial_fountain_visual_baselines.md`: accepted/useful visual baselines for the moonlit fountain branch.
- `boundary_iteration_playbook_v2_2026-07-03.md`: synthesized evidence-first strategy rules from workbook + Markdown + latest PV-077 branch.
- `references/choice-glossary.md`: streamlined user-facing verdict/reason/action choices.
- `$image-boundary`: global router and new-chat memory capsule; installed at `/Users/point/.codex/skills/image-boundary/` and snapshotted at `/Users/point/outputs/nudity_reference_prompting/skills/image-boundary/`.
- `$image-boundary-nonexplicit-max`: max-boundary non-explicit prompt strategy; installed at `/Users/point/.codex/skills/image-boundary-nonexplicit-max/` and snapshotted at `/Users/point/outputs/nudity_reference_prompting/skills/image-boundary-nonexplicit-max/`.
- `$image-boundary-safety-map`: risk-zone map for boundary-forward requests; installed at `/Users/point/.codex/skills/image-boundary-safety-map/` and snapshotted at `/Users/point/outputs/nudity_reference_prompting/skills/image-boundary-safety-map/`.
- `$image-boundary-rejection-recovery`: recovery workflow after blocks/rejects; installed at `/Users/point/.codex/skills/image-boundary-rejection-recovery/` and snapshotted at `/Users/point/outputs/nudity_reference_prompting/skills/image-boundary-rejection-recovery/`.
- `$image-boundary-polish`: live Codex skill for quality restoration without boundary escalation; installed at `/Users/point/.codex/skills/image-boundary-polish/` and snapshotted at `/Users/point/outputs/nudity_reference_prompting/skills/image-boundary-polish/`.
- `$image-boundary-efficient`: removable speed layer for fewer wasted retries without lowering quality; installed at `/Users/point/.codex/skills/image-boundary-efficient/` and snapshotted at `/Users/point/outputs/nudity_reference_prompting/skills/image-boundary-efficient/`.
- `workbook_update_workflow.md`: packet workflow.
- `excel_update_safety_notes.md`: workbook safety rules.
- `sensitive_figure_reference_prompting_glossary.verification-2026-06-24.xlsx`: main workbook.
- `sensitive_figure_reference_prompting_glossary.compiled.json`: active compiled JSON.
- `sensitive_figure_reference_prompting_glossary.compiled.min.json`: active minified JSON.
- `sensitive_figure_reference_prompting_glossary.eval_cases.json`: active eval cases.

## Workbook Contract

The active workbook is a mixed evidence/rules artifact. Keep current writes in the four packet-supported sheets:

- `Retest Results Log`: run-level user verdicts and important reject/learning evidence.
- `Passed Visuals`: user-passed image baselines only.
- `Prompt Templates`: reusable prompt wording only.
- `Adult Clarity Audit`: synthesis, cleanup, stale-note, and schema guidance.

Historical/compiler sheets can stay even if they look old. Rename/delete/combine them only with a coordinated migration of the workbook updater, compiler, packet template, compiled JSON, and docs.

## Refresh Policy

- In a new chat, start with `$image-boundary`; its Project Memory Capsule is enough for ordinary continuation.
- Read handoff at new branch, cold reset, exact branch-history lookup, or after workbook/compiled JSON changes.
- Read trigger index before prompt families close to known rejects.
- Read compiled JSON/workbook only when exact latest phrase mappings, templates, or logging evidence are needed.
- Do not load all files before every generation.

## Search Fallbacks

```bash
find /Users/point/outputs/nudity_reference_prompting -name '*.md' -print
find /Users/point/outputs/nudity_reference_prompting -name '*.xlsx' -print
find /Users/point/outputs/nudity_reference_prompting -name '*compiled*.json' -print
find /Users/point/outputs/nudity_reference_prompting -maxdepth 3 -type f \( -name '*.py' -o -name '*.mjs' \) -print
```
