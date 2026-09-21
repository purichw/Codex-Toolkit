# DOOTAA new-chat context

This is a pickup map, not a frozen release checkpoint. Read current repo files
before using the facts below. Relative paths resolve under
`/Users/point/Projects/DOOTAA`, except abbreviated `src/` and `assets/` paths,
which resolve under its `apps/mobile/` directory.

## Project and surfaces

- Checkout: `/Users/point/Projects/DOOTAA`.
- GitHub: `https://github.com/purichw/DOOTAA`.
- Main app: `apps/mobile`, Expo / React Native / TypeScript / Expo Router.
  Routes are in `apps/mobile/src/app`; `@/*` maps to `src/*`.
- Website: Vercel `purich-w/dootaa`, `https://dootaa.vercel.app`.
  `/` is the guide/Flow Map, `/app/` the browser app. Verify deployment separately
  when relevant; a local source change or build is not a deployed change.
- Local account forms, consent and real capture are implemented; read current
  evidence for device behavior. Local accounts do not send email or constitute
  production backend authentication. No clinical capability follows from QC.
- `packages/research` holds SQL/local test foundations, not a deployed backend
  or a pnpm workspace package. `tools/data` owns dataset tooling.

## Required reading and authority

Start with `AGENTS.md` → `README.md` → `docs/PROJECT_MAP.md` → relevant sections
of `docs/PLAYBOOK.md`. Use `docs/ROADMAP.md` for gates and pending work. Resolve
conflicts against owner source, current diff, dated evidence and latest explicit
owner decisions; do not silently change contracts to match old examples.

Choose additional reading by task:

| Task | Documents and owner areas |
| --- | --- |
| Account, consent, history, privacy, navigation | `docs/ACCOUNT-CAMERA-FLOW.md`; `src/state/account-provider.tsx`, `src/domain/navigation.ts`, `src/domain/real-screening.ts`, `src/storage/` under the app |
| UI, branding, language, screen density | `docs/PROJECT_MAP.md` shared-owner inventory; app `src/components/dootaa-ui.tsx`, `account-ui.tsx`, `real-capture-ui.tsx`, `src/design/tokens.ts`, `src/state/i18n.ts`, `assets/brand/`; relevant current QA under `docs/qa/` |
| iOS/Android setup, native dependency or device failure | `docs/PLAYBOOK.md`, root/app `package.json`, `.nvmrc`, `scripts/dev-env.sh`, app config/plugins and `apps/mobile/modules/dootaa-live-camera/` |
| Continuous camera or capture interaction | `docs/CAPTURE-QC.md`, `docs/ACCOUNT-CAMERA-FLOW.md`, then `docs/spec/v3/START_HERE.md` and its prescribed reading order |
| Eye recognition, gaze criteria or Benchmark | Final eye handoff and evidence sequence below; `src/capture/live-policy.ts`, `live-machine.ts`, `eye-local.ts`, `eye-corner-diagnostics.ts`, `guided-benchmark.ts`, `src/components/live-capture-session.tsx`, `scripts/benchmark/` |
| Native detector/model acquisition | Camera docs plus `docs/licenses/eye-local-models.md`, `apps/mobile/modules/dootaa-live-camera/models/manifest.json`, `scripts/prepare-eye-local-deps.py`; code, model and dataset rights are distinct |
| Dataset acquisition / data tooling | `data/README.md`, `data/PUBLIC_DATASET_REGISTRY.md`, `data/dataset_registry.json`, `data/DATA_LICENSE_POLICY.md`, `docs/DATA_ACQUISITION.md`, `docs/DATA-TOOLS.md`; follow their mandatory source reading before changes |
| Product/data/AI lifecycle or research | `docs/spec/v2/PACKAGE_INDEX.md` and its three top-level companions below, plus relevant schemas, safety/readiness/consent docs and `packages/research/README.md` |
| Flow Map or website gate/deploy | `docs/WEBSITE-DEPLOYMENT.md`, `docs/flow/index.html`, `scripts/build-website.mjs`, `website/`, `middleware.ts`, `vercel.json`, app `src/config/runtime.web.ts` and `website-policy.ts` |

For product/data/AI lifecycle changes, read together:

1. `docs/spec/v2/DOOTAA_E2E_PRODUCT_DATA_AI_LOOP_SPEC.md`.
2. `docs/spec/v2/codex/CODEX_MASTER_PROMPT.md`.
3. `docs/spec/v2/data/DATA_STRATEGY_V1.md`.

For eye recognition/benchmark changes, read:

1. `docs/spec/eye-recognition/DOOTAA_EYE_RECOGNITION_V1_FINAL_HANDOFF.md` —
   supersedes the older eye-recognition master; subsequent owner changes still apply.
2. `research/SUPERIOR_BENCHMARK_PLAN.md` — original investigation plan.
3. Current sections of `research/EYE_FRAMING_FEASIBILITY_REPORT.md` and
   `research/EYE_RECOGNITION_IMPLEMENTATION_AUDIT.md` — findings and gaps.
4. `research/BENCHMARK_PROTOCOL.md` and current `docs/CAPTURE-QC.md` — actual
   acquisition/diagnostic contracts.
5. Latest relevant evidence under `docs/qa/`; the close-eye checkpoint is
   `docs/qa/close-eye-2026-09-20/README.md`. Recheck for newer evidence.

The older `DOOTAA_EYE_RECOGNITION_RESEARCH_AND_CODEX_SPEC.md` supplies technical
context where not superseded; `deep-research-report.md` is research reference,
not implementation authority. Never rewrite supplied packages or their integrity
manifests to make a planned capability look implemented.

## Durable product rules

- Keep the supplied in-app `assets/brand/dootaa-logo.svg` through shared `Brand`.
  Launcher icon and compiled splash have different owners and require a native
  rebuild; check app config rather than assuming that changing `Brand` updates them.
- All active copy supports TH/EN with Thai default, Noto Sans Thai / Noto Sans
  400/600/700. Preserve the existing white/navy/blue/light-blue design direction.
  Reuse shared components. Keep primary camera controls visible on a phone;
  guidance must work without continually watching the screen.
- Normal customer copy avoids Demo/Mock labels while remaining truthful about
  unavailable assessment, local storage and account recovery. Internal metadata
  keeps honest provenance. The sign-in guide lives in `docs/ACCESS.md`; do not
  copy credentials into skills. Starter provisioning must not recreate deleted
  accounts, reset changed passwords or seed consent/images/history.
- Preserve account isolation, consent versions/event history, withdrawal,
  deletion recovery and real owner/session/file hashes. Back navigates through
  the actual entry stack; do not hardcode every back action to Profile/Home.
- Main screening uses physical-device camera data; Simulator/browser cannot
  substitute fake capture evidence. Legacy sample storage stays separate.
  `collected_unverified` is review-only, not verified five-gaze completion.
- Measured QC remains engineering evidence, not a diagnosis. Missing evidence
  cannot become normal/low risk, invented confidence or an automatic pass.
  Do not enable research collection/training or clinical models from a sample
  policy flag, source document or dataset URL.
- Read the **living** registry under root `data/`. Source version, purpose,
  access/license/provenance approval precede acquisition/use; manual import is
  not a bypass. Do not auto-accept terms, scrape gated sources or repurpose
  noncommercial research material commercially.
- Website username access is a server convenience gate, not real identity
  authentication or the app's local account. Keep its allowlist/rules in the
  owner source, protect direct routes/assets, and keep the server session secret
  out of clients/logs/Git. Hosted web opt-in must not loosen native release gates.

## Current checkpoint and historical traps

These facts were reconciled against the repo on 2026-09-21; refresh them from
source/evidence during pickup rather than treating this skill as live status.

- Active capture source is **V6 eye-local**, for a physically close, large,
  fully visible single eye. OpenCV eye candidates + MediaPipe iris-patch
  geometry replace the face-dependent active path. No display-only zoom or
  full-face/both-eyes prerequisite. Native `eyeLocalVersion: 1` is required.
- Later paragraphs headed 2026-09-17/V4 in retained docs are historical. V5
  stayed an offline experiment; V1–V5 recorded data retain their original
  validators. Inspect `live-policy.ts` and current capability before stating
  which version is active on a device; source and installed binary can differ.
- User reported partial success plus Inferior difficulty and possible wrong-
  direction acceptance. This is not independently labeled accuracy. Screenshot
  localization, Simulator/device builds and install/launch do not validate
  five-gaze recognition or successful exact-JPEG capture/storage.
- Fresh-neutral eye-axis diagnostics are separate from production classification.
  They do not mean personalized gaze calibration is active. Requested direction,
  spoken cue, operator neutral, system answer and independent human label remain
  separate; missing iris/pose/blink/confidence capabilities stay explicit.
- The guided comparison is **one roughly 45-second diagnostic round**, not
  45 seconds per gaze or a required consumer step. It has nine windows: fresh
  neutral, five direction controls, return to Primary and two wrong-target
  controls. Control windows run at least five seconds; the first two seconds of
  each control window are excluded from comparison. Initial reference acquisition
  can change total time.
  Both shutters are disabled; it advances by time without requiring a pass.
  It neither tunes thresholds nor calibrates automatically. Interruption stops
  the round; normal capture needs explicit resume. Use a separate normal-photo
  recording for post-shutter JPEG/storage failures.
- Current documented guided implementation has tests and browser component
  evidence, but no new physical guided export. Android native/camera validation
  remains pending in the cited checkpoint. Recheck latest evidence before
  carrying these blockers into a future handoff.
- Source registry entries and native model dependencies are different things.
  The current dataset docs report candidates without approved/ingested external
  datasets; query current registry/status before answering coverage questions.

Private diagnostics belong in ignored `.vercel/benchmarks/`. Copy only the
requested diagnostic artifact; keep real images, account exports, participant
identifiers and secrets out of Git/skills. No dataset, model training or medical
accuracy follows from procedural fixtures or simulated runs.

## Setup, commands and evidence

Read current `.nvmrc`, root `package.json` and `apps/mobile/package.json` for
versions. The documented setup uses Node 24 / pnpm 11 and root `pnpm-lock.yaml`.
`source scripts/dev-env.sh` selects project Node and JDK 17 in the current shell;
it currently requires Java even for iOS. For Node-only work without JDK, use the
Playbook's nvm/Node-only path rather than blocking on Android setup.

Command menu from `/Users/point/Projects/DOOTAA` — select only relevant actions:

| Purpose | Commands |
| --- | --- |
| Inspect changes | `git status --short --branch`, targeted `git diff`, `git diff --check` |
| Existing dev client / browser | `pnpm start` / `pnpm web`; reuse the correct existing Metro |
| Source checks | `pnpm typecheck`; targeted tests/lint, or root `pnpm test` / `pnpm lint` when scope warrants |
| Benchmark tooling | `pnpm test:benchmark`, `pnpm benchmark:validate <private-run.json>`, `pnpm benchmark:report <private-run.json> --out <new-private-output-dir>` |
| Dataset metadata and tests | `pnpm dataset:list`, `pnpm dataset:info <id>`, `pnpm dataset:check <id>`, `pnpm test:datasets` |
| SQL foundation | `pnpm test:research` uses local PGlite, not a remote migration |
| Native dependencies/build | `pnpm check:dependencies`; `pnpm eye:prepare-native` and Pods/build per Playbook only when that setup/change is in scope |
| Bundles | `pnpm export:mobile` is JS/assets export, not an IPA/APK |
| Website changes | `pnpm test:website`, `pnpm build:website`; authorized hosted checks/deploy per `docs/WEBSITE-DEPLOYMENT.md` |

Pure JS changes usually use Reload. Native module/config/plugin/icon changes
require a rebuilt development client; Expo Go cannot supply this local camera
module. Inspect installed CLI help before prebuild: the documented Expo 57
requires explicit `--no-clean` for incremental generation. Preserve custom
native edits and caches; never run destructive regeneration as onboarding.
The device build cache is `.vercel/native-build/DOOTAADevice` in the Playbook.

On the documented 8 GB Mac, avoid concurrent native/large JS builds; start with
two workers when appropriate. Discover current device IDs, signing and server
port; no stored personal IDs or borrowed LAN URLs. If iPhone is unavailable,
continue independent work and list exact pending hardware checks. Do not ask
the user to repeat the same physical failure without collecting new evidence.

Keep source checks, JS export, native build, install/launch, actual feature use
and deployment as distinct claims. Markdown-only onboarding updates need links,
source/command consistency and diff checks, not camera tests or native builds.
Keep living docs current when behavior or evidence changes; do not duplicate
PROJECT_MAP/PLAYBOOK/ROADMAP into another generic project-memory file.

## Copy-ready new-chat prompt

Adapt the task paragraph and verified state; keep the prompt short:

```text
ทำงานต่อโปรเจกต์ DOOTAA / ดูตา ที่ /Users/point/Projects/DOOTAA
ใช้ $dootaa-new-chat และอ่านไฟล์ปัจจุบันก่อน ไม่อิงความจำจากแชตเก่า

เริ่มจาก git status, AGENTS.md, README.md, docs/PROJECT_MAP.md และส่วนที่เกี่ยวข้องใน
docs/PLAYBOOK.md แล้วอ่านเอกสารเฉพาะงานตาม
/Users/point/.codex/skills/dootaa-new-chat/references/new-chat-context.md
งาน setup/build ให้ใช้ $ios-app-development ประกอบกับ Playbook

รักษา TH/EN (TH หลัก), Noto Sans, branding/shared components และ flow เดิม
งานกล้องยึดตาระยะใกล้ทีละข้าง ตรวจ policy/หลักฐานล่าสุด ไม่ย้อนกลับไปใช้ข้อกำหนดเก่า
แยกคำสั่งให้มองออกจากทิศที่ตรวจพบจริง และแยกการเก็บภาพออกจากการยืนยันว่าผ่าน
ห้ามเติมข้อมูล/ผลโรค/ความแม่นยำที่ไม่มีหลักฐาน รักษา account/consent/provenance
อย่า restart โปรเจกต์ ล้างข้อมูล หรือทับงานที่ค้างอยู่
ยังไม่ commit/push/deploy/train/migrate หรือเข้าถึงแชตอื่นถ้าฉันยังไม่ได้สั่ง

งานรอบนี้: [ระบุงาน]
หลังอ่าน สรุปสั้น ๆ ว่าตอนนี้ทำอะไรได้จริง ยังไม่ยืนยันอะไร แล้วทำงานที่สั่งต่อเลย
```
