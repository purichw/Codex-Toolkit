# Glenonchy reading map

Repository: `/Users/point/Projects/Glenonchy`
Canonical remote: `https://github.com/Glenonchy/Glenonchy.git`
Legacy remote `DeepXSolution/Glenonchy` redirects to this repository; verify the
resolved owner/repo and commit before publication. Do not rewrite other remotes.

Read these relative paths inside the verified repository. They own current facts;
this file is a routing map, not a second copy of project status.

| Current task | Read |
|---|---|
| Public website context | docs/website/NEW_CHAT.md, docs/website/README.md, docs/website/DESIGN_CONTRACT.md; invoke glenonchy-website-new-chat, then glenonchy-website-design for implementation |
| Public website release/access | apps/gm-console/README.md, docs/website/ACCESS_PROTECTION.md, latest dated website release and its retained status evidence; public entrance is not GM/member auth |
| GM Console / admin operations | docs/gamemaster-console/REPO_AUDIT.md, docs/gamemaster-console/IMPLEMENTATION_PLAN.md, docs/gamemaster-console/OPERATIONS_RUNBOOK.md, apps/gm-console/README.md; first operations slice, not the full V1 |
| Mobile visual design or shared UI repair | docs/25-design-direction.md, relevant component/asset owners, docs/26-current-ui-qa.md for evidence scope |
| Design evidence retention / disk cleanup | docs/ARTIFACT_RETENTION.md, docs/ENVIRONMENT.md, docs/PROGRESS.md; use the recorded per-feature replacement map and actual execution results, not an old deletion script as fresh authorization |
| Any context pickup | AGENTS.md, README_START_HERE_TH.md, docs/README.md, relevant recent sections of docs/PROGRESS.md and docs/DECISIONS.md, docs/PROJECT_MAP.md |
| Setup or device readiness | docs/ENVIRONMENT.md, docs/02-setup.md, apps/mobile/README.md, docs/11-device-support.md |
| Product scope / MVP | docs/00-product-scope.md, docs/06-codex-tasks.md |
| Client/game work | apps/mobile/README.md, docs/01-architecture.md; choose the actual game's contract below rather than applying the original Coffee Catch spec to every game |
| Brewrunner / original player art | docs/12-coffee-catch-integration.md, docs/17-character-roster.md, apps/mobile/vendor/brewrunner_animation_pack/GLENONCHY_ADAPTATIONS.md |
| Tavern Jam / Old Pals rhythm game | docs/18-tavern-jam.md, docs/tavern-jam-package-v2/START_HERE.md, docs/tavern-jam-package-v2/docs/ANIMATION_STATE_CONTRACT.md; owners apps/mobile/lib/features/tavern_jam/ and lib/data/world_progress.dart |
| Paradise Path / 1780's Road to Paradise | docs/27-paradise-path.md; apps/mobile/lib/features/paradise_path/ and its supplied scene/animation contracts |
| Wild Ink / Wild Studio Tattoo | docs/28-wild-ink.md, docs/30-app-completion.md; preserve the documented trial, save and retry contracts |
| Standalone Godot Tactics / GM-authored battles / combat art | prototypes/tactics/AGENTS.md, prototypes/tactics/CODEX_START_HERE.md, prototypes/tactics/README.md, prototypes/tactics/docs/ARCHITECTURE.md, prototypes/tactics/docs/CHARACTER_IDENTITY_CONTRACT.md, prototypes/tactics/docs/CHARACTER_REUSE_POLICY.md; follow the current runtime/QA and asset-manifest pointers there, not old intake status in isolation |
| Barista NPC / dialogue | docs/19-barista-dialogue.md, docs/16-world-map.md, docs/17-character-roster.md; inspect the supplied cafe_barista_glasses_uniform_pack_v1 manifest and art before integrating |
| Shared UI / QR camera | docs/13-game-selection-shared-ui.md; apps/mobile/lib/app/game_components.dart and features/game_selection/ |
| Local points / coupons / menus | docs/14-points-rewards.md, docs/15-merchant-menus.md; apps/mobile/lib/data/local_rewards.dart |
| Login/layout/brand/TH-EN | docs/10-membership.md, docs/11-device-support.md, assets/brand/README.md, assets/auth/README.md; owner apps/mobile/lib/features/auth/auth_screen.dart |
| Membership/API/session/recovery | docs/SIGNUP_RECOVERY_2026-11-07.md, docs/SUPABASE_RESTORE.md, docs/10-membership.md, backend/README.md, docs/09-infrastructure.md; owners backend/accounts/, apps/mobile/lib/data/auth_repository.dart, apps/mobile/lib/features/auth/auth_gate.dart |
| Supabase replacement / backup / migrations / reconnect | docs/SUPABASE_RESTORE.md, docs/SIGNUP_RECOVERY_2026-11-07.md, docs/ENVIRONMENT.md, docs/DECISIONS.md, docs/22-render-free.md, docs/gamemaster-console/OPERATIONS_RUNBOOK.md; distinguish hosted runtime, local env and CLI link, deployed baseline and pending account/player migrations; preserve stable realm identity and device data |
| Gameplay backend/progression | docs/04-data-api-security.md, docs/06-codex-tasks.md, docs/10-membership.md; preserve existing membership |
| QR/map/venue operations | docs/16-world-map.md, docs/qr-codes/README.md, apps/mobile/lib/data/local_qr_catalog.dart; docs/05-qr-map-ops.md is the earlier operations plan |
| UAT or release | docs/07-test-release.md, docs/26-current-ui-qa.md, docs/PROGRESS.md, current build sources; 21/23/24 are earlier QA baselines |
| New-chat prompt | docs/NEW_CHAT.md; website-only work uses docs/website/NEW_CHAT.md |
| Docs/skill alignment | docs/README.md, docs/NEW_CHAT.md, docs/website/README.md, docs/website/NEW_CHAT.md, README.md, README_START_HERE_TH.md, docs/ENVIRONMENT.md, docs/PROJECT_MAP.md, docs/skill-updates/README.md and task runbooks; skill entrypoint/reference/UI metadata |

Supabase target and lifecycle are recorded in docs/SUPABASE_RESTORE.md. Validate the
exact ref before any permitted remote action. CLI/browser sessions and ignored
supabase/.temp link metadata can disagree; successful CLI listing alone does not
prove access to the selected project. Never print credentials from local settings.
Read completed setup and the owner's current choice before proposing account
creation, migrations, hosting changes or mobile reconnect. Setup credentials and
database preservation files are not disposable caches. Do not copy current refs,
passwords, account details or verification counts into this routing map.

Use only checks needed for the current task. Documentation-only onboarding needs
file/link/metadata checks and Git status/diff, not builds or cloud/device tests.
For setup work, use the setup checker if it still exists:

```sh
git status --short --branch
python3 scripts/check_setup.py
git diff --check
```

Flutter commands run from apps/mobile/ via ../../scripts/flutter.sh; backend commands
run from the repo root using backend/.venv and scripts/manage-backend.py. Read their
runbooks rather than reconstructing commands or hardcoding old LAN/device values.

apps/mobile/test/auth_test.dart owns headless viewport/auth checks.
apps/mobile/integration_test/auth_flow_test.dart uses the real development API and creates
synthetic QA members; apps/mobile/integration_test/preview_flow_test.dart injects a test member for fixture-only
quest checks. Do not substitute one as proof of the other or run them just to onboard.
Real-device capture and source provenance are recorded in docs/PROGRESS.md; old
screenshots and test-runner completion screens are not current app evidence.
Superseded design images may have been deliberately removed under
docs/ARTIFACT_RETENTION.md. Keep the latest per-feature evidence and source art;
do not recreate retired flow sheets or re-download caches merely to onboard.

Keep app/test versions, counts, current process state and latest evidence in repo docs,
not this skill. Clearly separate historical T01/setup results from current membership.
