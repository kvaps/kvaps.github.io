#!/usr/bin/env python3
"""
RSS aggregator for kvaps.github.io.

Pulls posts from Habr, Medium, Dev.to and YouTube playlists, then writes
them as Hugo .md files under content/{en,ru}/post/.

Additive only: never deletes files. Medium returns only 10 latest items,
so a sync strategy would silently drop older posts.

Usage:
    python3 scripts/aggregate.py
"""
from __future__ import annotations

import email.utils
import html
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "kvaps-rss-aggregator/1.0 (+https://kvaps.github.io/)"
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "media": "http://search.yahoo.com/mrss/",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
}


@dataclass
class Source:
    name: str
    url: str
    kind: str
    lang: str


SOURCES = [
    Source("habr",       "https://habr.com/ru/rss/users/kvaps/articles/", "rss",  "ru"),
    Source("medium",     "https://medium.com/feed/@kvaps",                 "rss",  "en"),
    Source("dev.to",     "https://dev.to/feed/kvaps",                      "rss",  "en"),
    Source("youtube-ru", "https://www.youtube.com/feeds/videos.xml?playlist_id=PLigW96d6EqkhiQ8a8R0q29NoPfn3jSw__", "atom", "ru"),
    Source("youtube-en", "https://www.youtube.com/feeds/videos.xml?playlist_id=PLigW96d6EqkgsShnwdb0NHTLH1sAht34h", "atom", "en"),
]


@dataclass
class Entry:
    title: str
    link: str
    date: datetime
    body: str
    video_id: str | None = None


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def slugify(title: str) -> str:
    s = title.strip()
    s = re.sub(r"[^\w\s\-]+", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def parse_rss_date(s: str) -> datetime:
    dt = email.utils.parsedate_to_datetime(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def parse_atom_date(s: str) -> datetime:
    s = s.replace("Z", "+00:00")
    return datetime.fromisoformat(s)


def extract_cover(html_body: str) -> tuple[str | None, str]:
    m = re.search(r'<img[^>]+src="([^"]+)"[^>]*>', html_body)
    if not m:
        return None, html_body
    return m.group(1), html_body[:m.start()] + html_body[m.end():]


def html_to_markdown(h: str) -> str:
    def pre_to_fenced(m: re.Match) -> str:
        inner = m.group(1)
        inner = re.sub(r"<br\s*/?>", "\n", inner, flags=re.I)
        inner = re.sub(r"</p>\s*<p[^>]*>", "\n", inner, flags=re.I)
        inner = re.sub(r"<[^>]+>", "", inner)
        inner = html.unescape(inner).strip("\n")
        return "\n\n```\n" + inner + "\n```\n\n"

    def code_to_ticks(m: re.Match) -> str:
        inner = re.sub(r"<[^>]+>", "", m.group(1))
        return "`" + html.unescape(inner) + "`"

    h = re.sub(r"<pre[^>]*>(.*?)</pre>", pre_to_fenced, h, flags=re.I | re.S)
    h = re.sub(r"<code[^>]*>(.*?)</code>", code_to_ticks, h, flags=re.I | re.S)
    h = re.sub(r"<figure[^>]*>|</figure>", "", h, flags=re.I)
    h = re.sub(r'<img[^>]+src="([^"]+)"[^>]*/?>', r"\n\n![](\1)\n\n", h, flags=re.I)
    h = re.sub(r"<br\s*/?>", "\n", h, flags=re.I)
    for n in (1, 2, 3, 4, 5, 6):
        h = re.sub(
            rf"<h{n}[^>]*>(.*?)</h{n}>",
            lambda m, n=n: "\n\n" + "#" * n + " " + m.group(1).strip() + "\n\n",
            h, flags=re.I | re.S,
        )
    h = re.sub(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',
               lambda m: f"[{re.sub(r'<[^>]+>', '', m.group(2))}]({m.group(1)})",
               h, flags=re.I | re.S)
    h = re.sub(r"</?(em|i)>", "*", h, flags=re.I)
    h = re.sub(r"</?(strong|b)>", "**", h, flags=re.I)
    h = re.sub(r"<li[^>]*>", "\n- ", h, flags=re.I)
    h = re.sub(r"</?(ul|ol|li|blockquote)[^>]*>", "\n", h, flags=re.I)
    h = re.sub(r"</p>\s*<p[^>]*>", "\n\n", h, flags=re.I)
    h = re.sub(r"</?p[^>]*>", "\n\n", h, flags=re.I)
    h = re.sub(r"<[^>]+>", "", h)
    h = h.replace("&lt;", "\x00LT").replace("&gt;", "\x00GT")
    h = html.unescape(h)
    h = h.replace("\x00LT", "&lt;").replace("\x00GT", "&gt;")
    h = re.sub(r"\[\s*\]\([^)]*\)", "", h)
    h = re.sub(r"[ \t]+\n", "\n", h)
    h = re.sub(r"\n{3,}", "\n\n", h)
    return h.strip()


def truncate_html(h: str, max_paragraphs: int = 2) -> str:
    """Keep the cover <img>/<figure> plus the first N <p> blocks."""
    parts: list[str] = []
    first_img = re.search(r"<(?:figure[^>]*>\s*)?<img[^>]+>(?:\s*</figure>)?", h, re.I)
    if first_img:
        parts.append(first_img.group(0))
    kept = 0
    for m in re.finditer(r"<p[^>]*>.*?</p>", h, re.I | re.S):
        parts.append(m.group(0))
        kept += 1
        if kept >= max_paragraphs:
            break
    return "\n".join(parts) if parts else h[:800]


def parse_rss(xml_bytes: bytes) -> list[Entry]:
    root = ET.fromstring(xml_bytes)
    entries: list[Entry] = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        pub = item.findtext("pubDate") or ""
        date = parse_rss_date(pub) if pub else datetime.now(timezone.utc)
        desc = (item.findtext("description") or "").strip()
        enc = (item.findtext("{http://purl.org/rss/1.0/modules/content/}encoded") or "").strip()
        body = desc if desc else truncate_html(enc)
        entries.append(Entry(title=title, link=link, date=date, body=body))
    return entries


def parse_atom(xml_bytes: bytes) -> list[Entry]:
    root = ET.fromstring(xml_bytes)
    entries: list[Entry] = []
    for entry in root.findall("atom:entry", NS):
        title = (entry.findtext("atom:title", default="", namespaces=NS) or "").strip()
        link_el = entry.find('atom:link[@rel="alternate"]', NS)
        link = link_el.get("href") if link_el is not None else ""
        pub = entry.findtext("atom:published", default="", namespaces=NS) or ""
        date = parse_atom_date(pub) if pub else datetime.now(timezone.utc)
        video_id_el = entry.find("yt:videoId", NS)
        video_id = video_id_el.text if video_id_el is not None else None
        media = entry.find("media:group", NS)
        description = ""
        if media is not None:
            description = (media.findtext("media:description", default="", namespaces=NS) or "").strip()
        entries.append(Entry(title=title, link=link, date=date, body=description, video_id=video_id))
    return entries


def yaml_quote(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def strip_habracut(body: str) -> str:
    # Habr appends a <a href="...#habracut">Читать далее</a> marker at the end
    # of every RSS description. The theme already adds its own "read more"
    # link from the `link:` front-matter, so drop Habr's to avoid duplication.
    return re.sub(
        r'<a[^>]+href="[^"]*#habracut"[^>]*>.*?</a>\s*$',
        "",
        body,
        flags=re.I | re.S,
    )


def render_post(entry: Entry, source: Source) -> str:
    if source.kind == "rss":
        raw = strip_habracut(entry.body)
        cover, rest = extract_cover(raw)
        md_body = html_to_markdown(rest)
        body = ""
        if cover:
            body += f"![]({cover})\n\n"
        body += md_body
    else:
        parts = []
        if entry.video_id:
            parts.append(f"{{{{< youtube {entry.video_id} >}}}}")
        if entry.body:
            parts.append(entry.body)
        body = "\n\n".join(parts)

    body = body.rstrip() + "\n"

    fm = (
        "---\n"
        f"title: {yaml_quote(entry.title)}\n"
        f"date: {entry.date.isoformat()}\n"
        f"link: {entry.link}\n"
        f"source: {source.name}\n"
        "---\n\n"
    )
    return fm + body


def write_post(entry: Entry, source: Source) -> tuple[Path, bool]:
    slug = slugify(entry.title)
    if not slug:
        return Path(), False
    path = ROOT / "content" / source.lang / "post" / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    new_content = render_post(entry, source)
    if path.exists() and path.read_text(encoding="utf-8") == new_content:
        return path, False
    path.write_text(new_content, encoding="utf-8")
    return path, True


def main() -> int:
    errors = 0
    total_written = 0
    total_unchanged = 0
    for src in SOURCES:
        print(f"=== {src.name} ({src.url}) ===", file=sys.stderr)
        try:
            data = fetch(src.url)
            entries = parse_rss(data) if src.kind == "rss" else parse_atom(data)
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            errors += 1
            continue
        written = 0
        unchanged = 0
        for entry in entries:
            if not entry.title or not entry.link:
                continue
            path, was_written = write_post(entry, src)
            if was_written:
                written += 1
                print(f"  wrote {path.relative_to(ROOT)}", file=sys.stderr)
            else:
                unchanged += 1
        total_written += written
        total_unchanged += unchanged
        print(f"  done: {len(entries)} entries, {written} written, {unchanged} unchanged",
              file=sys.stderr)
    print(f"TOTAL: {total_written} written, {total_unchanged} unchanged, {errors} errors",
          file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
