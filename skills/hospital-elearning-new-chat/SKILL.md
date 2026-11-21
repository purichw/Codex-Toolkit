---
name: hospital-elearning-new-chat
description: "Onboard or refresh context for Hospital E-learning, Rattanametha Hospital, or โรงพยาบาลรัตนเมธา E-Learning. Use for new-chat prompts, handoffs, returning to this project, locating route/component owners, or continuing its frontend and deployment work. Read the project's current documentation before acting; preserve its Thai design, shared layout, responsive behavior, and release boundaries."
---

# Hospital E-learning New Chat

## Project and first read

Project root: `/Users/point/Projects/rattanametha`.
Private repository: `purichw/rattanametha`.
Canonical site: `https://rattanametha.vercel.app`.

Announce this skill once, then:

1. Run `git status --short --branch` with the project as `workdir`. Preserve unrelated changes.
2. Read `AGENTS.md`, `README.md`, `docs/project-map.md`, and `docs/ui-ux-workflow.md` in the project. These are the living source of truth; do not infer deployed state from the working tree.
3. Use the project map to find the requested route, component, data owner, feature specification, and relevant QA scripts. Read only the owners needed for the task.
4. For release/deploy work, also read `docs/infrastructure.md` and the latest recorded release audit. Verify the intended SHA, remote state, required checks, deployment, and canonical alias separately.
5. If only onboarding is requested, give a concise context summary and outstanding local changes. Do not start unrelated implementation or deployment.

If the root is missing, ask for the checkout location instead of searching unrelated projects or chats. Keep work in the current chat. Never inspect, monitor, message, or delegate to another chat without the user's explicit authorization identifying that chat.

If the selected primary checkout has pending work and trails `origin/main`, keep
that work intact. Newly versioned docs/skills may be read from the current remote
tree with `git show origin/main:<path>` when absent locally; do not switch/reset
the checkout just to load onboarding material. Report which revision was read.

## Product and architecture contracts

- React + TypeScript + Vite frontend, with Vercel server authentication/API boundaries. Check `package.json` and project docs for current versions and scripts. Use the documented Node runtime.
- UI data comes through domain/repository adapters over structured fixtures; learner interactions use browser-local state where documented. A working UI is not evidence of a CMS, authoritative learner database, genuine certificate issuance, or per-user permissions.
- Reuse the shared Home header/navigation, footer, content canvas, modal, enrolment dialog, competency UI, certificate collection, media player, and loading system. Read the actual owner before adding another implementation.
- Content width is owned by `src/page-layout.css`. Align all page content with Home using `.page-container` once at the outer boundary. Do not reintroduce narrower page-specific max-widths or duplicate horizontal padding. Header geometry is separate; readable inner prose and dialogs may have intentional limits.
- The redundant global Courses tab was removed. Home's primary “เริ่มเรียนรู้เลย” CTA opens `/categories`. Preserve the curriculum tab inside course details.
- Generic certificate entry opens `/certificates` first. Individual awards and verification retain their explicit routes and breadcrumb hierarchy.
- Authored routes render their actual pages. Known unfinished destinations use validated contextual availability copy and safe return targets. Unknown routes/entities must not become fabricated coming-soon pages.

## Design and responsive rules

Load `/Users/point/.codex/skills/ui-ux-expert/SKILL.md` for user-facing work. Use the existing hospital brand and supplied references; do not replace them with default skill tokens. Apply `mockup-to-product`, `shared-component-architecture`, `responsive-design`, and `snapshot` when their scope is relevant or the user invokes them.

- Use Noto Sans Thai throughout. Prefer clear Thai labels and realistic product copy. Do not expose “mock”, “demo”, CMS plumbing, or development commentary in user flows; the explicitly requested unavailable page is the exception.
- Preserve supplied composition, original reference files, and asset provenance. Annotation markers, device frames, palettes, and specification panels are not product UI.
- Prioritize tablet portrait. Tablet landscape should remain close to desktop while keeping readable text and comfortable touch controls. Mobile must wrap/reflow without clipped artwork or horizontal page overflow.
- Center button labels and their primary icons as a group. Trailing arrows must not shove the label off-center. Check Thai glyph alignment inside ribbons, shields, badges, pills, and certificates visually.
- Keep Home card dimensions unchanged unless the user explicitly changes that constraint. Additional competency recommendations belong in the shared dialog.
- Loading and Login must fit one viewport at supported sizes, including short landscape screens. Solve geometry rather than hiding inaccessible content with document overflow clipping. Preserve usable keyboard and zoom behavior.
- On initial entry through any URL, show the branded loader for at least three seconds and until real content/assets are ready. Progress reaches 100% only when both conditions hold. Navigation uses appropriate skeletons; never reveal broken layout or unstyled fallback.
- The five startup journey lights run once and hold the final “เติบโตไปด้วยกัน” pin; never wrap back to the first light. Reduced motion shows the final pin statically. Keep readiness/progress and pause behavior independent from that sequence.
- The classroom outline is native sticky, flush to the viewport top within its course container, with a viewport-height cap and internal scrolling. `src/course-lesson.css` owns the 768px side-column breakpoint; mobile returns to normal flow. Preserve access to the final item and clearance before the footer.
- Prefill supported happy-path interactions for presentation, but never expose the server login identifier or credentials in public frontend defaults.

## Authentication and media boundaries

Read `docs/authentication.md` before changing auth, public asset rules, sessions, secrets, or bundle protection. The username is exact-case and checked on the server. Do not print secret values, copy them into client code, or claim minification prevents users from retrieving delivered frontend code. This shared access gate is not individual identity or RBAC.

Read `docs/course-video-design-and-qa.md` before media changes. The project has an explicitly documented demonstration presentation that differs from a policy-compliant production embed; do not claim it is compliant. Preserve the documented Made-for-Kids/unknown-state tracking gate. Seek observations are advisory, not authoritative watched-time or certificate eligibility. Do not extract hosted video streams or invent licensed self-hosted rights. Keep the Data API key server-side.

The illustrated seek prompt is compact (460px maximum) and centers on the visible
video stage, excluding controls, while following layout shifts and clamping to
the viewport. Only review or acknowledgement dismisses it: no backdrop/content
click, Escape or close icon. Preserve paused/ended state on acknowledgement.
This restriction belongs to the media prompt, not ordinary shared dialogs.

## Relationship to Thai Palliative Nurse

Read `docs/learning-project-boundaries.md` when adapting learning behavior between
these projects. TPNA is an independent association site with its own Blue theme,
1200px container, header/footer, CMS, progress and release. Hospital retains its
own visual system, 1560px canvas and assessment/data contracts. Never impose this
project's shell or scored Final Assessment on TPNA; its final learning step is
course-experience feedback after its Post-test.

The owner's narrow exception is player/framing/control/illustrated seek-popup
parity, adapted to TPNA colors. Reuse is deliberate source adaptation, not runtime
coupling or automatic synchronization. The owner-authorized shared YouTube key
uses separate server env names, auth and allowlists; no learner/session data is
shared. Seek tracking stays advisory. A port including local Hospital edits does
not prove those edits are deployed here. Verify each project's source/release
independently; related-project context grants no cross-chat or release authority.

When the requested work covers behavior common to both learning products, follow
the owner's paired-maintenance preference: inspect and correct both equivalent
owners within the authorized scope, and verify each integration separately.
Keep product-specific UI and assessments independent; never infer permission to
publish either project or access another chat from this relationship.

## Verification and handoff

Choose the smallest safe scope for the current request. State depth, evidence, stop rule, and skipped checks before expensive or broad verification. Historical QA is evidence of the recorded revision only.

- Tiny UI fix: inspect its owner, edit narrowly, run `git diff --check`, and obtain one useful current visual/computed-layout check.
- Shared/routing changes: inspect affected consumers and representative mobile, tablet portrait, tablet landscape, and desktop layouts. Use the project's targeted scripts instead of starting unrelated suites.
- Personally inspect current rendered screenshots before handing off visible work. Check alignment, wrapping, image crops, interaction states, and accessible controls. Record route, viewport, revision/context, and limits; do not label unrun checks as passed.
- A content-width audit can use `scripts/qa-content-width.mjs`; consult its environment options and `docs/content-width-audit-2026-11-11.md`. Do not repeat its full matrix for unrelated copy changes.
- Update the affected feature doc and `docs/project-map.md` when ownership/routes change. Update README/infrastructure only when their contracts or release state change. Keep old dated QA historical rather than presenting it as fresh validation.
- Finish with final diff/status, concise outcome, evidence, and material remaining limitations. Link the changed docs or relevant screenshot using absolute local paths.

Commit/push/deploy only within the user's current authorized scope; creating or reading this skill is not release authorization. Follow the project release runbook, keep private-repo/source boundaries, and retain `sin1` unless explicitly changed. Diagnose failed or stalled phases before retrying; never force-push, cancel unrelated work, or bypass a required check to finish sooner.

The versioned source is `skills/hospital-elearning-new-chat/` in this repository;
the installed copy is `/Users/point/.codex/skills/hospital-elearning-new-chat/`.
Keep copies identical and validate changed metadata with the skill-creator
validator. Keep changing release SHAs/results in project docs, not the skill.
