# Composition And Contextual Calibration

Read for new composition, repeated "it still looks wrong" feedback, or skill
evaluation. A micro-edit with a known cause does not need all of these passes.

## Look At Three Scales

1. **Page/sequence:** inspect a full page or contact sheet. Identify the visual
   entry point and whether the reading order supports the actual task. Look for
   isolated heavy blocks, repetitive section rhythm and useful content pushed
   too far down. Do not shrink a whole-page screenshot and judge small type from it.
2. **Section/relationship:** inspect at working scale. Compare parent gutters,
   shared axes, content density, peer dimensions and within-group versus
   between-group spacing. Check whether intended peers actually feel related.
3. **Control/content:** inspect type metrics, glyph/painted-box alignment,
   readable contrast, image crop, labels and interaction states. Do this after
   structural problems, not instead of addressing them.

NN/g's [visual-design principles](https://www.nngroup.com/articles/principles-visual-design/)
describe scale, hierarchy, balance, contrast and perceptual grouping. Use those
as diagnostic lenses, not as a universal maximum number of sizes or an assurance
of usability. The three-scale method above is this skill's implementation
synthesis, not a validated NN/g test or an empirical quality score.

## Turn An Observation Into A Code Decision

| Observed relationship | Owner to inspect | Discriminating change / check |
| --- | --- | --- |
| Title dominates a compact tool | Page shell and heading role, not each child | Compare the title and first usable task at actual viewport size; preserve readable hierarchy |
| Rows cannot be compared | Column allocation, numeric styles, action group | Reserve meaningful value width and demote secondary emphasis before adding global padding |
| Page feels disconnected | Section grouping, repeated spacing and surfaces | Align meaningful groups and simplify redundant boundaries without boxing every section |
| Image looks weak despite correct dimensions | Asset choice, focal point, object-fit and surrounding scale | Inspect subject visibility/optical size; do not enlarge whitespace inside the source image |
| Fonts look wrong although family is declared | Actual loaded face, weight availability, line-height and script fallback | Inspect computed/loaded font and real text; a family declaration is not proof of rendering |
| Mobile looks like a squeezed desktop | Priority/order and component constraints | Recompose the task while retaining content and actions; do not merely shrink typography |

For a reference, record observed feature -> intended effect (an inference) ->
implementation owner -> matched rendered check. Keep observation separate from
inferred motive. When adapting, name the product/content reason and preserved
visual relationship rather than claiming pixel parity.

## Same-Content Demonstrations

[../evals/fixtures/index.html](../evals/fixtures/index.html) contains deliberately
flawed synthetic dashboard, mobile-form and editorial fixtures. Applying
[../evals/calibration.css](../evals/calibration.css) produces authored repairs
without changing their text/data/controls. See the evaluation protocol for the
runner. These are demonstrations of causal repair, NOT agent A/B results,
independent human preferences, or a universal best-looking design.

| Domain | Failure demonstrated | Authored repair | Where that repair would be wrong |
| --- | --- | --- | --- |
| Dashboard | Oversized heading, competing row actions and cramped amounts | Task-scale title, deliberate column allocation and action prominence | If actual touch targets collide, reducing emphasis alone does not fix hit areas; add usable space |
| Mobile form | Fixed label heights, centered helper/value prose, long error collisions | Let labels grow; center only user-preferred roles, keep native picker and input/error reading order | A centered short choice value is explicitly preferred; do not left-align every control |
| Editorial | Article paragraphs boxed as independent cards and squeezed beside each other | Restore title/deck/body/caption sequence and readable measure, preserving expressive serif/red direction | An article index can legitimately use cards; prose flow is not the right template for all editorial listings |

## Avoid Optimizing For The Benchmark

- Keep content/state unchanged across demonstration variants. A shorter label,
  removed action or flattering crop invalidates the apparent repair.
- Inspect states that might get worse: wrapping, error recovery, keyboard path,
  long headings, numbers/units and narrow layouts. A prettier default is not enough.
- Admit a tie or already-good surface. Do not invent defects to satisfy a quota.
- Do not standardize every project to the demo palette or type. The editorial
  counterexample intentionally differs from the neutral operational fixture.
- Record user feedback as a preference, not a usability study. A broader claim
  needs fresh held-out cases, controlled agent runs and independent review.

Primary guidance consulted 2026-10-12: NN/g above; W3C/Apple in
[accessibility-checks.md](accessibility-checks.md); Carbon/GOV.UK in
[layouts.md](layouts.md) and [components.md](components.md). These sources
support specific distinctions, not an endorsement of this skill.
