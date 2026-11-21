---
name: numchok-fitness-new-chat
description: Load current context for the Numchok Fitness storefront and CMS. Use for a new chat, project handoff, or context refresh before continuing work on Numchok Fitness or numchokfitness.vercel.app.
---

# Numchok Fitness New Chat

## Start here

- Open `/Users/point/Website Projects/Numchok Fitness` and run `git status --short --branch`. Read project instructions if present and use the current branch and files as the source of truth. Preserve existing worktree changes.
- Read `vercel.json` for routing, then the owner files for the user's task. The project is a Thai-language fitness equipment and repair website built with static HTML, CSS, and native browser modules. Its current checkout has no package build step.
- Onboarding stays in the current chat. When a task accompanies it, continue that task. For onboarding alone, give a short summary of verified context and current limits.

## Routes and source map

| Surface | Route | Owners |
| --- | --- | --- |
| Homepage | `/` | `index.html`, `app.js`, `storefront.js`, `site-content.js`, `styles.css` |
| Catalog | `/catalog.html?category=treadmill` | `catalog.html`, `storefront.js`, `components.js` |
| Product detail | `/product.html?model=d300` | `product.html`, `product-detail.js`, `product.css`, `components.js` |
| Shared storefront header and footer | Public routes | `layout.js`, `storefront.js`, `styles.css` |
| CMS dashboard | `/admin` | `admin/index.html`, `admin/dashboard.js`, `admin/shell.js` |
| CMS content list and editor | `/admin/content`, `/admin/content/edit?id=home` | `admin/content.js`, `admin/content-edit.js`, `admin/content-sections.js`, `site-content.js` |
| CMS product list and editor | `/admin/products`, `/admin/products/edit?id=d300` | `admin/products.js`, `admin/product-edit.js`, `admin/product-data.js`, `products.js` |

## Preserve these contracts

- The CMS is a browser-local demo. `admin/demo-data.js` owns the shared `numchok-cms-demo-v1` localStorage record and its migration of existing data. A fresh browser uses bundled initial content. Saves on one device do not publish globally. Real accounts and shared persistence need a separate request.
- Read editable product and content values through the shared CMS data. Avoid duplicate public hardcoded values. Keep unsupported CMS features hidden until there is a matching public or operational workflow. Preserve saved records for hidden sections.
- Preserve the draft, preview, and publication distinction. The storefront only shows published products, including on direct links. Stable product IDs and configured slugs both resolve. Preview uses the actual storefront in a same-origin iframe with the ready-message handshake in `admin/site-preview.js` and `app.js`. Preview overrides stay in memory.
- `site-startup.js` and `site-startup.css` own initial storefront loading. Keep the page hidden until CMS data, route CSS, and Thai and Latin Prompt fonts are ready. The skeleton appears after about 280 ms. Load failure or the 12-second deadline shows a retry action. Preserve public hash links and CMS preview readiness when changing startup.
- Reuse the project's Thai copy, Prompt typography, red and charcoal brand, and shared public or CMS components. Use `ui-ux-expert` and `snapshot` for visible work, and `mockup-to-product` when the user supplies a design reference. Verify the relevant responsive layouts. The existing mockups include 390 px mobile, 768 px portrait tablet, and 1365 px landscape tablet.

## Run and verify

- Reuse the local preview at `http://127.0.0.1:49362/` if it is serving this checkout. Otherwise run `node review/serve.cjs` from the repository when available. On a clean clone, use a local server that follows the rewrites in `vercel.json` so the clean `/admin` URLs resolve.
- `review/` is local and ignored. When present, `node review/cms-connection/check.cjs` covers CMS to storefront behavior. `PW_TEST_SCREENSHOT_NO_FONTS_READY=1 node review/storefront-loading/check.cjs` covers delayed loading, retry, and deep links. Use fresh browser storage and avoid touching real visitor data when testing. Run focused checks for the current change and inspect the final Git diff.

## Release

- Established targets are GitHub `purichw/Numchok-Fitness` on `main` and Vercel project `purich-w/numchokfitness` at [numchokfitness.vercel.app](https://numchokfitness.vercel.app). Verify the current remote, Vercel link, and production deployment when release is in scope.
- With current authorization, use `release-gate` and the Vercel deploy skill. Releases have used the linked project and Vercel CLI because GitHub auto-deploy was disabled. Check the active configuration before triggering a deployment so the same revision is released once.
- Verify the pushed SHA and production alias separately, then exercise the affected routes on the real URL. Treat commit, push, deploy, custom-domain changes, and production data writes as separately authorized actions. Never copy credentials or domain transfer codes into the skill, repo, or handoff.
