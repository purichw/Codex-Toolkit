# Claude Design Learning Brief

This file lists what `ui-ux-expert` still does not know deeply enough. Use it to
ask Claude Design or another design specialist for lessons, critique rubrics,
examples, and before/after artifacts that can become future references.

## Current Strength

`ui-ux-expert` is useful as an operating discipline:

- it prevents generic AI visual habits;
- it forces system-first design;
- it routes to component, layout, responsive, token, and QA references;
- it requires rendered visual evidence through `$snapshot`;
- it keeps brand/production UI above generic defaults.

It is not yet equivalent to a senior product designer's trained eye. It lacks a
large library of nuanced, domain-specific examples and critique patterns.

## Gaps To Ask Claude Design About

1. **Visual diagnosis vocabulary**
   - How to name why a screen feels cheap, heavy, cramped, scattered, generic,
     or low-trust from screenshots.
   - Need: a taxonomy with concrete image examples and repair moves.

2. **Domain-specific design taste**
   - Admin/CMS, SaaS ops, editorial/cultural sites, education apps, finance
     ledgers, mobile learning, dashboards, and landing pages need different
     density, hierarchy, rhythm, and copy.
   - Need: before/after examples per domain and "do not use this pattern here"
     rules.

3. **Information architecture and screen strategy**
   - The skill can polish a screen, but it needs better guidance on choosing
     navigation structure, content grouping, page sequencing, and progressive
     disclosure for complex products.
   - Need: IA heuristics, route/screen decision trees, and examples.

4. **Advanced interaction design**
   - Better patterns for multi-step flows, undo/redo, autosave, bulk actions,
     permissions, collaborative state, optimistic updates, and interruption
     recovery.
   - Need: interaction pattern library with state diagrams.

5. **Mobile-native product feel**
   - The current guidance handles responsive web better than native iOS/Android
     feel.
   - Need: iOS/Android screen patterns, safe areas, gestures, sheets, tab
     behavior, input ergonomics, and visual density examples.

6. **Design-system architecture**
   - The skill says "use a system" but needs stronger guidance on component
     taxonomy, variant naming, token layering, theming, and when to split or
     merge components.
   - Need: design-system audit rubrics and component inventory templates.

7. **Art direction and imagery**
   - The skill avoids bad placeholders, but does not deeply teach photo
     direction, crop strategy, editorial image rhythm, illustration style, or
     asset selection by brand mood.
   - Need: image critique examples and crop decision rules.

8. **Typography refinement**
   - The skill has safe defaults, but needs better advanced guidance for
     editorial rhythm, multilingual text, dense tables, numerical dashboards,
     slides, and mixed script systems.
   - Need: type pairing critiques, hierarchy ladders, and real screenshots.

9. **Motion choreography**
   - The skill has duration/easing basics, but not detailed choreography for
     complex transitions, scroll narratives, page changes, drawers, tabs, and
     reduced-motion equivalents.
   - Need: motion specs and examples that explain intent.

10. **Accessibility beyond the floor**
    - Current guidance covers basics. It needs stronger patterns for screen
      reader flows, cognitive load, error prevention, low vision, localization,
      complex widgets, and accessible data visualization.
    - Need: advanced accessibility critique and acceptance examples.

11. **Evidence-based design critique**
    - The skill needs a better rubric for comparing reference vs implementation
      beyond "looks close": geometry, rhythm, hierarchy, density, visual weight,
      and interaction affordance.
    - Need: screenshot annotation examples and scoring rubrics.

12. **Taste calibration library**
    - The skill lacks a broad set of excellent and poor examples across product
      categories.
    - Need: curated examples with why each works, where it fails, and what rules
      Codex should infer.

## Prompt To Ask Claude Design

```markdown
I have a Codex skill called `ui-ux-expert`. It already enforces system-first UI,
anti-slop rules, responsive checks, component/state coverage, accessibility
basics, and screenshot evidence.

Please teach it like a senior product designer would. Focus on what an AI coding
agent usually misses when judging UI from screenshots or implementing from a
design reference.

For each topic below, provide:
- the principle;
- what bad AI output looks like;
- what good product design looks like;
- a concrete before/after example;
- implementation-level rules Codex can follow;
- screenshot QA checks Codex can run;
- when the rule should be overridden.

Topics:
1. visual diagnosis vocabulary;
2. domain-specific design taste for admin/CMS, SaaS ops, editorial/cultural,
   learning apps, ledgers/finance, dashboards, and landing pages;
3. information architecture and screen strategy;
4. advanced interaction design and multi-step flows;
5. native iOS/Android product feel;
6. design-system architecture and component taxonomy;
7. art direction, imagery, and crop strategy;
8. typography refinement, including multilingual and dense data;
9. motion choreography and reduced-motion equivalents;
10. accessibility beyond the floor;
11. reference-vs-implementation screenshot critique;
12. a taste calibration library of good/bad examples.

Please format the answer as implementation-ready Markdown that can be split into
Codex skill reference files. Avoid generic advice; give concrete heuristics,
rubrics, examples, and acceptance checks.
```
