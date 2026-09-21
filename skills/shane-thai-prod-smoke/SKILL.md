---
name: shane-thai-prod-smoke
description: Run or set up authenticated production smoke checks for the Shane Thai app after Vercel deploys, production verification, release-gate closeout, learner-flow checks, topbar/Learning hub checks, or screenshot evidence. Use when Codex needs the Shane-specific production smoke account, safe learner test policy, Playwright/browser smoke, or snapshot evidence for https://shanethai.vercel.app.
---

# Shane Thai Prod Smoke

## Overview

Use this skill to verify Shane Thai production with the dedicated dummy learner account. It complements `$release-gate` and `$snapshot`; use those too when committing, deploying, or presenting visual evidence.

## Safety Rules

- Use only the production smoke learner account:
  - Username: `codex`
  - Password: `codexcodex`
- Do not use `Shane`, `Pointy`, `pointy`, admin accounts, personal accounts, or real learner accounts for automated/manual smoke checks.
- Do not submit quizzes, practice tests, cloze/listening answers, or admin changes in production unless the user explicitly asks for that live mutation.
- Treat `codex` account progress as disposable but still avoid unnecessary mutation. Navigation, login, dismissing onboarding, and reading pages are acceptable.
- Do not print secrets beyond this documented dummy account. If credentials change, update project docs before relying on them.

## Preflight

1. Work from `/Users/point/Website Projects/thai-flashcards` unless the user gives another path.
2. Read current repo/deploy context when relevant:
   - `git status --short --branch`
   - `git log --oneline --decorate -5`
   - `docs/memory.md`
   - `docs/playbook.md`
3. Confirm the deploy target:
   - Production alias: `https://shanethai.vercel.app`
   - Vercel deployment URL may differ; smoke both the alias and the reported deployment URL when debugging alias issues.

## Smoke Protocol

1. HTTP smoke:
   ```bash
   curl -I -L 'https://shanethai.vercel.app/?smoke=<commit-or-run-id>'
   ```
   Expect `200`, `content-type: text/html`, and the configured security headers.
2. Browser unauthenticated smoke:
   - Open the production URL.
   - Verify the title is `Learn Thai for Beginners | Shane Thai`.
   - Verify the login surface is visible.
   - Record console errors and failed requests.
3. Browser authenticated smoke:
   - Log in with `codex` / `codexcodex`.
   - `Opening your account...` may appear briefly, but it should not hang while
     background progress listeners or learning-event sync continue.
   - Dismiss the daily pace modal with `Skip for now` if it appears.
   - Verify `Signed in as codex`.
   - Verify topbar/action nav contains `Courses`, `Today`, `Badges`, and `Switch user`.
   - Open `Courses`, then choose `Learning hub`.
   - Verify supporting sections for Paiboon Reference, Romanized Thai, Thai Word Bank, Alphabet Explorer, and Reading Lab.
   - Capture a wide `$snapshot` that includes the topbar and main support-section context.
4. Optional route probes when the change touched them:
   - Main course unit page route.
   - `Fill` and `Listen` tabs only after the test data/progress state is safely controlled.
   - Admin routes only with explicit admin smoke policy and credentials.

## Playwright Pattern

Use a one-off Playwright script or an existing project e2e harness. Keep it non-mutating and save screenshots under `/tmp`:

```js
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } })
page.on('console', ...)
page.on('requestfailed', ...)
await page.goto('https://shanethai.vercel.app/?prodSmoke=<id>')
await page.getByLabel('Username').fill('codex')
await page.getByLabel('Password').fill('codexcodex')
await page.getByRole('button', { name: 'Sign in' }).click()
await page.getByLabel('Current profile').waitFor({ state: 'visible' })
```

Do not commit temporary smoke scripts unless the user asks to make the harness permanent.

## Failure Classification

Hard failures:
- Non-`200` production response.
- Login fails for the `codex` account.
- Expected Today/Learning hub/support-section UI is missing.
- Console errors from app code.
- Failed document, script, stylesheet, image, audio, Firebase auth, or Firestore requests during the exercised flow.

Usually benign:
- `Firestore/Listen/channel ... net::ERR_ABORTED` emitted after all assertions pass while the browser is closing. Mention it as teardown noise if it appears; do not treat it as a blocker by itself.

## Closeout

Report:
- Commit SHA and production URL.
- HTTP status and browser smoke result.
- Authenticated account used: `codex`.
- Console errors and failed requests, including any ignored teardown noise.
- Snapshot path and embedded image.
- Any skipped live coverage and why.
