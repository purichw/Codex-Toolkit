---
name: global-claude-design-md-request
description: Global reusable alias for the canonical claude-design-md-request skill. Use when the user asks for $global-claude-design-md-request, says this should be global or non-project-specific, or wants the reusable version of claude design md request. This alias routes to claude-design-md-request/SKILL.md; keep claude-design-md-request as the source of truth.
---

# Global Claude Design Md Request

This is a global alias for the canonical `claude-design-md-request` skill.

Before acting, read and follow the canonical skill:

```text
../claude-design-md-request/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements
whenever they apply. Do not treat this global alias as a way to bypass the
canonical snapshot gate.

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `claude-design-md-request` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
