# DeepX source protection

Use the active DeepX checkout. The primary checkout is
`/Users/point/Website Projects/DeepX`. The maintained owner contract is
`docs/CONTENT_PROTECTION.md`, with release evidence in `docs/RELEASE.md`.
The November 2026 notes record historical cloud policy. Inspect current
settings before relying on plan limits, rule status or repository visibility.

| Responsibility | Source |
| --- | --- |
| First-party JS transformation | `scripts/protect-build.ts`, registered in `vite.config.ts` |
| Public assets and private function packaging | `vite.config.ts`, `scripts/build-catalogue-server.mjs`, `api/`, `vercel.json`, `.vercelignore` |
| Build gate and route preloads | `scripts/check-public-build.mjs`, `scripts/check-route-bundles.mjs`, `scripts/route-preloads.mjs`, `package.json` |
| Published document requests | `src/content.ts`, `server/published-content.ts`, the Supabase published RPC and policy migrations |
| Crawler preference and recorded edge rules | `public/robots.txt`, `security/firewall-policy.json`, `docs/CONTENT_PROTECTION.md` |

DeepX's Vite plugin runs for production and transforms chunks containing
first-party code. Vendor-only chunks retain minification and consumer-based
splitting. The plugin seeds its transform from each chunk's input and uses
`browser-no-eval`, encoded strings, identifier renaming and selective
control-flow changes. Imports, global and property names retain their public
contracts. `debugProtection`, `selfDefending`, `deadCodeInjection` and
`disableConsoleOutput` are false for predictable runtime and debuggability.
The plugin records internal byte counts for review.

Vercel serves `dist/` as static output. DeepX writes the build manifest,
obfuscation metrics, route-preload metadata and server handlers to `.build/`.
The generated catalogue and portfolio functions explicitly include their
private preload metadata. The historical leak included
`/server/clinic-handler.mjs`, `/.vite/manifest.json` and
`/route-preloads.json`. Recheck known paths against the candidate after
changing build roots, static copies, include rules or rewrites. Preserve the
existing route-bundle and protected-output gates in `npm run build`.

The recorded edge policy combines a bot challenge, managed AI-bot rules,
and a scoped limit on public reads including the catalogue API. The browser's
published Supabase RPC and public media URLs are separate read surfaces.
For future changes, review staged and active rules, applicable plan and
deployment authorization. Count browser and API requests together when they
share a limit. The November 13 smoke recovered from 429 by waiting for the
existing window and resuming only unfinished probes. Check crawler recognition
through the provider's verified handling.
