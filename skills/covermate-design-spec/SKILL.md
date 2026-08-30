---
name: covermate-design-spec
description: Maintain, update, audit, snapshot, or hand off the CoverMate website and admin designs against the current production product spec. Use when working on CoverMate public visitor pages, admin login, Admin Portal shell, owner editor/control-panel routes, analytics surfaces, design handoffs, reference reconciliation, responsive/UI polish, production snapshot suites, Firestore CMS content behavior, SEO/analytics design implications, or any task that must preserve CoverMate product decisions.
---

# CoverMate Design Spec

## Overview

Use this skill to keep CoverMate website and admin design work aligned with the real production product, not older offline/reference exports. It packages the current full design spec and the workflow for reconciling new references with the existing implementation.

## Required Reference

For substantive design, implementation, or handoff work, read:

- `references/current-design-spec.md`

If the repository file exists at `/Users/point/CoverMate/docs/covermate-website-full-design-spec.md`, prefer that file as the newest source and use this bundled reference as a fallback snapshot. If they differ, the repository doc wins unless the user explicitly says otherwise.

For production snapshots, visual archives, release evidence, or design handoffs that need current screenshots, also read:

- `references/snapshot-suite.md`

## Workflow

1. Establish the task surface: public home, dedicated `/motor` page, `/#motor` legacy alias, admin login, Admin Portal shell, owner edit mode, owner control panel, or admin analytics.
2. Read the current design spec before changing design-sensitive behavior, copy, layout, nav, admin flows, analytics, SEO, or dynamic CMS assumptions.
3. Reconcile any new screenshot/spec/reference against the current product decisions. The newest explicit user request wins, but preserve existing CoverMate decisions unless the user intentionally changes them.
4. Preserve the two current public entry points: `/` is the full home page, and `/motor` is the dedicated motor-insurance campaign page in the same product. `/#motor` remains only a legacy home-page alias to `#insurers`.
5. Preserve the Admin Portal after login as the unified private shell for `Operations`, `Website content`, `Analytics`, and `Settings`. Website content uses one editor entry; do not reintroduce a separate `Arrange & customise` launcher card.
6. Preserve English admin chrome labels such as `Main`, `Public site`, `Log out`, `Panel`, `Edit text`, `Save draft`, `Preview`, `Publish`, and `Success`.
7. Preserve Google Sans family usage across Thai and English visitor/admin text.
8. Treat Firestore live content as canonical. Local fallback/cache must not override successfully loaded live content.
9. Capture or inspect snapshots before finishing when the task affects UI. Use ad-hoc snapshots only for narrow proof. Use the complete production snapshot suite for full-site, release, or design handoff evidence.
10. Do not commit, push, or deploy unless the user explicitly asks in the current turn.

## Snapshot Discipline

- Never call a partial viewport set a "full production snapshot" or "complete evidence".
- Label ad-hoc `/tmp` screenshots as narrow evidence with route, viewport, auth state, and whether `fullPage` was used.
- For complete evidence, capture the matrix in `references/snapshot-suite.md`, use matched viewport sets, wait for fonts/hydration/data to settle, and write a manifest with provenance.
- Use `fullPage: true` for long page archives. Use viewport crops only for specific anchor, drawer, form, or interaction states.
- Keep signed-out, signed-in, owner-hash, TH/EN, desktop/tablet/mobile, and data-state captures separate instead of mixing them as if they were comparable.
- If any required surface cannot be captured, state exactly which surface is missing and why.

## Must-Preserve Product Decisions

- The home visitor navbar shows one motor item only: Thai `ประกันรถยนต์`, English `Motor`, pointing to `#insurers`. The `/motor` page may use a local motor-page navbar with a `Home` link.
- No `[object Object]` labels may appear in nav or UI.
- `/#motor-focus` is legacy/unexposed compatibility only; `/motor` is the current dedicated motor page.
- Home keeps the expanded public-section contract: hero, trust, embedded cover accordions, review, fit, how, insurers, tiers, claim, renew, guides, voices, about, faq, fees, privacy, and talk. `/motor` keeps its dedicated section order: motor, motor-trust, motor-cover, insurers, tiers, how, claim, renew, guides, faq, and talk.
- The AIA logo uses the transparent red asset at `assets/logos/aia-logo.png`.
- Contact heading Thai `ขอรับคำปรึกษา` should fit as one line on desktop.
- Admin analytics remains a private admin module and route.
- GA4 measurement ID is `G-5TF3C235EF`; public analytics must not receive visitor names, phone numbers, LINE IDs, or freeform messages.
- Admin routes are private and `noindex`.

## When Producing A Design Handoff

Include:

- Source-of-truth precedence.
- The current route/surface map.
- Visitor section order and component map.
- Admin surface map, including login, Admin Portal shell, website content editor/control panel, analytics, operations, and settings.
- Typography, color, spacing, responsive, accessibility, assets, SEO, analytics, and Firestore CMS guardrails.
- Explicit acceptance checklist and `do not touch` constraints.
- Snapshot evidence paths when available.

Keep the handoff implementation-ready and clear about what is FACT, what is an inference from current code, and what is a recommendation.
