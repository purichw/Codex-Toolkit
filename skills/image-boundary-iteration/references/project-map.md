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
- `moonlit_celestial_fountain_branch_notes_2026-07-05.md`: moonlit fountain branch rules, assets, rejects, and prompt direction.
- `moonlit_celestial_fountain_visual_baselines.md`: accepted/useful visual baselines for the moonlit fountain branch.
- `boundary_iteration_playbook_v2_2026-07-03.md`: synthesized evidence-first strategy rules from workbook + Markdown + latest PV-077 branch.
- `references/choice-glossary.md`: streamlined user-facing verdict/reason/action choices.
- `workbook_update_workflow.md`: packet workflow.
- `excel_update_safety_notes.md`: workbook safety rules.
- `sensitive_figure_reference_prompting_glossary.verification-2026-06-24.xlsx`: main workbook.
- `sensitive_figure_reference_prompting_glossary.compiled.json`: active compiled JSON.
- `sensitive_figure_reference_prompting_glossary.compiled.min.json`: active minified JSON.
- `sensitive_figure_reference_prompting_glossary.eval_cases.json`: active eval cases.

## Refresh Policy

- Read handoff at new branch, cold reset, or after workbook/compiled JSON changes.
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
