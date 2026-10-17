# Native visual review and repair gate

This contract is deliberately separate from automated integrity checks. Its purpose is to make the
agent inspect the actual result, localize defects, and validate a targeted repair, not fill a checklist.

## Coverage before editing

Use a tiny plan for a micro-fix and a representative matrix for a flow/redesign. Name target OS/runtime,
build/source/bundle identity, device and logical size/scale, appearance, locale/text-size setting, route,
state and setup. Select default and pressured states from the change's risks, not every hypothetical
platform feature. Include a neighboring shared-component consumer. Expand coverage with reasons if the
change exposes a new risk; do not drop failed states after seeing them.

A useful screen pass includes whole viewport, relevant below-fold viewports and normal-scale control
or typography detail. Preserve overlap/context when scrolling. For keyboard, picker, menu and sheet
issues keep their surrounding system UI. Crops/stitched overviews are supplementary. Never crop an
obstruction out of the evidence. Generated mockups/spec images must be labeled design proposals.

## Inspect first, then diagnose

Open the images with actual image-inspection capability or provide them to a human reviewer. A path,
OCR output, source inspection or “screenshot saved” message does not mean the picture was seen.
Use the approved reference at comparable scale, and compare information relationships rather than
pixel similarity when the platform/available content legitimately differs.

Inspect task composition → hierarchy/grouping/typography → density/spacing → imagery → control detail.
Name defects in observable language: “helper appears closer to next field,” “secondary badge dominates
amount,” “bottom action overlaps keyboard,” “Thai marks clipped,” not simply “needs polish.”

## Minimal repair record

Use [review record](../templates/review-record.md) only for material issues. Capture the before state,
localize the problem, consider competing causes, choose a distinguishing check, identify the shared
owner, predict the change and check the same state afterward. Keep unsuccessful repairs and resulting
regressions visible. Avoid arbitrary fixed-offset patches and indiscriminate spacing inflation.

Don't demand a fixed number of defects or iterations. Clean surfaces should survive unchanged. If an
issue remains practical to fix within scope, fix and inspect again before claiming delivery. If blocked,
return the exact gap and executable next check. Do not quietly downgrade a serious visual flaw to
optional because behavior tests pass.

## Claims and release review

| Evidence | Establishes | Does not establish |
| --- | --- | --- |
| Schema/build/unit checks | Those checks' specific structural/code properties | Good composition or native use |
| Native screenshot | Visible state on the declared runtime, subject to provenance | Focus, gestures, persistence, sensor/haptic behavior |
| Recorded interaction/instrumentation | The specific exercised behavior | Universal device support or human ease-of-use |
| Human/blind comparison | Contextual visual/task judgment for those cases | General improvement from one preference |
| Bundled evidence checker | Hash/file/plan consistency and required-capture presence | Genuine build provenance, correct screen, image understanding or visual quality |

Use build IDs including dirty source/assets/dependency/bundle identity, not just an unchanged git commit.
Capture the final build after the last visual edit. For critical release claims, a reviewer or CI runner
should replay the predeclared states and verify installation/build provenance independently. Human
judgment belongs in the record with reviewer identity and disagreements, not an invented score.

In scope, reject critical data/permission/navigation/accessibility regressions, lost essential content,
and major visual defects that obstruct the task or approved reference. A minor subjective preference
can remain documented; do not invent perfection. Explicit preferences are constraints, not taste votes.

When testing a new skill release, use the separate evaluation kit outside the solver workspace. Compare
matched prompts/model/assets/budget and repeat runs; report losses/ties/missing evidence/cost too.
