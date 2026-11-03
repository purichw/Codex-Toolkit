#!/usr/bin/env node
/**
 * Responsive evidence collector — a teaching example, not an accessibility certificate.
 *
 * Prerequisites (run in the project where Playwright will be resolved):
 *   npm install -D playwright
 *   npx playwright install chromium
 *
 * Example:
 *   node responsive-audit.mjs --url http://localhost:8000/responsive-studio-demo.html \
 *     --out ./audit-studio --breakpoints 640,960,1200 --text-stress --reduced-motion
 *
 * Supply the breakpoints actually used by YOUR implementation. This script adds B−1,
 * B, B+1 to the width list. em/rem media-query thresholds use the browser's initial
 * font size, not the authored root font-size; convert them deliberately for a run.
 *
 * Optional runtime integration:
 *   RESP_AUDIT_PLAYWRIGHT_MODULE=/absolute/path/to/playwright/index.mjs
 *   RESP_AUDIT_BROWSER_EXECUTABLE=/absolute/path/to/chromium
 *
 * Exit 0: measured assertions passed, manual review may still be required.
 * Exit 1: document overflow, uncaught page JavaScript error, navigation failure,
 *         or screenshot capture failure in a requested evidence run.
 * Exit 2: invalid options, dependency/browser startup, or output-writing failure.
 *
 * This does NOT click application controls, assess beauty, certify WCAG, test a real
 * touch device, or simulate browser/OS zoom. Use it alongside interaction and visual QA.
 */

import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';

const DEFAULT_WIDTHS = [320, 360, 390, 600, 768, 820, 1024, 1280, 1440, 1920];
const DEFAULT_SHOTS = [390, 820, 1440];
const HELP = `
Responsive audit: collect actual viewport measurements and review evidence.

Required:
  --url URL                One http:, https:, or file: URL; no crawling
  --out DIR                New folder for report.json, report.md, screenshots

Options:
  --widths 320,390,...      CSS viewport widths (default: ${DEFAULT_WIDTHS.join(',')})
  --height 900             CSS viewport height, default 900
  --breakpoints 640,960    Add each actual breakpoint and its ±1px neighbours
  --screenshots 390,820,1440  Capture these widths (also included in audit)
  --screenshots none       Disable screenshots
  --browser chromium      chromium | firefox | webkit; one engine per run
  --sweep                  Also sample 320–1600 CSS px in increments of 32
  --text-stress            Extra runs at 320,390,820,1440 with root font-size 200%
  --reduced-motion         Extra runs at 390,820,1440 with reduced motion enabled
  --help                   Show this message

The default motion preference is no-preference. DPR is 1; no mobile emulation.
Text stress is an authored CSS override, NOT browser zoom or text-only zoom.
All extra stress widths are measured but their screenshots are not automatic.
Animations are disabled for screenshot capture only, not for layout measurements.

Setup in a project:
  npm install -D playwright
  npx playwright install chromium

Example:
  node responsive-audit.mjs --url http://localhost:8000/example.html \\
    --out ./audit --breakpoints 640,960 --text-stress --reduced-motion

Local packages resolve beside this script or from the working directory. An explicit
RESP_AUDIT_PLAYWRIGHT_MODULE can name an absolute Playwright module file. An optional
RESP_AUDIT_BROWSER_EXECUTABLE can select an existing browser executable.
`;

function integer(value, label, min, max) {
  if (!/^\d+$/.test(String(value)) || +value < min || +value > max) {
    throw new Error(`${label} must be an integer from ${min} to ${max}.`);
  }
  return +value;
}

function numberList(value, label) {
  if (!value) throw new Error(`${label} needs comma-separated values.`);
  return value.split(',').map(item => integer(item.trim(), label, 200, 4000));
}

function options(args) {
  const result = {
    widths: DEFAULT_WIDTHS, height: 900, breakpoints: [], screenshots: DEFAULT_SHOTS,
    browser: 'chromium', sweep: false, textStress: false, reducedMotion: false,
  };
  const flags = new Map([
    ['--sweep', 'sweep'], ['--text-stress', 'textStress'], ['--reduced-motion', 'reducedMotion'],
  ]);
  const valued = new Set(['--url', '--out', '--widths', '--height', '--breakpoints', '--screenshots', '--browser']);
  for (let i = 0; i < args.length; i += 1) {
    const arg = args[i];
    if (arg === '--help' || arg === '-h') return { help: true };
    if (flags.has(arg)) { result[flags.get(arg)] = true; continue; }
    if (!valued.has(arg)) throw new Error(`Unknown option: ${arg}`);
    const value = args[++i];
    if (!value || value.startsWith('--')) throw new Error(`${arg} requires a value.`);
    if (arg === '--height') result.height = integer(value, arg, 200, 4000);
    else if (arg === '--widths') result.widths = numberList(value, arg);
    else if (arg === '--breakpoints') result.breakpoints = numberList(value, arg);
    else if (arg === '--screenshots') result.screenshots = value === 'none' ? [] : numberList(value, arg);
    else result[arg.slice(2)] = value;
  }
  if (!result.url || !result.out) throw new Error('--url and --out are required.');
  const url = new URL(result.url);
  if (!['http:', 'https:', 'file:'].includes(url.protocol)) throw new Error('Use an http:, https:, or file: URL.');
  if (!['chromium', 'firefox', 'webkit'].includes(result.browser)) throw new Error('Unsupported --browser.');
  result.out = path.resolve(result.out);
  const widths = new Set([...result.widths, ...result.screenshots]);
  for (const b of result.breakpoints) for (const delta of [-1, 0, 1]) widths.add(b + delta);
  if (result.sweep) for (let w = 320; w <= 1600; w += 32) widths.add(w);
  result.widths = [...widths].sort((a, b) => a - b);
  return result;
}

async function loadPlaywright() {
  if (process.env.RESP_AUDIT_PLAYWRIGHT_MODULE) {
    const file = path.resolve(process.env.RESP_AUDIT_PLAYWRIGHT_MODULE);
    const imported = await import(pathToFileURL(file).href);
    return imported.chromium ? imported : imported.default;
  }
  const requireFromProject = createRequire(path.join(process.cwd(), 'package.json'));
  for (const pkg of ['playwright', '@playwright/test']) {
    try {
      const imported = await import(pkg);
      return imported.chromium ? imported : imported.default;
    } catch { /* Try working-directory resolution before reporting dependency absence. */ }
    try {
      const imported = await import(pathToFileURL(requireFromProject.resolve(pkg)).href);
      return imported.chromium ? imported : imported.default;
    } catch { /* Try the other supported package. */ }
  }
  throw new Error('Playwright is not resolvable. Run npm install -D playwright, then npx playwright install chromium.');
}

// Runs inside the page; no layout mutation and no assumption that every offscreen
// descendant is a defect. A wide table inside its own scrollport is legitimate.
function measurePage() {
  const root = document.documentElement;
  const scroll = document.scrollingElement || root;
  const css = element => getComputedStyle(element);
  const clippedValues = new Set(['hidden', 'clip']);
  const localScrollValues = new Set(['auto', 'scroll']);
  const all = [...document.body.querySelectorAll('*')];
  const visibilityCache = new WeakMap();
  function visible(element) {
    if (visibilityCache.has(element)) return visibilityCache.get(element);
    let result = element.getClientRects().length > 0;
    for (let node = element; result && node instanceof Element; node = node.parentElement) {
      const style = css(node);
      if (style.display === 'none' || style.visibility === 'hidden' || Number(style.opacity) === 0) result = false;
      if (node.hasAttribute('inert') || node.getAttribute('aria-hidden') === 'true') result = false;
    }
    const r = element.getBoundingClientRect();
    const style = css(element);
    if (r.width <= 1 && r.height <= 1) result = false; // common visually-hidden/focus-only label
    if (style.clip !== 'auto' && r.width <= 2) result = false;
    visibilityCache.set(element, result);
    return result;
  }
  function selector(element) {
    if (element.id) return `#${CSS.escape(element.id)}`;
    const classes = [...element.classList].slice(0, 3).map(name => `.${CSS.escape(name)}`).join('');
    const label = element.getAttribute('aria-label');
    return `${element.localName}${classes}${label ? `[aria-label=${JSON.stringify(label)}]` : ''}`;
  }
  function containedByLocalOverflow(element) {
    for (let ancestor = element.parentElement; ancestor && ancestor !== document.body && ancestor !== root; ancestor = ancestor.parentElement) {
      const style = css(ancestor);
      if (localScrollValues.has(style.overflowX) || clippedValues.has(style.overflowX)) return true;
    }
    return false;
  }
  const viewportWidth = root.clientWidth;
  const edgeCandidates = [];
  const clippedCandidates = [];
  const localScrollers = [];
  const smallTargets = [];
  for (const element of all) {
    if (!visible(element)) continue;
    const rect = element.getBoundingClientRect();
    const style = css(element);
    const hasHorizontalOverflow = element.scrollWidth > element.clientWidth + 1;
    const hasVerticalOverflow = element.scrollHeight > element.clientHeight + 1;
    if ((rect.right > viewportWidth + 1 || rect.left < -1) && !containedByLocalOverflow(element)) {
      edgeCandidates.push({ selector: selector(element), left: +rect.left.toFixed(2), right: +rect.right.toFixed(2) });
    }
    if (hasHorizontalOverflow && localScrollValues.has(style.overflowX)) {
      localScrollers.push({ selector: selector(element), scrollWidth: element.scrollWidth, clientWidth: element.clientWidth, reason: 'Local horizontal scroll region; inspect discoverability and keyboard access.' });
    }
    // A candidate may be an intentional avatar crop, decorative frame, or truncation.
    // Do not turn these heuristics into a universal pass/fail assertion.
    if ((hasHorizontalOverflow && clippedValues.has(style.overflowX)) || (hasVerticalOverflow && clippedValues.has(style.overflowY))) {
      clippedCandidates.push({ selector: selector(element), axis: [hasHorizontalOverflow && clippedValues.has(style.overflowX) ? 'x' : '', hasVerticalOverflow && clippedValues.has(style.overflowY) ? 'y' : ''].join(''), reason: 'Overflow is clipped; verify no required text or control is lost.' });
    }
    if (element.matches('button,input:not([type=hidden]),select,textarea,[role=button],a[href]') && !element.disabled) {
      if (rect.width < 44 || rect.height < 44) smallTargets.push({ selector: selector(element), width: +rect.width.toFixed(1), height: +rect.height.toFixed(1), reason: 'Below this kit’s preferred 44px target. Not by itself a WCAG failure; inline links and spacing need context.' });
    }
  }
  const images = [...document.images].filter(img => img.complete && img.naturalWidth === 0 && (img.currentSrc || img.getAttribute('src'))).map(img => ({ selector: selector(img), source: img.currentSrc || img.getAttribute('src') }));
  const fontErrors = document.fonts ? [...document.fonts].filter(font => font.status === 'error').map(font => font.family) : [];
  const globalClipping = ['html', 'body'].filter(name => clippedValues.has(css(document.querySelector(name)).overflowX));
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  return {
    viewport: { width: innerWidth, height: innerHeight, clientWidth: viewportWidth, dpr: devicePixelRatio },
    document: { scrollWidth: scroll.scrollWidth, clientWidth: scroll.clientWidth, scrollHeight: scroll.scrollHeight },
    horizontalOverflow: scroll.scrollWidth > scroll.clientWidth + 1,
    edgeCandidates: edgeCandidates.slice(0, 30),
    clippedCandidates: clippedCandidates.slice(0, 30),
    localScrollers: localScrollers.slice(0, 30),
    smallTargets: smallTargets.slice(0, 30),
    candidateLimits: { perCategory: 30, totalEdge: edgeCandidates.length, totalClipped: clippedCandidates.length, totalSmallTargets: smallTargets.length },
    brokenImages: images, fontErrors, globalClipping,
    rootFontSize: css(root).fontSize, reducedMotion,
  };
}

async function settle(page) {
  // Network-idle is unsuitable for long polling apps. Layout/fonts are enough for
  // these measurements, with a bounded timeout for a page that never settles.
  await page.evaluate(async () => {
    if (document.fonts) await Promise.race([document.fonts.ready, new Promise(resolve => setTimeout(resolve, 4000))]);
    await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
  });
}

async function runViewport(browser, config, width, variant = 'default') {
  const context = await browser.newContext({
    viewport: { width, height: config.height }, deviceScaleFactor: 1,
    reducedMotion: variant === 'reduced-motion' ? 'reduce' : 'no-preference',
  });
  const page = await context.newPage();
  const evidence = { width, height: config.height, variant, failures: [], warnings: [], consoleErrors: [], requestsFailed: [], httpErrors: [], pageErrors: [] };
  page.on('pageerror', error => evidence.pageErrors.push(error.message));
  page.on('console', msg => { if (msg.type() === 'error') evidence.consoleErrors.push(msg.text()); });
  page.on('requestfailed', request => evidence.requestsFailed.push({ url: request.url(), error: request.failure()?.errorText }));
  page.on('response', response => { if (response.status() >= 400) evidence.httpErrors.push({ url: response.url(), status: response.status() }); });
  try {
    const response = await page.goto(config.url, { waitUntil: 'load', timeout: 30000 });
    if (response && response.status() >= 400) evidence.failures.push(`Main document HTTP ${response.status()}`);
    if (variant === 'root-font-200') {
      await page.addStyleTag({ content: 'html { font-size: 200% !important; }' });
      evidence.warnings.push('Authored root font-size 200% stress only. This does not model browser zoom or multiply every text size by two.');
    }
    await settle(page);
    evidence.metrics = await page.evaluate(measurePage);
    if (evidence.metrics.horizontalOverflow) evidence.failures.push(`Document horizontal overflow: ${evidence.metrics.document.scrollWidth} > ${evidence.metrics.document.clientWidth} CSS px`);
    if (evidence.metrics.globalClipping.length) evidence.warnings.push(`Global overflow clipping on ${evidence.metrics.globalClipping.join(', ')} can mask layout defects; inspect manually.`);
    if (evidence.metrics.brokenImages.length) evidence.warnings.push(`${evidence.metrics.brokenImages.length} completed images have no decoded width.`);
    if (evidence.metrics.fontErrors.length) evidence.warnings.push(`Font loading errors: ${evidence.metrics.fontErrors.join(', ')}`);
    if (variant === 'default' && config.screenshots.includes(width)) {
      const filename = `viewport-${width}x${config.height}-${config.browser}.png`;
      await page.screenshot({ path: path.join(config.out, filename), fullPage: true, animations: 'disabled', caret: 'hide', timeout: 30000 });
      evidence.screenshot = filename;
    }
  } catch (error) {
    evidence.failures.push(error.message);
  } finally {
    if (evidence.pageErrors.length) evidence.failures.push(`${evidence.pageErrors.length} uncaught page JavaScript error(s)`);
    if (evidence.consoleErrors.length || evidence.requestsFailed.length || evidence.httpErrors.length) evidence.warnings.push('Console/network events require review; details are recorded in report.json.');
    await context.close();
  }
  evidence.status = evidence.failures.length ? 'FAIL' : 'PASS';
  return evidence;
}

function markdown(report) {
  const escape = value => String(value).replaceAll('|', '\\|').replaceAll('\n', ' ');
  const rows = report.runs.map(run => {
    const m = run.metrics;
    const reviewCount = (m?.edgeCandidates.length || 0) + (m?.clippedCandidates.length || 0) + (m?.smallTargets.length || 0);
    return `| ${run.width} × ${run.height} | ${run.variant} | ${run.status} | ${m ? `${m.document.scrollWidth} / ${m.document.clientWidth}` : 'unavailable'} | ${reviewCount} | ${run.screenshot ? `[PNG](${run.screenshot})` : '—'} |`;
  }).join('\n');
  const failures = report.runs.filter(run => run.failures.length).map(run => `- **${run.width}px / ${run.variant}:** ${run.failures.map(escape).join('; ')}`).join('\n') || 'None in the measured states.';
  const review = report.runs.filter(run => run.warnings.length).map(run => `- **${run.width}px / ${run.variant}:** ${run.warnings.map(escape).join('; ')}`).join('\n') || 'No extra runtime warnings. Candidate details still need visual judgement.';
  return `# Responsive audit evidence\n\n` +
    `- URL: ${report.url}\n- Recorded: ${report.startedAt}\n- Engine: ${report.environment.engine} ${report.environment.browserVersion}\n- Host: ${report.environment.platform}; Node ${report.environment.node}\n- Device pixel ratio: 1; desktop browser context; no real-device emulation\n- Result: **${report.summary.failed ? 'FAIL' : 'MEASURED CHECKS PASSED'}** (${report.summary.total} viewport/state runs)\n\n` +
    `## Measured states\n\n| CSS viewport | State | Assertions | Document scroll / client width | Review candidates* | Screenshot |\n| --- | --- | --- | --- | --- | --- |\n${rows}\n\n` +
    `*Candidates are capped per category in JSON. A small control, intentional image crop, or local table scroller is not automatically a defect. See candidateLimits for uncapped counts.\n\n` +
    `## Assertion failures\n\n${failures}\n\n## Runtime review notes\n\n${review}\n\n` +
    `## What these checks establish\n\nThe listed initial page states were rendered at their recorded CSS viewport sizes in the named engine. The collector checks document horizontal overflow (1px tolerance), uncaught page JavaScript errors, navigation, and requested screenshot capture. It records possible clipping, edge offenders, local scrollers, smaller targets, and network/font/image errors for review. Screenshots disable animations only at capture time.\n\n` +
    `## Remaining manual checks\n\n` +
    `- Judge visual hierarchy, spacing, crop/focal point, and correspondence with the reference at wide, middle, narrow, and transition widths.\n` +
    `- Test all controls, open menus/dialogs, errors, empty/loading states, keyboard focus, Escape, and focus return; this collector does not exercise interactions.\n` +
    `- Resize while an interactive state is open. Separate viewport loads do not prove that state survives resize.\n` +
    `- Test browser zoom (including 200%), reflow at the required effective width, and text spacing. Root-font stress is not an equivalent substitute.\n` +
    `- Verify that reduced-motion preference actually changes nonessential motion appropriately. Setting the preference alone does not establish that the page respects it.\n` +
    `- Check short landscape viewports, the mobile on-screen keyboard, safe areas, touch input, and a real mobile browser as applicable.\n` +
    `- Inspect local horizontal scrolling for meaningful labels, visible affordance, keyboard access, and preserved relationships.\n` +
    `- Run other target engines separately. A Chromium result says nothing conclusive about Firefox, WebKit, or real iOS Safari.\n` +
    `- Audit accessibility semantics, contrast, screen-reader behavior, target-size exceptions, and focus occlusion separately. Passing this file does not certify WCAG or design quality.\n\n` +
    `## Detailed evidence\n\n[report.json](report.json) contains environment, options, all measured metrics, candidate selectors, and runtime events.\n`;
}

async function main() {
  const config = options(process.argv.slice(2));
  if (config.help) { console.log(HELP); return; }
  const playwright = await loadPlaywright();
  // Claim a fresh directory atomically; never overwrite earlier evidence.
  await fs.mkdir(path.dirname(config.out), { recursive: true });
  try {
    await fs.mkdir(config.out);
  } catch (error) {
    if (error.code === 'EEXIST') throw new Error('Output directory already exists. Choose a new --out path to preserve earlier evidence.');
    throw error;
  }
  const startedAt = new Date().toISOString();
  const launchOptions = { headless: true };
  if (process.env.RESP_AUDIT_BROWSER_EXECUTABLE) launchOptions.executablePath = process.env.RESP_AUDIT_BROWSER_EXECUTABLE;
  const browser = await playwright[config.browser].launch(launchOptions);
  const report = {
    schemaVersion: 1, startedAt, url: config.url, options: config,
    environment: { engine: config.browser, browserVersion: browser.version(), node: process.version, platform: `${os.platform()} ${os.release()}`, dpr: 1 },
    runs: [],
  };
  try {
    for (const width of config.widths) {
      const run = await runViewport(browser, config, width);
      report.runs.push(run);
      console.log(`${run.status} ${width}×${config.height} default${run.failures.length ? ` — ${run.failures.join('; ')}` : ''}`);
    }
    for (const [enabled, variant, widths] of [
      [config.textStress, 'root-font-200', [320, 390, 820, 1440]],
      [config.reducedMotion, 'reduced-motion', [390, 820, 1440]],
    ]) {
      if (!enabled) continue;
      for (const width of widths) {
        const run = await runViewport(browser, config, width, variant);
        report.runs.push(run);
        console.log(`${run.status} ${width}×${config.height} ${variant}${run.failures.length ? ` — ${run.failures.join('; ')}` : ''}`);
      }
    }
  } finally {
    await browser.close();
  }
  report.completedAt = new Date().toISOString();
  report.summary = { total: report.runs.length, failed: report.runs.filter(run => run.status === 'FAIL').length };
  await fs.writeFile(path.join(config.out, 'report.json'), JSON.stringify(report, null, 2) + '\n');
  await fs.writeFile(path.join(config.out, 'report.md'), markdown(report));
  console.log(`Evidence: ${config.out}; ${report.summary.failed}/${report.summary.total} failed. Manual review remains necessary.`);
  process.exitCode = report.summary.failed ? 1 : 0;
}

main().catch(error => {
  console.error(`Responsive audit could not finish: ${error.message}`);
  process.exitCode = 2;
});
