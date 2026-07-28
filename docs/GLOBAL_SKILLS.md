# Global Skills

This page lists reusable, non-project-specific skills and their explicit
`global-*` names. Most `global-*` folders are thin aliases for canonical skills;
some are standalone global skills.

Use the `global-*` name when the user wants to be clear that the reusable/global
version should run.

## Standalone Global Skills

| Global skill | Context |
| --- | --- |
| [`global-full-design-spec`](../skills/global-full-design-spec/SKILL.md) | Export comprehensive implementation-ready UI design specs from screenshots, source files, CSS, routes, prototypes, live app state, or design references. |
| [`global-quick-design-spec`](../skills/global-quick-design-spec/SKILL.md) | Export concise implementation-ready UI design specs quickly from screenshots, source files, CSS, routes, prototypes, or live app state. |

## Alias Policy

- Canonical skills keep their original names so existing references still work.
- `global-*` folders route to the canonical skill's `SKILL.md`.
- Update the canonical skill first. Regenerate the alias only if alias routing
  language or metadata needs to change.
- If the canonical skill has `$snapshot` or visual-evidence requirements, the
  global alias must preserve them; an alias is not a bypass around the snapshot
  gate.
- Do not create `global-*` aliases for project-specific skills.

## Global Alias Map

| Global alias | Canonical skill | Context |
| --- | --- | --- |
| [`global-accessible-interaction`](../skills/global-accessible-interaction/SKILL.md) | [`accessible-interaction`](../skills/accessible-interaction/SKILL.md) | Accessibility, keyboard, focus, ARIA, contrast, touch, and modal/drawer behavior across projects. |
| [`global-account-recovery-key`](../skills/global-account-recovery-key/SKILL.md) | [`account-recovery-key`](../skills/account-recovery-key/SKILL.md) | Provider-neutral recovery-key flows for auth and account reset patterns. |
| [`global-admin-ops`](../skills/global-admin-ops/SKILL.md) | [`admin-ops`](../skills/admin-ops/SKILL.md) | Reusable admin portal, CMS, back-office, operator, lifecycle, and privileged-action workflows. |
| [`global-admin-prototype-reconciliation`](../skills/global-admin-prototype-reconciliation/SKILL.md) | [`admin-prototype-reconciliation`](../skills/admin-prototype-reconciliation/SKILL.md) | Reconciling admin/CMS/dashboard prototypes against live admin contracts. |
| [`global-claude-design-md-request`](../skills/global-claude-design-md-request/SKILL.md) | [`claude-design-md-request`](../skills/claude-design-md-request/SKILL.md) | Asking Claude Design for implementation-ready Markdown handoffs/specs. |
| [`global-claude-design-reference-bundle`](../skills/global-claude-design-reference-bundle/SKILL.md) | [`claude-design-reference-bundle`](../skills/claude-design-reference-bundle/SKILL.md) | Claude Design reference bundles with screenshots, measured specs, product contracts, and prompts. |
| [`global-claude-to-a-tee`](../skills/global-claude-to-a-tee/SKILL.md) | [`claude-to-a-tee`](../skills/claude-to-a-tee/SKILL.md) | Component-level visual parity from Claude/offline HTML references. |
| [`global-codex-handoff-for-claude`](../skills/global-codex-handoff-for-claude/SKILL.md) | [`codex-handoff-for-claude`](../skills/codex-handoff-for-claude/SKILL.md) | Codex-to-Claude implementation handoffs with contracts and acceptance checks. |
| [`global-consistency-audit`](../skills/global-consistency-audit/SKILL.md) | [`consistency-audit`](../skills/consistency-audit/SKILL.md) | UI/UX/frontend/shared-component consistency audits. |
| [`global-course-image-assets`](../skills/global-course-image-assets/SKILL.md) | [`course-image-assets`](../skills/course-image-assets/SKILL.md) | Educational course image generation, mapping, cropping, and QA. |
| [`global-data-dense-ux`](../skills/global-data-dense-ux/SKILL.md) | [`data-dense-ux`](../skills/data-dense-ux/SKILL.md) | Dashboards, tables, lists, ledgers, filters, bulk actions, and dense operational UI. |
| [`global-design-direction`](../skills/global-design-direction/SKILL.md) | [`design-direction`](../skills/design-direction/SKILL.md) | Product visual direction, design briefs, guardrails, and implementation handoffs. |
| [`global-design-system-guardian`](../skills/global-design-system-guardian/SKILL.md) | [`design-system-guardian`](../skills/design-system-guardian/SKILL.md) | Component/token drift prevention and design-system consistency. |
| [`global-accessibility-beyond-basics`](../skills/global-accessibility-beyond-basics/SKILL.md) | [`accessibility-beyond-basics`](../skills/accessibility-beyond-basics/SKILL.md) | Advanced accessibility beyond axe checks for screen-reader flow, cognitive load, low vision, complex widgets, charts, zoom, and forced colors. |
| [`global-art-direction-imagery`](../skills/global-art-direction-imagery/SKILL.md) | [`art-direction-imagery`](../skills/art-direction-imagery/SKILL.md) | Directs imagery, crops, focal points, hero media, thumbnails, placeholders, captions, loading states, and asset failure states. |
| [`global-design-quality-review`](../skills/global-design-quality-review/SKILL.md) | [`design-quality-review`](../skills/design-quality-review/SKILL.md) | Applies the shared design-quality rule language, severity model, screenshot QA protocol, calibration library, and definition of done. |
| [`global-visual-diagnosis`](../skills/global-visual-diagnosis/SKILL.md) | [`visual-diagnosis`](../skills/visual-diagnosis/SKILL.md) | Names visible UI defects such as cheap, cramped, scattered, generic, heavy, low-trust, or unfinished using observable rules. |
| [`global-domain-taste`](../skills/global-domain-taste/SKILL.md) | [`domain-taste`](../skills/domain-taste/SKILL.md) | Chooses category-appropriate density, hierarchy, controls, and evidence for admin, SaaS ops, dashboards, ledgers, editorial, learning, landing, and mobile screens. |
| [`global-information-architecture-ux`](../skills/global-information-architecture-ux/SKILL.md) | [`information-architecture-ux`](../skills/information-architecture-ux/SKILL.md) | Structures navigation, grouping, hierarchy, progressive disclosure, screen purpose, and sequencing. |
| [`global-interaction-design`](../skills/global-interaction-design/SKILL.md) | [`interaction-design`](../skills/interaction-design/SKILL.md) | Designs real UI interactions including autosave, undo, bulk actions, optimistic updates, permissions, interruption recovery, and destructive flows. |
| [`global-mobile-native-feel`](../skills/global-mobile-native-feel/SKILL.md) | [`mobile-native-feel`](../skills/mobile-native-feel/SKILL.md) | Audits mobile UI for safe areas, native controls, touch targets, keyboard behavior, thumb reach, sheets, gestures, and platform feel. |
| [`global-design-system-architect`](../skills/global-design-system-architect/SKILL.md) | [`design-system-architect`](../skills/design-system-architect/SKILL.md) | Architects tokens, component taxonomies, variants, galleries, drift metrics, and token-layer governance. |
| [`global-typography-refinement`](../skills/global-typography-refinement/SKILL.md) | [`typography-refinement`](../skills/typography-refinement/SKILL.md) | Refines type scale, measure, line-height, multilingual behavior, numeric data, dates, units, truncation, and typographic rhythm. |
| [`global-motion-choreography`](../skills/global-motion-choreography/SKILL.md) | [`motion-choreography`](../skills/motion-choreography/SKILL.md) | Specifies UI motion timing, easing, choreography, loading feedback, overlay transitions, scroll motion, and reduced-motion alternatives. |
| [`global-reference-implementation-critique`](../skills/global-reference-implementation-critique/SKILL.md) | [`reference-implementation-critique`](../skills/reference-implementation-critique/SKILL.md) | Compares reference design and implementation across geometry, rhythm, hierarchy, density, visual weight, affordance, states, and product decisions. |
| [`global-taste-calibration`](../skills/global-taste-calibration/SKILL.md) | [`taste-calibration`](../skills/taste-calibration/SKILL.md) | Uses paired works/fails specimens and calibration drills to improve UI taste with measurable smallest-change loops. |
| [`global-docs-cartographer`](../skills/global-docs-cartographer/SKILL.md) | [`docs-cartographer`](../skills/docs-cartographer/SKILL.md) | Architecture, route, module, data-flow, command, and handoff documentation. |
| [`global-efficient-execution`](../skills/global-efficient-execution/SKILL.md) | [`efficient-execution`](../skills/efficient-execution/SKILL.md) | Faster quality-preserving workflows, batching, and scoped evidence. |
| [`global-export-html`](../skills/global-export-html/SKILL.md) | [`export-html`](../skills/export-html/SKILL.md) | Standalone/offline HTML exports and clickable prototypes. |
| [`global-firebase-account-management`](../skills/global-firebase-account-management/SKILL.md) | [`firebase-account-management`](../skills/firebase-account-management/SKILL.md) | Firebase Auth users, profiles, Admin SDK, custom claims, and account flows. |
| [`global-firebase-security-rules`](../skills/global-firebase-security-rules/SKILL.md) | [`firebase-security-rules`](../skills/firebase-security-rules/SKILL.md) | Firestore Rules, Auth authorization, Admin SDK boundaries, and Firebase security. |
| [`global-form-flow-ux`](../skills/global-form-flow-ux/SKILL.md) | [`form-flow-ux`](../skills/form-flow-ux/SKILL.md) | Complete create/edit form journeys and validation/error states. |
| [`global-interaction-flow-qa`](../skills/global-interaction-flow-qa/SKILL.md) | [`interaction-flow-qa`](../skills/interaction-flow-qa/SKILL.md) | End-to-end UI/UX journey verification. |
| [`global-ledger-logic`](../skills/global-ledger-logic/SKILL.md) | [`ledger-logic`](../skills/ledger-logic/SKILL.md) | Collaborative ledger math, identity, guests, invites, and settlement behavior. |
| [`global-mobile-web-qa`](../skills/global-mobile-web-qa/SKILL.md) | [`mobile-web-qa`](../skills/mobile-web-qa/SKILL.md) | Responsive web QA across phone, tablet, and desktop. |
| [`global-native-parity`](../skills/global-native-parity/SKILL.md) | [`native-parity`](../skills/native-parity/SKILL.md) | Native iOS/Android parity with web/product source of truth. |
| [`global-placeholder-image`](../skills/global-placeholder-image/SKILL.md) | [`placeholder-image`](../skills/placeholder-image/SKILL.md) | Placeholder image sourcing, replacement, crop, and audit workflows. |
| [`global-prod-smoke-harness`](../skills/global-prod-smoke-harness/SKILL.md) | [`prod-smoke-harness`](../skills/prod-smoke-harness/SKILL.md) | Production/preview smoke harness policy and evidence. |
| [`global-product-ux-contracts`](../skills/global-product-ux-contracts/SKILL.md) | [`product-ux-contracts`](../skills/product-ux-contracts/SKILL.md) | Preserving product behavior while redesigning or refactoring UI. |
| [`global-production-asset-smoke`](../skills/global-production-asset-smoke/SKILL.md) | [`production-asset-smoke`](../skills/production-asset-smoke/SKILL.md) | Deployed media and asset rendering checks. |
| [`global-project-onboarding`](../skills/global-project-onboarding/SKILL.md) | [`project-onboarding`](../skills/project-onboarding/SKILL.md) | Reading and mapping unfamiliar or returning codebases before edits. |
| [`global-regression-hunter`](../skills/global-regression-hunter/SKILL.md) | [`regression-hunter`](../skills/regression-hunter/SKILL.md) | Searching for repeated bug patterns and nearby regressions. |
| [`global-release-gate`](../skills/global-release-gate/SKILL.md) | [`release-gate`](../skills/release-gate/SKILL.md) | Pre-commit, push, deploy, release, merge, PR, and handoff verification. |
| [`global-rollback-guardrail`](../skills/global-rollback-guardrail/SKILL.md) | [`rollback-guardrail`](../skills/rollback-guardrail/SKILL.md) | Checkpoints and hard stops before rollback-like work. |
| [`global-site-maintainer`](../skills/global-site-maintainer/SKILL.md) | [`site-maintainer`](../skills/site-maintainer/SKILL.md) | Website maintenance where source, generated artifacts, tests, docs, and hosting must align. |
| [`global-snapshot`](../skills/global-snapshot/SKILL.md) | [`snapshot`](../skills/snapshot/SKILL.md) | Screenshot/snapshot capture, crop, inspection, and presentation. |
| [`global-tts-audio-assets`](../skills/global-tts-audio-assets/SKILL.md) | [`tts-audio-assets`](../skills/tts-audio-assets/SKILL.md) | TTS audio generation, reuse, audit, QA, and data wiring across projects. |
| [`global-uat-environment`](../skills/global-uat-environment/SKILL.md) | [`uat-environment`](../skills/uat-environment/SKILL.md) | Lightweight UAT/staging/preview environments and promotion evidence. |
| [`global-ui-state-matrix`](../skills/global-ui-state-matrix/SKILL.md) | [`ui-state-matrix`](../skills/ui-state-matrix/SKILL.md) | UI state coverage beyond the happy path. |
| [`global-ui-ux-expert`](../skills/global-ui-ux-expert/SKILL.md) | [`ui-ux-expert`](../skills/ui-ux-expert/SKILL.md) | Polished user-facing UI/UX design, UX behavior/state coverage, implementation, audit, and QA. |
| [`global-ui-ux-orchestrator`](../skills/global-ui-ux-orchestrator/SKILL.md) | [`ui-ux-orchestrator`](../skills/ui-ux-orchestrator/SKILL.md) | Routing broad UI/UX work to the right focused skills. |
| [`global-usage-budget-gate`](../skills/global-usage-budget-gate/SKILL.md) | [`usage-budget-gate`](../skills/usage-budget-gate/SKILL.md) | Budget-aware depth, stop rules, and escalation triggers. |

## Not Global

These skills stay under their project or specialized names:

- Coin Quest: `coin-quest-admin-ops`, `coin-quest-ledger-logic`,
  `coin-quest-native-parity`
- Notenwert: `notenwert-design-direction`, `notenwert-maintainer`
- Mongkol Wela: `mongkol-new-chat`
- Shane and His Thai: `shane-thai-audio-generator`,
  `shane-thai-export-chatgpt`, `shane-thai-image-assets`,
  `shane-thai-new-chat`, `shane-thai-prod-smoke`
- Image-boundary workflow: `image-boundary`, `image-boundary-efficient`,
  `image-boundary-iteration`, `image-boundary-nonexplicit-max`,
  `image-boundary-polish`, `image-boundary-rejection-recovery`,
  `image-boundary-safety-map`
