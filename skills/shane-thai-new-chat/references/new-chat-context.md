# Shane Thai New Chat Context

Use this as the pickup map for a fresh Codex chat. Prefer current on-disk files over memory from any prior thread.

## Project

- Repo: `/Users/point/Website Projects/thai-flashcards`
- Production: `https://shanethai.vercel.app`
- Stack: Vite, React, TypeScript, Firebase Auth/Firestore, Vercel serverless API, Playwright, Vitest.
- Main product: beginner Thai learning app for English-speaking learners.
- Primary path: Main Course. Supporting references: Paiboon Reference,
  Romanized Thai, Thai Word Bank, Alphabet Explorer, Reading Lab.
- Current produced Main Course content: Units 1-17. Units 1-11 are Thai Foundations: Start; Units 12-17 are Thai Foundations: Build. Do not move them to Growth unless asked.

## Read Order

Always start with:

1. `/Users/point/Website Projects/thai-flashcards/README.md`
2. `/Users/point/Website Projects/thai-flashcards/docs/project-intent.md`
3. `/Users/point/Website Projects/thai-flashcards/docs/memory.md`
4. `/Users/point/Website Projects/thai-flashcards/docs/course-status.md`

Then choose by task:

- Architecture/routes/data ownership: `docs/architecture.md`, `docs/site-map.md`, `docs/user-journeys-and-interactions.md`
- Current plan/risk: `docs/roadmap.md`, `docs/architecture-plan.md`, `docs/rollback-parking-lot.md`
- Lesson authoring/content: `docs/lesson-production-pattern.md`, `docs/i-plus-one-lesson-framework.md`, `docs/content-exports/chatgpt-lesson-patch-2026-07-16/README.md`, `PATCH_PROTOCOL.md`, `SOURCE_MAP.md`, `ALL_UNITS_COMPACT.md`, and the relevant `unit-XX-*.md`
- QA and release: `docs/qa-coverage.md`, `README.md`, `package.json`
- Audio: `docs/audio-audit.md`, `docs/audio-naturalness-triage.md`, `docs/audio-audit.json`
- Claude Design / visual parity: relevant files under `docs/design-handoffs/`, especially source-rendered learner handoffs and current admin/asset handoffs.
- Admin/CMS: `docs/design-handoffs/claude-admin-portal-current/`, `docs/architecture.md`, `docs/memory.md`

## Skills To Use

Use the current on-disk `SKILL.md` each time a skill is invoked.

- New-chat onboarding: `$shane-thai-new-chat`
- Lesson export for ChatGPT patching: `$shane-thai-export-chatgpt`
- Image, HTML, or mixed-reference visual parity: `$reference-to-a-tee`
- UI/UX routing and broad UX judgment: `$ui-ux-orchestrator`
- Consistency-only audits: `$consistency-audit`
- Screenshots/snapshots: `$snapshot`
- Release readiness: `$release-gate`
- Production smoke: `$shane-thai-prod-smoke` or `$prod-smoke-harness`
- Efficient batching: `$efficient-execution`
- Docs maps: `$docs-cartographer`
- Rollback/revert/remove/undo guard: `$rollback-guardrail`
- Audio assets: `$shane-thai-audio-generator` or `$tts-audio-assets`
- Course images: `$shane-thai-image-assets` or `$course-image-assets`
- Firebase auth/account flows: `$firebase-account-management`, `$firebase-security-rules`, `$account-recovery-key`
- Admin operations: `$admin-ops`, `$admin-prototype-reconciliation`
- Mobile/responsive QA: `$mobile-web-qa`
- Interaction/browser QA: `$interaction-flow-qa`
- Forms: `$form-flow-ux`
- Accessibility: `$accessible-interaction`

## Durable Product Rules

- Preserve the project's Google Sans font system during reference parity work,
  even when a supplied reference uses another typeface, unless the user explicitly
  changes app-wide typography. Record it as an accepted project visual exception.
- Communication-first. Thai script stays visible. Learner-facing course content
  uses Shane/course romanization. Romanized Thai and Thai Word Bank may show
  canonical Paiboon plus IPA companion readings.
- Lesson content, media, progress, and IDs should remain data-driven.
- Preserve stable IDs by default.
- Long Thai phrase cards becoming phrase cards is valid product behavior, not drift.
- The Learning Hub return action belongs inside the Courses panel. Do not move it back to a topbar chip.
- Main Course Cards have Study/Reference behavior; Reference can support card/table variants where already implemented.
- Audio completion tracks heard Thai content, not literal button clicks.
- Quiz, Fill, and Listen are open whenever a unit has that content. Do not
  reintroduce completion-based locks for those tabs.
- Typing is optional learner-controlled recall practice. Current-unit Cards
  always come before current-unit Dialogue items across batches; Cards and
  Dialogues shuffle internally but never mix. Typed Thai checking ignores
  whitespace completely.
- Learning events are append-only supplemental analytics/mastery data. Pending
  local events live in `shaneThai.learningEvents.v1` and sync to
  `learners/{uid}/learningEvents/{eventId}` without replacing progress docs.
- Account startup shows `Opening your account...` while loading only
  startup-critical state: profile, Main Course progress, streak, learning
  preferences, onboarding, and account-level tour state. Full progress sync,
  active learning time, badges/alphabet/reading-lab hydration, and
  learning-event sync continue in the background.
- Refresh/practice rewards apply only when progress dots refill; no reward if already full.
- Every Delete/destructive action needs a customized warning popup. Highly destructive actions should use two confirmations or typed confirmation.
- Do not use real learner accounts for smoke tests. Use the dummy Codex account from `docs/memory.md` only.
- Do not commit, push, deploy, rollback, or revert unless explicitly asked in the current task.
- UI changes need visible snapshot evidence in final handoff.

## Current Setup Commands

```bash
cd "/Users/point/Website Projects/thai-flashcards"
npm install
npm run dev
npm run test:learning
npm run accessibility:release-gate
npm run pwa:release-gate
npm run ci:learner:quick
npm run ci:quick
npm run test:e2e:learner
npm run test:e2e:admin
npm run test:e2e:responsive
npm run test:firebase:rules
npm run test:firebase:e2e
npm run test:firebase:admin
```

Use targeted checks first, then broaden based on risk. Full quick CI is:

```bash
npm run ci:quick
```

## Common Source Areas

- Auth/login/settings/recovery: `src/auth/LoginScreen.tsx`, `src/auth/authState.ts`, `api/learner-signup.js`, `api/learner-recovery.js`
- Firebase/admin API: `src/firebase/*`, `server/firebaseAdminSecurity.cjs`, `api/admin-learner.js`, `firestore.rules`
- Account startup/progress sync: `src/App.tsx`, `src/firebase/progressSync.ts`, `src/auth/authState.ts`, `src/storageKeys.ts`, `tests/firebase-e2e/progress-sync.spec.ts`
- Main Course data: `src/data/mainCourse.ts`, `src/data/mainCourse*.ts`, `src/data/mainCourseLevels.ts`
- Main Course routes/state/progress: `src/main-course/*`, `src/navigation.ts`, `src/storageKeys.ts`
- Learner shell/screens: `src/App.tsx`, `src/app/*`, `src/CourseHome.tsx`, `src/MainCourse.tsx`, `src/MainCourseLessons.tsx`
- Typing practice: `src/main-course/typingGameLogic.ts`, `src/main-course/CourseTypingGame.tsx`
- Romanized Thai / Word Bank: `src/ThaiToPaiboonTool.tsx`, `src/ThaiWordBank.tsx`, `src/lib/thaiToPaiboon.ts`, `src/lib/thaiWordBank.ts`, `src/lib/romanizedThaiStyle.ts`, `src/workers/thaiWordBankWorker.ts`, `src/data/romanizedThaiAudioManifest.ts`, `tools/write-romanized-thai-audio-manifest-json.mjs`
- Learning events / skill graph / mastery SRS: `src/learning/*`, `src/firebase/learningEventSync.ts`
- Admin portal: `src/admin/*`
- Audio tools/assets: `tools/generate-main-course-chirp-audio.mjs`, `tools/audit-chirp-audio.mjs`, `public/audio/chirp/`
- Image tools/assets: `tools/audit-main-course-images.mjs`, `src/main-course/visuals`, `public/`

## New Chat Prompt Template

Use this when the user asks for a starter prompt:

```text
We are continuing the Shane Thai beginner Thai learning app at:
/Users/point/Website Projects/thai-flashcards

Before doing work, use $shane-thai-new-chat and read current on-disk docs, not prior memory. Start with README.md, docs/project-intent.md, docs/memory.md, and docs/course-status.md. Then read task-specific docs from /Users/point/.codex/skills/shane-thai-new-chat/references/new-chat-context.md.

Important constraints:
- Preserve existing routes, progress keys, data contracts, internal scroll containers, responsive constraints, and customized component geometry unless explicitly in scope.
- Do not commit, push, deploy, rollback, revert, remove, or undo unless explicitly asked in this current task.
- Keep account startup bounded: do not make `Opening your account...` wait for every background progress listener or learning-event sync.
- If a named skill is used, read its current on-disk SKILL.md first.
- UI work needs snapshot evidence.
- Rollback-like work must use $rollback-guardrail first.
- Destructive actions need customized warning popups; very destructive actions need double confirmation or equivalent.

After onboarding, summarize what you read and wait for my task unless I already gave one.
```
