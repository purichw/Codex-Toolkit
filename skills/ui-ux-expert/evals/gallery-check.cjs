// Local static-specimen checks, not a design score or production widget test.
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { createHash } = require('node:crypto');
const { chromium } = require('playwright');

const args = process.argv.slice(2);
if (args.includes('--help')) {
  console.log('node evals/gallery-check.cjs ROOT OUT [--record-baseline]\nRequires Playwright and installed Chrome (or CHROMIUM_BIN). OUT must be new and outside ROOT.');
  process.exit(0);
}
if (args.length < 2 || args.length > 3 || (args[2] && args[2] !== '--record-baseline')) throw Error('Use --help');
const root = fs.realpathSync(args[0]);
const out = path.resolve(args[1]);
if (out === root || out.startsWith(root + path.sep) || fs.existsSync(out)) throw Error('Use a new output directory outside ROOT');
const hash = data => createHash('sha256').update(data).digest('hex');
const sources = ['assets/component-gallery.html', 'tokens.css', 'assets/gallery-base.css'].filter(p => fs.existsSync(path.join(root, p)));
const sourceHashes = Object.fromEntries(sources.map(p => [p, hash(fs.readFileSync(path.join(root, p)))]));
fs.mkdirSync(out, { recursive: true });
const report = { scope: 'Static gallery geometry/contrast; no live widget or agent A/B claims', sourceHashes, captures: [], checks: [] };

(async () => {
  const browser = await chromium.launch(process.env.CHROMIUM_BIN
    ? { executablePath: process.env.CHROMIUM_BIN, headless: true }
    : { channel: 'chrome', headless: true });
  report.browser = browser.version();
  try {
    for (const [width, height] of [[1280, 800], [768, 1024], [390, 844], [320, 800]]) {
      const context = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: 1, locale: 'en-US', timezoneId: 'Asia/Bangkok', reducedMotion: 'reduce' });
      const page = await context.newPage();
      const errors = [];
      page.on('pageerror', e => errors.push(e.message));
      page.on('requestfailed', r => errors.push(`${r.url()}: ${r.failure()?.errorText}`));
      await page.goto(pathToFileURL(path.join(root, sources[0])).href, { waitUntil: 'load' });
      await page.evaluate(() => document.fonts.ready);
      for (const state of ['default', 'long-copy']) {
        if (state === 'long-copy') await page.evaluate(() => {
          document.querySelectorAll('.card h3,.modal h3').forEach(e => { e.textContent = 'Synthetic: review the complete regional delivery schedule'; });
          document.querySelectorAll('.card p,.modal p,.toast > span').forEach(e => { e.textContent = 'Synthetic: Changes could not be saved. Your entered details are retained; review the delivery date and try again.'; });
          document.querySelectorAll('.field__label').forEach(e => { e.textContent = 'ชื่อผู้รับการติดต่อและผู้ประสานงานสำรอง / Contact person'; });
        });
        const measurements = await page.evaluate(() => {
          const style = e => getComputedStyle(e);
          const rect = e => e.getBoundingClientRect();
          const cells = [...document.querySelector('tbody tr').children];
          const textFits = e => {
            const range = document.createRange(); range.selectNodeContents(e);
            const r = range.getBoundingClientRect(), b = rect(e);
            return r.bottom <= b.bottom + 1 && r.right <= b.right + 1 && r.left >= b.left - 1;
          };
          const ctx = document.createElement('canvas').getContext('2d', { willReadFrequently: true });
          const rgba = color => { ctx.clearRect(0, 0, 1, 1); ctx.fillStyle = color; ctx.fillRect(0, 0, 1, 1); return [...ctx.getImageData(0, 0, 1, 1).data]; };
          const over = (f, b) => f.slice(0, 3).map((c, i) => c * f[3] / 255 + b[i] * (1 - f[3] / 255));
          const luminance = c => c.map(v => v / 255).map(v => v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4).reduce((a, v, i) => a + v * [.2126, .7152, .0722][i], 0);
          const chip = document.querySelector('.chip--success');
          const bg = over(rgba(style(chip).backgroundColor), rgba(style(document.body).backgroundColor));
          const fg = over(rgba(style(chip).color), bg);
          const a = luminance(fg), b = luminance(bg);
          return {
            pageWidth: document.documentElement.scrollWidth, viewport: innerWidth,
            tableCells: cells.map(e => ({ display: style(e).display, x: rect(e).x, y: rect(e).y })),
            buttonWeight: style(document.querySelector('.btn')).fontWeight,
            labelsCentered: [...document.querySelectorAll('.field__label, th')].every(e => style(e).textAlign === 'center'),
            textFits: [...document.querySelectorAll('.card h3,.card p,.modal h3,.modal p,.toast > span')].every(textFits),
            modalFits: rect(document.querySelector('.modal')).bottom <= rect(document.querySelector('.modal-frame')).bottom + 1,
            successContrast: (Math.max(a, b) + .05) / (Math.min(a, b) + .05),
          };
        });
        const cells = measurements.tableCells;
        const checks = {
          noPageOverflow: measurements.pageWidth <= width,
          tableGeometry: cells.every(c => c.display === 'table-cell' && Math.abs(c.y - cells[0].y) < 1) && cells[1].x > cells[0].x && cells[2].x > cells[1].x,
          buttonWeight: measurements.buttonWeight === '600',
          labelsCentered: measurements.labelsCentered,
          textFits: measurements.textFits && measurements.modalFits,
          successContrast: measurements.successContrast >= 4.5,
          noRuntimeErrors: errors.length === 0,
        };
        report.checks.push({ width, height, state, checks, measurements, errors: [...errors] });
        const capture = async (suffix, options) => {
          const name = `${width}-${state}-${suffix}.png`;
          await page.screenshot({ path: path.join(out, name), ...options });
          report.captures.push({ file: name, sha256: hash(fs.readFileSync(path.join(out, name))), viewport: [width, height], state, url: page.url(), sourceHashes, reviewed: false });
        };
        await page.evaluate(() => scrollTo(0, 0));
        await capture('full', { fullPage: true });
        if (width === 320 || width === 1280) {
          for (const index of [1, 5, 6, 8, 9, 10]) {
            const r = await page.locator('section').nth(index).boundingBox();
            const maxHeight = await page.evaluate(() => document.documentElement.scrollHeight);
            const y = Math.max(0, r.y + await page.evaluate(() => scrollY) - 16);
            await capture(`section-${index + 1}`, { fullPage: true, clip: { x: 0, y, width, height: Math.min(r.height + 32, maxHeight - y) } });
          }
        }
      }
      await context.close();
    }
  } finally { await browser.close(); }
  report.failures = report.checks.flatMap(r => Object.entries(r.checks).filter(([, ok]) => !ok).map(([check]) => `${r.width}/${r.state}/${check}`));
  fs.writeFileSync(path.join(out, 'report.json'), JSON.stringify(report, null, 2));
  console.log(JSON.stringify({ captures: report.captures.length, failures: report.failures, out }, null, 2));
  if (report.failures.length && !args.includes('--record-baseline')) process.exitCode = 1;
})().catch(error => { console.error(error); process.exitCode = 1; });
