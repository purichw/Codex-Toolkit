---
name: image-boundary-iteration
description: Controlled iteration workflow for adult non-explicit image prompting/editing in the nudity_reference_prompting project. Use for boundary-forward fantasy/RPG/watercolor character art, fewer costume pieces or visual clutter, stronger or sensual-coded poses, Pass/Partial/Reject loops, local edits, prompt hygiene, rejection handling, branch-separated visual baselines, workbook/JSON/Markdown logging, or continuing this project from a handoff.
---

# Image Boundary Iteration

## Core Contract

Use simple Thai. Continue this project as boundary-forward adult non-explicit image iteration: fewer costume pieces, less visual clutter, stronger/sensual-coded posing when requested, while staying non-explicit. Preserve accepted identity, proportions, medium, branch, and visual baselines.

Do not default back to conservative armor/coverage unless the user asks for a reset/base or a temporary safer base is strategically needed. Safe bases are stepping stones, not final goals.

Never claim `generated`, `Pass`, `Partial`, `Reject`, or `accepted` without actual tool output or user verdict.

## Operational Synthesis

Use the user's shorthand as a three-part control signal when present:

- First slot = verdict: `PASS`, `PARTIAL`, `BASE`, or `REJECT`.
- Second slot = dimension: `BOUNDARY`, `COSTUME`, `POSE`, `LOOK`, `DRIFT`, or combined dimensions.
- Third slot = next action: `CONTINUE`, `CHANGE HOW`, `EDIT`, or `BACKTRACK`.

Interpretation:

- `PASS` means the image is visually accepted for the stated dimension; it can become the next base.
- `BASE` means usable stepping stone, not necessarily close to the final boundary.
- `PARTIAL` means preserve what worked but the named dimension still misses; do not call it accepted.
- `REJECT` means do not continue from that image unless the user explicitly says to salvage something.
- `CONTINUE` means keep the same successful family but make one controlled step.
- `CHANGE HOW` means stop strengthening the same wording; change scene, composition, material language, base, or edit strategy.
- `EDIT` means prefer a local/specific edit when feasible; if local edits melt details or drift twice, return to clean generation.
- `BACKTRACK` means return to the last stronger accepted base.

Core learned pattern: successful boundary pushes usually come from changing the visual system, not directly saying what to remove. Use scene, material, light, atmosphere, pose, or ornamental layout to make the desired image read naturally while staying non-explicit.

## Branch Routing

Keep branch knowledge separated. Reuse workflow discipline across branches, but do not import visual vocabulary by default.

- RPG / celestial / chroma branches: use `rpg_guy_visual_baselines.md`, PV-076, PV-077, and celestial prompt-strategy notes.
- Watercolor bathhouse branch: use `watercolor_bathhouse_branch_notes_2026-07-05.md` and `watercolor_bathhouse_visual_baselines.md`; preserve watercolor bathhouse medium, robe/wrap drapery, adult Elf identity, and cozy non-explicit scene anchors.
- Moonlit celestial fountain branch: use `moonlit_celestial_fountain_branch_notes_2026-07-05.md` and `moonlit_celestial_fountain_visual_baselines.md`; preserve adult white-haired Elf identity, masculine S-curve dancer presence, moonlit fountain courtyard, black reflective marble, water curtains, star motes, compact white-gold center accent, and narrow translucent energy ribbons.
- Classical black-marble bath trio branch: use the 2026-07-10 sections in `references/prompt-strategy.md` and `references/rejection-handling.md`; preserve classical museum oil painting, three adult mythic men, black-marble pool, continuous reflective waterline, moonlight, steam, and non-explicit water/reflection lower-frame structure.
- If a branch departs from the old RPG style, create/update branch notes, branch asset names, workbook tags/notes, and handoff pointers instead of mixing baselines.

## Latest Must-Know

Full RPG/celestial synthesis:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/boundary_iteration_playbook_v2_2026-07-03.md`

Current clean north-star continuation:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/generated_assets/seraph_elf_duet_champagne_single_sash_full_pass_2026-07-03.png`

`PV-077` verdict: `Pass คะแนนเต็ม`.

PV-077 rule: preserve bright champagne/white-gold light-surface, close duet chemistry, one clean thin luminous diagonal sash-line per character, and one tiny radiant star glyph. Direct pants/waist/lower-garment/coverage wording rejected; broad whole-figure ornamental-layout simplification passed. Attempts below PV-077 rejected, so treat it as the current known boundary unless the user explicitly asks for a controlled risky test.

Watercolor bathhouse branch:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/watercolor_bathhouse_branch_notes_2026-07-05.md`

Current ideal non-RPG pass baseline:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/generated_assets/watercolor_bathhouse_three_mythic_men_mist_ideal_pass_2026-07-07.png`

2026-07-07 user verdict: `สวยมากที่สุดใน non-RPG ที่ทำมาเลย ใกล้เคียงกับ ideal มากที่สุด`.

Watercolor three-character rule: the strongest route is not direct garment-removal language. Use a believable soaking-pool composition where warm mist, opaque water, foam clusters, pool ledges, foreground plants, and reflected golden light carry the non-explicit visual structure. Keep three mature adult fantasy men readable: white-haired Elf, tan haloed man with no wings, and wingless Devil with horns/tail and only tiny ruby-gold accent glints. Preserve cozy warm watercolor, loose pencil line, cream stone, jade tile, brass spouts, plants, lantern glow, and natural triangular group posing. Avoid awkward raised tub poses and avoid direct "no garment / no fabric / less clothing" wording; translate user reduction requests into atmosphere-led composition and low-bulk accent simplification.

2026-07-07 natural-volume continuation: user wanted a small non-explicit bulge/natural form read for the haloed man and Devil. Do not put `bulge`, `crotch`, or direct genital wording into prompts. Translate to: `small naturalistic anatomy refinement`, `lower torso / upper-thigh transition reads slightly more natural under opaque water and mist`, `extremely subtle soft watercolor indication of natural male form beneath the waterline and steam`, and keep `mist, water surface, foam clusters, and reflected golden light as the main visual structure`. This generated a good continuation but changed the image more like a regenerate than a precise local edit; use it as a CHANGE HOW candidate, not a guaranteed exact edit.

Watercolor prompt discipline:

- Best base: PV-081 mist-led three-character soaking pool.
- Best HOW: `spa atmosphere carries coverage`.
- Best reduction language: lower visual clutter, tiny accent glints, opaque water, foam clusters, warm mist, reflected light, natural ledges.
- Best naturalness language: soft natural body volume under water/steam; lower torso / upper-thigh transition reads more natural.
- Avoid: active shower + minimal costume, direct garment-removal wording, explicit anatomy words, object-as-censor framing, awkward raised tub poses, and over-preserving exact composition when the prompt asks for a subtle anatomical read.
- If the tool regenerates instead of precise-edits, evaluate as `CHANGE HOW` rather than failed local edit unless identity or branch style is lost.

Earlier single-Elf pass baseline:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/generated_assets/watercolor_bathhouse_adult_elf_fullbody_masculine_pose_pass_2026-07-05.png`

PV-078 verdict: user said `โอเค สวย`.

Watercolor rule: direct active-shower + minimal visible costume prompts rejected; safe robe/spa watercolor base passed. Continue with branch-specific bathhouse drapery and pose/design language. Do not import PV-077 single-sash/glyph/chroma defaults unless explicitly cross-testing.

Moonlit celestial fountain branch:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/moonlit_celestial_fountain_branch_notes_2026-07-05.md`

Current pass baseline:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/generated_assets/moonlit_celestial_fountain_adult_elf_scurve_boundary_pass_2026-07-05.png`

PV-079 verdict: user said `PASS / BOUNDARY / CONTINUE`.

Moonlit fountain rule: fresh scene reset away from bathhouse passed; attempts to reduce below PV-079 rejected twice, including whole-figure simplification and light-surface/star-motif wording. Treat PV-079 as current known branch boundary. Continue via pose, camera, composition, face, lighting, or scene changes before trying lower visual coverage.

2026-07-06 update: the branch moved past the original PV-079-only guidance through controlled genre tests. User gave `PASS` to an ornamental-layout route, then `PARTIAL / BOUNDARY / CONTINUE` to a whole-figure light-surface route. A one-piece magical lacquer stage suit was visually liked but could not be pushed into skin-tone/thin/body-paint wording; that family rejected repeatedly. Genre previews showed `Fashion Editorial` and `Stage Costume Concept Sheet` as the preferred next route; user personally chose `Fashion Editorial + Stage Costume`. Use fashion/editorial material language for sexy polished mood and stage-costume concept language for minimal intentional design. Avoid direct lower-costume, brief/wrap, skin-tone, body-paint, painted-on, same-color-as-skin, and negative-space wording on adult full-body dancer prompts. Abstract Celestial Figure rejected repeatedly and should not be the next primary route.

Mature graphic-novel / editorial trio branch, 2026-07-09:

The current strongest post-RPG direction is a mature graphic-novel / fashion-editorial trio with the white-haired Elf, haloed brown-haired celestial man, and horned black-haired Devil. The user liked the warm lounge / intimate portrait direction and asked to continue from it, especially reducing visible fabric on the Elf. Preserve the three adult identities, close triangular composition, warm amber-beige room, dark sofa/daybed, simple curtains, low sparkle, and clean ink/painterly rendering. Do not preserve the older soft watercolor bathhouse or chroma RPG styling unless requested.

Useful current evidence:

- Accepted graphic-novel lounge direction:
  `/Users/point/.codex/generated_images/019f4ba9-c316-744a-88f7-07e70675446c/ig_0bb98ed6b69ca611016afd00db9b7881919ecb1b52b73707a4.png`
- Strong continuation candidate:
  `/Users/point/.codex/generated_images/019f4d1d-df10-75c2-92c9-e8d845a555d3/ig_08cb9899d80519b2016b0d755d90d88191ba7634384c01718a.png`

These `.codex/generated_images` paths are ephemeral. Verify they exist before
using them; if missing, search handoff/project assets or continue from the
latest visible user-provided image instead of inventing evidence.

Best prompt HOW for this branch:

- Use `mature graphic-novel fashion editorial`, `close triangular lounge portrait`, `bare shoulders and upper-body focus`, `reduced fabric bulk`, `lower-body styling mostly outside the crop`, `sofa edge / arm placement / crop as natural non-explicit visual structure`.
- If the user asks for stronger or more exposed, translate to camera, crop, pose, and fabric-bulk language. Do not use direct explicit, porn, no-clothing, garment-removal, crotch, or bulge wording in image prompts.
- Avoid excessive sparkle, heavy oil shine, busy jewelry, armor return, black trouser-like shapes, large draped cloth panels, and over-dark shadows that hide the characters.

Recent rejected family:

Soft-anime / sensual-water-ref family rejected repeatedly in this context, including attempts that removed the reference images and backed off to head-and-shoulders or safe style-sheet wording. Treat this as context-sensitive. In a fresh chat, do not start by attaching those sensual soft-anime refs. If testing that style again, start with a single character or fully safe clothed style calibration before reintroducing trio intimacy.

## Context Refresh

Do not load everything before every generation.

- New branch: read `new_chat_handoff_prompt.md`; add branch baselines/notes only as needed.
- Cold reset: read `new_chat_handoff_prompt.md` and `rejection_trigger_index.md`; draft from the current goal without old trigger wording.
- Prompt near known trigger: read `rejection_trigger_index.md` plus relevant `imagen_rejection_efficiency_notes.md`; optionally run `scripts/prompt_risk_check.py`.
- After workbook/compiled JSON update: read `new_chat_handoff_prompt.md`; read compiled JSON/workbook only when exact mappings/templates/evidence matter.
- User asks for glossary, verdict options, or easy feedback choices: read [choice-glossary.md](references/choice-glossary.md) and provide that streamlined list first.
- Same-chat continuation: use latest user verdict/image and keep momentum.

## Image Workflow

If generating/editing images, also use the system `imagegen` skill and read its `SKILL.md`.

Before each image call:

- Tell the exact prompt.
- Tell the user to give `Pass`, `Partial`, or `Reject` after the image appears.
- Keep the prompt clean and task-local.
- Translate risky user wording into non-explicit artistic/fantasy/design/sculptural wording without weakening intent.
- Do not paste avoid lists, workbook rows, retrospective notes, or project rules into prompts.
- Use the current accepted image as base when the user says "ต่อ"/"ทำต่อ", unless they ask to backtrack/reset.

After each image call:

- Do not add extra text in the same response after the image tool returns.
- Let the image tool output stand, then wait for the user's next verdict.

## Strategy

- For stronger/boundary-forward requests, use a boundary acceleration loop:
  identify the missing axis, choose one stronger HOW, generate/edit once, then
  classify the result from user verdict or visible output. Missing axes include
  costume bulk, visual clutter, pose/body language, crop/composition,
  material/surface system, atmosphere/light structure, identity, and quality.
- Prefer changing HOW over simply intensifying the same wording. Stronger HOW
  includes tighter editorial crop, more direct gaze, cleaner lower-frame
  structure, fewer accent pieces, continuous water/light/lacquer surface,
  stronger pose silhouette, or branch-specific atmosphere carrying the
  non-explicit structure.
- Imagen remains empirical. Treat each prompt as a hypothesis with evidence:
  `works`, `underdelivers`, `rejects`, `drifts`, or `regresses conservative`.
  Preserve the winning HOW and stop repeating losing families.
- Stop a prompt family after 2 related rejects; then backtrack, switch base, cold reset, or change HOW.
- One high-risk ladder rejection can be enough to step back.
- If user says `Pass`/`Partial` and one local issue remains, prefer local edit.
- Local edit default: 1 target; max 2 attempts on the same issue/region unless the user explicitly says to continue.
- If edits melt details, cause drift, or miss intent, return to a cleaner base.
- When direct wording is risky but the intent is clear, translate first and show the exact translated prompt before calling the image tool.
- If a prompt succeeds visually but by regeneration, preserve it as a candidate continuation and tell the user it is not a precise local edit.
- For two-character contact/carry/relationship: spacing -> gaze -> near contact -> one neutral contact -> protective pose -> stronger pose.

## Boundary Language

Prefer positive design wording:

- `streamlined ceremonial fantasy design`
- `remove visual clutter`
- `one signature gold celestial accent`
- `sleek emblem-like center design`
- `low-bulk ceremonial mark`
- `smooth sculptural anatomy without explicit detail`
- `smooth continuous magical lacquer surface`
- `simplify ornamental layout across both figures`
- `one clean thin luminous diagonal sash-line`
- `tiny radiant star glyph`
- `small naturalistic anatomy refinement under opaque water and mist`
- `soft watercolor indication of natural body volume beneath the waterline`
- `lower torso / upper-thigh transition reads slightly more natural`

Avoid unless the user explicitly asks for a controlled risky test:

- direct smaller/tighter/less-fabric wording around central garments
- `no fabric`, `no coverage`, `no garment`
- pants / waist garment / lower-garment removal wording in the PV-077 branch
- object/shadow/weapon-as-censor framing
- direct `bulge`, `crotch`, genital, or explicit anatomy wording; translate into subtle natural form under water/steam when the intent is non-explicit naturalness
- long anatomy/explicitness negative lists
- stacked relationship/carry words with close-face, torso touch, support, lift, or weight-shift

For details, read [prompt-strategy.md](references/prompt-strategy.md) and [rejection-handling.md](references/rejection-handling.md).

## Logging

Keep generation and logging separate. Update workbook/JSON/Markdown only when the user asks, gives a clear verdict, or the learning/baseline matters.

For workbook updates, read [logging-workflow.md](references/logging-workflow.md), use the packet workflow, dry-run first, inspect rows, apply only when correct, regenerate compiled JSON/eval cases, and read newly added rows before final.

For faster future updates, prefer `scripts/fast_workbook_update.py` after creating or editing a packet. It wraps the safe updater, defaults to dry-run, and summarizes changed ranges, backup path, render folder, compiled JSON checks, and expected IDs.

## Project Files

Project root: `/Users/point/outputs/nudity_reference_prompting/`

Primary docs/workbook: `/Users/point/outputs/nudity_reference_prompting/References for Codex/`

Read as needed:

- `new_chat_handoff_prompt.md`
- `boundary_iteration_playbook_v2_2026-07-03.md`
- `codex_communication_preferences.md`
- `imagen_rejection_efficiency_notes.md`
- `rejection_trigger_index.md`
- `rpg_guy_visual_baselines.md`
- `watercolor_bathhouse_branch_notes_2026-07-05.md`
- `watercolor_bathhouse_visual_baselines.md`
- `moonlit_celestial_fountain_branch_notes_2026-07-05.md`
- `moonlit_celestial_fountain_visual_baselines.md`
- `sensitive_figure_reference_prompting_glossary.compiled.json`
- `workbook_update_workflow.md`
- `excel_update_safety_notes.md`

## Helpers And References

- `scripts/prompt_risk_check.py`
- `scripts/create_logging_packet.py`
- `scripts/fast_workbook_update.py`
- `scripts/project_status.py`
- [operation-rules.md](references/operation-rules.md)
- [choice-glossary.md](references/choice-glossary.md)
- [prompt-strategy.md](references/prompt-strategy.md)
- [rejection-handling.md](references/rejection-handling.md)
- [logging-workflow.md](references/logging-workflow.md)
- [project-map.md](references/project-map.md)
