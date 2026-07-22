---
name: global-admin-prototype-reconciliation
description: Global reusable alias for the canonical admin-prototype-reconciliation skill. Use when the user asks for $global-admin-prototype-reconciliation, says this should be global or non-project-specific, or wants the reusable version of admin prototype reconciliation. This alias routes to admin-prototype-reconciliation/SKILL.md; keep admin-prototype-reconciliation as the source of truth.
---

# Global Admin Prototype Reconciliation

This is a global alias for the canonical `admin-prototype-reconciliation` skill.

Before acting, read and follow the canonical skill:

```text
../admin-prototype-reconciliation/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements
whenever they apply. Do not treat this global alias as a way to bypass the
canonical snapshot gate.

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `admin-prototype-reconciliation` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
