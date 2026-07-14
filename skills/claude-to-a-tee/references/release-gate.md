# Release Gate

Read this before claiming done, committing, pushing, deploying, opening a PR, or
handing off Claude-to-a-tee work.

## Non-Negotiable Execution Gate

Use this skill as a release blocker, not as inspiration. Do not claim success,
commit, push, or deploy until this gate is satisfied, even when the user says
"continue until done".

Before editing, render and inspect both the Claude reference and the target app
in the relevant state; never implement from memory, screenshots alone, or broad
"looks close" judgment.
Open every reachable page, screen, route, tab, drawer, and modal, click every
visible control, and record static/no-op Claude behavior explicitly.

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
BLOCKERS BEFORE COMMIT:
PRODUCTION ARTIFACT SMOKE:
```

A broad screenshot comparison is not enough. Use browser-computed geometry for
high-risk components: global shell, header/topbar, nav/sidebar, page title,
primary cards, filters/tabs, table/list rows, dialogs/drawers, history/footer,
and page rhythm. Wrong default route, stale artifact, selector miss, loading or
login state, shell geometry, primary component geometry, item order/count, or
undocumented product-driven visual change is a critical mismatch by default.

These fail the skill:

- "Claude-inspired polish" instead of component-level measured parity;
- preserving current product UX without evidence or without reporting what does
  not follow Claude and why;
- flattening existing sub-containers, internal scroll regions, sticky subpanels,
  or active-item scroll behavior without a decision ledger and verification;
- removing persistence, routing/deep links, progressive disclosure,
  keyboard/focus, non-happy states, permission-aware UI, destructive safety,
  data-density controls, responsive interaction, media fallbacks, search
  click-through, or scroll choreography without a decision ledger and
  verification;
- rewriting tests or acceptance checks to bless the loss of proven product UX
  before the ledger classifies that loss as intentional;
- editing first and measuring only after the user complains;
- using product CSS clamps, spacing, or old primitives when they alter Claude
  geometry without declaring a visual exception;
- shipping mock-only controls as inert UI;
- downgrading a handoff-declared feature to read-only, hidden, disabled, or
  "future API" state before first mapping and attempting the real product write
  path;
- calling real product data/auth/API differences "behavior exceptions" while
  also allowing avoidable visual drift;
- production smoke that checks only HTTP 200 or login, not the deployed
  artifact that contains the changed UI.

Behavior exceptions are allowed when they preserve Claude geometry; visual
exceptions must be explicit, and critical ones require acceptance before
commit/push/deploy.

Do not ship broken product behavior because Claude was static, and do not add
invented animation or interactions as a substitute for faithful UI/UX parity.

## Verify The Implementation

1. Start the application in its normal local runtime.
2. Use `vercel:agent-browser` when available to test the implementation,
   capture comparable screenshots, inspect console errors, and exercise
   interactions.
3. Compare reference and implementation component by component, not from memory.
4. Verify computed styles for the values in the component contract. For any
   value the user questioned, compare the rendered implementation against the
   exact Claude source/computed value and treat mismatch as not done.
5. Verify all source-defined breakpoints. For a mobile web task, also use the
   default matrix in the verification checklist unless the project defines a
   stricter one.
6. Test content extremes, long labels, loading, empty, disabled, focus, modal,
   keyboard, and touch states that can alter geometry.
7. Run focused tests after edits, then the repository's required full test suite
   when risk or release policy calls for it.
8. Reinspect every detail the user named, even if broader screenshots look
   right.
9. Fill the measured parity audit table and mark every row `matched`,
   `behavior exception`, `visual exception`, or `not done`.

## Evidence Provenance

Use the artifact provenance, default responsive matrix, and browser evidence
sections in [verification-checklist.md](verification-checklist.md) as
release-blocking checks. Reject captures from the wrong route, login/protect
screens, stale artifacts, pre-hydration shells, unsupported browser claims, or
selector misses; fix setup and recapture before claiming parity.

## Enforce The Release Gate

Do not claim completion, commit, push, or deploy a Claude-to-a-tee change until:

- relevant reference and implementation states were rendered and compared;
- the pre-implementation decision ledger exists and every non-Claude decision
  names its reason, evidence, risk, and verification;
- the reference state/surface coverage ledger is complete, and every reference
  state is either implemented, product-adapted, explicitly omitted, or deferred
  with the reason documented;
- the route component manifest is complete for every affected route, and the
  missing-component report has no unclassified Claude components;
- the default rendered reference screen was compared against the target default
  screen, not just an internal route that happened to look similar;
- the affected component contracts were extracted from Claude and checked
  against implementation computed styles;
- page rhythm and scroll/sticky outcomes were measured beyond the first viewport
  where they affect visible UI, while preserving product-owned scroll, scrub,
  lazy loading, load-more, pagination, and virtualization mechanics;
- preserved or hybrid product UX has focused regression coverage or equivalent
  recorded checks for the retained selectors, controls, item counts, scroll
  bounds, first/last item reachability, and reload/session behavior;
- every preserved or hybrid product UX contract named in the decision ledger has
  a matching verification result: persistence, routing, disclosure, focus,
  non-happy states, permissions, destructive safety, density, responsive
  interaction, media fallback, search click-through, or scroll choreography;
- desktop, tablet, and required mobile viewports passed without incoherent
  overlap, clipping, or page-level horizontal overflow;
- required interactions and the product engineering contract still work;
- every visible action is either functional, intentionally disabled with a real
  reason, or removed as a documented mock-only divergence;
- browser console, page errors, failed requests, and 4xx/5xx asset responses
  were checked after live data hydration;
- the tested generated artifact and deployed build identifiers match the target
  commit, and requested/final URLs prove the intended environment was measured;
- intentional divergences and unverified coverage are disclosed;
- the measured parity audit has no `critical` or `not done` rows;
- product exceptions are separated into behavior exceptions and visual
  exceptions;
- product-UX-preserved and hybrid rows have verification that proves the current
  product UX is more complete, safer, or more useful than the Claude reference
  for that component;
- any visual exceptions are explicitly reported to and accepted by the user
  before release.

Commit, push, or deploy only when the user requests it or repository
instructions already authorize it.

If the user asks to commit, push, or deploy before the hard gate passes, stop
and report the blocking mismatches instead of shipping. The only exception is
when the user explicitly says to ship despite the listed mismatches.

After deploy, rerun a small production parity smoke against the deployed URL:
default route/page title, header/nav geometry, primary hero/card/grid geometry,
first primary interaction, console errors, and page-level overflow at desktop
and one mobile viewport. A production smoke that only checks HTTP 200 and basic
functionality is not enough for Claude-to-a-tee work.

For changed authenticated admin surfaces, production smoke must reach the
changed authenticated surface or an equivalent preview/test environment with the
same deployed artifact and seeded state. A smoke that stops at the login/admin
gate does not verify the changed UI and cannot close the release gate.

## Completion Report

Report the reference files, routes/components, decision ledger summary, measured
parity status, viewport matrix, tests, browser coverage, deployed URL if any,
what followed Claude, what did not follow Claude, why, risks, and every
intentional or remaining divergence in the closeout.
