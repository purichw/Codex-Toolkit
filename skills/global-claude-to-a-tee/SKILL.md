---
name: global-claude-to-a-tee
description: Legacy global alias for reference-to-a-tee. Use when an existing prompt invokes global-claude-to-a-tee; follow the generic HTML, image-only, or mixed-reference workflow.
---

# Global Claude To A Tee (Compatibility)

This legacy name routes to the canonical `reference-to-a-tee` skill.

Before acting, read and follow the canonical skill:

```text
../reference-to-a-tee/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements
whenever they apply. Do not treat this global alias as a way to bypass the
canonical snapshot gate.

New prompts should use `$global-reference-to-a-tee` or `$reference-to-a-tee`.
Keep this compatibility entrypoint for existing prompts.
