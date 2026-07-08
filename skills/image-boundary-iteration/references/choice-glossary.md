# Choice Glossary

Use this when the user asks for the project glossary, verdict choices, simple labels, or an easy option list for image iteration feedback.

Keep the list streamlined. Offer these choices first instead of a long custom taxonomy.

## Format

`[Verdict] / [Reason] / [Next Action]`

Example:

`BASE / LOOK / CONTINUE`

Meaning: the image works as a visual/style base and should be continued, but it is not a final boundary pass.

## Verdict

- `PASS` = final visual pass; can continue from it or record it as a passed visual when user confirms.
- `BASE` = accepted as a construction base, but not the final target.
- `PARTIAL` = some parts work, but a clear issue remains.
- `REJECT` = fails the user's goal, or the tool produced no usable image.

## Reason

- `LOOK` = face, style, beauty, character appeal.
- `POSE` = pose, body language, stance, gesture.
- `BOUNDARY` = sexy/minimal/see-through direction or boundary level.
- `COSTUME` = outfit, cloth, drapery, accessories, visual coverage.
- `SCENE` = setting, lighting, composition, framing.
- `DRIFT` = drift from identity, branch, or accepted baseline.
- `QUALITY` = anatomy, hands, details, rendering quality.

## Next Action

- `CONTINUE` = use this image as the next base.
- `EDIT` = local edit one specific issue on this image.
- `RETRY` = try again in the same direction or prompt family.
- `CHANGE HOW` = keep the goal, but change the prompting/editing method.
- `BACKTRACK` = return to a previous better image.
- `RESET` = start clean with a short prompt and reduced context bleed.

## Common Short Labels

- `BASE / LOOK / CONTINUE`
- `PARTIAL / BOUNDARY / EDIT`
- `PARTIAL / COSTUME / CHANGE HOW`
- `PASS / BOUNDARY / CONTINUE`
- `REJECT / DRIFT / BACKTRACK`
- `REJECT / QUALITY / RETRY`
- `BASE / SCENE / CONTINUE`

## Interpretation Rules

- Treat `BASE` as `Baseline Pass / Target Partial`: useful and accepted as a stepping stone, but not a final pass.
- Do not put `BASE` or `PARTIAL` into Passed Visuals unless the user later upgrades it to `PASS`.
- If the user gives one slot only, preserve it and ask only if the next action is ambiguous.
- If the user later changes the verdict, trust the latest user verdict.
