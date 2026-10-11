# External Design Learning Brief

The legacy filename is retained for existing links. Use this brief with Claude
Design or any design reviewer. The twelve topics below now have specialist
coverage; they are not twelve missing skills. Ask for concrete counterexamples,
critique, and evidence that improves the existing guidance rather than another
generic manual.

## Current Strength

`ui-ux-expert` is useful as an operating discipline:

- it instructs the agent to diagnose generic visual output in context;
- it prioritizes system-first design;
- it routes to component, layout, responsive, token, and QA references;
- it requires rendered visual evidence through `$snapshot`;
- it keeps brand/production UI above generic defaults.
- it now includes cause-directed diagnosis, explicit tradeoffs, contextual rules,
  selective alternatives, and a matched evaluation protocol with eight synthetic
  scenarios, three runnable synthetic fixtures, authored same-content calibration
  repairs, and negative evidence-integrity tests. These are tools and examples,
  not measured agent A/B improvement or independent human review.

It is not yet equivalent to a senior product designer's trained eye. It lacks a
large library of nuanced, domain-specific examples and critique patterns.

## Existing Coverage To Challenge

1. **Visual diagnosis vocabulary**
   - Existing: `$visual-diagnosis`. Challenge its symptom-to-cause reasoning for
     cheap, heavy, cramped, scattered, generic, or low-trust screens.
   - Need: a taxonomy with concrete image examples and repair moves.

2. **Domain-specific design taste**
   - Existing: `$domain-taste`. Challenge category defaults with real admin,
     editorial, learning, ledger, and mobile counterexamples.
   - Need: before/after examples per domain and "do not use this pattern here"
     rules.

3. **Information architecture and screen strategy**
   - Existing: `$information-architecture-ux`. Challenge navigation/grouping
     choices and the cost of alternatives for complex tasks.
   - Need: IA heuristics, route/screen decision trees, and examples.

4. **Advanced interaction design**
   - Existing: `$interaction-design`. Challenge multi-step, autosave, bulk,
     permission, optimistic-update, and interruption-recovery tradeoffs.
   - Need: interaction pattern library with state diagrams.

5. **Mobile-native product feel**
   - Existing: `$mobile-native-feel`. Test actual platform behavior rather than
     assuming responsive web evidence establishes native feel.
   - Need: iOS/Android screen patterns, safe areas, gestures, sheets, tab
     behavior, input ergonomics, and visual density examples.

6. **Design-system architecture**
   - Existing: `$design-system-architect`. Challenge component boundaries,
     token layering, themes, and split/merge decisions with real consumers.
   - Need: design-system audit rubrics and component inventory templates.

7. **Art direction and imagery**
   - Existing: `$art-direction-imagery`. Challenge crops, image sequence,
     editorial rhythm, and brand fit with actual image pairs.
   - Need: image critique examples and crop decision rules.

8. **Typography refinement**
   - Existing: `$typography-refinement`. Test Thai/mixed-script rendering,
     dense numbers, long text, and medium-specific reading conditions.
   - Need: type pairing critiques, hierarchy ladders, and real screenshots.

9. **Motion choreography**
   - Existing: `$motion-choreography`. Challenge transition intent, interruption,
     and reduced-motion equivalents with recorded behavior, not still images.
   - Need: motion specs and examples that explain intent.

10. **Accessibility beyond the floor**
    - Existing: `$accessibility-beyond-basics`. Test assistive flows, complex
      widgets, low vision, and data visualization with appropriate tools/users.
    - Need: advanced accessibility critique and acceptance examples.

11. **Evidence-based design critique**
    - Existing: `$reference-implementation-critique` and `$reference-to-a-tee`.
      Challenge geometry, hierarchy, and inferred behavior with calibrated pairs.
    - Need: screenshot annotation examples and scoring rubrics.

12. **Taste calibration library**
    - Existing: `$taste-calibration` has textual specimens. A broad, permissioned
      image library with independent review and counterexamples is still missing.
    - Need: curated examples with why each works, where it fails, and what rules
      Codex should infer.

## Prompt To Ask Claude Design

```markdown
I have a Codex skill called `ui-ux-expert`. It already enforces system-first UI,
anti-slop rules, responsive checks, component/state coverage, accessibility
basics, and screenshot evidence. It also routes to specialists for the twelve
topics below and now has diagnosis, tradeoff, contextual-rule, alternative-choice,
and evaluation guidance. Do not assume those topics are absent.

Please critique the supplied guidance and artifacts as a design reviewer. Focus
on incorrect assumptions, competing explanations, counterexamples, and missing
evidence when judging screenshots or implementing references. Mark anything you
cannot verify; do not claim access to hidden methods or invent test results.

For each topic below, provide:
- the principle;
- what bad AI output looks like;
- what good product design looks like;
- a concrete before/after example;
- implementation-level rules Codex can follow;
- screenshot QA checks Codex can run;
- when the rule should be overridden.
- how to test the proposed improvement and what would disprove the diagnosis.

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
