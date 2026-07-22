---
name: global-prod-smoke-harness
description: Global reusable alias for the canonical prod-smoke-harness skill. Use when the user asks for $global-prod-smoke-harness, says this should be global or non-project-specific, or wants the reusable version of prod smoke harness. This alias routes to prod-smoke-harness/SKILL.md; keep prod-smoke-harness as the source of truth.
---

# Global Prod Smoke Harness

This is a global alias for the canonical `prod-smoke-harness` skill.

Before acting, read and follow the canonical skill:

```text
../prod-smoke-harness/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements
whenever they apply. Do not treat this global alias as a way to bypass the
canonical snapshot gate.

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `prod-smoke-harness` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
