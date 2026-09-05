# Design Judgment

Use for ambiguous defects, consequential redesign, or conflicting principles.
For a clear small edit, keep only the task, constraint, change, and relevant test.
This is a decision method, not another mandatory review ceremony.

## Diagnose Before Prescribing

1. State the task in product terms: who needs to decide or do what, in which
   state, with what cost if they are wrong? Preserve the requested scope.
2. Observe the actual surface. Separate measured geometry/content/behavior from
   interpretation ("hard to scan") and unknowns (actual user completion time).
3. Name the dominant symptom and at most a few plausible causes. Prefer causes
   that explain several related observations rather than unrelated polish.
4. Pick the cheapest discriminating check: inspect grouping, count repeated
   controls, trace one journey, measure a clipped label, or compare the same
   screen with a single changed variable. Use `$snapshot` for visual evidence.
5. Apply the smallest cause-directed fix. Predict both its intended benefit and
   what could get worse. Recheck using the same content, state, and viewport.
6. If the expected change is absent, revise the diagnosis before adding fixes.
   Stop when the requested outcome is covered; do not chase unrelated polish.

Do not claim a causal usability improvement merely because a screenshot looks
cleaner. Controlled visual checks support visual claims; user outcomes require
appropriate user evidence. Use `$visual-diagnosis` for detailed visual rules and
`$interaction-flow-qa` for behavioral proof instead of reproducing those manuals.

### Worked Hypothesis: Crowded Admin List

- Observed: four equally prominent actions repeat in every row; amounts wrap;
  operators must compare amounts across records. Row height alone is not proof
  that density is wrong.
- Candidate causes: action competition, unsuitable column allocation, or truly
  insufficient reading/touch space.
- Discriminating check: inspect available width and action priority, then test
  demoting secondary actions without changing text size or row padding.
- Candidate fix: keep the frequent action visible, use an accessible overflow
  menu for the remainder, and reserve width for numeric comparison.
- Expected visual result: unwrapped amounts and clearer action hierarchy.
- Regression checks: secondary actions still discoverable and operable with
  keyboard/touch; selection scope and permissions remain unchanged. Measure the
  actual target surface rather than imposing a universal rows-per-viewport goal.
- Unknown until tested with people: whether operators finish work faster.

If grouping is already clear and hit areas collide, this fix is not appropriate;
increase usable spacing or change the responsive layout instead.

## Resolve Conflicting Principles

List non-negotiable constraints before craft preferences: applicable user/project
rules, accessibility requirements, product/data contracts, supported platforms,
and the scope of authorized work. Brand/reference authority governs presentation
within those constraints; it does not silently override them.

| Conflict | Decision method | Evidence / cost to name |
| --- | --- | --- |
| Density vs readability | Keep information needed for comparison together; test the longest content and actual input method before changing row size. | Clipping, readable values, touch/focus access, extra navigation. |
| Reference vs real content/mobile | Preserve observed intent, identify absent states, and propose the smallest explicit adaptation. | What is measured parity vs inferred adaptation; no deleted content to fit. |
| Consistency vs local need | Try existing variants first; justify a new variant by a real task difference. | Which other usages could change; test representative consumers. |
| Minimalism vs discoverability | Demote infrequent actions only if labels, keyboard/touch access, and recovery remain clear. | Added steps and hidden-action risk; do not assume fewer controls means better UX. |
| Visual polish vs delivery scope | Fix blockers and the dominant requested defect first. | What is verified now and what is intentionally outside scope. |

For unresolved consequential choices, ask one focused question with the impact.
For reversible low-risk choices, choose a documented assumption and proceed.
Do not ask the user to decide every spacing value. Never trade away a required
check or access/data safeguard for a prettier screenshot.

## Compare Alternatives Selectively

Use alternatives when designing a new screen, changing navigation/grouping, or
when two plausible structures carry materially different user costs. Skip for
literal reference reproduction, obvious defects, and micro edits.

Compare 2-3 feasible approaches in a short note, wireframe, or component sketch;
do not build multiple full apps unless requested. Include the current approach
when retaining it is viable. Eliminate options that violate constraints before
ranking preferences. Avoid fake precision such as unsupported weighted scores.

Example: reviewing many records while retaining list context.

- Inline expansion: preserves position but can disrupt cross-row comparison.
- Detail pane: retains list context on wide screens; needs an explicit narrow
  screen path and focus management.
- Dedicated detail route: supports deep work/linking; requires preserved filters,
  selection, and return position to avoid losing context.

Choose based on the actual task and content, not a universal winning pattern.
Test the chosen path and the most likely regression. The normal deliverable is
one implemented answer with a concise rationale, not every rejected concept.

## Compact Decision Record

Use an existing task/PR note for consequential work; do not create a new file for
every edit. Report conclusions and evidence, not private reasoning transcripts.

```text
Task / constraints:
Observed symptom / candidate cause:
Discriminating check / result:
Chosen change / material alternative rejected:
Expected benefit / cost / preserved contracts:
Visual and behavior evidence:
Unknowns / what would change this decision:
```

For recurring failures, promote a lesson only with the evidence and applicability
conditions described in [evaluation-protocol.md](evaluation-protocol.md).
