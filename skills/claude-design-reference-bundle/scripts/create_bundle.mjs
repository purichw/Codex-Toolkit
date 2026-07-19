#!/usr/bin/env node
import fs from "node:fs/promises";
import path from "node:path";
import { createRequire } from "node:module";

function parseArgs(argv) {
  const args = {
    viewports: "desktop=1440x1800,mobile=390x1200",
    wait: "1000",
    ready: "body",
    states: [],
    localStorage: [],
    sessionStorage: [],
  };
  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];
    if (!token.startsWith("--")) continue;
    const key = token.slice(2);
    const next = argv[index + 1];
    if (key === "state") {
      args.states.push(next || "");
      index += 1;
    } else if (key === "local-storage") {
      args.localStorage.push(next || "");
      index += 1;
    } else if (key === "session-storage") {
      args.sessionStorage.push(next || "");
      index += 1;
    } else {
      args[key] = next;
      index += 1;
    }
  }
  return args;
}

function parsePairs(values) {
  return values
    .map((value) => {
      const equalsIndex = value.indexOf("=");
      if (equalsIndex === -1) return null;
      return [value.slice(0, equalsIndex), value.slice(equalsIndex + 1)];
    })
    .filter(Boolean);
}

function parseViewports(value) {
  return String(value || "")
    .split(",")
    .map((entry) => entry.trim())
    .filter(Boolean)
    .map((entry) => {
      const [name, size] = entry.split("=");
      const [width, height] = String(size || "").split("x").map((part) => Number.parseInt(part, 10));
      if (!name || !width || !height) throw new Error(`Invalid viewport: ${entry}`);
      return { name, width, height };
    });
}

function parseStates(values) {
  return values
    .map((entry) => {
      const separator = entry.indexOf("=");
      if (separator === -1) return null;
      return {
        name: entry.slice(0, separator).trim(),
        selector: entry.slice(separator + 1).trim(),
      };
    })
    .filter((state) => state?.name && state?.selector);
}

async function loadPlaywright() {
  try {
    return await import("playwright");
  } catch {
    const requireFromCwd = createRequire(path.join(process.cwd(), "package.json"));
    return requireFromCwd("playwright");
  }
}

function slugify(value) {
  return String(value || "page")
    .toLowerCase()
    .replace(/[^a-z0-9ก-๙]+/gi, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80) || "page";
}

async function writeIfMissing(filePath, content) {
  try {
    await fs.access(filePath);
  } catch {
    await fs.writeFile(filePath, content, "utf8");
  }
}

async function preparePage(page, args) {
  const localPairs = parsePairs(args.localStorage);
  const sessionPairs = parsePairs(args.sessionStorage);
  if (!localPairs.length && !sessionPairs.length) return;
  await page.addInitScript(({ localPairs: local, sessionPairs: session }) => {
    try {
      local.forEach(([key, value]) => localStorage.setItem(key, value));
      session.forEach(([key, value]) => sessionStorage.setItem(key, value));
    } catch {
      // Storage may be unavailable on opaque origins or restricted pages.
    }
  }, { localPairs, sessionPairs });
}

async function collectMetrics(page) {
  return page.evaluate(() => {
    const selectors = {
      body: "body",
      header: "header, .site-header, nav",
      main: "main",
      hero: "[class*='hero'], .hero, main > section:first-child",
      h1: "h1",
      primaryPanel: ".temple-search-panel, [class*='panel'], form",
      grid: "[data-popular-temple-grid], [class*='grid']",
      card: "[data-popular-temple-card], [class*='card'], article",
      footer: "footer, .site-footer",
      floatingAction: "[class*='float'], [class*='floating'], [data-temple-map-open]",
    };
    const rectFor = (selector) => {
      const element = document.querySelector(selector);
      if (!element) return null;
      const rect = element.getBoundingClientRect();
      const style = getComputedStyle(element);
      return {
        selector,
        x: Math.round(rect.x),
        y: Math.round(rect.y),
        width: Math.round(rect.width),
        height: Math.round(rect.height),
        fontSize: style.fontSize,
        fontWeight: style.fontWeight,
        lineHeight: style.lineHeight,
        color: style.color,
        backgroundColor: style.backgroundColor,
        borderRadius: style.borderRadius,
        boxShadow: style.boxShadow,
        display: style.display,
        text: (element.textContent || "").replace(/\s+/g, " ").trim().slice(0, 160),
      };
    };
    const cards = [
      ...document.querySelectorAll("[data-popular-temple-card], [class*='card'], article"),
    ];
    const visibleCards = cards.filter((element) => {
      const rect = element.getBoundingClientRect();
      const style = getComputedStyle(element);
      return !element.hidden && style.display !== "none" && rect.width > 0 && rect.height > 0;
    });
    return {
      title: document.title,
      finalUrl: location.href,
      viewport: {
        width: document.documentElement.clientWidth,
        height: window.innerHeight,
      },
      document: {
        scrollWidth: document.documentElement.scrollWidth,
        scrollHeight: document.documentElement.scrollHeight,
        bodyClass: document.body.className,
      },
      counts: {
        candidateCards: cards.length,
        visibleCards: visibleCards.length,
      },
      components: Object.fromEntries(
        Object.entries(selectors).map(([name, selector]) => [name, rectFor(selector)]),
      ),
    };
  });
}

function manifestTemplate({ name, url, screenshots, metricsPath }) {
  const rows = screenshots
    .map((item) => `| ${item.state} | ${item.viewport} | ${item.file} | ${item.url} |`)
    .join("\n");
  return `# ${name} Claude Design Bundle

## Source

- Source URL/file: ${url}
- Created: ${new Date().toISOString()}
- Working directory: ${process.cwd()}
- Metrics: ${metricsPath}

## Screenshots

| State | Viewport | File | URL |
| --- | --- | --- | --- |
${rows}

## Notes

- Fill in user-supplied screenshots, handoff files, exclusions, and known product exceptions.
`;
}

function projectContextTemplate({ name, url }) {
  return `# Project Context

## Surface

- Bundle: ${name}
- Source: ${url}

## What This Page Does

TODO: Explain the user job and where this page fits in the product journey.

## Audience

TODO: Name the primary audience and what they need to decide or do.

## Design Direction

TODO: Describe mood, density, hierarchy, color/material rationale, and brand fit.

## Data And Product Truth

TODO: Record real item counts, source data constraints, CMS/runtime behavior, and content model.

## Current Design Gaps

TODO: List design weaknesses or open questions Claude Design should know.
`;
}

function designSpecTemplate({ name }) {
  return `# Design Spec

## Intent

Replicate the current ${name} surface unless the user explicitly requests redesign.

## Visual Direction

TODO: Mood, material, density, hierarchy, and rhythm.

## Tokens

TODO: Colors, typography, shadows, borders, radius, spacing scale.

## Layout

TODO: Container widths, section heights, grid columns, gaps, padding, breakpoints.

## Components

TODO: Header/nav, hero, controls, cards/list, floating actions, modal/drawer, footer.

## States

TODO: Default, hover, focus, selected, open, empty, loading, disabled, error, mobile menu.

## Responsive

TODO: Desktop/tablet/mobile differences and no-overflow constraints.

## Measured Parity Table

| Component | Viewport | Reference metric | Notes |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |
`;
}

function statesTemplate(screenshots) {
  const rows = screenshots
    .map((item) => `| ${item.state} | ${item.file} | ${item.viewport} | ${item.url} | TODO | needs fill-in |`)
    .join("\n");
  return `# Reference States

| State | File | Viewport | Route | Active UI | Status |
| --- | --- | --- | --- | --- | --- |
${rows}

## State Notes

TODO: Explain what Claude Design should learn from each screenshot.
`;
}

function contractTemplate() {
  return `# Implementation Contract

## Claude Design Should Replicate

TODO: List visual and structural elements to reproduce.

## Product Behavior To Preserve

TODO: Routes, data counts, filters, search, load-more, map, accordions, modals, permissions, privacy, responsive constraints.

## Known Exceptions

TODO: Separate visual exceptions from behavior exceptions.

## Needs Owner Decision

TODO: List uncertain differences that should not be silently standardized.
`;
}

function promptTemplate({ name }) {
  return `# Claude Design Prompt

Use the attached screenshots, metrics, project context, design spec, reference states, and implementation contract to replicate the ${name} page.

Do not redesign unless explicitly asked. Preserve the real product behavior, data counts, routes, responsive constraints, and interaction contracts documented in IMPLEMENTATION-CONTRACT.md.

Deliver a faithful implementation proposal/design that matches the screenshots and measured layout. Call out any place where you intentionally diverge from the source or need an owner decision.
`;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.url || !args.out) {
    throw new Error("Usage: create_bundle.mjs --url <url> --out <output-dir> [--name name]");
  }

  const name = args.name || slugify(args.url);
  const outDir = path.resolve(process.cwd(), args.out);
  const screenshotsDir = path.join(outDir, "screenshots");
  const viewports = parseViewports(args.viewports);
  const states = parseStates(args.states);
  const waitMs = Number.parseInt(args.wait, 10) || 1000;
  const { chromium } = await loadPlaywright();
  const browser = await chromium.launch();
  const metrics = [];
  const screenshots = [];

  await fs.mkdir(screenshotsDir, { recursive: true });

  try {
    for (const viewport of viewports) {
      const context = await browser.newContext({
        viewport: { width: viewport.width, height: viewport.height },
        deviceScaleFactor: 1,
      });
      const page = await context.newPage();
      await preparePage(page, args);
      await page.goto(args.url, { waitUntil: "domcontentloaded" });
      await page.waitForSelector(args.ready, { timeout: 30_000 });
      await page.waitForTimeout(waitMs);

      const defaultFile = `screenshots/${viewport.name}.png`;
      await page.screenshot({ path: path.join(outDir, defaultFile), fullPage: false });
      screenshots.push({ state: "default", viewport: `${viewport.width}x${viewport.height}`, file: defaultFile, url: page.url() });
      metrics.push({ state: "default", viewport: viewport.name, data: await collectMetrics(page) });

      for (const state of states) {
        await page.goto(args.url, { waitUntil: "domcontentloaded" });
        await page.waitForSelector(args.ready, { timeout: 30_000 });
        await page.waitForTimeout(waitMs);
        await page.click(state.selector, { timeout: 10_000 });
        await page.waitForTimeout(waitMs);
        const stateFile = `screenshots/${viewport.name}-${slugify(state.name)}.png`;
        await page.screenshot({ path: path.join(outDir, stateFile), fullPage: false });
        screenshots.push({ state: state.name, viewport: `${viewport.width}x${viewport.height}`, file: stateFile, url: page.url() });
        metrics.push({ state: state.name, viewport: viewport.name, data: await collectMetrics(page) });
      }

      await context.close();
    }
  } finally {
    await browser.close();
  }

  const metricsPath = "metrics.json";
  await fs.writeFile(path.join(outDir, metricsPath), `${JSON.stringify(metrics, null, 2)}\n`, "utf8");
  await writeIfMissing(path.join(outDir, "MANIFEST.md"), manifestTemplate({ name, url: args.url, screenshots, metricsPath }));
  await writeIfMissing(path.join(outDir, "PROJECT-CONTEXT.md"), projectContextTemplate({ name, url: args.url }));
  await writeIfMissing(path.join(outDir, "DESIGN-SPEC.md"), designSpecTemplate({ name }));
  await writeIfMissing(path.join(outDir, "REFERENCE-STATES.md"), statesTemplate(screenshots));
  await writeIfMissing(path.join(outDir, "IMPLEMENTATION-CONTRACT.md"), contractTemplate());
  await writeIfMissing(path.join(outDir, "CLAUDE-DESIGN-PROMPT.md"), promptTemplate({ name }));

  console.log(JSON.stringify({ outDir, screenshots: screenshots.length, metrics: metrics.length }, null, 2));
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
