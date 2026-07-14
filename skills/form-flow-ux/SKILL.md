---
name: form-flow-ux
description: Design, audit, implement, or verify complete form journeys. Use for create/edit forms, validation, dirty state, autosave, drafts, save/cancel/reset, submit loading, duplicate-submit prevention, server errors, permission denied, optimistic UI, mobile keyboard behavior, file/image upload, crop state, multistep forms, admin/CMS forms, and preserving form UX while restyling.
---

# Form Flow UX

Use this skill when a form must be usable as a workflow, not just visually
complete. A form is not done until create/edit, validation, save, failure, and
escape paths are clear.

Use `$ui-state-matrix` for state coverage, `$accessible-interaction` for
keyboard/focus, `$interaction-flow-qa` for journey proof, `$product-ux-contracts`
for persistence/routing, `$snapshot` for visual evidence, `$mobile-web-qa` for
mobile keyboard, and `$release-gate` before shipping.

## Form Contract

Define before editing:

- mode: create, edit, duplicate, draft, preview, publish, or destructive;
- data source and save target;
- required, optional, derived, readonly, hidden, and role-gated fields;
- validation timing: on blur, on submit, live, server-side;
- dirty state, autosave, draft, cancel/back, reset, and discard confirmation;
- submit behavior: loading, duplicate prevention, optimistic update, rollback;
- success destination: stay, detail page, list page, preview, toast, modal close;
- error behavior: field error, form error, network/server error, permission
  denied, conflict/stale data;
- mobile keyboard and focus path.

## Flow Matrix

```text
Form:
Mode:
Entry point:
Initial data:
Dirty/change behavior:
Validation:
Submit/loading:
Success:
Failure:
Cancel/back/reset:
Reload/autosave:
Permission:
Mobile keyboard:
Verification:
```

## Workflow

1. Trace current data, validation, submit, and navigation handlers.
2. Preserve existing form contracts unless the user intentionally changes them.
3. Implement visual changes without losing labels, helper text, errors, focus,
   disabled reasons, or field grouping.
4. Exercise create and edit separately when both exist.
5. Test invalid submit, valid submit, server failure, cancel/back with dirty
   data, reload/autosave when supported, and permission denied when relevant.
6. Capture `$snapshot` evidence for default, error, loading/disabled, and mobile
   keyboard states when visible.

## File/Image Inputs

For upload or crop flows, verify selected file, preview, replace, remove,
validation, upload failure, persisted asset, crop state, and public rendering.
Use project image/media skills when asset semantics matter.

## Closeout

Report form modes tested, validation/save/cancel/error behavior, mobile/focus
coverage, screenshots/tests, and any unverified backend or permission risk.
