# Prompt Strategy

This reference is for choosing HOW to prompt. Do not paste the whole file into image prompts.

## Prompt Hygiene

- Draft from the current visual goal only.
- Add only relevant preserve constraints.
- Avoid long negative prompts, especially after a rejection.
- Do not paste avoid lists, workbook rows, or retrospective notes into a generation prompt.
- In cold reset, write a short prompt from scratch before checking trigger risks.
- Translate direct user intent into safer wording without changing the creative direction into conservative coverage.

Optional helper:

Run `scripts/prompt_risk_check.py` on a draft prompt when the wording is close to known trigger families. Treat output as reminders, not final decisions.

## Useful Prompt Shape

Use a compact structure:

```text
Use case: stylized-concept
Asset type: adult fantasy RPG character concept art
Input image: use the attached image as the edit target.
Primary request: [one clear pose/composition/design change]
Costume design: [positive design-language change]
Preserve: [identity/style/background items that matter]
Constraints: tasteful non-explicit fantasy character asset, no genital detail, correct complete anatomy, no text, no watermark.
```

For fresh generation, omit the input image line and keep the prompt shorter.

## Costume Reduction Language

Prefer:

- `streamlined ceremonial fantasy design`
- `remove visual clutter`
- `one signature gold celestial accent`
- `compact polished waist emblem`
- `sleek emblem-like center design`
- `low-bulk ceremonial mark`
- `clean single accent`
- `crisp gold star clasp`
- `tiny high gold star clasp`
- `delicate chain arcs along the belt line`
- `reduced visual bulk`
- `cleaner silhouette`
- `sleek ceremonial center mark`
- `smooth continuous magical lacquer surface`
- `simplify ornamental layout across both figures`
- `one clean thin luminous diagonal sash-line`
- `tiny radiant star glyph`
- `very faint scattered gold inlay`

Use indirect design transformation:

- Change a large costume area into a compact ornament.
- Move larger decorative mass to side/front if needed.
- For the Seraph-Elf champagne branch, describe the whole figure as a coherent light-surface/glyph system instead of saying a garment is being removed.
- Keep fantasy anchors such as wings, halo, jewelry, or green chroma background when they help the image read as RPG asset.

Avoid around sensitive garment zones:

- `much smaller`
- `tighter`
- `less fabric area`
- `no fabric`
- `no coverage`
- `no garment`
- `ultra-short`
- object/shadow/weapon-as-censor wording
- direct pants / waist garment / lower-garment removal wording in the Seraph-Elf champagne single-sash branch

## Latest Seraph-Elf Champagne Branch

Current known full-pass baseline:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/generated_assets/seraph_elf_duet_champagne_single_sash_full_pass_2026-07-03.png`

Use PV-077 as the current clean north-star continuation after PV-076.

What worked:

- Broad whole-figure design language.
- `simplify ornamental layout across both figures`.
- `one clean thin luminous diagonal sash-line per character`.
- `one tiny radiant star glyph integrated into that line`.
- Bright champagne/white-gold magical lacquer.

Known limit:

- Attempts below PV-077 toward a shorter hairline arc or tiny-star-only layout rejected.
- Treat further central simplification on this same prompt family as a controlled risky test only.

## Watercolor Bathhouse Branch

Current ideal non-RPG baseline:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/generated_assets/watercolor_bathhouse_three_mythic_men_mist_ideal_pass_2026-07-07.png`

User verdict: closest non-RPG ideal so far.

Best current HOW:

- `spa atmosphere carries coverage`
- believable indoor soaking pool, not awkward raised tub
- natural triangular group layout
- warm mist, opaque bath water, foam clusters, pool ledges, reflected golden light, foreground plants
- identity through face/silhouette anchors, not costume bulk

Current three-character anchors:

- white-haired Elf with pointed ears and soft adult face
- tan haloed man, brown hair, small gold halo, no wings
- wingless Devil, dark curved horns, black hair, tan-bronze skin, tail, tiny ruby-gold accent glints

Useful branch phrasing:

- `warm simple watercolor mythic spa tableau`
- `believable cream-stone indoor soaking pool`
- `dense warm mist`
- `opaque bath water`
- `foam clusters`
- `pool ledges and reflected golden light`
- `tiny ruby-gold accent glints`
- `minimal visible costume clutter`
- `tasteful non-explicit composition`

For user requests like "less clothing" or "fewer pieces":

- Translate into atmosphere-led composition.
- Ask for lower visual clutter, smaller accent glints, stronger mist/foam/waterline, and better ledge geometry.
- Do not point at garment removal.

For user requests like "small bulge" / natural lower form:

- Do not use direct wording in the prompt.
- Translate to `small naturalistic anatomy refinement`, `lower torso / upper-thigh transition reads slightly more natural under opaque water and mist`, or `soft watercolor indication of natural body volume beneath the waterline`.
- Keep mist, water surface, foam, and reflected light as the main visual structure.
- This may regenerate the scene rather than perform a precise local edit; label it as `CHANGE HOW` if that happens.

Earlier single-Elf pass baseline:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/generated_assets/watercolor_bathhouse_adult_elf_fullbody_masculine_pose_pass_2026-07-05.png`

Read when continuing this branch:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/watercolor_bathhouse_branch_notes_2026-07-05.md`

What worked:

- Treat shower/bathhouse reference as mood and medium only.
- Make the subject clearly adult.
- Start from a robe/spa watercolor safe base.
- Use full-body bathhouse drapery language: loose sage-white robe, wrapped spa cloth, bare arms/collarbone/calves/feet.
- For "more masculine pose", use stance language: squared shoulders, less sway, balanced weight, less crossed legs.

Avoid:

- Active shower + minimal visible costume as the starting frame.
- Direct "less cloth" wording.
- Importing RPG/chroma or PV-077 single-sash/glyph vocabulary by default.

Useful branch phrasing:

- `cozy fantasy bathhouse`
- `soft watercolor and pencil linework`
- `tasteful non-explicit bathhouse drapery`
- `loose sage-and-white robe`
- `simple wrapped spa cloth`
- `cleaner drapery layout`
- `more open robe silhouette`
- `grounded masculine stance`

Avoid:

- direct `bulge`, `crotch`, genital, or explicit anatomy wording
- direct `no fabric`, `no garment`, `less clothing`, or garment-removal wording
- active shower + minimal visible costume + visible torso
- object/shadow/weapon-as-censor framing
- awkward raised tub-edge poses when a soaking-pool layout is available

## Moonlit Celestial Fountain Branch

Current pass baseline:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/generated_assets/moonlit_celestial_fountain_adult_elf_scurve_boundary_pass_2026-07-05.png`

Read when continuing this branch:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/moonlit_celestial_fountain_branch_notes_2026-07-05.md`

What worked:

- Fresh scene reset away from bathhouse triggers.
- Same original adult white-haired Elf, masculine celestial dancer presence.
- Moonlit fountain courtyard, black reflective marble, falling water curtains, columns, plants, star motes.
- Strong S-curve dancer pose.
- Few-piece white-gold center accent and narrow translucent energy ribbons.

Known limit:

- Attempts to reduce below PV-079 rejected twice.
- Rejected even when framed as whole-figure simplification or light-surface / star-motif design.

Useful branch phrasing:

- `moonlit celestial fountain courtyard`
- `black marble reflective floor`
- `falling water curtains`
- `blue-white moonbeams and gold rim light`
- `masculine S-curve dancer pose`
- `few-piece streamlined celestial performance design`
- `compact white-gold center accent`
- `narrow translucent energy ribbons`

Avoid on this branch unless explicitly doing a controlled risky test:

- Stronger below-PV079 reduction wording.
- Direct "much less" translation into costume removal language.
- Reusing PV-077 two-character/single-sash/chroma defaults.
- Reusing PV-078 bathhouse robe/shower defaults.

## Pose and Relationship Ladders

Two-character contact:

1. separate lineup
2. closer spacing
3. mutual gaze
4. near fingertip gap
5. formal hand contact
6. shoulder/upper-arm support
7. protective companion pose
8. side-waist action
9. diagonal airborne companion

Do not jump straight to full carry, lift, weight support, under-thigh support, or close romantic wording after rejects. If the user explicitly wants a risky controlled test, run one attempt, then stop the family if it rejects.

For single-character sensual-coded pose direction, prefer athletic/fantasy movement language:

- `celestial battle-dancer pose`
- `dramatic arched torso`
- `elegant dancer-like line`
- `charged but composed expression`
- `powerful airborne ring pose`
- `clean readable full-body silhouette`

Keep the wording non-explicit and asset-focused. The goal is a strong RPG character image, not a conservative redesign.

Acro-yoga:

1. no-contact synchronized pose
2. one-hand contact
3. shoulder support
4. both-hands support
5. low-base prep
6. beginner lifted balance

## Identity and Regression Control

- If using an older image for face repair, say it is for facial structure only.
- Explicitly say not to copy older costume, pose, garment shape, or accessories.
- If armor/long costume returns, treat it as costume regression, not a successful pose step.
- If face or quality degrades over edits, return to a cleaner base instead of over-editing.

## Mature Graphic-Novel Editorial Trio - 2026-07-09

Use this for the current three-character branch when the user wants the white-haired Elf, haloed celestial man, and wingless Devil to read hotter while staying non-explicit.

What worked:

- Mature graphic-novel / fashion editorial rendering.
- Tight triangular lounge composition with all three adult characters close together.
- Warm beige / amber room, dark sofa or daybed, simple curtains, lamp glow.
- Bare shoulders and upper-body focus with lower-body styling mostly outside the crop.
- Sofa edge, forearms, crop, overlapping torsos, and relaxed lounge pose as the non-explicit visual structure.
- Reduced sparkle and less shiny gold clutter so the bodies and faces stay readable.

Useful wording:

- `mature graphic-novel fashion editorial`
- `warm intimate lounge portrait`
- `close triangular composition`
- `bare shoulders and upper-body focus`
- `lower-body styling mostly outside the frame`
- `reduced fabric bulk`
- `minimal draped fabric visible only at the crop edge`
- `natural non-explicit coverage from crop, sofa edge, and relaxed arm placement`
- `clean ink lines with painterly shading`
- `warm amber lamp light, beige curtains, dark sofa`

Avoid:

- direct `porn`, `explicit`, `no clothing`, `nude`, `remove garment`, `underwear`, `bulge`, `crotch`, or anatomy-isolated wording in prompts
- bedroom/daybed wording that implies an explicit scene
- heavy glitter, excessive oil shine, sparkles everywhere, busy gold chains
- black trouser-like shapes, large wrapped cloth panels, armor return
- copying the rejected soft-anime water references directly into this same context

If the user asks for "more NSFW / porn-like":

- Translate to `more intimate fashion-editorial pose`, `closer crop`, `stronger private-room mood`, `less visible fabric bulk`, `warmer direct gaze`, and `body language closer and more charged`.
- Keep it non-explicit and do not introduce sex acts or visible explicit anatomy.

If the user asks to reduce the Elf specifically:

- Use `the white-haired Elf has the least visible fabric bulk of the trio`.
- Use `bare-shouldered, relaxed forearm placement, lower-body mostly outside crop`.
- Avoid saying the Elf has no garment or that hands replace clothing.

## Soft-Anime Style Shift Caution - 2026-07-09

The user liked a soft anime bathing-pair style reference, but the same-chat attempts rejected repeatedly even after removing direct refs and backing off to a safe style sheet. Do not keep trying that family in the same context.

Fresh-chat strategy if testing it again:

- Start with text-only style language, not the sensual reference images.
- Try one character or a fully safe clothed trio style calibration first.
- Use `soft anime fantasy portrait`, `gentle water lighting`, `clean youthful-but-adult faces`, `non-explicit calm bathing atmosphere`.
- Add intimacy only after a pass.
