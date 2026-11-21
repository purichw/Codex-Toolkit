---
name: kk-fitness-new-chat
description: Onboard or refresh a Codex chat for the KK Fitness storefront. Use when starting or resuming work on KK Fitness, picking up a handoff, or asking for a KK Fitness new-chat prompt.
---

# KK Fitness New Chat

Use the checkout specified by the user, or `/Users/point/Projects/KKFitness` by default. The GitHub repository is `purichw/KKFitness`, the production branch is `main`, and the production domain is [kk-fitness.vercel.app](https://kk-fitness.vercel.app/).

## Start from the current checkout

1. Read applicable `AGENTS.md` instructions, including `/Users/point/.codex/AGENTS.md`. Check `git status --short --branch` before editing and preserve unrelated changes.
2. Read the checkout’s `README.md` and the files that own the requested behavior. Use `package.json` for local commands and `vercel.json` for the build contract. Verify the deployed revision separately when production state matters.
3. Continue the accompanying task in the current chat. For onboarding alone, summarize the verified project state and relevant limits. For a prompt request, give a copy-ready invocation with the project path and requested work. Cross-chat actions require separate explicit authorization.

## Find the owner

| Area | Entry point |
| --- | --- |
| Home and navigation | `src/pages/index.astro`, `src/components/SiteHeader.astro`, `src/components/SiteFooter.astro`, `src/store.ts` |
| Catalogue and product detail | `src/catalog.ts`, `src/pages/products.astro`, `src/catalog-browser.ts`, `src/pages/products/[id].astro` |
| Cart and checkout | `src/pages/cart.astro`, `src/cart-browser.ts`, `src/pages/checkout.astro` |
| Transfer, pay later and proof | `src/pages/payment.astro`, `src/pages/payment-later.astro`, `src/pages/payment-notification.astro`, `src/components/PaymentEvidenceReceipt.astro` |
| Loading and retry | `src/components/StoreReadiness.astro`, `src/components/StoreLoading.astro` |

## Preserve the storefront behavior

- Astro pre-renders the storefront from local catalogue records. Check the checkout for a real CMS integration before treating catalogue data as a runtime fetch. Current prices, availability, shipping fees and bank details require confirmation from the store.
- DCMD67 at `/products/501` is the complete product demo and appears first in the default catalogue order. Unfinished product details and secondary navigation use the local preparation page. Keep existing phone, LINE and social contact actions.
- The cart, checkout review, pay-later draft and evidence receipt are browser-side flows. Bank transfer is the payment method. Keep the evidence receipt clear that the file is still local and must be sent to the team. Adding real order creation, evidence submission, payment methods or payment deadlines requires an explicit feature request.
- Keep the readiness gate in the document head. Reveal the storefront after the required fonts, marked primary imagery and browser-prepared content are ready. Use `store:content-ready` after initialization on pages that opt in. Verify the delayed skeleton and the retry action under a simulated failure when touching the gate.

## UI and release

- Preserve the existing Thai-first design and route proportions across desktop, tablet and mobile. Reuse `Action`, `Breadcrumbs`, `Panel` and the purchase layout where they already own a shared pattern. Use `ui-ux-expert` for visible work, `mockup-to-product` for supplied mockups and `snapshot` to inspect the changed browser states. Match the checks to the change.
- Use `npm run dev` for edits and `npm run build` for the static `dist/` artifact. Reuse a healthy local preview when available.
- Commit, push and deploy only when authorized for the current work. For an authorized release, use `release-gate` and `vercel:deploy`. Check whether the project has automatic Git deployment before starting a CLI deployment. Confirm the pushed SHA, Vercel readiness and the production domain serving the same revision.

Example invocation: `$kk-fitness-new-chat อ่านบริบทล่าสุด แล้วปรับหน้ารายการสินค้าตามภาพแนบ`
