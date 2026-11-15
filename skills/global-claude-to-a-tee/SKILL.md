---
name: global-claude-to-a-tee
description: Legacy global alias for mockup-to-product. Use when an existing prompt invokes global-claude-to-a-tee; follow the generic HTML, image-only, or mixed-reference workflow.
---

# Global Claude To A Tee (Compatibility)

This legacy name routes to the canonical `mockup-to-product` skill.

Before acting, read and follow the canonical skill:

```text
../mockup-to-product/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements
whenever they apply. Do not treat this global alias as a way to bypass the
canonical snapshot gate.

New prompts should use `$global-mockup-to-product` or `$mockup-to-product`.
Keep this compatibility entrypoint for existing prompts.
The legacy name does not impose an exact-by-default mode; respect only the
user's actual matching constraints and the canonical product-judgment workflow.
