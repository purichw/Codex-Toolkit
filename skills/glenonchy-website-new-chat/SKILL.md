---
name: glenonchy-website-new-chat
description: "Onboard or refresh Glenonchy's public shop storybook website. Use for Glenonchy Website New Chat, website handoff, context pickup, required reading, website setup or documentation alignment; not Flutter games, GM Console or Godot Tactics."
---

# Glenonchy Website New Chat

Onboard in the current chat. This skill does not create, inspect, message or
delegate to other chats, and does not authorize a release or cloud changes.

## Locate and read

Default repository: `/Users/point/Projects/Glenonchy`. Verify that location and
its Git state; if missing, ask for the repository instead of selecting a Downloads
starter or similarly named checkout. Preserve unrelated working-tree changes.

Read, in order:

1. Repository `AGENTS.md`; run `git status --short --branch` before edits.
2. [Website new-chat guide](/Users/point/Projects/Glenonchy/docs/website/NEW_CHAT.md).
3. [Design contract](/Users/point/Projects/Glenonchy/docs/website/DESIGN_CONTRACT.md).
4. The latest release and relevant feature/reference linked by the
   [website index](/Users/point/Projects/Glenonchy/docs/website/README.md).
5. Only the owner source/CSS/data needed for the actual task.

Keep mutable release IDs, live URLs, source maps and verification results in the
repository documents, not duplicated here. If they disagree, inspect source and
dated evidence and report the discrepancy; do not silently treat local WIP as live.

## Keep the correct surface

The public website lives in `apps/gm-console/src/website/` despite the package
name. It shares packaging with GM, not its UI, login or release scope. Read the
guide's routing and local commands before opening a page. Do not apply Flutter
fonts, minigame economy, GM permissions or Tactics contracts to the shop website.

Use [glenonchy-website-design](../glenonchy-website-design/SKILL.md) for visible
work. Explicit product decisions remain authoritative until the owner changes
them; mockups are visual evidence, not permission to restore removed decorations,
change navigation or replace the approved book layout.

Preserve shared components, desktop-relative proportions, paper safe areas,
complete artwork, all required sections, in-paper numbered pagination, the
approved loading/readiness/auto-open flow and entrance protection. The design
contract owns their precise rules. Never bypass readiness with a broken fallback.

## Execute and verify proportionately

When a concrete task accompanies onboarding, continue that task. If none is
supplied, summarize the verified context and wait; don't launch a whole-site audit,
install SDKs, migrate data, build native apps or deploy merely to get oriented.

For UI work load `ui-ux-expert`; use `mockup-to-product` when references lead the
change and `snapshot` to inspect current rendered output before handoff. Load
responsive, shared-component or motion skills only when their risks are touched.
Inspect the changed interaction as well as its screenshot. For a small change,
one targeted check is enough; broad shared/routing/release work needs broader
affected-surface evidence. Never call a browser viewport a physical-device test.

For documentation-only work, validate links, source ownership and skill metadata;
do not build or repeat visual/runtime tests. Reconcile current entry docs and
contracts while leaving dated evidence and imported handoffs historical.

Read `docs/ARTIFACT_RETENTION.md` for cleanup. Preserve source art, current QA,
credentials and device backups. Follow the owner's exact authorization and
AGENTS deletion rules; onboarding alone authorizes no removal.

Before finishing, check the scoped diff/status and report what changed, evidence,
and material limitations. Update repository status/decision docs only when their
facts changed. Commit, push and deploy need explicit authorization for the scope;
use the current release runbook and `release-gate` when authorized.

Example: `$glenonchy-website-new-chat อ่านบริบทเว็บ แล้วแก้หน้า Events ตาม reference ล่าสุด`
