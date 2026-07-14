---
name: uat-environment
description: Design, implement, audit, or use lightweight UAT/preview environments before production. Use for production-like preview URLs, seeded test data, auth bypass policy, test accounts, environment isolation, feature flags, admin/data/API validation, promotion gates, rollback checks, or deciding what must be verified in UAT versus local or production.
---

# UAT Environment

Use this skill when a change needs realistic verification before production but
does not justify turning every commit into a heavy release ceremony.

## Goal

Create a lightweight, production-like UAT/preview environment that catches
integration, UI, auth/data, admin, mobile, asset, and deploy issues before
production. UAT should be fast, isolated, resettable, and honest about what it
does and does not prove.

UAT is for T3-T5 risk: frontend UI, auth/data/API/config, admin/CMS, migrations,
generated assets, Claude parity, mobile QA, and deploy readiness. It is usually
not required for docs-only or tiny non-runtime changes.

Use `$efficient-execution` to keep UAT lightweight. The goal is a small,
resettable environment that proves the changed risk, not a second production
process for every commit.

## Environment Contract

At minimum define:

- UAT URL or preview deployment and how it is created;
- build source: branch, preview build, saved version, or release candidate;
- env vars and secrets, separate from production;
- database/storage target, seed/reset strategy, and data retention;
- test accounts, roles, bypasses, and credentials handling;
- external services: sandbox, stub, fake, read-only, or production-safe;
- observability: console, network, logs, errors, analytics isolation;
- promotion rule: what evidence lets UAT move to production.

Never clone production data casually. Prefer production-shaped synthetic data,
small sanitized snapshots, or seeded fixtures.

## Auth Bypass Policy

Auth should be bypassable in UAT when auth is not the feature under test. This
keeps UAT fast and prevents every UI/admin/data check from becoming a login
debugging session.

Allowed bypass patterns:

- test-only route or query flag enabled only in UAT/test builds;
- signed test session fixture or seeded token;
- role selector backed by synthetic test users;
- local emulator/test provider;
- server-side bypass guarded by UAT-only env var and non-production host.

Required safeguards:

- bypass code must be impossible or inert in production;
- UAT bypass must be visible in docs/config and easy to search;
- bypass must not grant access to production data or production secrets;
- privileged/destructive actions still need explicit fake/sandbox boundaries;
- UAT reports must say when auth was bypassed.

Do not bypass auth when the change is about login/signup, OAuth/provider config,
session expiry, roles/claims, password reset, invite acceptance after login,
permission denial, account deletion, or any security boundary. For those tasks,
test real auth paths with test accounts and use `$firebase-account-management`
or `$firebase-security-rules` when relevant.

## Data And Reset

UAT data should be realistic enough to exercise product behavior:

- normal, empty, loading, error, long-label, multilingual, and edge-case records;
- admin/user/guest/role variants;
- draft/published/archived/deleted lifecycle states;
- generated asset references and missing/failed asset cases;
- migration/backward-compatible records when data shape changes.

Provide a reset command or documented manual reset. If reset is expensive, define
a small stable fixture set and a cleanup policy. Never let UAT drift so far that
test results depend on accidental old state.

## Minimum Viable UAT Loop

1. Deploy or open the preview build for the exact branch/version.
2. Seed only the roles and data states required by the changed risk.
3. Use test-only auth bypass when auth is not under test; use real test accounts
   when auth, roles, or permissions are under test.
4. Verify the smallest set of flows that can fail because of the change.
5. Record URL, build, fixture, auth mode, checks, skips, and rollback.

Escalate to broader UAT only for shared layout, admin/data lifecycle, auth/rules,
migrations, generated asset maps, Claude parity, mobile-critical releases, or
production promotion.

## What To Verify In UAT

Choose checks by risk:

- **UI/mobile:** changed routes, responsive breakpoints, sticky/fixed elements,
  console/network errors, screenshots via `$snapshot`, `$mobile-web-qa`.
- **Admin/CMS:** create/edit/publish/restore/delete, audit logs, revisions,
  permissions, and public rendering via `$admin-ops`.
- **Auth/data/API:** real or bypassed auth according to scope, read/write paths,
  permission denied cases, migrations, rollback, rules via Firebase skills when
  relevant.
- **Claude parity:** rendered reference vs UAT build with `$claude-to-a-tee`.
- **Assets/audio/images:** mapping audits, representative rendered UI, failed
  asset handling via `$tts-audio-assets` or `$course-image-assets`.
- **Deploy:** correct commit/build id, env target, URL, service worker/cache,
  logs, and rollback path via `$release-gate`.

## Promotion Gate

Before production, record:

```text
UAT URL:
Build/commit/version:
Data fixture/reset:
Auth mode: real / bypassed / mixed
Roles/accounts tested:
Routes/flows:
Checks run:
Screenshots/logs:
Known skips:
Decision:
Rollback:
```

Production promotion is allowed only when UAT evidence covers the highest-risk
touched surface, skipped checks are explicit, test data is isolated, auth mode is
appropriate to the change, and rollback/recovery is known.

## Anti-Patterns

- using production as UAT;
- cloning production user data without a clear sanitization and access policy;
- UAT sharing production secrets unnecessarily;
- auth bypass that can run in production;
- stale preview URL with an old build;
- UAT that cannot be reset;
- checking only HTTP 200 for a UI/data/admin change;
- requiring UAT for docs-only changes and slowing everything down.

## Closeout

Report the UAT target, build/version, data source, auth mode, flows verified,
evidence captured, skips, promotion decision, and residual risk. If UAT does not
exist yet, propose the minimum viable setup and which checks remain local-only
until it exists.
