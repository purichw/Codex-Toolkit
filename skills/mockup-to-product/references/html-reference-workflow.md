# HTML Reference Workflow

Use when HTML/CSS or a runnable prototype can answer an in-scope question.
Image-only work does not require HTML. For mixed authority and comparison, read
[reference-evidence.md](reference-evidence.md).

## Inspect The Selected Source

1. Identify the selected version, assets and state. Render relevant source with
   available browser tooling and inspect loading, fonts and missing resources.
2. Read relevant CSS, handlers and dependencies; initial rendering may miss
   routes, dialogs or responsive states. Exercise only the controls needed for
   the requested work or touched behavior. Demo code is evidence, not an
   architecture to transplant into the real product.
3. Use source/computed values when they actually describe the selected visual
   target. Old HTML is not authoritative for a region superseded by an image.
   Keep observed prototype behavior separate from real product requirements.
4. Map the requested surfaces to existing component/data/action owners. Preserve
   permissions, persistence, focus, scroll and supported states; route changed
   contracts to [product-ux-contracts](../../product-ux-contracts/SKILL.md).

If the prototype cannot run, state the limitation and continue from usable image
evidence where it supports the task. Do not claim to have inspected executable
states or exact source-dependent behavior that remains unavailable.

## Optional Inventory Helper

For larger HTML bundles, the standard-library extractor can accelerate discovery:

```sh
python3 /Users/point/.codex/skills/mockup-to-product/scripts/extract_reference.py \
  path/to/reference.html --out .design-reference
```

Optional initial-state rendering requires Python Playwright and a working
browser; use an existing authorized runtime rather than installing by habit:

```sh
python3 /Users/point/.codex/skills/mockup-to-product/scripts/extract_reference.py \
  path/to/reference.html --out .design-reference-rendered \
  --render --screenshots --viewport 1440x900 --viewport 390x844
```

Outputs are `reference-manifest.json`, `reference-manifest.md` and an optional-use
`MOCKUP_TO_PRODUCT_WORKLOG.md` seed. Detected routes, controls, components and
assets are candidates, not an exhaustive inventory or required scope. The
rendered probe observes initial states only; it does not exercise every control,
review images or certify fidelity, accessibility, product behavior or release
readiness. It rejects image files; inspect those directly with an image viewer.

Use a fresh output directory for new evidence. Manifests/captures can be replaced
on rerun; existing worklog notes are preserved. HTML hashes do not cover external
CSS, fonts, scripts or assets: check relevant dependencies before reusing evidence.
A failed optional render returns a failure status while retaining static inventory;
never describe that inventory as successful rendered inspection.

For a small repair, direct source inspection and a brief comparison note are
enough. For page/flow work, track the whole requested scope, including lower-page
sections and relevant states. Do not adopt every generated candidate as a task,
add product capabilities from decorative demo controls or require a release gate
merely because the helper generated a worklog.
