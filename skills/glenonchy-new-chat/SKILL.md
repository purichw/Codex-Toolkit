---
name: glenonchy-new-chat
description: "Onboard or refresh the Glenonchy mobile activity and minigame project. Use for a Glenonchy new-chat prompt, project handoff, context pickup, required reading, setup status, or documentation alignment."
---

# Glenonchy New Chat

Read current project files before continuing Glenonchy work. This skill runs in
the current chat; it does not authorize creating, reading or messaging other chats.

## Locate and read

Default repository: `/Users/point/Projects/Glenonchy`.
Verify the directory and Git remote `DeepXSolution/Glenonchy` before edits.
If moved or missing, ask for the path rather than choosing a similarly named project.
Do not work in the original Downloads starter.

Read `AGENTS.md`, `README_START_HERE_TH.md`, `docs/PROGRESS.md`,
`docs/DECISIONS.md`, and `docs/PROJECT_MAP.md`, then the task-specific files in
[references/new-chat-context.md](references/new-chat-context.md).
Run `git status --short --branch` before edits and preserve existing changes.
Treat current user directions as authoritative over older starter decisions.

## Project decisions that affect implementation

- Glenonchy is the shop/project name; Community Quest is the original starter.
- Flutter + Flame remains the client; Django/DRF owns auth, API, admin and business rules.
- iOS is the current implementation and physical-test target. Keep UI, game rules,
  dialogue content and assets in shared Flutter/Dart, with platform services behind
  adapters so Android can follow later. Do not start Android setup/testing merely
  to finish an iOS task; retain portability without claiming Android readiness.
- Supabase is hosted PostgreSQL only. Do not infer Supabase Auth/Data API or
  supabase_flutter adoption from the presence of a project URL/publishable key.
- Email/password membership uses Django/DRF; no guest entry. LINE is a stub,
  not OAuth. Signup is not proof of email ownership. Read `docs/10-membership.md`
  for implemented endpoints, secure sessions, DB scope and recovery limitations.
- Keep bundled Noto Sans/Noto Sans Thai, TH default with persistent EN selection,
  and the approved shop logo with transparency inside the app. Launcher icons
  keep their opaque platform assets; preserve original brand files.
- For visual work read `docs/25-design-direction.md` and its component/asset map.
  Main navigation is World Map / Rewards / Character; Character opens the existing
  Profile with settings. Points/scan/history/benefits live under Rewards. The mock
  package's points bonus uses the main local wallet per the current economy doc.
  Do not restore the older separate trial-wallet or four-tab member journey.
  Reward instructions stay visible inside their own item/coupon popups.
- Login must show its full frame in one viewport with the keyboard closed and
  normal text size. Preserve the smaller centered LINE button, centered email
  divider and absence of a coming-soon caption below the button. The stub dialog
  remains. Read the detailed UI contract and `docs/11-device-support.md`.
- Use the Mac M1 8 GB workflow: physical devices, Profile builds and one target
  at a time. Do not start Emulator/Simulator, even to check other phone sizes.
  Use headless Flutter layout tests for viewport coverage; they do not verify
  those physical devices. Do not start Docker/Supabase local services automatically.
- Profile has no hot reload. Use the project build runbook without enabling the
  Profile debugger/device-symbol preparation. Inspect exact paths and current
  callers before cleanup; preserve source packs, user changes and current evidence.
  Apply the current user's cleanup authorization and applicable AGENTS guardrails,
  without inventing an additional approval rule in this skill.
- Keep pure Dart rules, Flame rendering, repositories and UI separate.
  Replay resets the current game session, not previously earned progression.
- QR identifies an activity point; it does not prove presence or award rewards.
  Server validation, ownership, transactions and idempotency still apply.
- The owner approved local points/coupons/items and staff handover. Read
  `docs/14-points-rewards.md`; do not reinstate the starter's blanket reward ban.
  This does not authorize server redemption, payment/POS or cross-device claims.
- World entry does not require Glenonchy first. Preserve each venue's QR, unlock,
  durable-save, fog/reveal and mini-map contracts in `docs/16-world-map.md`.
- Read the game-specific contract before touching character assets: Brewrunner
  and Tavern Jam have different approved packages. Tavern Jam's v2 package owns
  both players, states, frame geometry, anchors, timing and event mapping; it is a
  rhythm game with a stage performer. Do not substitute the Brewrunner atlas or
  a static pose. See `docs/18-tavern-jam.md` and its preserved source contracts.
- NPC/dialogue work follows `docs/19-barista-dialogue.md` and its current status.
  Preserve player identity and the supplied Barista uniform; a concept sheet is
  not an animation manifest. Mark authored runtime crops/transitions explicitly.

## Scope and evidence

Read current ticket status; never launch T00–T08 as a batch. Onboarding alone does
not authorize SDK installs, cloud changes, migrations, deployment or publishing.
When a concrete task is supplied, continue within its existing authorization;
do not invent a new confirmation requirement for ordinary local work.
The owner approved the documented development membership schema work. Read what
was actually applied before proposing migrations; onboarding is not a reason to
repeat setup or expand that approval to unrelated DB/cloud changes.

Commit, push and deploy each require the owner's explicit instruction for the
current scope/round. A prior release instruction does not authorize the next one.
Do not read, create, monitor, message or delegate to other chats from this skill.

Separate source checks, CLI linking, SQL connectivity, build, install, launch and
physical feature verification. Missing Flutter/Android tooling must not be
reported as ready just because Xcode or a paired iPhone exists. Do not copy device
IDs, keys, tokens or passwords into reusable docs or this skill.
Check the development API process/address when it is needed; a past LAN test is
not evidence of a running or hosted backend. Keep credentials in ignored env/OS
storage. Do not print env contents, bootstrap SQL, tokens or signed login URLs.

Distinguish real membership integration from fixture-only quest previews, and
headless layout coverage from hardware/OS coverage. After a device integration
test, restore the normal main entrypoint before calling the app ready for use.

Use `project-onboarding` for broader discovery and `docs-cartographer` for maps;
load `ui-ux-expert` and `ui-ux-expert-mobile-native` for visible native UI,
`mockup-to-product` for reference-led work, and `release-gate` for
authorized release work. Do not load a broad audit for a small follow-up.

Update `docs/PROGRESS.md` when work/status changes and `docs/ENVIRONMENT.md` when
tooling or readiness changes. Keep live status in the repository, not in this skill.
For documentation refreshes, reconcile stale statements across entry docs,
handoff, environment, map and relevant runbooks; mark historical evidence clearly.
Validate links and skill metadata. Do not rebuild the app or repeat DB/native
tests solely for documentation changes.
Use `docs/26-current-ui-qa.md` for the latest UI/native evidence scope, and read
dated earlier QA as historical. Before combining work for publication, compare
current sources/assets with the tested baseline and check the changed consumers;
do not call an older export or native suite proof of later changes.
For a handoff, use `docs/NEW_CHAT.md` and summarize verified state, open work and
the requested next task. If no implementation task was supplied, stop after onboarding.
