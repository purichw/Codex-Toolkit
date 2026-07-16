#!/usr/bin/env node
/* Generic production media smoke for browser-rendered websites. */
const fs = require('fs');
const path = require('path');
const { createRequire } = require('module');

function parseArgs(argv) {
  const opts = {
    routes: [],
    staleDomains: [],
    viewport: { width: 1440, height: 1600 },
    wait: 1000,
    scrollStep: 900,
    screenshots: true,
    allowConsoleErrors: false
  };
  for (let i = 2; i < argv.length; i += 1) {
    const arg = argv[i];
    const next = argv[i + 1];
    if (arg === '--url') { opts.url = next; i += 1; }
    else if (arg === '--route') { opts.routes.push(next); i += 1; }
    else if (arg === '--stale-domain') { opts.staleDomains.push(next); i += 1; }
    else if (arg === '--screenshot-dir') { opts.screenshotDir = next; i += 1; }
    else if (arg === '--viewport') {
      const parts = String(next || '').split('x').map(Number);
      if (parts.length === 2 && parts[0] > 0 && parts[1] > 0) opts.viewport = { width: parts[0], height: parts[1] };
      i += 1;
    } else if (arg === '--wait') { opts.wait = Number(next || opts.wait); i += 1; }
    else if (arg === '--scroll-step') { opts.scrollStep = Number(next || opts.scrollStep); i += 1; }
    else if (arg === '--no-screenshots') opts.screenshots = false;
    else if (arg === '--allow-console-errors') opts.allowConsoleErrors = true;
    else if (arg === '--help' || arg === '-h') opts.help = true;
    else throw new Error(`Unknown argument: ${arg}`);
  }
  if (!opts.routes.length) opts.routes.push('');
  if (!opts.screenshotDir) opts.screenshotDir = path.join('/tmp', `asset-smoke-${Date.now()}`);
  return opts;
}

function usage() {
  return `Usage: node asset_smoke.js --url https://example.com [--route /] [--route '#/page'] [--stale-domain cdn.example.com/old] [--screenshot-dir /tmp/smoke]`;
}

function resolveRoute(base, route) {
  if (/^https?:\/\//i.test(route)) return route;
  const cleanBase = String(base || '').replace(/#.*$/, '');
  if (!route) return cleanBase;
  if (route.startsWith('#')) return cleanBase + route;
  return new URL(route, cleanBase).toString();
}

function safeName(value) {
  return String(value || 'root').replace(/^https?:\/\//, '').replace(/[^a-z0-9]+/gi, '-').replace(/^-|-$/g, '').slice(0, 90) || 'root';
}

function isAssetRequest(url) {
  return /\.(avif|gif|jpe?g|png|svg|webp|mp4|webm|mov|m4v|woff2?|ttf|otf|css|js)(\?|#|$)/i.test(url);
}

function loadPlaywright() {
  try {
    return require('playwright');
  } catch (firstErr) {
    try {
      const projectRequire = createRequire(path.join(process.cwd(), 'package.json'));
      return projectRequire('playwright');
    } catch (secondErr) {
      const err = new Error('Cannot find Playwright. Run this script from a project with playwright installed, or install playwright where the script can resolve it.');
      err.cause = secondErr || firstErr;
      throw err;
    }
  }
}

async function main() {
  let opts;
  try { opts = parseArgs(process.argv); } catch (err) {
    console.error(err.message);
    console.error(usage());
    process.exit(2);
  }
  if (opts.help) {
    console.log(usage());
    process.exit(0);
  }
  if (!opts.url) {
    console.log(usage());
    process.exit(2);
  }

  const { chromium } = loadPlaywright();
  fs.mkdirSync(opts.screenshotDir, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: opts.viewport, deviceScaleFactor: 1 });
  const results = [];

  for (const route of opts.routes) {
    const url = resolveRoute(opts.url, route);
    const page = await context.newPage();
    const consoleErrors = [];
    const pageErrors = [];
    const failedRequests = [];
    page.on('console', msg => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });
    page.on('pageerror', err => pageErrors.push(err.message));
    page.on('requestfailed', req => {
      const requestUrl = req.url();
      if (isAssetRequest(requestUrl) || opts.staleDomains.some(domain => requestUrl.includes(domain))) {
        failedRequests.push({ url: requestUrl, failure: req.failure() && req.failure().errorText });
      }
    });

    const response = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(opts.wait);
    const height = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    for (let y = 0; y <= height; y += opts.scrollStep) {
      await page.evaluate(scrollY => window.scrollTo(0, scrollY), y);
      await page.waitForTimeout(120);
    }
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(400);

    const media = await page.evaluate(staleDomains => {
      function bgUrls(value) {
        const urls = [];
        const re = /url\((['"]?)(.*?)\1\)/g;
        let match;
        while ((match = re.exec(value || ''))) urls.push(new URL(match[2], location.href).href);
        return urls;
      }
      const images = [...document.images].map(img => ({
        tag: 'img',
        src: img.currentSrc || img.src,
        complete: img.complete,
        naturalWidth: img.naturalWidth,
        naturalHeight: img.naturalHeight,
        loading: img.loading || '',
        alt: img.alt || ''
      }));
      const backgrounds = [...document.querySelectorAll('*')].flatMap(el => {
        return bgUrls(getComputedStyle(el).backgroundImage).map(src => ({ tag: 'background', src }));
      });
      const videos = [...document.querySelectorAll('video, video source')].map(el => ({
        tag: el.tagName.toLowerCase(),
        src: el.currentSrc || el.src || el.getAttribute('src') || '',
        poster: el.poster || ''
      })).flatMap(item => {
        const rows = [];
        if (item.src) rows.push({ tag: item.tag, src: item.src });
        if (item.poster) rows.push({ tag: 'poster', src: item.poster });
        return rows;
      });
      const allUrls = images.map(item => item.src).concat(backgrounds.map(item => item.src), videos.map(item => item.src)).filter(Boolean);
      return {
        title: document.title,
        h1: document.querySelector('h1') ? document.querySelector('h1').innerText : '',
        imageCount: images.length,
        backgroundCount: backgrounds.length,
        videoAssetCount: videos.length,
        brokenImages: images.filter(img => img.complete && img.naturalWidth === 0).map(img => img.src),
        incompleteImages: images.filter(img => !img.complete).map(img => img.src),
        staleMedia: allUrls.filter(src => staleDomains.some(domain => src.includes(domain))),
        mediaUrls: allUrls
      };
    }, opts.staleDomains);

    let screenshot = '';
    if (opts.screenshots) {
      screenshot = path.join(opts.screenshotDir, `${safeName(route || url)}.png`);
      await page.screenshot({ path: screenshot, fullPage: false });
    }

    const status = response ? response.status() : 0;
    const routeResult = {
      route,
      url,
      status,
      screenshot,
      ...media,
      consoleErrors,
      pageErrors,
      failedRequests
    };
    routeResult.failed =
      status < 200 || status >= 400 ||
      routeResult.brokenImages.length > 0 ||
      routeResult.incompleteImages.length > 0 ||
      routeResult.staleMedia.length > 0 ||
      routeResult.failedRequests.length > 0 ||
      routeResult.pageErrors.length > 0 ||
      (!opts.allowConsoleErrors && routeResult.consoleErrors.length > 0);
    results.push(routeResult);
    await page.close();
  }

  await browser.close();
  const report = {
    target: opts.url,
    viewport: opts.viewport,
    staleDomains: opts.staleDomains,
    screenshotDir: opts.screenshotDir,
    failedCount: results.filter(row => row.failed).length,
    results
  };
  const reportPath = path.join(opts.screenshotDir, 'asset-smoke-results.json');
  fs.writeFileSync(reportPath, JSON.stringify(report, null, 2));
  console.log(JSON.stringify({ reportPath, failedCount: report.failedCount, results }, null, 2));
  process.exit(report.failedCount ? 1 : 0);
}

main().catch(err => {
  console.error(err && err.stack ? err.stack : String(err));
  process.exit(1);
});
