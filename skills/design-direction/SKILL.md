---
name: design-direction
description: Define, critique, or preserve product visual direction across projects. Use when the user asks what a product should feel like, wants a redesign strategy, visual north star, brand/product UX principles, public-site vs admin direction, typography/color/imagery guardrails, Claude Design prompts, design critique, or implementation handoff guidance before building UI.
---

# Design Direction

Use this skill when the work needs a coherent product/design point of view before
implementation. Project-specific design skills should add brand facts,
references, and local constraints.

## Inputs To Find

Read only what the task needs:

- product purpose, audience, positioning, and current user goal;
- existing design briefs, screenshots, prototypes, Claude/Figma handoffs, brand
  assets, copy tone, and competitor/reference examples;
- current UI implementation, design system primitives, typography, colors,
  imagery, motion, responsive behavior, and admin/public surfaces;
- operational constraints: CMS, data shape, localization, accessibility, mobile,
  performance, and release requirements.

Use `$ui-ux-orchestrator` when the UI/UX task is broad or the right specialist
skill is unclear. Use `$reference-to-a-tee` for exact offline Claude parity,
`$consistency-audit` for site-wide coherence against requirements or inferred
patterns, `$design-system-guardian` for component/token consistency,
`$product-ux-contracts` for preserving proven product behavior,
`$ui-state-matrix` for state coverage, `$interaction-flow-qa` for journeys,
`$placeholder-image` for image sourcing/crop choices, `$mobile-web-qa` and
`$snapshot` for visual proof, and project maintainer skills before
implementation.

Use `$snapshot` automatically before the final response whenever design
direction work includes a live/renderable UI, supplied visual reference,
screenshot comparison, concrete visual audit, implementation guidance tied to a
specific surface, or completed UI change. Do not wait for the user to ask. If no
new snapshot can be captured, state which supplied artifacts were used and what
visual risk remains.

Use `$efficient-execution` when direction work is broad: inspect enough
references to define the decision, then stop before it becomes a full redesign
audit. Escalate only when the user asks for architecture, Claude parity,
responsive verification, or implementation.

## Direction Frame

Produce or preserve:

- **identity:** what the product should feel like and what it must not feel like;
- **hierarchy:** what the first viewport or primary workflow must communicate;
- **interaction language:** navigation, motion, sticky/scrub, modals, forms,
  admin density, and feedback states;
- **visual system:** typography, color roles, spacing, radii, icons, images,
  cards/lists/tables, and empty/error/loading states;
- **responsive behavior:** what simplifies on phone/tablet and what must remain
  visible;
- **implementation guardrails:** what can change, what must be preserved, and
  which surfaces need tests or visual QA.

## Public vs Admin UX

Public/marketing/editorial surfaces can be expressive, content-led, and
brand-defining. Admin/operations surfaces should be quiet, dense, predictable,
and optimized for repeated work. Do not solve admin UX with oversized marketing
cards, and do not flatten a distinctive public site into generic SaaS UI.

## Critique Checklist

- Does the first viewport signal the product, not just a generic layout?
- Is the visual language tailored to the domain and audience?
- Are typography and spacing appropriate for the container size?
- Do images/assets show the actual product, place, object, state, or use case?
- Does the design handle long labels, localization, empty/error/loading states,
  and mobile constraints?
- Are motion and decorative elements purposeful rather than ornamental noise?
- Are implementation risks and verification gates clear?

## Output

For design-only work, report:

```text
Design intent:
Audience / domain:
References inspected:
North star:
Do / do not:
Responsive implications:
Admin/public implications:
Implementation guardrails:
Assets or screenshots needed:
Follow-on skills:
```

When the user asks to implement, hand off to the appropriate maintainer skill
after the direction is clear.

## Handoff Prompt Guidance

When preparing a design prompt or handoff for another design agent, request
artifacts that implementation agents can verify rather than mood alone:

- standalone HTML or a runnable prototype for every referenced screen;
- wide screenshots at desktop, tablet, and mobile with route/state labels;
- component inventory, item counts, responsive rules, and visible interactions;
- source-of-truth notes for what is presentation-only versus product-owned data,
  auth, routing, persistence, and operations;
- mock/unbuilt list for controls, dashboards, uploads, revisions, roles,
  scheduling, or backend-dependent features;
- asset brief and licensing/source expectations for images, video, and embeds;
- explicit behavior exceptions and visual exceptions.

Use `$reference-to-a-tee` for exact implementation from such a handoff and
`$admin-prototype-reconciliation` when the handoff changes admin/data contracts.
