# Source And Adaptation Notes

Created 2026-11-03 from the user-supplied
`Codex_Fully_Responsive_Web_Design_Kit_v1` folder. The original remains unchanged
in the user's Downloads. Read order began with
`Codex_Responsive_Project_Prompt_TH.md` as requested, then the handbook, source
verification report and relevant demo/helper implementations.

The supplied prompt describes a project workflow, not a skill installer. This
skill distills that material; it does not execute the prompt against an app or
grant permission to redesign, install packages, push or deploy.

## Source Map

| Original | Maintained use |
| --- | --- |
| `Codex_Responsive_Project_Prompt_TH.md` | Core modes, preservation contract, behavior matrix and honest completion evidence |
| `Codex_Responsive_Design_Handbook_TH.md` | Focused layout and verification references, with adaptations below |
| `Responsive_Examples_Verification_TH.md` | Historical source evidence limits, not verification performed by this skill |
| `responsive-audit.mjs` | Reused in `scripts/`, with an existing-output-directory guard and maintained fixture tests |
| `responsive-studio-demo.html` | Teaching example for content-driven composition/navigation, not a production starter |
| `responsive-booking-demo.html` | Teaching example for shared filters, alternate views and resize/focus recovery, not a booking backend |

Original SHA-256 identifiers for future source comparison:

```text
2f637ca9adc5acee9ee7f0bb5deb7e7e8a7a779c773a1cb90eb46f98bfa5e054  Codex_Responsive_Project_Prompt_TH.md
4acc828d4ef96ed6c11e5db77e992865d0c15c638ca12ab7ac0e78884026a506  Codex_Responsive_Design_Handbook_TH.md
0f848b584bb418b163ea740c8f3f43968c900359252e620063ad9c8eec3b2f26  Responsive_Examples_Verification_TH.md
2670a5f88b0d2b69ee35812bc062a3ae49a47e40a755b64a18bbd25d1b7da7ba  responsive-audit.mjs
```

## Intentional Adaptations

- Keep the supplied Thai manual/demos as source material, not duplicated default
  context. The maintained references are self-contained and load by task.
- Use readable role-based type and layout changes instead of the examples'
  viewport-fluid font sizes. Current task/developer constraints take precedence.
- Do not inherit demo branding, large radii, split-hero layout or artwork. Reuse
  only a pattern justified by the real product and active design constraints.
- Scope matrices/sweeps to the touched risk. The source's broad project workflow
  is not mandatory for a one-control repair.
- Require automatic `$snapshot` evidence for visible work, keeping the toolkit's
  visual workflow; source-only skill maintenance is not a visual QA task.
- Preserve earlier evidence: the collector now rejects an existing output path
  instead of overwriting its reports/screenshots. Runtime results remain limited
  to the recorded initial states, not interactions or aesthetic quality.

The supplied verification report explicitly lacked rendered browser evidence.
Do not turn its static/syntax checks into a claim that the demo UI, accessibility
or real-device behavior passed. New helper fixture results are separate evidence,
not retrospective certification of those demos.
