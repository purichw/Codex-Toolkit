# 03 · Information architecture & screen strategy

How screens are divided, ordered, and grouped. This is where engineers do the most accidental
design: the schema becomes the navigation, the endpoints become the pages, and the resulting
product is technically complete and unusable.

## What designers notice that developers often miss

- **The screen answers a question.** Designers name the question ("which orders need my attention
  today?"). Developers name the resource ("Orders"). The first produces a default filter, a sort
  order, and a primary action; the second produces a table.
- **Grouping follows task, not data model.** Users don't know your join tables. "Notifications"
  belongs next to "Team access" if both are things an admin configures on Monday morning.
- **Nav depth costs more than nav width.** Designers flatten. Developers nest, because nesting
  matches the URL structure they already have.
- **Sequence carries meaning.** The order of steps, of sections on a page, and of fields in a form
  is an argument. Reordering to match API convenience destroys the argument.
- **What's hidden is a decision.** Progressive disclosure done well hides *rarely needed* things.
  Done badly it hides *required* things — behind tabs, accordions, and "advanced".
- **Where the user came from.** Designers design entry points; developers design pages. A screen
  reached from a notification needs different context than the same screen reached from nav.
- **Empty and partial states are architecture.** What a screen shows when there's nothing is often
  the most-viewed version of it, and it's where onboarding actually lives.

## Bad patterns

| Pattern | Why it fails | Observable tell `[FACT]` |
| --- | --- | --- |
| **Schema-as-navigation** | Nav mirrors resources; users must know the model to find anything | Nav labels are plural nouns matching table names; "Entities", "Configurations" |
| **Nav accretion** | Every feature adds an item; nothing is ever removed | >7 top-level items; an "Other"/"More" bucket; two items whose difference you can't explain in one sentence |
| **Tab-hiding required input** | Users submit and get errors pointing at a tab they never opened | Validation errors reference fields not on screen |
| **Everything on one page** | 14 sections, no hierarchy, 6 save buttons | Page height > 6 viewports with no in-page nav |
| **Modal chains** | Modal opens modal; context lost; back does nothing | Two scrims stacked; browser back closes the whole flow |
| **Detail page as read-only twin** | Users bounce between view and edit; the edit form is the real page | A "View" page whose only action is "Edit" |
| **Wizard for a 3-field form** | Ceremony without benefit | Steps with one input each and no branching |
| **Single page for a 12-decision flow** | Users can't hold state; abandonment mid-page loses everything | One form with >12 required inputs and no save |
| **Breadcrumbs to nowhere** | Breadcrumb trail invented for a flat structure | Breadcrumb segments that aren't clickable or that all point to the same page |
| **Search as the only path** | Discovery impossible; the user must know the name | No browsable list; empty state says "search for something" |
| **Dead-end success** | Task completes, user is stranded | Confirmation screen with no next action, or a redirect to an unrelated home |

## Before / after

### 1. Settings grouped by schema → grouped by task

```
❌ Settings                                  ✅ Settings
   Users                                       Your account
   UserRoles                                     Profile · Notifications · Sessions
   UserPreferences                             People and access
   OrganizationSettings                          Members · Roles · Invitations · SSO
   OrganizationBilling                         Billing
   NotificationConfig                            Plan · Payment method · Invoices · Usage
   IntegrationTokens                           Connections
   WebhookEndpoints                              Integrations · API tokens · Webhooks
   ApiKeys
```

Five groups, task-named, each answerable by "when would I come here?". Item count unchanged.

### 2. One page of 14 decisions → sequenced flow

```
❌ Create project (one page)                 ✅ Create project
   [14 fields, 6 optional, 2 conditional]      Step 1 · Name and owner          (2 fields)
   [Save]                                      Step 2 · Where it runs           (3 fields, branches)
                                               Step 3 · Who can access it       (1 field + invite)
                                               Review · everything, editable inline
                                               Advanced settings available after creation
```

Rule of thumb: split when a step's answers change what the next step asks. Don't split a flat form.

### 3. Progressive disclosure done wrong → right

```
❌ [Basic ▾]  [Advanced ▾]                   ✅ Name        [___________]
   Required "Region" lives under Advanced       Region      [ us-east-1 ▾ ]
   with 11 optional fields                      ─────────────────────────────
                                                ▸ Advanced (retries, TTL, custom DNS)
                                                  — all optional, all with defaults shown
```

**IA law:** anything required is never behind disclosure. Anything behind disclosure shows its
current value in the summary line when it differs from default.

### 4. Modal chain → routed panel

```
❌ Orders → [modal: order] → [modal: refund] → [modal: confirm]
✅ Orders → /orders/1043 (page, keeps list in breadcrumb)
             → side panel: Refund (list stays visible, deep-linkable /orders/1043/refund)
             → inline confirm inside the panel
```

## Rules

### Navigation

- **IA-1** ≤7 top-level destinations; ≤2 levels of nesting before you reach a working screen. A third level must be in-page (tabs/anchors), not in the nav tree. `[CRAFT]`
- **IA-2** Every nav label is a noun a user would say out loud, and no two labels overlap in meaning. If you need a sentence to explain the difference, merge or rename. `[CRAFT]`
- **IA-3** The current location is unambiguous at a glance: the active item has ≥2 differentiators (weight + rule/tint), not color alone. `[FACT]`
- **IA-4** Nav is stable — items don't reorder, appear, or disappear per page. Permission-gated items follow [IX-21](04-interaction-design.md) (hide vs. disable), decided once. `[PD]`
- **IA-5** Every screen is directly linkable, including filters, sort, tab, pagination, and open panel. `[FACT]`

### Grouping

- **IA-6** Group by "when would a user do this together", then name the group with that occasion. Never expose internal model names in group titles. `[CRAFT]`
- **IA-7** 3–7 items per group. Fewer than 3 → merge upward. More than 7 → find the second axis (frequency, scope, lifecycle) and split by it. `[CRAFT]`
- **IA-8** Group boundaries are drawn with space and rules, in the ratio from [VD-4](01-visual-diagnosis.md) — not with boxes around everything. `[CRAFT]`

### Hierarchy

- **IA-9** One primary object per screen. The screen's title names it; the primary action acts on it. `[CRAFT]`
- **IA-10** One primary action per screen, visually dominant; ≤2 secondary; everything else is a link or lives in an overflow menu. `[CRAFT]`
- **IA-11** The three-question test: *Where am I? What can I do? What just happened?* — all answerable within 2 seconds of a fresh screenshot, without hovering. `[CRAFT]`
- **IA-12** Heading levels match visual hierarchy exactly (`h1` = the dominant text). No skipped levels, no `h3` chosen for its size. `[FACT]`

### Sequencing

- **IA-13** Split a flow into steps when (a) an answer branches later questions, (b) a step requires waiting, or (c) >8 required inputs. Otherwise keep one page. `[CRAFT]`
- **IA-14** Show step *n* of *m* with real numbers; if *m* varies by branch, show the known remainder and update honestly. `[CRAFT]`
- **IA-15** Back is always available and never destructive: returning to a previous step preserves entered data. `[FACT]`
- **IA-16** A multi-step flow ends on a screen that states what happened and offers the two most likely next actions. `[CRAFT]`
- **IA-17** Page order = decision order. Cheap, reversible, and identifying decisions first; expensive or irreversible ones last, immediately before a review step. `[CRAFT]`

### Progressive disclosure

- **IA-18** Required fields are never behind disclosure. Ever. `[FACT]`
- **IA-19** A collapsed section shows a summary of its non-default contents ("3 rules · retries off"). Collapsed ≠ invisible. `[CRAFT]`
- **IA-20** Default state of a disclosure is a product decision based on how often it's needed — not on how it looks. `[PD]`
- **IA-21** Disclosure depth ≤1 inside a form; nested accordions are a defect. `[CRAFT]`
- **IA-22** Anything a user must read before acting (cost, permanence, scope) is inline, never behind a tooltip or "learn more". `[FACT]`

### Screen types

- **IA-23** For any collection, design the triad: **list** (find and compare), **detail** (understand one), **edit** (change one). Don't collapse detail and edit unless changes are trivially reversible and autosaved. `[CRAFT]`
- **IA-24** Modal only when the task is short, atomic, and doesn't require reading the page behind it. Anything deep-linkable, resumable, or reference-requiring becomes a page or a side panel. `[CRAFT]`
- **IA-25** Every list has designed: empty (never used), zero-results (filters too narrow — with a way to widen), loading, error, and permission-limited ("showing 12 of 40; 28 hidden by your role"). `[CRAFT]`

## Screenshot QA

Run on a static capture, no interaction.

1. **Cover the navigation.** Can you still name the page and what it's for? (IA-9, IA-11)
2. **Count top-level nav items.** ≤7? Any two you can't distinguish in one sentence? (IA-1, IA-2)
3. **Find the active nav item.** Does it differ by ≥2 visual channels? Convert to grayscale to check. (IA-3)
4. **Count primary-looking actions.** More than one filled/dominant button = failure. (IA-10)
5. **Count decisions demanded on this screen.** >8 required inputs with no step structure? (IA-13)
6. **Read the group titles.** Any of them a model/table name? (IA-6)
7. **Measure gap inside a group vs. between groups.** Ratio ≥2? (IA-8)
8. **Check the heading outline** (DOM or a11y tree): does it match the visual hierarchy, no skips? (IA-12)
9. **Copy the URL, open in a clean window.** Do filters, tab, sort, page, and open panel survive? (IA-5)
10. **Screenshot each list state**: empty, zero-results, loading, error, permission-limited. All five designed? (IA-25)
11. **Expand every disclosure.** Is anything required in there? Does the collapsed summary reflect non-default values? (IA-18, IA-19)
12. **Follow the success path.** Does the final screen state the outcome and offer a next action? (IA-16)

## Adapt or override

- **Expert tools invert IA-13.** Power users prefer one dense page over a wizard they can't skip.
  If >60% of sessions are repeat users doing the same task, a single form with keyboard order and
  saved defaults beats a flow. Which population you optimize for is `[PD]`.
- **Consumer onboarding inverts IA-10's austerity** — a single-purpose screen with one huge action
  and no nav is correct; IA-1 doesn't apply because there is no nav yet.
- **IA-24 (no modals):** platform conventions win on mobile — sheets carry tasks that would be
  pages on desktop ([MB-12](05-mobile-native-feel.md)).
- **Legally mandated placement** (consent, disclosures, cancellation paths) overrides IA-17 and
  IA-22 sequencing. Follow the regulation. `[PD]`
- **Search-first is legitimate** when the corpus is genuinely too large to browse (>10k items,
  no meaningful taxonomy). Still provide facets and recent/saved items so there's a path without
  a query.
- **When the reference nests deeper than IA-1 allows**, implement the reference and log it: deep
  nav is often a symptom of an org chart, and the fix is a product conversation, not a CSS change. `[PD]`
