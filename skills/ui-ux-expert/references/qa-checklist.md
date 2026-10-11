# Rendered QA And Evidence

Scope this to current acceptance criteria and touched risks. It is not a required
whole-site audit for every visual edit. A checklist is a memory aid, not proof
that the composition is good or users prefer it.

## Capture Readiness

- Render the intended route, auth/data state and overlays. Use bounded,
  state-specific readiness: loaded fonts, decoded visible media, expected data
  and controls. Do not equate a vanished spinner with correct content.
- Record source/build identity, browser/engine, viewport, DPR/zoom, route,
  data/fixture identity, scroll and state. Match these for before/after work.
- Preserve earlier-state evidence before edits when comparison is required.
  A baseline reconstructed later must be labeled as a reproduction.
- Use `$snapshot` automatically. Include parent context and enough page coverage
  for the claim. A local crop cannot certify the whole page.
- Open the captured image. Record which image/state was actually reviewed;
  capture success, a saved path, or a checksum is not visual inspection.
- After a relevant late edit, recapture. Reuse only when all relevant sources,
  assets, content and conditions still match.

## Inspect The Composition

Check the [composition pass](composition-and-calibration.md), not only isolated
CSS values. Identify entry point, reading sequence, grouping, visual weight,
density, media crop and the actual task/action. Inspect full-page rhythm when
that is in scope. Do not invent a required number of defects.

## Required Checks, When Applicable

| Surface | Evidence needed |
| --- | --- |
| Geometry | No unintended overlap/clipping/page overflow; meaningful text survives long-content/narrow states. Local two-dimensional scroll remains usable. |
| Typography | Correct loaded font/weight/script coverage; role hierarchy, readable measure, stable wrapping and no clipped combining marks. |
| Alignment | Actual painted controls, groups and parent edges; user preferences survive closed/open and responsive states. |
| Color | Measured actual foreground/background pairs, including tint/alpha; non-color state meaning. Use the accessibility reference, not "all UI is 3:1." |
| Product fit | Source direction and established system preserved; no fake facts, dead controls or unauthorized capability removal. |
| Interaction | Exercise keyboard/focus, click/touch, transitions, return paths and relevant loading/error recovery. A screenshot alone is insufficient. |
| Data/Admin | Actual supported editor/save/reopen/render contracts; delayed response must not clobber dirty data. See product-redesign-contracts.md. |
| Responsive | Relevant narrow/intermediate/wide states, input model, content pressure, sticky/fixed controls; actual engine/device for platform claims. |
| Assets/runtime | Relevant media/font loading, console/request errors and fallback behavior. Do not hide errors by retrying until green. |
| Accessibility | Semantic names/roles, focus and keyboard, contrast, targets, text enlargement/reflow and reduced motion as scoped. |

## Defect To Repair Record

For substantive or repeated corrections, keep a compact record:
```text
Observation + image/state:
Hypothesis + discriminating check:
Owner/source change:
Matched after evidence:
Affected behavior/neighbor regression:
Result / remaining limitation:
```
Fix practical defects and re-render. A passing CSS assertion only proves the
assertion, not the desired visual effect. When required checks fail, diagnose
whether the cause is application behavior or harness/readiness. Keep failure
evidence, fix the causal problem and rerun affected checks. Do not weaken gates,
fabricate data, or extend arbitrary sleeps to manufacture a pass.

## Verdict

- **VERIFIED:** every required acceptance check for the named scope passed;
  visual evidence is current and actually inspected, and behavior claims have
  executed behavior evidence.
- **PARTIAL:** some required states/checks/evidence are missing or not run.
- **BLOCKED:** a prerequisite prevents required verification.
- **FAIL:** any required check failed. Disclosing it does not make it acceptable.

Failure takes precedence over missing evidence. Narrow the claim honestly, not
the original acceptance criteria. Optional polish may be disclosed without
blocking; an untested requirement may not be relabeled optional after the run.

Use a concise result with scope, evidence, failures/missing checks and limitations.
Do not claim compliant accessibility, user preference, faster completion or
general quality improvement from a static render.

## Machine Evidence Gate

[../evals/evidence.py](../evals/evidence.py) validates a manifest against an
explicit required-state matrix and current source/image hashes. It rejects
missing files, stale captures, wrong conditions, unreviewed images and failed
required checks. It does not inspect pixels, choose the right test matrix, or
prove a reviewer told the truth. Human/agent visual judgment stays separate.
Small edits may record the same facts compactly without a JSON manifest.
