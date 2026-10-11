# UI/UX Expert Refinement, 2026-10-12

## Scope And Provenance

The user asked to study the supplied handoff, update the skill, refine beyond
its proposals, and use online research. Work is limited to ui-ux-expert and its
toolkit documentation. No production app, other skill, other chat or paid agent
run is part of this update. Publishing is a separate, user-authorized follow-up.

Input: ui-ux-expert-codex-handoff.zip from Downloads. Its nested baseline matches
the 21-file live skill at the start. Baseline ZIP SHA-256:
`aa9f75cd7d5c8e472383681f8987526dda664551caf73be1f6a007c4e0d3e908`.
The handoff's audit claims were checked against source and a fresh local render;
attached prose was treated as proposals, not higher-priority instructions.
The original archive is preserved. Existing live changes not yet in Git were
retained before refinement; the exported patch compares against that live
baseline, not an older Git version.

## Change Map

| Failure / need | Owner changed | Result and verification |
| --- | --- | --- |
| Table placeholder cells became grid items | assets/component-gallery.html | Restored table-cell layout; measured common row coordinates and increasing column x positions |
| Fixed-height text collided with other content | Gallery card/modal/toast styles | Text-driven sizing and responsive bounds; default/long-copy renders at four widths |
| Invalid button font shorthand | Gallery and references/components.md | Valid longhands; computed weight 600 instead of 400 |
| Faint semantic text / contradictory preferences | tokens.css, gallery | Success chip measured 5.45795:1 instead of 3.10454:1; field names/table headings centered |
| Tokens imported a global reset | tokens.css and assets/gallery-base.css | Tokens now contain custom properties only; gallery base is separate and opt-in |
| Universal style recipes conflicted with brand/context | Token, component, layout, anti-slop, craft and brand references | Role-based defaults and explicit exceptions; no mandatory gallery, single-accent-only rule, or fixed primary-button quota |
| Checklist prose did not establish rendered quality | Core, QA, design judgment | First useful render, observation-to-owner repair, matched evidence, scoped verdicts and regression check |
| Missing contextual composition guidance | references/composition-and-calibration.md | Page/section/control inspection, concrete code-owner hypotheses, same-content domain counterexamples |
| Stale or missing evidence could masquerade as pass | evals/evidence.py and tests | Hash/coverage/state/review/check-result integrity gate with negative tests |
| Evaluation scenarios lacked executable inputs | evals/fixtures, calibration.css, fixture-check.cjs, prepare.py | Three runnable synthetic domains; authored repairs and solver-only packaging kept separate |
| Entry points were long and contradictory | SKILL.md and AGENTS.md | Core 369 -> 173 lines; detailed preferences/reference work routed to dedicated files |

Detailed product-redesign-contracts.md is byte-identical to the baseline.
All explicit alignment preferences and detailed alignment guidance were moved
without dropping content. Existing agent metadata and automatic skill discovery
remain unchanged. No global alias needed a change because the canonical name
and entrypoint remain ui-ux-expert.

## Research Applied

Sources checked on 2026-10-12; links and applicability are recorded in the skill:

- [W3C contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html),
  [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html),
  [target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
  and [reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html): separate
  requirements from comfort defaults and account for actual exceptions.
- [WAI-ARIA dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/):
  static modal styling is not focus containment, background inertness or recovery.
- [Apple browser-engine support](https://developer.apple.com/support/alternative-browser-engines/):
  remove the blanket claim that every iOS browser uses WebKit.
- [GOV.UK validation](https://design-system.service.gov.uk/patterns/validation/)
  and [error summary](https://design-system.service.gov.uk/components/error-summary/):
  distinguish invalid input from service failure and adapt recovery patterns.
- [Carbon data tables](https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines):
  treat density and capabilities as contextual choices.
- [NN/g visual-design principles](https://www.nngroup.com/articles/principles-visual-design/):
  use hierarchy, balance and grouping as diagnostic lenses. The new three-scale
  implementation method is a local synthesis, not an independently validated test.

## Verification Results

### Structural

- Existing scenario validator: eight scenario definitions valid, not eight agent runs.
- Python unit suite: 26 tests pass (11 original, 13 evidence-integrity, 2 packaging).
- Skill-creator validator: valid.
- Toolkit verifier: 138 skills, zero errors; 12 existing warnings in unrelated
  CoverMate external links and the iOS helper executable bit.
- Explicit preference preservation and unchanged product-contract file: checked.
- Baseline/candidate solver preparation CLI: exercised; output excludes reviewer
  pack, authored solution CSS and eval tooling. Filesystem isolation is NOT
  supplied by merely creating separate folders.
- The first full verifier run after workspace preparation found links to excluded
  evaluation files in solver copies. The preparation tool now converts only those
  links to explicit omission notes; regression tests cover this and the verifier
  passes. Rubrics/solutions were not restored to solver inputs.

### Rendered Gallery

Chrome 155.0.8059.39 on this Mac, Playwright, local file URL, DPR 1, en-US,
Asia/Bangkok, reduced motion. Default and synthetic long-copy states at
1280x800, 768x1024, 390x844 and 320x800.

- 56 targeted assertions across eight viewport/state combinations pass.
- Baseline reproduced table geometry, font weight, alignment, text overflow and
  success contrast defects. At 320px, document width was 352px; final is 320px.
- Final run produced 32 PNGs, including full-page context and section crops.
- Personally inspected targeted labels/modal/table/toast/card images plus
  broader context. Not every saved image was individually reviewed at full scale.
- Five inspected contextual captures have a passing evidence-integrity manifest.
  This is a focused gate smoke test, not an independent whole-product audit.
  Final PNG bytes match the reviewed images after a whitespace-only token cleanup.

Long-copy injection deliberately uses identical synthetic stress strings across
some specimens; it is a geometry test, not approved status microcopy.
The gallery is mostly inert and is explicitly not a production widget library.

### Synthetic Behavior And Calibration

Three domains at 1280, 390 and 320 CSS px: nine test combinations pass; eleven
final captures include narrow-table end-scroll states. Executed checks cover
filtering, retained query, action feedback, native form input retention,
invalid-email explanation/focus, horizontal keyboard scrolling and last-action
reachability, text geometry, editorial measure and nonblank bitmap rendering.

The CSS repairs are author-written demonstrations with the same source content,
not independent agent outputs. A narrow table intentionally uses horizontal
scroll: offscreen columns/actions are reachable, but cross-column context is a
tradeoff, not a universally ideal phone layout. The editorial diagram is a
synthetic authored bitmap, not a photograph or real map.

### Not Run / Not Established

- Baseline-versus-candidate agent trials, blind human preference, user task
  timing, conversion or generalized design-quality improvement: NOT RUN.
- Real Safari/iOS picker/keyboard, Firefox, screen reader and full WCAG audit:
  NOT RUN. Chromium viewport emulation is not those platforms.
- Production dialog/menu/tab behavior and backend persistence: not claimed.
- Five of the eight broader scenario setups still require their own fixtures;
  the three new fixtures only cover the stated narrow tasks.

## Reproduction And Artifacts

Use [the evaluation protocol](../skills/ui-ux-expert/references/evaluation-protocol.md)
for commands, prerequisites, matrix schema and baseline/candidate isolation.
No server is needed for the standalone HTML. Bundled Node/Playwright and installed
Chrome were used; no browser/package installation or API spend was needed.

Generated local artifacts live under
`exports/ui-ux-expert-update-2026-10-12/`. The original export remains separate.
The final delivery set contains the updated skill ZIP, baseline-relative patch,
this report, source manifest, final gallery/fixture evidence and labeled comparison.
Partial debug captures and intermediate renders are not included in the delivery
archive. Treat screenshots/exports as local evidence, not mandatory runtime files.

The live skill was selectively synced and is byte-identical to the tested repo
copy. Before sync, live was verified unchanged against the saved baseline. The
evidence gate also passed against the installed live sources. Future syncs must
reconcile concurrent changes rather than overwrite them. Unrelated .DS_Store/
export files and other skills were preserved. No commit or push was performed
during the refinement pass; the user subsequently requested publishing.
