---
name: claude-to-a-tee
description: Reproduce an offline Claude Design HTML reference at component level while preserving proven product UX, behavior, and engineering contracts. Use when the user says "Claude to a tee", "to a tee", "exactly like the Claude HTML", "pixel-perfect", "holy grail", or asks Codex to implement, audit, compare, extract, repair, or balance a web UI from Claude-generated offline HTML, screenshots, handoff files, exported assets, or reference manifests, especially when responsive mobile, tablet, desktop, animation, interaction, product-UX preservation, decision/risk ledgers, or pre-deploy visual verification is required.
---

# Claude To A Tee

Treat the supplied offline Claude HTML as executable design documentation. Match
its rendered components and user-visible states, not merely its palette or broad
layout.

Treat the target product as real software, not a display case for a pretty mock.
The reference is a UI presentation source of truth; the target product remains
the source of truth for data, routing, auth, persistence, performance,
accessibility, security, tests, operations, and frontend architecture.

Expand "to a tee" internally to:

```text
CLAUDE TO A TEE AUDIT. Implement from the offline Claude HTML exactly at component level, mobile included, and verify before commit/deploy.
```

## Core Message

Use this skill as a release blocker, not as inspiration. Before editing, render
and inspect both the Claude reference and the target app in the relevant state;
never implement from memory, screenshots alone, or broad "looks close" judgment.
Start with exhaustive reference reconnaissance: open every reachable page,
screen, tab, drawer, modal, and route; click every visible control; and record
what happens even when the Claude reference is static or no-op.

For broad pages, converge component-by-component. Do not treat a whole HTML file
or a single full-page screenshot as enough detail to implement everything at
once. Lock high-risk elements in small passes: shell/header, nav, hero/banner,
sidebar/rail, list/grid rows, cards, drawers/modals, footer, and responsive
breakpoints. Each pass needs rendered reference evidence, rendered app evidence,
and a narrow measured parity table before moving to the next pass.

A broad screenshot comparison is not enough. Use browser-computed geometry for
high-risk components: global shell, header/topbar, nav/sidebar, page title,
primary cards, filters/tabs, table/list rows, dialogs/drawers, history/footer,
and page rhythm. Wrong default route, stale artifact, selector miss, loading or
login state, shell geometry, primary component geometry, item order/count, or
undocumented product-driven visual change is a critical mismatch by default.

Treat the HTML/CSS visual layer as a first-class contract. Before editing,
extract and preserve the reference's rendered DOM/component structure, shell and
header geometry, page spacing rhythm, typography system, card/list geometry,
border/radius/shadow/background treatment, image/media frames, and responsive
breakpoints. Use exact source or computed values from the Claude HTML/CSS when
available; screenshots are required evidence for rendered state and visual
inspection, but they do not replace source/computed measurement.

Use `$snapshot` automatically for every Claude-to-a-tee implementation, parity
audit, repair, or handoff before the final response. Do not wait for the user to
ask. When a reference exists, the primary visual evidence must be a side-by-side
`Reference` and `Development` comparison, with a mobile comparison included when
responsive behavior is in scope.

Behavior exceptions are allowed only when they preserve Claude geometry. Visual
exceptions must be explicit, and critical ones require acceptance before
commit/push/deploy. Do not claim success, commit, push, deploy, open a PR, or
handoff until the release gate passes.

Balance faithful UI/UX with product-owned engineering behavior. Claude
references often omit behavior, persistence, real data, or animation; absence in
Claude is not permission to ship broken product behavior, invent decorative
motion, or drift away from the rendered UI. Match animations only when the
reference shows them or the product already requires them.

Use `$product-ux-contracts` when Claude may overwrite proven product UX,
`$ui-state-matrix` when Claude shows only the happy path, `$interaction-flow-qa`
when visible controls imply real journeys, `$design-system-guardian` when
Claude affects reusable primitives, `$accessible-interaction` for keyboard/focus
risk, `$data-dense-ux` for tables/lists/admin density, `$form-flow-ux` for
forms, `$admin-prototype-reconciliation` when an admin prototype changes live
data or publish contracts, and `$production-asset-smoke` when the parity work
adds or repairs production media.

Before implementation, always output or maintain a decision ledger for the
requested scope. The ledger must say what will follow Claude, what will preserve
the current product, what will be hybridized, why, how it will be verified, and
what risk remains. This can be a short user-facing plan, a working note, or
both depending on task size, but it must exist before edits that could overwrite
current UX.

## Quick Read Path

Read this `SKILL.md` first, then choose the smallest safe reference set. If
uncertain, read the larger path.

- **Scoping, planning, or tiny component:** read
  [references/operating-guide.md](references/operating-guide.md) and
  [references/reference-workflow.md](references/reference-workflow.md).
- **Implementing or repairing Claude HTML in a product:** read
  [references/operating-guide.md](references/operating-guide.md),
  [references/reference-workflow.md](references/reference-workflow.md), and
  [references/product-contract.md](references/product-contract.md) before
  editing.
- **Multi-screen, auth/admin, persistent actions, or handoff-declared behavior:**
  read all reference files before editing.
- **Verification, commit, push, deploy, PR, or handoff:** read
  [references/verification-checklist.md](references/verification-checklist.md)
  and [references/release-gate.md](references/release-gate.md) before claiming
  completion.

The shorter path controls context size; it does not reduce the acceptance bar.
Once a phase begins, its reference file is required.

## Reference Extraction Accelerator

When offline Claude HTML files are available, create a machine-generated
inventory before manual mapping unless the task is a tiny single component or
the helper cannot run. Use the manifest to save time; do not treat it as
verification.

```bash
python3 /Users/point/.codex/skills/claude-to-a-tee/scripts/extract_reference.py \
  path/to/claude.html \
  --out .claude-reference
```

For environments with Python Playwright available, add rendered measurement and
screenshots:

```bash
python3 /Users/point/.codex/skills/claude-to-a-tee/scripts/extract_reference.py \
  path/to/claude.html \
  --out .claude-reference \
  --render --screenshots \
  --viewport 1440x900 --viewport 820x1180 --viewport 390x844
```

Use `reference-manifest.md` and `CLAUDE_TO_A_TEE_WORKLOG.md` as the first draft
of the coverage ledger, controls ledger, asset inventory, breakpoint list,
route/state signal list, and parity table seed. Reuse a previous manifest only
when the recorded SHA still matches the current Claude HTML.

## Operating Loop

1. Confirm the newest user requirement and all supplied reference artifacts.
2. Run the extractor when it applies, then render and inspect the Claude
   reference manually from the first screen through every reachable page,
   control, and state.
3. Build the coverage ledger, controls ledger, route component manifest,
   HTML/CSS visual layer contract, component contracts, and parity table seed.
4. Map each Claude component and visible action to product-owned files, data,
   permissions, persistence, tests, and operations; mark static/no-op Claude
   behavior explicitly instead of guessing.
5. Produce the decision and risk ledger before editing: Claude adopted, product
   UX preserved, hybrid, needs user decision, risk, and verification.
6. Implement component-level parity while preserving proven product UX and
   product-owned engineering behavior.
7. Measure reference vs implementation with `$snapshot` evidence, screenshots,
   computed geometry, source/computed CSS values, responsive states,
   interactions, and browser evidence.
8. Apply the release gate before claiming done or shipping.

## Required Distinctions

Apply this source-of-truth order:

1. The user's newest explicit requirement.
2. The supplied offline Claude rendered UI, CSS, assets, and visible states.
3. Existing product behavior, data contracts, tests, accessibility, i18n,
   security, performance, and production operations.
4. Older handoff notes and screenshots.

Split every intended divergence into two labels:

- `behavior exception`: the product keeps real data, APIs, auth, routing, media,
  persistence, permissions, performance architecture, accessibility, security,
  tests/selectors, analytics hooks, or operations while preserving Claude's
  visible intent and geometry.
- `visual exception`: the product intentionally changes Claude's layout,
  spacing, copy, item count, assets, colors, or component state.

Behavior exceptions are allowed when needed. Visual exceptions require explicit
documentation and should be treated as failed Claude-to-a-tee parity unless the
user accepts them or the reference cannot support a real product path.

## Product UX Preservation Gate

The current product may beat Claude only with evidence, not taste. Before
preserving current UX over Claude, prove at least one of these:

- real functionality exists where Claude is static, mock-only, no-op, or
  visually implied but incomplete;
- the product flow completes a user task that Claude does not support end to
  end;
- the product preserves useful nested containers, internal scroll regions,
  sticky subpanels, virtualized lists, or scroll restoration that Claude omits
  or flattens;
- the product covers important states Claude omits: loading, empty, error,
  denied, disabled, partial failure, long text, mobile keyboard, or reload;
- the product protects operational safety: role checks, confirmation, audit
  logs, rollback, destructive-action safeguards, or permission denial;
- the product has stronger accessibility, mobile, performance, or reliability
  evidence;
- the product behavior is covered by tests, docs, production usage, or a known
  regression history.

If none of these are proven, Claude wins for design and interaction shape by
default. When evidence exists, prefer `hybrid`: use Claude's visual language,
geometry, hierarchy, and rhythm while preserving the product's stronger real
behavior.

Use this ledger before implementation and again in closeout:

```text
Component:
Claude behavior/UI:
Current product behavior/UX:
Evidence current is better:
Decision: Claude adopted / product UX preserved / hybrid / needs user decision
Reason:
Implementation rule:
Verification:
Risk:
```

Report the ledger explicitly when the decision affects user-visible UX, product
behavior, release risk, or any place where Claude will not be followed exactly.
If a `needs user decision` row blocks a critical visual or behavior choice, ask
before editing that row or continue only on clearly independent work.

Do not flatten an existing product sub-container, nested scroll region, sticky
subpanel, virtualized list, or scroll-restoration behavior just because a newer
Claude HTML puts the same content in a simpler page flow. First record the
existing container behavior, decide `Claude adopted`, `product UX preserved`, or
`hybrid`, and verify the post-change scroll container itself: first item, last
item, manual scroll, active-item auto-scroll, keyboard/touch behavior, and
page-level overflow.

Do not rewrite regression tests or acceptance checks to bless a Claude-flattened
version until the decision ledger proves that change is intentional. Tests for
preserved or hybrid UX must assert the preserved container, control, state, or
workflow behavior, including item counts, page-size controls, scroll bounds, and
first/last item reachability when relevant.

## Product UX Contracts Claude Must Not Flatten

Before copying a newer Claude page flow, inspect whether the target product
already has any of these contracts. If yes, put them in the decision ledger and
default to `hybrid` unless Claude clearly improves the real UX:

- state persistence: selected tabs, filters, search, expanded rows, selected
  item, progress, local draft, reload, browser back/forward, and session return;
- progressive disclosure: accordions, details panels, drawers, modals, side
  panels, step flows, and show-more/show-less behavior;
- URL and routing: route params, hash/query deep links, shareable filters,
  item anchors, redirects, browser history, and fallback routes;
- keyboard and focus: tab order, focus trap, escape/outside-click close, focus
  restore, scroll-to-input, shortcuts, and screen-reader semantics;
- non-happy states: loading, skeleton, empty, error, denied, disabled with
  reason, validation, partial failure, stale session, and retry;
- permission-aware UI: role-based visibility, allowed/denied paths, readonly
  state, audit-sensitive actions, and server-backed authorization;
- destructive safety: confirmation, undo/restore, tombstone, audit log,
  rollback, irreversible-action copy, and disabled current-state reasons;
- data density: pagination, load more, virtualization, page-size controls,
  sort, filters, bulk select, item counts, and large-list performance;
- responsive interaction: mobile drawer, bottom sheet, sticky footer action,
  safe areas, touch targets, keyboard viewport, and tablet-specific layout;
- real asset/media handling: lazy loading, fallbacks, failed asset state, CMS
  visibility, audio/video controls, captions, poster frames, and source repair;
- search and result click-through: result metadata, real destination, highlight
  target, selected item visibility, and non-generic fallback behavior;
- scroll choreography: sticky offsets, anchor scroll, active-item auto-scroll,
  manual scroll ownership, scroll restoration, and page-level overflow.

Claude can restyle these contracts, but replacing or removing them requires
evidence, risk disclosure, verification, and user acceptance when the tradeoff
is product-visible.

Do not silently reinterpret "to a tee" as general polish, a shell-level restyle,
or copying Claude's demo architecture. Treat Claude JavaScript and demo
interactions as evidence of intended visible states, not as architecture to
clone.

If a visible control cannot be real in the target product, make it real, adapt
it into an equivalent real product action, remove it as a documented mock-only
divergence, or block release until the user accepts a defer. Do not ship inert
mock controls.

## Completion Gate

Before finalizing, produce this compact self-check in working notes or closeout:

```text
REFERENCE RENDERED: yes/no + file/hash/state/viewport
APP RENDERED: yes/no + URL/commit/state/viewport
DECISION LEDGER: Claude adopted / product UX preserved / hybrid / needs user decision + reason/risk
COVERAGE LEDGER: matched / behavior exception / visual exception / not done
HTML/CSS VISUAL LAYER: shell/header | spacing | typography | card/list geometry | responsive breakpoints | matched/exception/not done
MEASURED PARITY TABLE: component | viewport | reference x/y/w/h/style/count | implementation x/y/w/h/style/count | delta | status
PRODUCT UX PRESERVED:
BEHAVIOR/ENGINEERING EXCEPTIONS:
VISUAL EXCEPTIONS:
SNAPSHOT EVIDENCE:
BLOCKERS BEFORE COMMIT:
PRODUCTION ARTIFACT SMOKE:
```

Do not claim completion, commit, push, deploy, open a PR, or handoff while any
coverage row, route component, visible control, measured parity row, required
viewport, or release-gate check remains `not done`, critical, unrendered,
unmapped, or unaccepted.

After deploy, rerun a small production parity smoke against the deployed URL:
default route/page title, header/nav geometry, primary hero/card/grid geometry,
first primary interaction, console errors, and page-level overflow at desktop
and one mobile viewport. A production smoke that only checks HTTP 200 and basic
functionality is not enough for Claude-to-a-tee work.
If the changed screen uses CMS images, video, CSS backgrounds, external embeds,
or generated assets, include `$production-asset-smoke` evidence for the deployed
URL before saying the visual parity work is complete.
