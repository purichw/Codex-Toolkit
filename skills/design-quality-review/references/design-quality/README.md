# Design Quality Guide (for engineers)

A working manual for developers who implement UI from screenshots, prototypes, and design
references. It exists to make design judgement **inspectable**: every claim here is either
something you can measure in a screenshot or something explicitly marked as a product decision.

This is not a style guide and not a component library. It is a set of diagnostic vocabulary,
observable checks, and implementation rules you can cite in a pull request.

## Who this is for

- Engineers implementing a design that already exists (Figma, screenshot, live reference).
- Engineers building UI with no designer attached, who need to not produce generic output.
- Reviewers doing screenshot-based design QA on someone else's PR.

## How to use it

| Situation | Read |
| --- | --- |
| "This looks off and I can't say why." | [01 · Visual diagnosis](01-visual-diagnosis.md) |
| Starting a screen in an unfamiliar product type | [02 · Domain taste](02-domain-taste.md) |
| Given a feature, not a design | [03 · IA & screen strategy](03-information-architecture.md) |
| Building flows, bulk actions, destructive actions | [04 · Interaction design](04-interaction-design.md) |
| Shipping to iOS/Android (native or web) | [05 · Mobile-native feel](05-mobile-native-feel.md) |
| Adding/changing shared components | [06 · Design systems](06-design-systems.md) |
| Any screen with photography or placeholders | [07 · Art direction & imagery](07-art-direction-imagery.md) |
| Tables, dashboards, prose, non-Latin text | [08 · Typography refinement](08-typography.md) |
| Anything that moves | [09 · Motion](09-motion.md) |
| Beyond contrast + alt text | [10 · Accessibility beyond basics](10-accessibility.md) |
| Comparing your build to a reference | [11 · Reference-vs-implementation critique](11-reference-critique.md) |
| Calibrating your own taste | [12 · Taste calibration library](12-taste-calibration.md) |
| Running the review / writing the notes | [A · Screenshot QA protocol](appendix-a-screenshot-qa-protocol.md) · [B · Implementation notes & checklists](appendix-b-notes-and-checklists.md) |

**Read [00 · Conventions](00-conventions.md) first.** It defines the notation (`[FACT]`, `[PD]`,
rule IDs, severities) that the rest of the files depend on.

## File map

Each file is self-contained and uses the same six sections, so any file can be lifted into a
team wiki, a CONTRIBUTING appendix, or an agent's context window without the others.

```
design-quality/
  README.md                                 this index
  00-conventions.md                         notation, severities, how to cite a rule
  01-visual-diagnosis.md                    cheap / cramped / scattered / generic / heavy / low-trust / unfinished
  02-domain-taste.md                        admin, SaaS ops, editorial, learning, dashboards, ledgers, landing, mobile
  03-information-architecture.md            navigation, grouping, hierarchy, sequencing, progressive disclosure
  04-interaction-design.md                  multi-step, undo, autosave, bulk, permissions, optimistic, recovery, destructive
  05-mobile-native-feel.md                  platform patterns, safe areas, gestures, sheets, tabs, inputs, density
  06-design-systems.md                      taxonomy, variants, token layers, theming, naming, drift
  07-art-direction-imagery.md               crops, rhythm, placeholders, asset selection
  08-typography.md                          multilingual, dense data, numerics, editorial rhythm
  09-motion.md                              choreography, drawers, tabs, scroll, feedback, reduced motion
  10-accessibility.md                       SR flow, cognitive load, low vision, complex widgets, data viz
  11-reference-critique.md                  geometry, rhythm, hierarchy, density, weight, affordance, states
  12-taste-calibration.md                   paired good/bad specimens by category
  appendix-a-screenshot-qa-protocol.md      capture setup, the 25-item pass, PR review template
  appendix-b-notes-and-checklists.md        design-intent notes, ticket template, definition of done
```

## The three habits this guide is trying to install

1. **Name the defect before fixing it.** "Cramped" and "scattered" have different causes and
   different fixes. Guessing produces churn.
2. **Separate what you can see from what you must ask.** A 2px misalignment is a fact. Whether
   a delete needs a confirm dialog is a product decision. Never resolve the second by taste.
3. **Review your own screenshots.** Almost every defect in this guide is visible in a static
   capture at 100% zoom. Looking at the screen while your hand is on the mouse is not review.
