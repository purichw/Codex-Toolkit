#!/usr/bin/env python3
"""Extract a source-neutral HTML reference manifest (not an image analyzer).

The static path uses only Python's standard library. The optional rendered probe
uses Python Playwright when it is available in the active environment.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin


TEXT_TAGS = {"title", "button", "a", "label", "h1", "h2", "h3", "h4", "h5", "h6", "option"}
HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
CONTROL_TAGS = {"button", "a", "input", "select", "textarea", "summary", "label"}
STRUCTURE_TAGS = {
    "header",
    "nav",
    "main",
    "section",
    "article",
    "aside",
    "footer",
    "form",
    "dialog",
}
ASSET_ATTRS = {
    "src",
    "href",
    "poster",
    "srcset",
    "data-src",
    "data-bg",
    "data-background",
}
STATE_PATTERNS = {
    "screen/view/tab keys": r"\b(?:screen|view|tab|step|modal|dialog|route|page)\b",
    "state setters": r"\bset(?:Screen|View|Tab|Step|Modal|Dialog|Route|Page)\b",
    "click handlers": r"\b(?:onClick|onclick|addEventListener\(['\"]click|@click)\b",
    "forms": r"\b(?:onSubmit|onsubmit|addEventListener\(['\"]submit)\b",
    "storage/history": r"\b(?:localStorage|sessionStorage|history\.pushState|location\.hash)\b",
    "conditional render": r"\b(?:active|selected|current|open|expanded|hidden|disabled|locked|complete|completed)\b",
}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def short_text(value: str, limit: int = 110) -> str:
    cleaned = re.sub(r"\s+", " ", value or "").strip()
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 1].rstrip() + "..."


def attr_dict(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
    return {name.lower(): value or "" for name, value in attrs}


def compact_attrs(attrs: dict[str, str], keep_data: bool = True) -> dict[str, str]:
    keys = [
        "id",
        "class",
        "role",
        "type",
        "name",
        "href",
        "aria-label",
        "aria-controls",
        "aria-expanded",
        "data-screen",
        "data-view",
        "data-tab",
        "data-route",
        "data-state",
    ]
    out: dict[str, str] = {}
    for key in keys:
        if key in attrs and attrs[key] != "":
            out[key] = short_text(attrs[key], 140)
    if keep_data:
        for key, value in attrs.items():
            if key.startswith("data-") and key not in out and value != "":
                out[key] = short_text(value, 90)
    return out


def parse_srcset(value: str) -> list[str]:
    urls: list[str] = []
    for part in value.split(","):
        url = part.strip().split(" ")[0]
        if url:
            urls.append(url)
    return urls


def css_urls(css: str) -> list[str]:
    urls = []
    for match in re.finditer(r"url\(([^)]+)\)", css, flags=re.IGNORECASE):
        raw = match.group(1).strip().strip("\"'")
        if raw and not raw.startswith("data:"):
            urls.append(raw)
    return urls


def media_queries(css: str) -> list[str]:
    queries = []
    for match in re.finditer(r"@media\s*([^{]+){", css, flags=re.IGNORECASE):
        queries.append(short_text(match.group(1), 180))
    return queries


def breakpoint_tokens(css: str) -> list[str]:
    tokens = set()
    for match in re.finditer(r"\b(?:min|max)-width\s*:\s*([0-9.]+(?:px|rem|em))", css, flags=re.IGNORECASE):
        tokens.add(match.group(0).replace(" ", ""))
    return sorted(tokens)


def color_tokens(css: str, limit: int = 60) -> list[str]:
    tokens = Counter()
    patterns = [
        r"#[0-9a-fA-F]{3,8}\b",
        r"\brgba?\([^)]{1,80}\)",
        r"\bhsla?\([^)]{1,80}\)",
    ]
    for pattern in patterns:
        tokens.update(match.group(0) for match in re.finditer(pattern, css))
    return [token for token, _ in tokens.most_common(limit)]


def font_tokens(css: str, limit: int = 30) -> list[str]:
    tokens = Counter()
    for match in re.finditer(r"font-family\s*:\s*([^;}{]+)", css, flags=re.IGNORECASE):
        tokens[short_text(match.group(1), 120)] += 1
    return [token for token, _ in tokens.most_common(limit)]


@dataclass
class ElementRecord:
    tag: str
    attrs: dict[str, str]
    line: int
    text: str = ""


@dataclass
class ParsedHtml:
    title: str = ""
    tag_counts: Counter[str] = field(default_factory=Counter)
    text_by_tag: dict[int, list[str]] = field(default_factory=lambda: defaultdict(list))
    elements: list[ElementRecord] = field(default_factory=list)
    controls: list[ElementRecord] = field(default_factory=list)
    assets: list[dict[str, str]] = field(default_factory=list)
    styles: list[str] = field(default_factory=list)
    scripts: list[dict[str, str]] = field(default_factory=list)
    links: list[dict[str, str]] = field(default_factory=list)
    headings: list[ElementRecord] = field(default_factory=list)


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parsed = ParsedHtml()
        self.stack: list[tuple[int, str]] = []
        self.records: dict[int, ElementRecord] = {}
        self.current_style: list[str] | None = None
        self.current_script: dict[str, str] | None = None
        self.record_index = 0

    def handle_starttag(self, tag: str, attrs_raw: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attrs = attr_dict(attrs_raw)
        self.parsed.tag_counts[tag] += 1
        self.record_index += 1
        record_id = self.record_index
        record = ElementRecord(tag=tag, attrs=attrs, line=self.getpos()[0])
        self.records[record_id] = record
        self.stack.append((record_id, tag))

        if self.should_record_element(tag, attrs):
            self.parsed.elements.append(record)
        if self.is_control(tag, attrs):
            self.parsed.controls.append(record)
        if tag in HEADING_TAGS:
            self.parsed.headings.append(record)
        if tag == "style":
            self.current_style = []
        if tag == "script":
            script_record = {"line": str(self.getpos()[0])}
            if "src" in attrs:
                script_record["src"] = attrs["src"]
                self.add_asset(tag, "src", attrs["src"], attrs)
            self.parsed.scripts.append(script_record)
            self.current_script = script_record if "src" not in attrs else None
        if tag == "link":
            self.parsed.links.append({"line": str(self.getpos()[0]), **compact_attrs(attrs, keep_data=False)})

        for attr, value in attrs.items():
            if attr in ASSET_ATTRS and value:
                if attr == "srcset":
                    for url in parse_srcset(value):
                        self.add_asset(tag, attr, url, attrs)
                else:
                    self.add_asset(tag, attr, value, attrs)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "style" and self.current_style is not None:
            self.parsed.styles.append("".join(self.current_style))
            self.current_style = None
        if tag == "script" and self.current_script is not None:
            self.current_script["inline_sha256"] = sha256_text(self.current_script.get("inline", ""))
            self.current_script["inline_chars"] = str(len(self.current_script.get("inline", "")))
            self.current_script = None
        while self.stack:
            _, open_tag = self.stack.pop()
            if open_tag == tag:
                break

    def handle_data(self, data: str) -> None:
        if self.current_style is not None:
            self.current_style.append(data)
        if self.current_script is not None:
            self.current_script["inline"] = self.current_script.get("inline", "") + data
        text = short_text(data, 500)
        if not text:
            return
        if self.stack:
            record_id, tag = self.stack[-1]
            if tag in TEXT_TAGS:
                self.text_by_record(record_id).append(text)

    def close(self) -> None:
        super().close()
        for record_id, text_parts in self.parsed.text_by_tag.items():
            record = self.records.get(record_id)
            if not record:
                continue
            record.text = short_text(" ".join(text_parts), 180)
            if record.tag == "title":
                self.parsed.title = record.text

    def text_by_record(self, record_id: int) -> list[str]:
        return self.parsed.text_by_tag[record_id]

    @staticmethod
    def should_record_element(tag: str, attrs: dict[str, str]) -> bool:
        return (
            tag in STRUCTURE_TAGS
            or tag in CONTROL_TAGS
            or tag in HEADING_TAGS
            or "role" in attrs
            or "id" in attrs
            or "class" in attrs
            or any(key.startswith("data-") for key in attrs)
        )

    @staticmethod
    def is_control(tag: str, attrs: dict[str, str]) -> bool:
        if tag in CONTROL_TAGS:
            return True
        role = attrs.get("role", "")
        if role in {"button", "tab", "link", "menuitem", "checkbox", "radio", "switch", "option"}:
            return True
        return any(name.startswith("on") for name in attrs)

    def add_asset(self, tag: str, attr: str, value: str, attrs: dict[str, str]) -> None:
        if value.startswith(("data:", "javascript:", "#")):
            return
        self.parsed.assets.append(
            {
                "tag": tag,
                "attr": attr,
                "value": value,
                "alt": attrs.get("alt", ""),
                "rel": attrs.get("rel", ""),
                "line": str(self.getpos()[0]),
            }
        )


def extract_static(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="replace")
    parser = ReferenceParser()
    parser.feed(text)
    parser.close()
    parsed = parser.parsed
    css = "\n".join(parsed.styles)
    state_source = text

    for url in css_urls(css):
        parsed.assets.append({"tag": "css", "attr": "url", "value": url, "alt": "", "rel": "", "line": ""})

    state_signals = []
    for label, pattern in STATE_PATTERNS.items():
        matches = list(re.finditer(pattern, state_source, flags=re.IGNORECASE))
        if matches:
            state_signals.append(
                {
                    "kind": label,
                    "count": len(matches),
                    "examples": [short_text(state_source[max(0, m.start() - 60) : m.end() + 80], 180) for m in matches[:8]],
                }
            )

    route_candidates = sorted(
        {
            item
            for item in re.findall(r"(?:href|to|path|route)\s*[:=]\s*['\"]([^'\"]{1,120})['\"]", text)
            if item and not item.startswith(("http", "mailto:", "tel:", "javascript:"))
        }
    )
    state_values = sorted(
        {
            item
            for item in re.findall(
                r"(?:set(?:Screen|View|Tab|Step|Modal|Dialog|Route|Page)\(|(?:screen|view|tab|step|modal|route)\s*[:=])\s*['\"]([^'\"]{1,80})['\"]",
                text,
                flags=re.IGNORECASE,
            )
        }
    )

    return {
        "path": str(path),
        "file": path.name,
        "sha256": sha256_text(text),
        "size_bytes": len(text.encode("utf-8", errors="replace")),
        "modified_utc": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
        "title": parsed.title,
        "tag_counts": dict(parsed.tag_counts.most_common()),
        "headings": [record_to_dict(record) for record in parsed.headings[:80]],
        "controls": [record_to_dict(record) for record in parsed.controls[:250]],
        "component_candidates": [record_to_dict(record) for record in parsed.elements[:300]],
        "assets": normalize_assets(path, parsed.assets),
        "links": parsed.links[:120],
        "scripts": [{k: v for k, v in script.items() if k != "inline"} for script in parsed.scripts[:80]],
        "media_queries": media_queries(css)[:80],
        "breakpoints": breakpoint_tokens(css),
        "colors": color_tokens(css),
        "fonts": font_tokens(css),
        "state_signals": state_signals,
        "route_candidates": route_candidates[:120],
        "state_value_candidates": state_values[:120],
    }


def record_to_dict(record: ElementRecord) -> dict[str, Any]:
    return {
        "tag": record.tag,
        "line": record.line,
        "text": record.text,
        "attrs": compact_attrs(record.attrs),
    }


def normalize_assets(base_path: Path, assets: list[dict[str, str]]) -> list[dict[str, str]]:
    seen = set()
    normalized = []
    base = base_path.resolve().parent.as_uri() + "/"
    for asset in assets:
        value = asset["value"]
        absolute = urljoin(base, value)
        key = (asset["tag"], asset["attr"], value)
        if key in seen:
            continue
        seen.add(key)
        normalized.append({**asset, "absolute": absolute})
    return normalized[:300]


def parse_viewport(value: str) -> tuple[int, int]:
    match = re.match(r"^(\d+)x(\d+)$", value.lower().strip())
    if not match:
        raise argparse.ArgumentTypeError(f"Invalid viewport '{value}', expected WIDTHxHEIGHT")
    return int(match.group(1)), int(match.group(2))


def rendered_probe(paths: list[Path], viewports: list[tuple[int, int]], out_dir: Path, screenshots: bool) -> dict[str, Any]:
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:  # pragma: no cover - depends on local environment
        return {
            "available": False,
            "error": f"Python Playwright unavailable: {type(exc).__name__}: {exc}",
        }

    results: dict[str, Any] = {"available": True, "captures": []}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        try:
            for path in paths:
                for width, height in viewports:
                    page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
                    page.goto(path.resolve().as_uri(), wait_until="networkidle")
                    page.wait_for_timeout(250)
                    capture = page.evaluate(
                        """
                        () => {
                          const selectorFor = (el) => {
                            if (el.id) return `#${CSS.escape(el.id)}`;
                            const cls = Array.from(el.classList || []).slice(0, 3).map(c => `.${CSS.escape(c)}`).join('');
                            return `${el.tagName.toLowerCase()}${cls}`;
                          };
                          const interesting = Array.from(document.querySelectorAll(
                            'header,nav,main,section,article,aside,footer,form,dialog,h1,h2,h3,h4,button,a,input,select,textarea,[role]'
                          ));
                          const components = interesting.map((el) => {
                            const r = el.getBoundingClientRect();
                            const s = getComputedStyle(el);
                            return {
                              selector: selectorFor(el),
                              tag: el.tagName.toLowerCase(),
                              text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\\s+/g, ' ').trim().slice(0, 140),
                              role: el.getAttribute('role') || '',
                              rect: { x: Math.round(r.x), y: Math.round(r.y), width: Math.round(r.width), height: Math.round(r.height) },
                              style: {
                                display: s.display,
                                position: s.position,
                                fontSize: s.fontSize,
                                fontWeight: s.fontWeight,
                                lineHeight: s.lineHeight,
                                color: s.color,
                                backgroundColor: s.backgroundColor,
                                borderRadius: s.borderRadius,
                                padding: s.padding,
                                margin: s.margin,
                                gap: s.gap,
                              }
                            };
                          }).filter(item => item.rect.width > 0 && item.rect.height > 0).slice(0, 260);
                          return {
                            title: document.title,
                            url: location.href,
                            document: {
                              width: document.documentElement.scrollWidth,
                              height: document.documentElement.scrollHeight,
                              bodyTextChars: document.body ? document.body.innerText.length : 0
                            },
                            components
                          };
                        }
                        """
                    )
                    shot_path = ""
                    if screenshots:
                        shot_name = f"{path.stem}-{width}x{height}.png"
                        shot_path = str(out_dir / shot_name)
                        page.screenshot(path=shot_path, full_page=True)
                    results["captures"].append(
                        {
                            "file": str(path),
                            "viewport": f"{width}x{height}",
                            "screenshot": shot_path,
                            **capture,
                        }
                    )
                    page.close()
        finally:
            browser.close()
    return results


def markdown_table(rows: list[list[str]], headers: list[str]) -> str:
    table = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        table.append("| " + " | ".join(cell.replace("|", "\\|") for cell in row) + " |")
    return "\n".join(table)


def render_markdown(manifest: dict[str, Any]) -> str:
    lines = [
        "# Design Reference Manifest",
        "",
        f"Generated: `{manifest['generated_utc']}`",
        "",
        "Use this as an HTML-mode seed for the Reference-to-a-tee coverage ledger. It is not a replacement for rendered inspection, product mapping, or release-gate verification.",
        "",
        "## Files",
        "",
    ]
    file_rows = []
    for item in manifest["files"]:
        file_rows.append([item["file"], item["sha256"][:12], str(item["size_bytes"]), item.get("title", "")])
    lines.append(markdown_table(file_rows, ["file", "sha256", "bytes", "title"]))
    lines.extend(["", "## Fast Implementation Seeds", ""])
    lines.append("- Reuse unchanged manifests only when the source hash still matches.")
    lines.append("- Start mapping from headings, component candidates, controls, assets, breakpoints, and state signals below.")
    lines.append("- Treat every generated row as `not done` until rendered, mapped to target product code, and verified.")
    lines.extend(["", "## Headings", ""])
    heading_rows = []
    for item in manifest["files"]:
        for heading in item["headings"][:40]:
            heading_rows.append([item["file"], heading["tag"], str(heading["line"]), heading["text"]])
    lines.append(markdown_table(heading_rows or [["", "", "", ""]], ["file", "tag", "line", "text"]))

    lines.extend(["", "## Controls Ledger Seed", ""])
    control_rows = []
    for item in manifest["files"]:
        for control in item["controls"][:120]:
            attrs = " ".join(f"{k}={v!r}" for k, v in control["attrs"].items())
            control_rows.append([item["file"], control["tag"], str(control["line"]), control["text"], short_text(attrs, 180), "not done"])
    lines.append(markdown_table(control_rows or [["", "", "", "", "", ""]], ["file", "tag", "line", "text", "attrs", "status"]))

    lines.extend(["", "## Route And State Signals", ""])
    for item in manifest["files"]:
        lines.append(f"### {item['file']}")
        routes = ", ".join(f"`{route}`" for route in item["route_candidates"][:40]) or "none detected"
        states = ", ".join(f"`{state}`" for state in item["state_value_candidates"][:40]) or "none detected"
        lines.append(f"- routes/hrefs: {routes}")
        lines.append(f"- state values: {states}")
        for signal in item["state_signals"]:
            lines.append(f"- {signal['kind']}: {signal['count']} hit(s)")
            for example in signal["examples"][:3]:
                lines.append(f"  - `{example}`")
        lines.append("")

    lines.extend(["## Component Candidates", ""])
    component_rows = []
    for item in manifest["files"]:
        for component in item["component_candidates"][:160]:
            attrs = " ".join(f"{k}={v!r}" for k, v in component["attrs"].items())
            label = component["text"] or short_text(attrs, 100)
            component_rows.append([item["file"], component["tag"], str(component["line"]), label, "not done"])
    lines.append(markdown_table(component_rows or [["", "", "", "", ""]], ["file", "tag", "line", "label", "status"]))

    lines.extend(["", "## Assets", ""])
    asset_rows = []
    for item in manifest["files"]:
        for asset in item["assets"][:140]:
            asset_rows.append([item["file"], asset["tag"], asset["attr"], short_text(asset["value"], 140), asset.get("alt", "")])
    lines.append(markdown_table(asset_rows or [["", "", "", "", ""]], ["file", "tag", "attr", "value", "alt"]))

    lines.extend(["", "## CSS Tokens", ""])
    for item in manifest["files"]:
        lines.append(f"### {item['file']}")
        lines.append(f"- breakpoints: {', '.join(f'`{b}`' for b in item['breakpoints']) or 'none detected'}")
        lines.append(f"- fonts: {', '.join(f'`{f}`' for f in item['fonts'][:12]) or 'none detected'}")
        lines.append(f"- colors: {', '.join(f'`{c}`' for c in item['colors'][:24]) or 'none detected'}")
        if item["media_queries"]:
            lines.append("- media queries:")
            for query in item["media_queries"][:20]:
                lines.append(f"  - `{query}`")
        lines.append("")

    rendered = manifest.get("rendered")
    lines.extend(["## Rendered Probe", ""])
    if not rendered:
        lines.append("Not requested. Run with `--render` when Python Playwright is available.")
    elif not rendered.get("available"):
        lines.append(f"Unavailable: `{rendered.get('error', 'unknown error')}`")
    else:
        render_rows = []
        for capture in rendered.get("captures", []):
            doc = capture.get("document", {})
            render_rows.append(
                [
                    Path(capture["file"]).name,
                    capture["viewport"],
                    str(doc.get("width", "")),
                    str(doc.get("height", "")),
                    str(len(capture.get("components", []))),
                    capture.get("screenshot", ""),
                ]
            )
        lines.append(markdown_table(render_rows, ["file", "viewport", "doc width", "doc height", "components", "screenshot"]))

    lines.extend(["", "## Measured Parity Table Seed", ""])
    parity_rows = []
    for item in manifest["files"]:
        for component in item["component_candidates"][:40]:
            label = component["text"] or component["tag"]
            parity_rows.append([short_text(label, 80), "desktop/mobile", "see manifest/probe", "", "not done"])
    lines.append(markdown_table(parity_rows or [["", "", "", "", ""]], ["component", "viewport", "reference", "target mapping", "status"]))
    lines.append("")
    return "\n".join(lines)


def render_worklog(manifest: dict[str, Any]) -> str:
    file_rows = []
    for item in manifest["files"]:
        file_rows.append(f"- `{item['file']}` sha256 `{item['sha256']}` title `{item.get('title', '')}`")

    control_rows = []
    for item in manifest["files"]:
        for control in item["controls"][:80]:
            label = control["text"] or " ".join(f"{k}={v!r}" for k, v in control["attrs"].items())
            control_rows.append(f"- [ ] `{item['file']}:{control['line']}` {control['tag']} {short_text(label, 120)} -> not done")

    route_rows = []
    for item in manifest["files"]:
        for route in item["route_candidates"][:60]:
            route_rows.append(f"- [ ] `{route}` -> not done")
        for state in item["state_value_candidates"][:60]:
            route_rows.append(f"- [ ] state `{state}` -> not done")

    asset_rows = []
    for item in manifest["files"]:
        for asset in item["assets"][:80]:
            asset_rows.append(f"- [ ] `{item['file']}` {asset['tag']} {asset['attr']} `{short_text(asset['value'], 140)}`")

    lines = [
        "# Reference To A Tee Worklog",
        "",
        "Generated from the reference manifest. Every generated row starts as not done.",
        "",
        "## Reference Files",
        "",
        *(file_rows or ["- not done"]),
        "",
        "## Source Of Truth Order",
        "",
        "1. Newest user requirement",
        "2. Selected reference per surface/state/version; use authoritative HTML values and resolve any image conflicts explicitly",
        "3. Existing product behavior, data contracts, tests, accessibility, i18n, security, performance, and operations",
        "4. Older handoff notes and screenshots",
        "",
        "## Coverage Ledger",
        "",
        *(route_rows or ["- [ ] default rendered state -> not done"]),
        "",
        "## Controls Ledger",
        "",
        *(control_rows or ["- [ ] no controls detected -> verify manually"]),
        "",
        "## Asset Inventory",
        "",
        *(asset_rows or ["- [ ] no assets detected -> verify manually"]),
        "",
        "## Component Contracts",
        "",
        "- [ ] global shell",
        "- [ ] header/topbar/nav",
        "- [ ] first viewport primary components",
        "- [ ] repeated cards/lists/tables",
        "- [ ] dialogs/drawers/modals",
        "- [ ] footer/history/end state",
        "",
        "## Product Mapping",
        "",
        "- [ ] files/components/selectors:",
        "- [ ] data/read paths:",
        "- [ ] write/action paths:",
        "- [ ] permissions/security:",
        "- [ ] tests/selectors:",
        "",
        "## Exceptions",
        "",
        "Behavior exceptions:",
        "- none recorded",
        "",
        "Visual exceptions:",
        "- none recorded",
        "",
        "Observed static/no-op reference behavior:",
        "- none recorded",
        "",
        "## Measured Parity Table",
        "",
        "| component | viewport | reference | implementation | delta | status |",
        "| --- | --- | --- | --- | --- | --- |",
        "| global shell | desktop/mobile | not done | not done | not done | not done |",
        "",
        "## Verification",
        "",
        "- [ ] reference rendered",
        "- [ ] target app rendered",
        "- [ ] every page/screen/route visited",
        "- [ ] every visible control clicked or operated",
        "- [ ] required responsive viewports checked",
        "- [ ] browser console/page/network errors checked",
        "- [ ] product behavior verified",
        "- [ ] release gate passed",
        "",
        "## Blockers Before Release",
        "",
        "- none recorded",
        "",
    ]
    return "\n".join(lines)


def write_outputs(manifest: dict[str, Any], out_dir: Path, *, legacy: bool = False) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "reference-manifest.json"
    md_path = out_dir / "reference-manifest.md"
    worklog_path = out_dir / "REFERENCE_TO_A_TEE_WORKLOG.md"
    json_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    md_path.write_text(render_markdown(manifest), encoding="utf-8")
    worklog_path.write_text(render_worklog(manifest), encoding="utf-8")
    print(f"Wrote {md_path}")
    print(f"Wrote {json_path}")
    print(f"Wrote {worklog_path}")
    if legacy:
        legacy_path = out_dir / "CLAUDE_TO_A_TEE_WORKLOG.md"
        legacy_path.write_text(render_worklog(manifest), encoding="utf-8")
        print(f"Wrote {legacy_path} (compatibility copy)")


def main(argv: list[str] | None = None, *, legacy: bool = False) -> int:
    parser = argparse.ArgumentParser(description="Create an HTML reference manifest. For images, use the reference-to-a-tee image workflow.")
    parser.add_argument("html", nargs="+", type=Path, help="Offline HTML file(s), from any source")
    parser.add_argument("--out", type=Path, default=Path(".claude-reference" if legacy else ".design-reference"), help="Output directory")
    parser.add_argument("--viewport", action="append", type=parse_viewport, help="Rendered viewport WIDTHxHEIGHT")
    parser.add_argument("--render", action="store_true", help="Run optional Playwright rendered probe")
    parser.add_argument("--screenshots", action="store_true", help="Capture full-page screenshots during rendered probe")
    args = parser.parse_args(argv)
    if args.screenshots and not args.render:
        parser.error("--screenshots requires --render")

    paths = [path.expanduser().resolve() for path in args.html]
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        print("Missing HTML file(s): " + ", ".join(missing), file=sys.stderr)
        return 2
    unsupported = [str(path) for path in paths if path.suffix.lower() not in {".html", ".htm"}]
    if unsupported:
        print("HTML extractor accepts .html/.htm only; inspect image references with the image workflow: " + ", ".join(unsupported), file=sys.stderr)
        return 2

    manifest: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "cwd": os.getcwd(),
        "mode": "html",
        "files": [extract_static(path) for path in paths],
    }
    out_dir = args.out.expanduser().resolve()
    if args.render:
        viewports = args.viewport or [(1440, 900), (820, 1180), (390, 844)]
        out_dir.mkdir(parents=True, exist_ok=True)
        try:
            manifest["rendered"] = rendered_probe(paths, viewports, out_dir, args.screenshots)
        except Exception as exc:
            manifest["rendered"] = {"available": False, "error": f"{type(exc).__name__}: {exc}"}
    write_outputs(manifest, out_dir, legacy=legacy)
    if args.render and not manifest["rendered"].get("available"):
        print("Rendered probe failed; static inventory only. " + manifest["rendered"].get("error", ""), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
