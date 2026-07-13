---
name: notenwert-design-direction
description: Use when designing, redesigning, critiquing, or briefing Notenwert visual direction, Claude Design prompts, homepage hero motion, NGA-style sticky/scrub interactions, public site UX, admin CMS UX, typography, color, imagery, or responsive behavior.
---

# Notenwert Design Direction

Use `$design-direction` for reusable design-brief, critique, and implementation
guardrail workflow. This skill is the Notenwert overlay: brand/product facts,
specific design references, and local maintainer handoff.

Use this skill for Notenwert design work. It is not for generic frontend coding;
it is for preserving the product/design intent while evolving the site.

## Project Root

```text
/Users/point/Library/Mobile Documents/com~apple~CloudDocs/Website Projects/notenwert
```

## Required Reading

Read only what the task needs:

- For full redesign or Claude Design handoff: `docs/design-brief-for-claude.md`.
- For homepage hero / sticky scroll / card rail: `docs/design-reference/nga-banner-system.md`.
- For source map before implementation: `docs/codebase-map.md`.
- For CMS data constraints: `docs/content-model.md`.
- For current working rules: `AGENTS.md`.

Screenshots for the NGA reference live in:

```text
docs/design-reference/screenshots/
```

Use adjacent skills when the task moves beyond direction:

- `$design-direction` for the global design direction framework.
- `$notenwert-maintainer` for implementation, tests, build, docs work-log, or
  commit/deploy prep.
- `$claude-to-a-tee` for exact Claude HTML parity.
- `$mobile-web-qa` and `$snapshot` for responsive visual proof.
- `$placeholder-image` for sourcing/cropping real imagery.
- `$docs-cartographer` for durable design or architecture documentation.

## Design North Star

Notenwert is a bilingual Dresden cultural network. It should feel like:

- a cultural publication
- a museum network guide
- a refined civic platform
- editorial, warm, European, musical, and institutionally credible

It should not feel like:

- a generic SaaS landing page
- a stock-photo marketing site
- a decorative gradient/orb UI
- a grid of identical promotional cards

## Signature Interaction

The homepage hero is the identity-defining interaction:

- sticky editorial banner stack
- scrub-scroll / card-peel / curtain-from-below behavior
- about `200vh` of scroll runway per banner
- right rail of pinned editorial cards
- subtle banner/chapter dot sync
- image/video banners with poster fallback
- reduced-motion readable fallback
- phone layout simplifies into a normal readable stack

Preserve the idea even if the visual treatment changes. Do not replace it with a
plain hero + card grid unless the user explicitly asks.

## Public Site Principles

- Use real cultural imagery where possible.
- Make the first viewport immediately feel like Notenwert.
- Keep typography editorial and refined.
- Keep navigation usable in English and German.
- Treat Dresden Life like a cultural magazine.
- Treat venues as discoverable cultural places, with map support but not map
  domination.
- Association pages should build trust, mission, values, and people.
- Instagram should feel integrated into the Notenwert system, not pasted in.

## Admin CMS Principles

Admin design should be quiet, dense, and reliable:

- clear sidebar navigation
- compact editing controls
- bilingual fields that are hard to confuse
- visible draft / preview / publish state
- safe modal editing
- practical image upload, crop, import, and marker states
- dashboard health, revision, subscriber, analytics, and content summaries

Avoid marketing-style admin screens or oversized decorative cards.

## Visual Guardrails

- Use restrained radii.
- Avoid one-note palettes.
- Avoid default purple/blue gradient language.
- Dresden yellow can be a strong accent, not the whole palette.
- German text can be longer; test wrapping.
- Text must not clip inside cards, buttons, nav, or panels.
- Mobile must not overflow horizontally.

## When Implementing Designs

Follow Notenwert maintainer rules:

- edit source in `src/`
- run `node build.js` after source changes
- add/update focused regression tests for behavior changes
- use browser verification for visual work when a dev server is involved
- update `docs/codex-work-log.md` after meaningful work

## Brief / Critique Output

For design-only work, report:

- design intent and audience;
- references/docs inspected;
- recommended visual direction;
- responsive/admin/public-site implications;
- implementation risks or required maintainer follow-up;
- assets/images/screenshots needed.
