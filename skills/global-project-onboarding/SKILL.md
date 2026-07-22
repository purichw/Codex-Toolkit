---
name: global-project-onboarding
description: Global reusable alias for the canonical project-onboarding skill. Use when the user asks for $global-project-onboarding, says this should be global or non-project-specific, or wants the reusable version of project onboarding. This alias routes to project-onboarding/SKILL.md; keep project-onboarding as the source of truth.
---

# Global Project Onboarding

This is a global alias for the canonical `project-onboarding` skill.

Before acting, read and follow the canonical skill:

```text
../project-onboarding/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements
whenever they apply. Do not treat this global alias as a way to bypass the
canonical snapshot gate.

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `project-onboarding` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
