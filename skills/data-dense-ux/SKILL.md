---
name: data-dense-ux
description: Design, implement, audit, or verify data-dense UI such as admin dashboards, tables, lists, ledgers, CMS grids, search results, filters, pagination, bulk actions, virtualized lists, relationship maps, and operational panels. Use when the user asks to make dense information easier to scan, compare, sort, filter, select, paginate, compress responsively, or operate at large-data scale without turning it into a marketing-style layout.
---

# Data Dense UX

Use this skill for interfaces people scan, compare, filter, and operate
repeatedly. Dense UI should be calm, legible, and fast, not decorative.

Use `$admin-ops` for privileged admin operations, `$ledger-logic` for financial
tables, `$product-ux-contracts` for pagination/scroll/routing contracts,
`$ui-state-matrix` for empty/loading/error/selected states, `$snapshot` as
mandatory visual proof before final response, `$mobile-web-qa` for responsive
compression, and `$release-gate` before shipping.

## Design Rules

- Prioritize scan paths: primary label, status, owner, date, amount/count, action.
- Keep row/card density consistent; avoid marketing-sized cards for operations.
- Make filters, search, sort, pagination, and selected count visible and stable.
- Preserve item counts, page size, load more, virtualization, and scroll bounds.
- Keep destructive or privileged actions visually distinct and confirmed.
- Handle long labels, empty values, unknown data, partial failures, and stale
  records.
- Use responsive compression: hide secondary columns behind detail panels or
  row expansion rather than cramming unreadable tables.

## Workflow

1. Identify the primary data task: scan, compare, find, edit, select, export,
   audit, publish, delete, or investigate.
2. Map data fields by priority and risk.
3. Preserve existing data contracts: sorting, filtering, pagination, selection,
   URL state, and reload behavior.
4. Design dense states: loading, empty, no results, error, partial data, selected,
   disabled, permission denied, bulk action, and overflow.
5. Verify with realistic item counts, long text, and at least one edge record.
6. Capture `$snapshot` evidence before final response; include desktop and
   mobile/tablet when responsive behavior changes.

## Verification

- Search/filter/sort produce expected visible rows and URL/state when supported.
- First/last item reachable; page size and total counts are honest.
- Selection survives intended navigation or clears intentionally.
- Bulk actions show count, confirmation, success/failure, and undo/rollback if
  supported.
- Tables/lists do not overflow horizontally except intentional internal scroll.
- Mobile layout keeps primary fields and actions reachable.

## Closeout

Report data task, fields prioritized, density decisions, preserved contracts,
states tested, item counts used, screenshots/tests, and remaining large-data risk.
