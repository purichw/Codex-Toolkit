// Checks deterministic synthetic interactions; authored calibration is not agent A/B.
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { createHash } = require('node:crypto');
const { chromium } = require('playwright');
const args = process.argv.slice(2);
if (args.includes('--help')) {
  console.log('node evals/fixture-check.cjs FIXTURE_DIR OUT [--calibration CSS] [--record-baseline]\nRequires Playwright + Chrome or CHROMIUM_BIN. New OUT outside FIXTURE_DIR.');
  process.exit(0);
}
const [input, output, ...flags] = args;
if (!input || !output) throw Error('Use --help');
let calibration;
let baseline = false;
for (let i = 0; i < flags.length; i++) {
  if (flags[i] === '--record-baseline') baseline = true;
  else if (flags[i] === '--calibration' && flags[i + 1]) calibration = path.resolve(flags[++i]);
  else throw Error('Unknown argument; use --help');
}
const root = fs.realpathSync(input);
const out = path.resolve(output);
if (fs.existsSync(out) || out === root || out.startsWith(root + path.sep)) throw Error('Use a new OUT outside fixtures');
const hash = data => createHash('sha256').update(data).digest('hex');
const sourceHashes = Object.fromEntries(['index.html', 'fixture.css', 'fixture.js'].map(p => [p, hash(fs.readFileSync(path.join(root, p)))]));
if (calibration) sourceHashes.authoredCalibration = hash(fs.readFileSync(calibration));
fs.mkdirSync(out, { recursive: true });
(async () => {
  const browser = await chromium.launch(process.env.CHROMIUM_BIN ? { executablePath: process.env.CHROMIUM_BIN } : { channel: 'chrome' });
  const report = { browser: browser.version(), mode: calibration ? 'authored demonstration, not agent output' : 'fixture output', sourceHashes, captures: [], failures: [] };
  try {
    for (const [width, height] of [[1280, 800], [390, 844], [320, 800]]) {
      for (const name of ['dashboard', 'mobile-form', 'editorial']) {
        const context = await browser.newContext({ viewport: { width, height }, locale: 'en-US', timezoneId: 'Asia/Bangkok', reducedMotion: 'reduce', deviceScaleFactor: 1 });
        const page = await context.newPage();
        const errors = [];
        page.on('pageerror', e => errors.push(e.message));
        page.on('requestfailed', r => errors.push(r.url()));
        await page.goto(pathToFileURL(path.join(root, 'index.html')).href + '#' + name);
        if (calibration) await page.addStyleTag({ path: calibration });
        await page.evaluate(() => document.fonts.ready);
        const checks = {};
        if (name === 'dashboard') {
          await page.locator('#filter').fill('Central');
          checks.filterWorks = await page.locator('tbody tr:visible').count() === 1;
          await page.locator('tbody tr:visible button').first().click();
          checks.actionWorks = (await page.locator('#detail').textContent()).includes('Review: Central library');
          checks.filterRetained = await page.locator('#filter').inputValue() === 'Central';
          await page.locator('#filter').fill('');
          await page.evaluate(() => { document.querySelector('#detail').textContent = 'Select an action to inspect a synthetic record.'; document.querySelector('.table-scroll').scrollLeft = 0; });
          checks.amountsSingleLine = await page.locator('.amount').evaluateAll(cells => cells.every(e => { const r = document.createRange(); r.selectNodeContents(e); return r.getClientRects().length === 1; }));
          if (width < 850) {
            const scroll = page.locator('.table-scroll');
            await scroll.focus();
            await page.keyboard.press('ArrowRight');
            try {
              await page.waitForFunction(() => document.querySelector('.table-scroll').scrollLeft > 0, null, { timeout: 1000 });
              checks.keyboardHorizontalScroll = true;
            } catch { checks.keyboardHorizontalScroll = false; }
            await page.locator('tbody tr').last().locator('button').last().click();
            checks.lastActionReachable = (await page.locator('#detail').textContent()).includes('Archive preview: East learning centre');
            const endFile = `${name}-${width}-scroll-end.png`;
            await page.screenshot({ path: path.join(out, endFile), fullPage: true });
            report.captures.push({ file: endFile, sha256: hash(fs.readFileSync(path.join(out, endFile))), route: page.url(), viewport: [width, height], state: 'last-action', reviewed: false });
            await page.evaluate(() => { document.querySelector('.table-scroll').scrollLeft = 0; document.querySelector('#detail').textContent = 'Select an action to inspect a synthetic record.'; });
          }
        } else if (name === 'mobile-form') {
          await page.locator('button[type=submit]').click();
          checks.invalidEmailExplained = await page.locator('#email-error').isVisible();
          checks.inputRetained = await page.locator('[name=contact]').inputValue() === 'กนกวรรณ Example';
          checks.focusAtError = await page.locator('[name=email]').evaluate(e => e === document.activeElement);
          checks.noLabelOrErrorCollision = await page.locator('.field-name,.error:visible').evaluateAll(nodes => nodes.every(e => { const r = document.createRange(); r.selectNodeContents(e); return r.getBoundingClientRect().bottom <= e.getBoundingClientRect().bottom + 1; }));
          checks.preferenceRoles = await page.evaluate(() => [...document.querySelectorAll('.field-name')].every(e => getComputedStyle(e).textAlign === 'center') && ['start', 'left'].includes(getComputedStyle(document.querySelector('.hint')).textAlign));
        } else {
          checks.readingMeasure = await page.locator('article p').evaluateAll(nodes => nodes.every(e => e.getBoundingClientRect().width >= Math.min(innerWidth - 96, 320) - 1));
          checks.bitmapRendered = await page.locator('canvas').evaluate(c => new Set(c.getContext('2d').getImageData(0, 0, c.width, c.height).data).size > 10);
        }
        checks.noPageOverflow = await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth);
        checks.noRuntimeErrors = errors.length === 0;
        await page.evaluate(() => { document.activeElement?.blur(); scrollTo(0, 0); });
        const file = `${name}-${width}.png`;
        await page.screenshot({ path: path.join(out, file), fullPage: true });
        report.captures.push({ file, sha256: hash(fs.readFileSync(path.join(out, file))), route: page.url(), viewport: [width, height], state: name === 'mobile-form' ? 'invalid-email' : 'ready', checks, errors, reviewed: false });
        report.failures.push(...Object.entries(checks).filter(([, ok]) => !ok).map(([key]) => `${name}/${width}/${key}`));
        await context.close();
      }
    }
  } finally { await browser.close(); }
  fs.writeFileSync(path.join(out, 'report.json'), JSON.stringify(report, null, 2));
  console.log(JSON.stringify({ out, failures: report.failures, captures: report.captures.length }, null, 2));
  if (report.failures.length && !baseline) process.exitCode = 1;
})().catch(e => { console.error(e); process.exitCode = 1; });
