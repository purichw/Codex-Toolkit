# Skill Index

This folder contains custom Codex skills. Each subfolder is intended to be usable
as a standalone skill directory under `~/.codex/skills`.

## General Workflow Skills

| Skill | Description | Context |
| --- | --- | --- |
| [`project-onboarding`](project-onboarding/SKILL.md) | Reads project docs, commands, architecture, source layout, and git state before implementation. | Use at the start of work in an unfamiliar or returning repository. |
| [`docs-cartographer`](docs-cartographer/SKILL.md) | Produces living documentation for routes, modules, data flow, interactions, deployment paths, and ownership boundaries. | Use when a codebase needs better maps, handoff notes, or future-maintainer context. |
| [`regression-hunter`](regression-hunter/SKILL.md) | Turns one bug into a targeted search for related patterns and nearby regressions. | Use after finding a suspicious hardcoded value, duplicated behavior, brittle selector, or repeated logic bug. |
| [`release-gate`](release-gate/SKILL.md) | Defines the verification checklist before publishing, committing, pushing, deploying, or handing off work. | Use when changes are about to leave the local working state. |
| [`mobile-web-qa`](mobile-web-qa/SKILL.md) | Verifies responsive UI across representative mobile, tablet, and desktop viewports. | Use for mobile web bugs, pre-deploy QA, keyboard behavior, overflow, safe areas, and touch interaction checks. |

## Design And Frontend Parity

| Skill | Description | Context |
| --- | --- | --- |
| [`claude-to-a-tee`](claude-to-a-tee/SKILL.md) | Treats offline Claude HTML as executable design documentation and verifies measured component parity. | Use for exact visual implementation from Claude Design exports, screenshots, or handoff files. |
| [`notenwert-design-direction`](notenwert-design-direction/SKILL.md) | Captures Notenwert's editorial, civic, cultural-network design intent. | Use for Notenwert design direction, homepage hero behavior, NGA-style references, typography, imagery, and public/admin UX critique. |

## Firebase And Security

| Skill | Description | Context |
| --- | --- | --- |
| [`firebase-account-management`](firebase-account-management/SKILL.md) | Clarifies Firebase Auth, Firestore user profiles, Admin SDK, custom claims, and billing-sensitive assumptions. | Use for account creation, signup/login, admin user operations, or Spark vs Blaze questions. |
| [`firebase-security-rules`](firebase-security-rules/SKILL.md) | Focuses on Firestore Rules, Admin SDK bypass behavior, service-account setup, and production access guarantees. | Use for security audits, rules changes, privileged endpoints, and Firebase deployment risk. |

## Project-Specific Skills

| Skill | Description | Context |
| --- | --- | --- |
| [`coin-quest-admin-ops`](coin-quest-admin-ops/SKILL.md) | Defines safe behavior for the Coin Quest Ledger Admin Portal. | Use for Super Admin auth, users, boards, lifecycle actions, delete/reset flows, revisions, and Firebase-backed admin operations. |
| [`coin-quest-ledger-logic`](coin-quest-ledger-logic/SKILL.md) | Protects Party Ledger rules for split math, invites, guests, Character IDs, and settlement. | Use for Coin Quest participant entry, payer/participant logic, reminders, direct invite links, or ledger regressions. |
| [`coin-quest-native-parity`](coin-quest-native-parity/SKILL.md) | Keeps the Coin Quest native Expo app aligned with the web data model and native build requirements. | Use for native app changes, iOS/Android gates, `playerModules`, and web/native parity checks. |
| [`notenwert-maintainer`](notenwert-maintainer/SKILL.md) | Defines the operating playbook for the Notenwert project. | Use for Notenwert implementation, CMS/admin work, tests, docs, deploy prep, and commits. |
| [`shane-thai-audio-generator`](shane-thai-audio-generator/SKILL.md) | Manages Google Chirp audio generation, regeneration, audit, and QA for Thai lessons. | Use for Shane and His Thai lesson audio, Thai TTS text, audio IDs, voice selection, stale/missing audio, or naturalness fixes. |
| [`shane-thai-image-assets`](shane-thai-image-assets/SKILL.md) | Manages image selection, generation, reuse, cropping, and QA for Thai vocabulary lessons. | Use for Shane and His Thai lesson art, badge imagery, Unit image generation, or semantic asset mapping. |
| [`image-boundary-iteration`](image-boundary-iteration/SKILL.md) | Controls adult non-explicit image iteration with prompt hygiene, verdict loops, branch notes, and logging. | Use for the nudity-reference-prompting project when continuing boundary-forward visual iterations or maintaining baselines. |

## Image And Media Sourcing

| Skill | Description | Context |
| --- | --- | --- |
| [`placeholder-image`](placeholder-image/SKILL.md) | Sources, selects, replaces, crops, and audits placeholder images as real product content. | Use when populating missing images, replacing weak stock, finding hero/card/gallery photos, fixing crops, or making an image sourcing playbook. |
