#!/usr/bin/env node
'use strict';

const assert = require('node:assert/strict');
const path = require('node:path');
const { createRequire } = require('node:module');

if (process.argv.includes('--help')) {
  console.log('Usage: node verify-example.cjs /absolute/path/to/compiled-example');
  console.log('Compile the supplied example with strict TypeScript and CommonJS first.');
  console.log('React and react-dom must resolve from the compiled output directory.');
  process.exit(0);
}
if (process.argv.length !== 3) {
  console.error('Provide the compiled example directory; use --help for prerequisites.');
  process.exit(2);
}

const fromBuild = createRequire(path.resolve(process.argv[2], 'consumers.js'));
const { createElement: h, version } = fromBuild('react');
const { renderToStaticMarkup: render } = fromBuild('react-dom/server');
const { StatusBadge } = fromBuild('./shared/ui');
const { PageHeader } = fromBuild('./shared/layout');
const { BookingStatusBadge } = fromBuild('./features/bookings');
const { MembershipStatusBadge } = fromBuild('./features/membership');
const { BookingsExamplePage, MembershipExamplePage } = fromBuild('./consumers');
let passed = 0;

function check(name, run) {
  run();
  passed += 1;
  console.log(`PASS ${name}`);
}

// Labels and tones are the feature's public presentation mapping, not shared rules.
const mappings = [
  [BookingStatusBadge, 'confirmed', '\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e41\u0e25\u0e49\u0e27', 'positive'],
  [BookingStatusBadge, 'awaiting-confirmation', '\u0e23\u0e2d\u0e01\u0e32\u0e23\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19', 'caution'],
  [BookingStatusBadge, 'cancelled', '\u0e22\u0e01\u0e40\u0e25\u0e34\u0e01', 'neutral'],
  [MembershipStatusBadge, 'active', '\u0e2a\u0e21\u0e32\u0e0a\u0e34\u0e01\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19', 'positive'],
  [MembershipStatusBadge, 'under-review', '\u0e01\u0e33\u0e25\u0e31\u0e07\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e40\u0e2d\u0e01\u0e2a\u0e32\u0e23', 'caution'],
  [MembershipStatusBadge, 'expired', '\u0e2a\u0e21\u0e32\u0e0a\u0e34\u0e01\u0e2b\u0e21\u0e14\u0e2d\u0e32\u0e22\u0e38', 'negative'],
];
for (const [Component, status, label, tone] of mappings) {
  check(`${Component.name}: ${status}`, () => {
    const html = render(h(Component, { status }));
    assert.ok(html.includes(label));
    assert.ok(html.includes(`data-tone="${tone}"`));
    assert.ok(!html.includes('aria-live='));
  });
}

check('badge defaults and native attributes survive', () => {
  const html = render(h(StatusBadge, { lang: 'th', title: 'Status', 'data-record': 'fixture', className: 'consumer-slot' }, 'Ready'));
  for (const value of ['data-tone="neutral"', 'lang="th"', 'title="Status"',
    'data-record="fixture"', 'consumer-slot', '>Ready</span>']) assert.ok(html.includes(value));
});

check('visible text is escaped instead of interpreted as markup', () => {
  const html = render(h(StatusBadge, null, '<script>alert("x")</script> & ready'));
  assert.ok(!html.includes('<script>'));
  assert.ok(html.includes('&lt;script&gt;'));
  assert.ok(html.includes('&amp; ready'));
});

check('domain wrappers forward native attributes', () => {
  for (const Component of [BookingStatusBadge, MembershipStatusBadge]) {
    const status = Component === BookingStatusBadge ? 'confirmed' : 'active';
    const html = render(h(Component, { status, lang: 'th', title: 'Details' }));
    assert.ok(html.includes('lang="th"'));
    assert.ok(html.includes('title="Details"'));
  }
});

check('page heading and optional slots retain semantics', () => {
  const html = render(h(PageHeader, {
    title: 'Items <today>', headingId: 'items-title', description: 'Current items',
    'aria-labelledby': 'items-title',
    actions: h('a', { href: '#items' }, 'View items'),
  }));
  assert.ok(html.includes('<h1 id="items-title">Items &lt;today&gt;</h1>'));
  assert.ok(html.includes('aria-labelledby="items-title"'));
  assert.ok(html.includes('<p>Current items</p>'));
  assert.ok(html.includes('<a href="#items">View items</a>'));
  assert.ok(!html.includes('role="toolbar"'));
  const minimal = render(h(PageHeader, { title: 'Items', headingId: 'items-title' }));
  assert.ok(!minimal.includes('<p>'));
  assert.ok(!minimal.includes('<a '));
});

for (const [Page, heading, target] of [
  [BookingsExamplePage, 'bookings-title', 'bookings-list'],
  [MembershipExamplePage, 'membership-title', 'membership-details'],
]) {
  check(`${Page.name}: independent labelled page and action destination`, () => {
    const html = render(h(Page));
    assert.equal((html.match(/<h1(?:\s|>)/g) || []).length, 1);
    assert.ok(html.includes(`aria-labelledby="${heading}"`));
    assert.ok(html.includes(`<h1 id="${heading}">`));
    assert.ok(html.includes(`href="#${target}"`));
    assert.ok(html.includes(`id="${target}"`));
  });
}
console.log(`${passed} server-render checks passed with React ${version}.`);
console.log('This does not verify browser layout, focus, accessibility or backend behavior.');
