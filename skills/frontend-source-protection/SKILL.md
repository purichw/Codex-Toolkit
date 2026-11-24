---
name: frontend-source-protection
description: Reduce frontend source exposure and bulk extraction of public web data. Use when auditing or implementing production JavaScript obfuscation, private build artifacts and source maps, published API data boundaries, or targeted anti-scraping controls for an owned website.
---

# Frontend Source Protection

Treat JavaScript, HTML and data sent to a browser as observable. Use
obfuscation to increase the effort of casual code reuse. Keep confidential
logic, data and credentials behind a server-side authorization boundary.
Use [frontend-copy-deterrence](../frontend-copy-deterrence/SKILL.md) for
selection, copy, drag and image-save behavior on a rendered page.

## Inspect what the site delivers

1. Identify the asset and who needs it. Trace the production HTML, JS/CSS and
   source maps, the build manifest and static upload root, server packages,
   JSON payloads and direct API or storage origins relevant to the request.
   Check repository visibility and permissions when protecting proprietary
   source. Look at the actual build output and route behavior as well as config.
2. Keep private source packages, build manifests, server handlers, tests,
   migration files, credentials and debug maps outside the static output
   root. Package server dependencies and preloads through the hosting
   platform's function mechanism. Keep source maps private if authorized
   monitoring needs them. An environment variable included by the client
   bundler belongs to the public surface.
3. For sensitive content, check the authorization applied to the data
   request itself. Expose the published fields needed by the page. Validate
   access to drafts, records and original files at the API, database or
   storage owner. Include direct upstream endpoints when assessing what an
   intermediary cache or firewall can cover.

## Choose the minimum effective change

- For bulk reads, scope edge or application rate rules to the affected
  published routes and methods. Include direct API paths part of that scope.
  Preserve public navigation, assets, editor/preview and form requests, and
  the owner's search discovery requirements. Base trusted crawler exceptions
  on verified identity when available. Treat robots directives as crawler
  preferences. Check the provider's current behavior and plan before modifying
  a live rule. Follow the project's authorization for visibility, firewall or
  release changes.
- For DeepX, read [the project example](references/deepx.md) to find the
  obfuscation plugin, artifact gates and policy owners. Start with the current
  checkout and release runbook.

## Obfuscate first-party production JavaScript

1. Distinguish minification and disabled source maps from obfuscation. When
   obfuscation is requested, run it only for the production browser build.
   Identify first-party and vendor chunks by module origin, and separate mixed
   chunks before transforming them. Check inline first-party scripts too,
   especially startup code that needs to run before first paint.
2. Transform emitted browser code after tree shaking and before content hashes
   and preload references are finalized. Preserve imports, exports, externally
   read property names, storage keys, localization, licensing, and the deployed
   CSP. Use a reproducible seed and a no-eval target where supported. Start with
   narrow identifier and string transformations. Leave runtime debugger traps,
   self-defending code, and heavy control-flow transforms off by default.
3. Compare transformed production output with the readable development build
   and untouched vendor assets. Measure the bundle cost and test affected
   browser flows against the actual production build before a requested push
   or deploy. For a storefront, cover checkout, payment confirmation,
   proof-of-payment upload and review, and saving and resuming payment later
   when supported. Use test data and preserve the site's payment boundaries.

## Verify the delivered protection

- Inspect a clean production output for private artifacts and source-map
  references. Check that functions still have their package and that expected
  CSS/JS URLs resolve. On an authorized candidate or deployment, check known
  former public paths for status and response type/body. A generic HTML shell
  or denial must never include the private file's contents.
- Compare output size and boot/lazy-load behavior after obfuscation. Exercise
  the affected published pages and representative preview/editor routes.
  Use the project's build and route-budget gates. Follow
  [release-gate](../release-gate/SKILL.md) for an authorized release.
- For a rate-limit change, exercise normal traffic and a bounded check against
  an authorized target. Track shared request budgets and distinguish a platform
  challenge or 429 from an application failure. Check effective policy and
  recovery before retrying. Report the revision, route, access mode and
  observed result for each check.
