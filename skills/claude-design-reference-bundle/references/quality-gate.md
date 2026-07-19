# Quality Gate

Before finalizing a Claude Design reference bundle, verify:

## Evidence

- Rendered the target surface in a real browser.
- Captured desktop and mobile, unless the user scoped one viewport.
- Captured all user-mentioned states.
- Recorded user-supplied screenshots/files in `MANIFEST.md`.
- Stored screenshots using stable relative paths under `screenshots/`.

## Consistency

- `MANIFEST.md`, `REFERENCE-STATES.md`, and screenshots describe the same route/state.
- `DESIGN-SPEC.md` uses the real product counts and copy unless an exception is documented.
- `IMPLEMENTATION-CONTRACT.md` lists preserved behavior and known exceptions.
- `CLAUDE-DESIGN-PROMPT.md` references every required attachment and constraint.

## Visual Coverage

- Header/nav, hero/title, primary controls, repeated cards/lists, floating/sticky UI, modal/drawer if relevant, and footer are covered.
- Desktop and mobile layout differences are explicit.
- High-risk geometry includes measured width/height/gap/font values.
- Important assets and placeholder/fallback behavior are named.

## Product Protection

- No route, data contract, search/filter, load-more, modal, permission, privacy, or responsive behavior is silently changed in the spec.
- Mock-only differences are labeled as behavior or visual exceptions.
- Unknowns are marked as unknowns, not invented as requirements.

## Final Report

In the closeout, report:

- output directory
- screenshots produced
- Markdown files produced
- source URL/file
- viewports and states covered
- validation performed
- remaining exceptions or gaps
