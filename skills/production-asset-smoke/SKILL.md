---
name: production-asset-smoke
description: Verify deployed website media and asset rendering after image, video, CMS, fallback, or deploy changes. Use when the user says images/videos are missing or asks to prove production/preview assets load; check for broken images, stale external media domains, lazy-load false positives, ORB/CORS-blocked assets, missing bundled files, bad fallbacks, failed poster/video sources, and asset request failures, especially after placeholder-image, release-gate, prod-smoke-harness, or snapshot work.
---

# Production Asset Smoke

Use this skill when assets are part of the shipped experience. It complements
`$prod-smoke-harness` and `$release-gate`: those prove the app is reachable and
the flow works; this proves the deployed media actually renders.

## Core Rule

Do not trust local screenshots, HTTP 200 for the page, or static file existence
as proof that production media is healthy. Verify the deployed URL in a browser,
scroll through lazy-loaded content, inspect DOM media sources, and record
failed requests plus stale external domains.

Use `$snapshot` for visual evidence, `$placeholder-image` for sourcing/crop
decisions, and `$release-gate` before commit, push, deploy, or handoff.

## What To Check

- `<img>` elements: `currentSrc`, `complete`, `naturalWidth`, `naturalHeight`,
  `loading`, and whether lazy images load after scrolling.
- CSS `background-image` URLs on visible/content sections.
- `<video>`, `<source>`, and poster URLs when media is present.
- Browser `requestfailed` events, console/page errors, and blocked media such
  as ORB/CORS/MIME failures.
- Stale or retired domains, buckets, filenames, data URLs, and old CDN paths.
- Production bundle availability: deployed asset paths, service-worker/cache
  interference, and cache-busted reloads.
- Fallback behavior: broken or retired assets should become an intentional
  local/generated fallback or a designed placeholder, not a blank box.

## Workflow

1. Identify the target deploy URL, commit/build, route list, and changed media
   surfaces.
2. Add a cache buster to the URL unless the deploy artifact is already unique.
3. Render each route in a browser. Wait for DOM content, then scroll from top
   to bottom in steps so lazy images mount.
4. Inspect DOM media URLs and network failures. Treat stale domains as failures
   even when the browser has not attempted to load them yet.
5. Capture wide `$snapshot` evidence for the highest-risk route or create a
   contact sheet when several routes changed.
6. If failures appear, decide whether to repair data, replace assets, add a
   public fallback, or document an intentional external dependency.
7. Rerun the smoke after the fix on the final deployed URL.

## Script

Use the bundled Playwright helper when a quick automated pass is useful:

```bash
node /Users/point/.codex/skills/production-asset-smoke/scripts/asset_smoke.js \
  --url https://example.com \
  --route / \
  --route '#/gallery' \
  --stale-domain res.cloudinary.com/old-bucket \
  --screenshot-dir /tmp/example-asset-smoke
```

Run it from a project that already has `playwright` installed, or install
Playwright in the environment first. The helper tries the skill environment and
then the current working directory's `node_modules`.

Optional flags:

- `--viewport 1440x1600`
- `--wait 1200`
- `--scroll-step 900`
- `--no-screenshots`
- `--allow-console-errors`

The script exits nonzero when a route has broken images, incomplete images
after full-page scroll, stale media URLs, failed asset requests, console/page
errors, or non-2xx/3xx responses.

## Failure Policy

Block release unless clearly unrelated or accepted:

- broken `<img>` after route scroll;
- stale media domain or retired CDN URL in DOM;
- request failure for image, font, stylesheet, script, video, API-backed media,
  or CSS background;
- console/page error caused by media loading or render;
- page rendered from stale build or wrong route;
- fallback produces blank space, invisible label, overlapping text, or an
  obviously wrong crop.

Potentially nonblocking noise must be named, not hidden:

- analytics/ad pixels blocked by privacy tools;
- websocket/long-poll aborts from closing the browser after assertions;
- external embeds intentionally blocked with a designed fallback.

## Closeout

Report compactly:

```text
Target:
Commit/build:
Routes smoked:
Media checked:
Stale domains checked:
Broken/incomplete/failed requests:
Snapshots:
Decision:
Residual risk:
```
