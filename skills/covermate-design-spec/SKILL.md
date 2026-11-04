---
name: covermate-design-spec
description: Maintain, implement, audit, or hand off CoverMate design contracts. Use for public pages, Articles, Customers/Cases, Admin/CMS, responsive polish, reference reconciliation, visual evidence, or the standalone motor poster and selected-page exports. Preserves current product owners and distinguishes local source, historical snapshots, CMS publication and deployment.
---

# CoverMate Design Spec

## Overview

Keep CoverMate design work aligned with current product owners and explicitly
approved references, without reviving obsolete exports or treating source as
deployed. The website/Admin system and standalone print poster are distinct
approved visual directions; neither automatically restyles the other.

## Required Reference

For substantive website/Admin design, implementation, or handoff work, read:

- `references/current-design-spec.md`

Prefer `docs/covermate-website-full-design-spec.md` in the active CoverMate
checkout. The primary repository is `/Users/point/CoverMate`, but an already
selected task checkout takes precedence. Use the bundled reference only as a
fallback snapshot. The active repository doc wins unless the user says otherwise.
Resolve primary-repository links in that snapshot against the active checkout
when working in a task checkout; do not switch to older primary-checkout docs.

For standalone poster work, start with `exports/poster-v36/README.md` and its
source fragments. Do not require reading the whole website spec or building the
website for a print-only change. Read `docs/ARTIFACT_RETENTION.md` for any cleanup.

For production snapshots, visual archives, release evidence, or design handoffs that need current screenshots, also read:

- `references/snapshot-suite.md`

## Workflow

1. Establish the task surface: public Home/service/Articles, private Admin/Customers/Cases/editor, or standalone poster. Read the relevant owner rather than applying every workflow to all surfaces.
2. Read the current design spec before changing design-sensitive behavior, copy, layout, nav, admin flows, analytics, SEO, or dynamic CMS assumptions.
3. Reconcile any new screenshot/spec/reference against the current product decisions. The newest explicit user request wins, but preserve existing CoverMate decisions unless the user intentionally changes them.
4. Preserve public routes under `docs/SITE_MAP.md`, including `/motor` and publication-gated Articles. `/#motor` is the Home anchor into the unchanged `insurers` DOM/CMS section; old `/#insurers` URLs normalize to it.
5. Preserve the unified private Admin shell: Home, Operations/Cases, Customers, Website content, Articles and Analytics, with existing role gates. Settings/Role Preview are retired; account controls live in the shared account menu. The three Home shortcut cards are not the full module inventory. Website content and Articles have distinct editors and publication boundaries.
6. Preserve natural Thai Admin controls with conventional English terms such as `Save draft`, `Preview`, `Publish`, `Undo` and `Redo`; follow `docs/ADMIN_LANGUAGE.md`. Public TH/EN content switching must not translate Admin controls or overwrite the other content language.
7. Preserve Google Sans family usage across Thai and English visitor/admin text.
8. Treat Firestore live content as canonical. Local fallback/cache must not override successfully loaded live content.
9. Capture and personally inspect rendered screenshots before finishing UI work. Choose evidence by touched risk; a release does not automatically require a complete archive. Use the full snapshot suite when a full-site archive/handoff is requested. Paths, DOM checks and successful captures alone are not visual review.
10. Do not commit, push, or deploy unless the user explicitly asks in the current turn.
11. For documentation/skill-text-only maintenance, validate changed links, skill structure and synchronized copies. Do not recapture UI, rebuild artifacts or infer current production from old screenshots.

## Snapshot Discipline

- Never call a partial viewport set a "full production snapshot" or "complete evidence".
- Label ad-hoc `/tmp` screenshots as narrow evidence with route, viewport, auth state, and whether `fullPage` was used.
- For complete evidence, capture the matrix in `references/snapshot-suite.md`, use matched viewport sets, wait for fonts/hydration/data to settle, and write a manifest with provenance.
- Use `fullPage: true` for long page archives. Use viewport crops only for specific anchor, drawer, form, or interaction states.
- Keep signed-out, signed-in, owner-hash, TH/EN, desktop/tablet/mobile, and data-state captures separate instead of mixing them as if they were comparable.
- If any required surface cannot be captured, state exactly which surface is missing and why.

## Must-Preserve Product Decisions

- Home navigation has one Motor item pointing to `#motor`. Article index/reader reuse that header; Home anchors become localized Home URLs and obey Home visibility, while the Articles link has its separate saved visibility flag. `/motor` retains its motor-local nav and Home link.
- No `[object Object]` labels may appear in nav or UI.
- `/#motor-focus` is legacy/unexposed compatibility only; `/motor` is the current dedicated motor page.
- Home follows the approved compact redesign in `docs/HOME_REDESIGN.md`, with standalone editable Coverage and legacy Guides items consolidated into FAQ. Section availability is not a mandate to show every section. Preserve current CMS visibility, complete tier choices and truthful content. Read current live/draft data for order rather than restoring a historical list.
- Public TH/EN voice is a helpful companion, not a marketer: plain, warm and serious about facts. FAQ headings should sound like questions ordinary customers ask; answer directly and keep necessary conditions. Limit punchlines to genuinely useful brand moments, without turning "companion" into a slogan. Follow `docs/COPY_VOICE_AUDIT_20260927.md`; preserve licence, consent and coverage facts.
- FAQ collection ownership is `sections.@faq.items.@id.{th,en}.{q,a,label,meta}`. Add must be discoverable and focus the new question. Confirmed Delete removes both languages from Draft and is undoable; Hide is not deletion. Preserve stable IDs/order, intentional blanks and empty arrays, and never resurrect archived Guides. Read `docs/CMS_CONTENT_OWNERSHIP.md#faq-collection-editing` for command owners and the local browser harness.
- Existing Firestore copy is not updated by changing defaults or deploying code. Use reviewed field-level proposals with old-value/inline-override conflicts against fresh state, and preserve unrelated draft work. The read-only public copy preview is not a CMS test environment. Check `docs/HANDOFF.md` for candidate/publication status rather than storing a release assertion in this skill.
- Every visitor content image has a CMS media owner and ratio-aware crop/fit flow; keep source/output URLs and draft/live semantics. Read `docs/CMS_MEDIA.md` for Cloudinary setup and limits. Never hard-code replacements around Admin or revive Firebase Storage.
- Compare complete desktop/mobile composition, section density, optical logo size, equal collapsed peer cards and disclosure padding. Tablet should retain desktop-like composition with touch/mobile behavior. The owner requested roughly 3-4 viewports for this compact Home; measure actual comparable state, never force that by clipping content or shrinking text beyond readability.
- Latest owner-approved references govern visual direction; production governs existing behavior/data until an authorized migration. Use `docs/HANDOFF.md` to distinguish candidate evidence from production.
- The AIA logo uses the transparent red asset at `assets/logos/aia-logo.png`.
- Contact headings follow current CMS copy; keep compact, legible wrapping without restoring historical wording.
- Admin analytics remains a private admin module and route.
- Admin Home and Cases follow `docs/ADMIN_HOME_DESIGN.md` and `docs/ADMIN_CASES_V2.md`. Preserve real metrics/loading/error states, owner-only Cases access, explicit Save, version-conflict recovery and the mobile detail drawer. Legacy Leads/Tasks/Audit APIs are compatibility, not the current visible tabs.
- Read `docs/ADMIN_CASES_WORKBENCH.md` for current customer-linked activity and queues. Read `docs/ADMIN_CUSTOMERS.md` for manual entry, consent, validation and the entry/review/acknowledged-success journey. New Customer's labels/text/dates/hints align left, with dropdown values/options centered; do not blanket-center all forms. Private GCS storage and identity remain configuration-gated, without automatic billing activation or public-media fallback.
- Article information belongs above the writing editor, not in a full-screen writing toolbar. Use `docs/ARTICLE_EDITOR.md` for the green readiness checklist, disabled incomplete Publish, independent TH/EN publication, confirmed media reuse and editable draggable summary blocks. Keep Home's twelve-item/three-card desktop carousel separate from index pin ordering (`docs/HOME_ARTICLES.md`).
- CMS editor Undo/Redo and Reset operate on Draft; Reset reads the newest published snapshot and remains undoable. Save Draft flushes autosave without clearing history. The separate 30-second post-Publish undo changes Live and must stay explicitly labeled. Use `docs/CMS_EDITOR_HISTORY.md` for buffers, identity-scoped history and failure behavior.
- Follow actual source ownership: visitor renderer in `src/visitor/runtime.js`, editor commands in `src/visitor/cms-controller.js`, history in `editor-history.js`, CMS persistence in `covermate-firebase.js`, and freshness in `covermate-freshness.mjs`. The controller extraction does not lazy-load the whole editor UI.
- GA4 measurement ID is `G-5TF3C235EF`; public analytics must not receive visitor names, phone numbers, LINE IDs, or freeform messages.
- Admin routes are private and `noindex`.

## Standalone Poster Contract

- `exports/poster-v36/README.md` owns the current artifact, source fragments,
  immutable v35 input, approved mock direction and focused checks. Do not
  rewrite the supplied external original or create website routes for it.
- Keep three pages: introduction, original comparison and revised review.
  Preview and export selection are independent. Default 1+3, presets 1+2/all,
  custom nonempty subsets in page order; Save HTML always keeps all pages.
- Preserve shared logo/contact/legal fields, independent page QR controls,
  rich text, undo/redo, image validation, layout guards and draft confirmation.
  Do not invent personal-profile content, licence facts or promotion terms.
- Check actual PDF/print and PNG/JPG outputs when those owners change; exactly
  two selected pages are required for an A4 landscape spread, which is not
  duplex printing. Open saved HTML again to verify edits and selection persist.
- Chrome evidence is not physical-printer or Safari/iOS proof. QR and promotion
  placeholders are not production-ready values. Print delivery is not web deploy.
- Retain latest verified page/state evidence under `docs/ARTIFACT_RETENTION.md`;
  preserve original/reference inputs and never delete whole artifact folders.

## When Producing A Design Handoff

Include:

- Source-of-truth precedence.
- The current route/surface map.
- Visitor section order and component map.
- In-scope surface map: public routes and private Home, Customers, Cases, Articles, website editor/control panel, Analytics and account controls; poster pages/exports when relevant.
- Typography, color, spacing, responsive, accessibility, assets, SEO, analytics, and Firestore CMS guardrails.
- Explicit acceptance checklist and `do not touch` constraints.
- Snapshot evidence paths when available.

Keep the handoff implementation-ready and clear about what is FACT, what is an inference from current code, and what is a recommendation.

The installed skill and repository `skills/covermate-design-spec/` are kept in
sync. Refresh the bundled `references/current-design-spec.md` from the canonical
repository spec when that spec changes. It is a fallback snapshot, not proof of
the current deployed version; consult `docs/HANDOFF.md` and release evidence.
