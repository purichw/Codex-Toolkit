---
name: covermate-design-spec
description: Maintain, update, audit, snapshot, or hand off the CoverMate website and admin designs against the current production product spec. Use when working on CoverMate public visitor pages, admin login/launcher/edit/arrange/analytics surfaces, Claude Design handoffs, design reconciliation, responsive/UI polish, production snapshot suites, Firestore CMS content behavior, SEO/analytics design implications, or any task that must preserve CoverMate product decisions.
---

# CoverMate Design Spec

## Overview

Use this skill to keep CoverMate website and admin design work aligned with the real production product, not older standalone exports. It packages the current full design spec and the workflow for reconciling new references with the existing implementation.

## Required Reference

For substantive design, implementation, or handoff work, read:

- `references/current-design-spec.md`

If the repository file exists at `/Users/point/CoverMate/docs/covermate-website-full-design-spec.md`, prefer that file as the newest source and use this bundled reference as a fallback snapshot. If they differ, the repository doc wins unless the user explicitly says otherwise.

For production snapshots, visual archives, release evidence, or Claude handoffs that need current screenshots, also read:

- `references/snapshot-suite.md`

## Workflow

1. Establish the task surface: public visitor site, `/#motor` alias, admin login, admin launcher, owner edit mode, owner arrange panel, or admin analytics.
2. Read the current design spec before changing design-sensitive behavior, copy, layout, nav, admin flows, analytics, SEO, or dynamic CMS assumptions.
3. Reconcile any new screenshot/spec/reference against the current product decisions. The newest explicit user request wins, but preserve existing CoverMate decisions unless the user intentionally changes them.
4. Keep the public site as one continuous anchor page. `/#motor` is an alias to `#insurers`, not a separate public page.
5. Preserve the admin launcher after login with three primary cards: `Edit the words`, `Arrange & customise`, and `Analytics`.
6. Preserve English admin chrome labels such as `Main`, `Public site`, `Log out`, `Panel`, `Edit text`, `Save draft`, `Preview`, `Publish`, and `Success`.
7. Preserve Google Sans family usage across Thai and English visitor/admin text.
8. Treat Firestore live content as canonical. Local fallback/cache must not override successfully loaded live content.
9. Capture or inspect snapshots before finishing when the task affects UI. Use ad-hoc snapshots only for narrow proof. Use the complete production snapshot suite for full-site, release, or Claude handoff evidence.
10. Do not commit, push, or deploy unless the user explicitly asks in the current turn.

## Snapshot Discipline

- Never call a partial viewport set a "full production snapshot" or "complete evidence".
- Label ad-hoc `/tmp` screenshots as narrow evidence with route, viewport, auth state, and whether `fullPage` was used.
- For complete evidence, capture the matrix in `references/snapshot-suite.md`, use matched viewport sets, wait for fonts/hydration/data to settle, and write a manifest with provenance.
- Use `fullPage: true` for long page archives. Use viewport crops only for specific anchor, drawer, form, or interaction states.
- Keep signed-out, signed-in, owner-hash, TH/EN, desktop/tablet/mobile, and data-state captures separate instead of mixing them as if they were comparable.
- If any required surface cannot be captured, state exactly which surface is missing and why.

## Must-Preserve Product Decisions

- The visitor navbar shows one motor item only: Thai `ประกันรถยนต์`, English `Motor`, pointing to `#insurers`.
- No `[object Object]` labels may appear in nav or UI.
- The hidden focused motor variant remains hidden unless explicitly requested.
- All 16 public sections remain part of the design contract: hero, trust, cover, review, fit, how, insurers, claim, renew, guides, voices, about, faq, fees, privacy, and talk.
- The AIA logo uses the transparent red asset at `assets/logos/aia-logo.png`.
- Contact heading Thai `ขอรับคำปรึกษา` should fit as one line on desktop.
- Admin analytics remains the third admin launcher card and a private admin route.
- GA4 measurement ID is `G-5TF3C235EF`; public analytics must not receive visitor names, phone numbers, LINE IDs, or freeform messages.
- Admin routes are private and `noindex`.

## When Producing A Claude Handoff

Include:

- Source-of-truth precedence.
- The current route/surface map.
- Visitor section order and component map.
- Admin surface map, including login, launcher, edit, arrange, and analytics.
- Typography, color, spacing, responsive, accessibility, assets, SEO, analytics, and Firestore CMS guardrails.
- Explicit acceptance checklist and `do not touch` constraints.
- Snapshot evidence paths when available.

Keep the handoff implementation-ready and clear about what is FACT, what is an inference from current code, and what is a recommendation.
