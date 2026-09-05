# Contextual Rules

Use when adapting fallback values, diagnosing an exception, or reviewing a rule
that seems to contradict the product. Existing craft values and calibration
specimens describe starting arrangements, not universal evidence of quality.

## Rule Contract

For a new or revised rule record: intended outcome, applicability, exceptions,
observable check, and source/evidence. Separate mandatory requirements from
craft heuristics, product decisions, and untested hypotheses. A rule ID identifies
a statement; it is not evidence that the statement applies to this task.

Consult `$design-quality-review` for its established tags/severities. Do not
relabel a preferred pixel value as `[FACT]`; the measured value may be factual,
but its desirability is contextual. Current authoritative standards must be
verified when making compliance claims; fallback numbers are not certification.

| Guideline | Useful when | Adapt / do not apply blindly | Check |
| --- | --- | --- | --- |
| Compact rows | Repeated record comparison is the main job. | Multi-line content, touch input, zoom, assistive needs, and action complexity can require more room. Do not shrink text just to hit a row count. | Actual content remains readable; targets/focus usable; key columns comparable. |
| Prose measure near 60-75 characters | Sustained reading in a compatible script/font. | Thai segmentation, CJK, mixed scripts, tables, and narrow panels need actual render inspection; `ch` is not a universal perceived character width. | Read paragraphs, inspect line breaks/leading, and avoid clipped combining marks. |
| One primary action | One task or next step clearly dominates. | Comparison or multi-object operations may have several legitimate actions; hierarchy is not deletion of functionality. | Intended next step visible; other required actions remain reachable. |
| Few fonts/accents | A new design needs a restrained starting system. | Script fallback, chart semantics, established brand roles, and accessible state encoding may need more. | Consistent roles and meaningful contrast, not an arbitrary count. |
| Single-column forms | Fields form a sequential journey. | Tightly related short inputs or established expert workflows can benefit from a group. | Logical reading/tab order; labels, errors, and narrow-screen reflow work. |
| Blur-time validation | A field is complete on blur and early errors would interrupt typing. | Dependent fields, asynchronous checks, existing errors being corrected, and submit-time constraints need tailored timing. | No premature errors; stale responses ignored; input preserved; blocker explained. |
| Add whitespace to a cramped view | Usable space or hit areas genuinely collide. | Poor grouping, redundant labels, or competing visual weight may be the cause. | Test the hypothesized cause; do not hide useful data or create unnecessary scrolling. |
| Hide secondary actions | Frequency and consequences justify lower prominence. | Required discovery, touch/keyboard operation, and destructive consequences cannot depend on hover. | Named accessible control, discoverable location, clear action scope/recovery. |
| Use a category specimen | The user's job resembles the specimen's task. | Brand intent, device, actual content, and mixed categories can justify a different composition. | Explain the task benefit; do not count "failing traits" as proof of bad design. |

## Multilingual And Content Stress

Use actual representative strings from the authorized project, including its
longest labels, Thai/Latin mixtures, numerals/units, empty values, and failures.
When unavailable, mark synthetic fixtures explicitly; never pretend they are
real customer data. Test translation expansion and zoom only on relevant
surfaces; do not assume a fixed expansion percentage covers every language.

Keep semantic order and important content intact when reflowing. Do not solve
clipping by silently deleting text, abbreviating consequential values, shrinking
everything, or imposing reference-only fixed heights. Use the existing system's
wrapping/truncation policy and preserve access to full values when needed.
Route detailed script checks to `$typography-refinement` and responsive checks
to `$mobile-web-qa` or `$mobile-native-feel` as appropriate.

## Updating Rules From Experience

One case can justify a local fix, not a universal law. For reusable lessons keep
before/after evidence, original task/constraints, the failed hypothesis if any,
and a counterexample. Prefer refining a rule's applicability over appending a
new absolute prohibition. Preserve supplied source manuals as provenance;
maintain corrections in the local interpretation layer and identify conflicts.
