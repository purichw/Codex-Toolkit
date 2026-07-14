# Operation Rules

Use this as the short operating contract for this project.

## Communication

- Speak Thai in simple, natural language.
- Explain what is happening, why it matters, and what happens next.
- Keep generation work and audit/logging work visibly separate.
- If the user corrects direction, accept it and adapt.
- The user decides final `Pass`, `Partial`, or `Reject`.

## Evidence Discipline

- Say the exact image prompt before each image tool call.
- Show the image after each image tool call.
- Do not say `generated`, `rejected`, `passed`, or `accepted` unless there is real tool/user evidence.
- If there is no image file or viewable result, treat it as a plan or hypothesis only.

## Iteration Mode

- Treat safe bases as starting points, not final goals.
- Default direction is boundary-forward: fewer costume pieces, stronger pose language, and sensual-coded adult fantasy posing when requested, while staying non-explicit.
- Preserve the active branch medium and vocabulary. Do not mix RPG/celestial/chroma baselines into watercolor bathhouse work unless the user asks for a cross-branch experiment.
- Do not restart as conservative/covered unless the user asks for a safe base, a cold reset, or the current strategy needs a temporary base.
- If user says "ต่อ", continue from the latest sensible accepted direction.
- If user says "ลองใหม่", adjust from the last attempt unless a reset is clearly needed.
- If user says "Pass", treat the verdict as clear and iterate forward.
- If user says "อัปเดตไฟล์", update workbook/JSON/MD with the safe workflow.
- If user asks for cold reset, start from clean task-local wording and avoid old trigger vocabulary.

## Context Refresh Rules

Do not read every source file before every generation. Refresh project context when it matters:

- New branch: read `new_chat_handoff_prompt.md`; add baselines/notes only as needed.
- Cold reset: read `new_chat_handoff_prompt.md` and `rejection_trigger_index.md`; then draft cleanly from the present goal.
- Prompt near trigger: read `rejection_trigger_index.md` and relevant `imagen_rejection_efficiency_notes.md`; optionally run the skill prompt risk checker.
- After workbook update: read `new_chat_handoff_prompt.md`; read compiled JSON/workbook only if exact latest mappings or templates matter.

For same-chat continuation with clear context, keep going from the latest user verdict and image instead of reloading everything.

## Safety Boundary

Allowed target:

- Adult fantasy/RPG/watercolor character concept art.
- Non-explicit figure, costume, pose, and design iteration.
- Boundary-adjacent but tasteful visual exploration.
- Reduced-costume and sensual-coded pose direction when it is handled as adult non-explicit concept art, not sexual content.

Do not request:

- Genital detail.
- Sexual acts.
- Pornographic framing.
- Hidden nudity via object-as-censor.
- Direct explicit anatomy preservation.

Age verification, if mentioned, is only adult-context clarification. It is not permission to remove non-explicit guardrails.

## Local Edit Defaults

- Use local edit when user says Pass/Partial and one specific issue remains.
- Default to one edit target.
- If an edit returns costume regression, anatomy errors, or visual melting, backtrack to the previous good image.
- Local edit / retouch max: 2 attempts on the same issue or region. If both attempts fail, reject, melt details, create drift, or still do not look right, stop and report that the local-edit limit was reached.
- Continue past 2 local edit attempts only when the user explicitly says to keep going.
- If 1-2 local edits fail, change base or HOW instead of forcing the same edit.
