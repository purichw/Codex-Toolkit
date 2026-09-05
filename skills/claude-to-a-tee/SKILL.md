---
name: claude-to-a-tee
description: Compatibility name for reference-to-a-tee. Use when an existing prompt explicitly invokes claude-to-a-tee or says Claude to a tee. Route to the generic skill for HTML, image-only, or mixed references from any source.
---

# Claude To A Tee (Compatibility)

The canonical skill is now [reference-to-a-tee](../reference-to-a-tee/SKILL.md).
Read and follow it before implementation, comparison, repair, or handoff.

The reference may be HTML, image files, or both; image-only work does not require
HTML. Use the canonical mode-specific workflows, product-contract safeguards,
and mandatory automatic `$snapshot` comparison. Do not apply the former
HTML-only restrictions.

Keep this entrypoint for existing prompts. New prompts should use
`$reference-to-a-tee`. The old reference paths redirect to canonical guidance,
and the old extractor command forwards to the HTML-only helper while preserving
its legacy default output directory and worklog filename.
