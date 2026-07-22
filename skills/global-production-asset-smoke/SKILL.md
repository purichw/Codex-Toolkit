---
name: global-production-asset-smoke
description: Global reusable alias for the canonical production-asset-smoke skill. Use when the user asks for $global-production-asset-smoke, says this should be global or non-project-specific, or wants the reusable version of production asset smoke. This alias routes to production-asset-smoke/SKILL.md; keep production-asset-smoke as the source of truth.
---

# Global Production Asset Smoke

This is a global alias for the canonical `production-asset-smoke` skill.

Before acting, read and follow the canonical skill:

```text
../production-asset-smoke/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements
whenever they apply. Do not treat this global alias as a way to bypass the
canonical snapshot gate.

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `production-asset-smoke` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
