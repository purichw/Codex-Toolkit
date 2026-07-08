---
name: regression-hunter
description: Search a repository for repeated bug patterns, stale hardcoded values, fragile selectors, duplicated logic, and nearby regressions after one issue is found. Use when the user asks to audit for similar problems, check other places, find weird hardcoded placeholders, make sure the same bug is not elsewhere, or investigate brittle behavior across a codebase.
---

# Regression Hunter

Treat one bug as a clue. Look for the family of failures, then fix or report the
pattern without wandering into unrelated refactors.

## Frame The Pattern

1. Restate the concrete bug and the invariant it violates.
2. Identify likely pattern classes: hardcoded user data, stale copy, duplicated
   calculation, selector dependency, unchecked auth, broken responsive state,
   unsafe async flow, inconsistent rounding, asset substitution, or missing
   validation.
3. Search with `rg` before opening many files. Include strings, selectors,
   function names, constants, route names, data fields, and test names.

## Audit Nearby Risk

- Compare all implementations of the same behavior.
- Check tests, fixtures, mock data, seed data, stories, demos, and generated
  docs for stale assumptions.
- Inspect event delegation, IDs, class names, data attributes, and DOM hierarchy
  before changing selectors.
- For logic bugs, build a small truth table or worked example and verify edge
  cases around rounding, empty data, duplicates, permissions, and persistence.
- For UI bugs, verify responsive states and dynamic content that could recreate
  the issue.

## Fix Strategy

- Prefer one canonical helper or invariant check when duplication caused the
  regression.
- Keep cosmetic cleanup separate from behavior fixes unless the bug requires
  both.
- Add focused regression tests when a future break would be silent.
- Do not mass-rewrite files just because a pattern search found harmless
  mentions.

## Report

List patterns searched, files changed, files intentionally left alone, tests
added or run, and residual risk. If no broader issue is found, say that clearly
and include the searches that support it.
