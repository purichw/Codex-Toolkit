import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import { mkdtemp, mkdir, readFile, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { after, test } from 'node:test';

const script = fileURLToPath(new URL('./responsive-audit.mjs', import.meta.url));
const evidenceRoot = await mkdtemp(path.join(os.tmpdir(), 'responsive-design-tests-'));
const page = (body, css = '') => `<!doctype html><html lang="en"><head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>*{box-sizing:border-box}body{margin:0}main{padding:16px;min-width:0}
  button{min-height:44px;min-width:44px} ${css}</style></head><body>${body}</body></html>`;
const fixtures = new Map([
  ['/ok', page('<main><h1>Layout fixture</h1><p>Content wraps within its owner.</p><button>Continue</button></main>')],
  ['/overflow', page('<main><div style="width:800px">Wide content</div></main>')],
  ['/local', page('<main><div id="local" role="region" aria-label="Data" tabindex="0" style="overflow-x:auto"><table style="width:800px"><tr><th scope="col">Data</th></tr><tr><td>Value</td></tr></table></div></main>')],
  ['/clipped', page('<main><p id="clipped" style="width:80px;white-space:nowrap;overflow:hidden">Important content that is clipped</p></main>', 'body{overflow-x:hidden}')],
  ['/error', page('<script>throw new Error("fixture page error")</script><main>Error fixture</main>')],
  ['/image', page('<main><img src="/missing.png" alt="Missing fixture image"></main>')],
]);
const server = createServer((request, response) => {
  const body = fixtures.get(new URL(request.url, 'http://localhost').pathname);
  response.writeHead(body ? 200 : 404, { 'Content-Type': 'text/html; charset=utf-8' });
  response.end(body || page('<main>Not found</main>'));
});
await new Promise((resolve, reject) => {
  server.once('error', reject);
  server.listen(0, '127.0.0.1', resolve);
});
const origin = `http://127.0.0.1:${server.address().port}`;
after(async () => {
  await new Promise(resolve => server.close(resolve));
  console.log(`Fixture evidence retained: ${evidenceRoot}`);
});

function cli(args) {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, [script, ...args], {
      env: process.env, stdio: ['ignore', 'pipe', 'pipe'],
    });
    let output = '';
    child.stdout.on('data', data => { output += data; });
    child.stderr.on('data', data => { output += data; });
    const timer = setTimeout(() => {
      child.kill('SIGTERM');
      reject(new Error(`Collector exceeded fixture timeout: ${output}`));
    }, 60000);
    child.once('error', error => { clearTimeout(timer); reject(error); });
    child.once('close', code => { clearTimeout(timer); resolve({ code, output }); });
  });
}

async function audit(name, route, extra = [], expected = 0) {
  const out = path.join(evidenceRoot, name);
  const result = await cli(['--url', `${origin}${route}`, '--out', out,
    '--widths', '390', '--screenshots', 'none', ...extra]);
  assert.equal(result.code, expected, result.output);
  const report = JSON.parse(await readFile(path.join(out, 'report.json'), 'utf8'));
  assert.equal(report.url, `${origin}${route}`);
  assert.equal(report.environment.engine, 'chromium');
  assert.ok(report.environment.browserVersion);
  return { report, out };
}

test('help succeeds and malformed input fails without requiring a browser', async () => {
  assert.equal((await cli(['--help'])).code, 0);
  const base = ['--url', `${origin}/ok`, '--out', path.join(evidenceRoot, 'invalid')];
  for (const args of [[], [...base, '--widths', '0'], [...base, '--widths', '390,bad'],
    [...base, '--height', '100'], [...base, '--browser', 'unknown'],
    [...base, '--url', 'javascript:alert(1)'], [...base, '--unknown']]) {
    assert.equal((await cli(args)).code, 2, JSON.stringify(args));
  }
});

test('captures real viewport evidence including breakpoint neighbors', async () => {
  const { report, out } = await audit('boundaries', '/ok', ['--breakpoints', '640', '--screenshots', '390']);
  assert.deepEqual(report.runs.map(run => run.width), [390, 639, 640, 641]);
  assert.equal(report.summary.failed, 0);
  for (const run of report.runs) {
    assert.equal(run.metrics.viewport.width, run.width);
    assert.equal(run.metrics.viewport.dpr, 1);
    assert.equal(run.metrics.horizontalOverflow, false);
  }
  const capture = report.runs[0].screenshot;
  assert.ok(capture);
  const png = await readFile(path.join(out, capture));
  assert.deepEqual([...png.subarray(0, 8)], [137, 80, 78, 71, 13, 10, 26, 10]);
  assert.equal(png.readUInt32BE(16), 390);
  assert.ok(png.readUInt32BE(20) >= 900);
});

test('document overflow fails measured assertions', async () => {
  const { report } = await audit('overflow', '/overflow', [], 1);
  assert.equal(report.summary.failed, 1);
  assert.equal(report.runs[0].metrics.horizontalOverflow, true);
});

test('an intentional local table scroller is not document overflow', async () => {
  const { report } = await audit('local', '/local');
  const metrics = report.runs[0].metrics;
  assert.equal(metrics.horizontalOverflow, false);
  assert.ok(metrics.localScrollers.some(item => item.selector === '#local'));
});

test('clipping remains review evidence even when measured assertions pass', async () => {
  const { report } = await audit('clipped', '/clipped');
  const run = report.runs[0];
  assert.ok(run.metrics.globalClipping.includes('body'));
  assert.ok(run.metrics.clippedCandidates.some(item => item.selector === '#clipped'));
  assert.ok(run.warnings.length > 0);
});

test('uncaught page errors fail the measured run', async () => {
  const { report } = await audit('page-error', '/error', [], 1);
  assert.ok(report.runs[0].pageErrors.includes('fixture page error'));
});

test('main-document HTTP failures fail the measured run', async () => {
  const { report } = await audit('not-found', '/missing', [], 1);
  assert.ok(report.runs[0].httpErrors.some(item => item.status === 404));
  assert.equal(report.runs[0].status, 'FAIL');
});

test('broken images are reported for review, not silently certified', async () => {
  const { report } = await audit('image-warning', '/image');
  assert.equal(report.runs[0].metrics.brokenImages.length, 1);
  assert.ok(report.runs[0].warnings.length > 0);
});

test('root-font and reduced-motion probes retain their actual variant semantics', async () => {
  const { report } = await audit('stress', '/ok', ['--text-stress', '--reduced-motion']);
  assert.equal(report.runs.length, 8);
  const baseSize = parseFloat(report.runs[0].metrics.rootFontSize);
  const textRuns = report.runs.filter(run => run.variant === 'root-font-200');
  const motionRuns = report.runs.filter(run => run.variant === 'reduced-motion');
  assert.equal(textRuns.length, 4);
  assert.equal(motionRuns.length, 3);
  for (const run of textRuns) {
    assert.ok(parseFloat(run.metrics.rootFontSize) > baseSize);
    assert.ok(run.warnings.length > 0);
    assert.equal(run.screenshot, undefined);
  }
  for (const run of motionRuns) assert.equal(run.metrics.reducedMotion, true);
  assert.equal(report.runs[0].metrics.reducedMotion, false);
});

test('existing output is refused and earlier evidence remains unchanged', async () => {
  const out = path.join(evidenceRoot, 'existing');
  await mkdir(out);
  const previous = '{"preserve":"original evidence"}\n';
  await writeFile(path.join(out, 'report.json'), previous);
  const result = await cli(['--url', `${origin}/ok`, '--out', out,
    '--widths', '390', '--screenshots', 'none']);
  assert.equal(result.code, 2, result.output);
  assert.equal(await readFile(path.join(out, 'report.json'), 'utf8'), previous);
});
