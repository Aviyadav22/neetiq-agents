#!/usr/bin/env python3
"""
intel-feed/poll.py

Polls RSS feeds + scrape-targets listed in sources.yml.
Writes normalized JSON to outputs/intel-feed/YYYY-MM-DD.json at repo root.

Runs inside GitHub Actions (see .github/workflows/intel-feed.yml).
Never run this from Claude's session — Claude reads the *output* only.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import feedparser
import requests
import yaml
from bs4 import BeautifulSoup
from dateutil import parser as dateparser

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]
SOURCES = SCRIPT_DIR / "sources.yml"
OUT_DIR = REPO_ROOT / "outputs" / "intel-feed"
USER_AGENT = "neetiq-intel-feed/1.0 (+https://neetiq.ai)"
TIMEOUT = 20
MAX_SNIPPET = 400


def _hash(*parts: str) -> str:
    h = hashlib.sha1()
    for p in parts:
        h.update(p.encode("utf-8", errors="ignore"))
    return "sha1:" + h.hexdigest()[:16]


def _iso(dt: Any) -> str | None:
    if dt is None:
        return None
    try:
        if isinstance(dt, str):
            dt = dateparser.parse(dt)
        return dt.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    except Exception:
        return None


def poll_rss(name: str, url: str) -> list[dict]:
    feed = feedparser.parse(url, agent=USER_AGENT)
    if feed.bozo and not feed.entries:
        raise RuntimeError(f"rss parse failed: {feed.bozo_exception}")
    out = []
    for e in feed.entries[:15]:
        title = (e.get("title") or "").strip()
        link = (e.get("link") or "").strip()
        snippet = BeautifulSoup(e.get("summary", ""), "html.parser").get_text(" ", strip=True)[:MAX_SNIPPET]
        published = _iso(e.get("published") or e.get("updated"))
        out.append({
            "source": name,
            "source_type": "rss",
            "title": title,
            "url": link,
            "published": published,
            "snippet": snippet,
            "hash": _hash(name, link, title),
        })
    return out


def poll_page(name: str, url: str, selector: str) -> list[dict]:
    r = requests.get(url, timeout=TIMEOUT, headers={"User-Agent": USER_AGENT})
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    out = []
    for a in soup.select(selector)[:15]:
        title = a.get_text(strip=True)
        href = a.get("href", "")
        if not title or not href:
            continue
        if href.startswith("/"):
            base = "/".join(url.split("/")[:3])
            href = base + href
        out.append({
            "source": name,
            "source_type": "page",
            "title": title,
            "url": href,
            "published": None,
            "snippet": title[:MAX_SNIPPET],
            "hash": _hash(name, href, title),
        })
    return out


def main() -> int:
    if not SOURCES.exists():
        print(f"missing {SOURCES}", file=sys.stderr)
        return 2
    cfg = yaml.safe_load(SOURCES.read_text())
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    entries: list[dict] = []
    polled = 0
    failed: list[str] = []

    for s in cfg.get("rss", []) or []:
        polled += 1
        try:
            entries.extend(poll_rss(s["name"], s["url"]))
        except Exception as e:
            failed.append(s["name"])
            print(f"RSS fail {s['name']}: {e}", file=sys.stderr)

    for group in ("pages", "india_regulators", "grants"):
        for s in cfg.get(group, []) or []:
            polled += 1
            try:
                entries.extend(poll_page(s["name"], s["url"], s["selector"]))
            except Exception as e:
                failed.append(s["name"])
                print(f"PAGE fail {s['name']}: {e}", file=sys.stderr)

    run_at = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    stamp = run_at[:10]
    payload = {
        "run_at": run_at,
        "sources_polled": polled,
        "sources_failed": failed,
        "entries": entries,
    }
    (OUT_DIR / f"{stamp}.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"wrote {stamp}.json — {len(entries)} entries, {len(failed)} failed")
    return 0 if not failed or len(failed) < polled else 1


if __name__ == "__main__":
    sys.exit(main())
