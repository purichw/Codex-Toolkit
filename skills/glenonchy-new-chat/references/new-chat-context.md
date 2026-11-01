# Glenonchy reading map

Repository: `/Users/point/Projects/Glenonchy`
Expected remote: `https://github.com/DeepXSolution/Glenonchy.git`

Read these relative paths inside the verified repository. They own current facts;
this file is a routing map, not a second copy of project status.

| Current task | Read |
|---|---|
| Any visual design or shared UI repair | docs/25-design-direction.md, relevant component/asset owners, docs/26-current-ui-qa.md for evidence scope |
| Any context pickup | AGENTS.md, README_START_HERE_TH.md, docs/PROGRESS.md, docs/DECISIONS.md, docs/PROJECT_MAP.md |
| Setup or device readiness | docs/ENVIRONMENT.md, docs/02-setup.md, apps/mobile/README.md, docs/11-device-support.md |
| Product scope / MVP | docs/00-product-scope.md, docs/06-codex-tasks.md |
| Client/game work | apps/mobile/README.md, docs/01-architecture.md; choose the actual game's contract below rather than applying the original Coffee Catch spec to every game |
| Brewrunner / original player art | docs/12-coffee-catch-integration.md, docs/17-character-roster.md, apps/mobile/vendor/brewrunner_animation_pack/GLENONCHY_ADAPTATIONS.md |
| Tavern Jam / Old Pals rhythm game | docs/18-tavern-jam.md, docs/tavern-jam-package-v2/START_HERE.md, docs/tavern-jam-package-v2/docs/ANIMATION_STATE_CONTRACT.md; owners apps/mobile/lib/features/tavern_jam/ and lib/data/world_progress.dart |
| Barista NPC / dialogue | docs/19-barista-dialogue.md, docs/16-world-map.md, docs/17-character-roster.md; inspect the supplied cafe_barista_glasses_uniform_pack_v1 manifest and art before integrating |
| Shared UI / QR camera | docs/13-game-selection-shared-ui.md; apps/mobile/lib/app/game_components.dart and features/game_selection/ |
| Local points / coupons / menus | docs/14-points-rewards.md, docs/15-merchant-menus.md; apps/mobile/lib/data/local_rewards.dart |
| Login/layout/brand/TH-EN | docs/10-membership.md, docs/11-device-support.md, assets/brand/README.md, assets/auth/README.md; owner apps/mobile/lib/features/auth/auth_screen.dart |
| Membership/API/session/recovery | docs/10-membership.md, backend/README.md, docs/09-infrastructure.md; owners backend/accounts/, apps/mobile/lib/data/auth_repository.dart, apps/mobile/lib/features/auth/auth_gate.dart |
| Gameplay backend/progression | docs/04-data-api-security.md, docs/06-codex-tasks.md, docs/10-membership.md; preserve existing membership |
| QR/map/venue operations | docs/16-world-map.md, docs/qr-codes/README.md, apps/mobile/lib/data/local_qr_catalog.dart; docs/05-qr-map-ops.md is the earlier operations plan |
| UAT or release | docs/07-test-release.md, docs/26-current-ui-qa.md, docs/PROGRESS.md, current build sources; 21/23/24 are earlier QA baselines |
| New-chat prompt | docs/NEW_CHAT.md |
| Docs/skill alignment | docs/NEW_CHAT.md, README.md, README_START_HERE_TH.md, docs/ENVIRONMENT.md, docs/PROJECT_MAP.md and task runbooks; skill entrypoint/reference/UI metadata |

Supabase target is identified in docs/09-infrastructure.md. Validate the exact ref
before any permitted remote action. Link metadata lives in ignored supabase/.temp;
never print credentials from it. Database writes are a separate scope from linking.
The owner-approved development membership work is recorded in docs/10-membership.md;
read it before treating schema/roles as missing or asking to authorize the same work again.

Current low-impact checks, if the files still exist:

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

Keep app/test versions, counts, current process state and latest evidence in repo docs,
not this skill. Clearly separate historical T01/setup results from current membership.
