# Primary references

Consult the documentation for the framework and versions actually installed in the project. The links below support platform behavior and verification guidance; they do not prescribe this skill's folder names or require a particular tool. Sharing scopes, extraction criteria, and ownership records are engineering recommendations to apply in context.

The supplied package lists these sources as reviewed on 2026-11-03. Installation
does not re-audit every external page; verify the installed framework's current
documentation when a version-specific claim matters.

| Source | Relevant use |
| --- | --- |
| [React — Thinking in React](https://react.dev/learn/thinking-in-react) | Decompose UI responsibilities, model visual states, and reason about data flow. |
| [React — Sharing State Between Components](https://react.dev/learn/sharing-state-between-components) | Give coordinated state an appropriate common owner; distinguish controlled and uncontrolled components. |
| [React — Choosing the State Structure](https://react.dev/learn/choosing-the-state-structure) | Avoid contradictory and duplicated state; derive values when possible. |
| [React — Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state) | Understand how component position, type, and keys affect state during refactors. |
| [React — `use client`](https://react.dev/reference/rsc/use-client) | Respect client module boundaries and transitive dependencies in React Server Component environments. |
| [Next.js — Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) | Apply server/client composition rules when the host is Next.js; other frameworks have their own rules. |
| [TypeScript — Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) | Use discriminated unions and exhaustiveness checking for coherent typed states. |
| [TypeScript — Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) | Type assertions do not add runtime checking; validate unknown data at its boundary. |
| [TypeScript — The `satisfies` Operator](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html#the-satisfies-operator) | Check an expression against a type while retaining useful inference, as in the example's status mappings. |
| [WAI-ARIA APG — Modal Dialog Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) | Understand a dialog's focus and keyboard obligations before creating or wrapping that interaction. |
| [Testing Library — Guiding Principles](https://testing-library.com/docs/guiding-principles/) | Prefer tests of user-observable behavior over private implementation details. |
| [Testing Library — About Queries](https://testing-library.com/docs/queries/about/) | Query by accessible role/name and labels where appropriate. |
| [Storybook — Accessibility Tests](https://storybook.js.org/docs/writing-tests/accessibility-testing) | Use automated checks as one part of component verification when Storybook is already useful. |
| [ESLint — `no-restricted-imports`](https://eslint.org/docs/latest/rules/no-restricted-imports) | Enforce specified import restrictions; aliases alone do not create an architectural boundary. |
| [Semantic Versioning 2.0.0](https://semver.org/) | Define and communicate compatibility for independently released public APIs. A single application may instead migrate its consumers together. |

Check the source's exact scope before extending a claim. For example, a component being rendered beneath a client component does not alone prove its implementation joins the client module graph; inspect imports and the framework's supported composition mechanism. Likewise, an automated accessibility check passing is not a complete assessment of an interactive component.

## Local Integration

Imported on 2026-11-03 from the user's `shared-component-architecture` folder,
keeping the original Downloads package unchanged. Its original `SKILL.md`
SHA-256 is `29115014a44634ea8af0dd71f42ee66a6552373966d0ec5475e81dc0303b071c`.

The installed copy adds focused toolkit routing, automatic snapshot evidence for
visible work, complete-deliverable checks and explicit authorization boundaries.
Codex metadata keeps supported interface/implicit-invocation fields instead of
the source's multi-product policy list. The example uses role-based heading
type, excludes raw-HTML overrides from content-owning components and adds negative
type cases plus a reproducible server-render helper. These checks do not certify
visual design, accessibility, real interaction or any application's backend.
