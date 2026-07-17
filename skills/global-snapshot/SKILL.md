---
name: global-snapshot
description: Global reusable alias for the canonical snapshot skill. Use when the user asks for $global-snapshot, says this should be global or non-project-specific, or wants the reusable version of snapshot. This alias routes to snapshot/SKILL.md; keep snapshot as the source of truth.
---

# Global Snapshot

This is a global alias for the canonical `snapshot` skill.

Before acting, read and follow the canonical skill:

```text
../snapshot/SKILL.md
```

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `snapshot` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
