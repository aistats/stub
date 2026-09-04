#!/usr/bin/env python3
"""Tier A year-site / stub contract checks.

No network, no pandoc, stdlib only. Intended for PR CI on stub and aistats20XX.

Year mode: required archival pages present, no virtual chrome in markdown,
conference.year consistent with dated conference.dates entries.

Stub mode: template page set present, 20XX placeholders retained, no leftover
theme forks / obvious venue-year pollution outside _doc examples.

Tier C sync faithfulness (convert fixtures, live virtual) lives in
aistats/site-management scripts/sync_virtual/ — not here.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

# CIP-0004 archival / sync inventory (markdown bodies). _config.yml checked separately.
REQUIRED_YEAR_PAGES: Sequence[str] = (
    "index.md",
    "dates.md",
    "call-for-papers.md",
    "code-of-conduct.md",
    "faqs.md",
    "camera.md",
    "poster.md",
    "reviewer_guidelines.md",
    "ac_guidelines.md",
    "journal-track.md",
    "workshops.md",
    "accommodation.md",
    "visa.md",
    "invited.md",
    "awards.md",
    "registration.md",
    "schedule.md",
)

# Stub template pages (accommodation is still HTML; visa lands when year needs it).
REQUIRED_STUB_PAGES: Sequence[str] = (
    "index.md",
    "dates.md",
    "call-for-papers.md",
    "code-of-conduct.md",
    "faqs.md",
    "camera.md",
    "poster.md",
    "reviewer_guidelines.md",
    "ac_guidelines.md",
    "journal-track.md",
    "workshops.md",
    "_accommodation.html",
    "invited.md",
    "awards.md",
    "registration.md",
    "schedule.md",
    "committee.html",
    "other.md",
)

FORBIDDEN_CHROME: Sequence[Tuple[str, str]] = (
    ("child-menu", "virtual year-nav chrome"),
    ("Select Year:", "virtual year selector"),
    ("container-fluid", "Bootstrap layout chrome from virtual"),
)

STUB_FORBIDDEN: Sequence[Tuple[str, str]] = (
    ("lawrennd/proceedings", "old theme fork reference"),
)

# Cities / venues that must not appear in stub *public* pages (examples OK in _doc/).
STUB_POLLUTION: Sequence[str] = (
    "Valencia",
    "Mai Khao",
    "Phuket",
    "Tangier",
    "Palermo",
    "Kadriorg",
)

YEAR_RE = re.compile(r"\b((?:19|20)\d{2})\b")
PLACEHOLDER_YEAR_RE = re.compile(r"20XX|XXXX", re.I)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def detect_mode(root: Path, explicit: Optional[str]) -> str:
    if explicit in ("stub", "year"):
        return explicit
    config = root / "_config.yml"
    if not config.is_file():
        return "year"
    text = _read_text(config)
    year = _extract_conference_year(text)
    if year is None or PLACEHOLDER_YEAR_RE.search(str(year)) or year == "20XX":
        return "stub"
    return "year"


def _extract_conference_year(config_text: str) -> Optional[str]:
    """Best-effort: first `year:` under a `conference:` block."""
    in_conference = False
    conference_indent = 0
    for line in config_text.splitlines():
        if re.match(r"^conference:\s*$", line):
            in_conference = True
            conference_indent = 0
            continue
        if not in_conference:
            continue
        if line.strip() and not line.startswith(" ") and not line.startswith("\t"):
            if not line.lstrip().startswith("#"):
                in_conference = False
                continue
        m = re.match(r"^(\s+)year:\s*(.+?)\s*$", line)
        if m and in_conference:
            raw = m.group(2).strip().strip("\"'")
            if raw.startswith("#"):
                continue
            return raw.split("#", 1)[0].strip().strip("\"'")
        # leave conference on dedent to key at column 0 handled above
        _ = conference_indent
    return None


def _extract_conference_dates(config_text: str) -> List[str]:
    """Collect list items under conference.dates (shallow YAML)."""
    lines = config_text.splitlines()
    dates: List[str] = []
    in_conference = False
    in_dates = False
    dates_indent = 0
    for line in lines:
        if re.match(r"^conference:\s*$", line):
            in_conference = True
            in_dates = False
            continue
        if in_conference and line.strip() and not line[0].isspace() and not line.lstrip().startswith("#"):
            in_conference = False
            in_dates = False
            continue
        if not in_conference:
            continue
        m_dates = re.match(r"^(\s+)dates:\s*(.*)$", line)
        if m_dates:
            in_dates = True
            dates_indent = len(m_dates.group(1))
            rest = m_dates.group(2).strip()
            if rest and not rest.startswith("#"):
                dates.append(rest.strip("[] ").strip("\"'"))
            continue
        if in_dates:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            indent = len(line) - len(line.lstrip(" "))
            if indent <= dates_indent and not line.lstrip().startswith("-"):
                in_dates = False
                continue
            item = re.match(r"^\s*-\s+(.+)$", line)
            if item:
                val = item.group(1).split("#", 1)[0].strip().strip("\"'")
                if val:
                    dates.append(val)
    return dates


def iter_markdown_files(root: Path) -> Iterable[Path]:
    skip_dirs = {".git", "_site", "node_modules", "vendor", ".bundle", "sync-report", "sync-report-sfv"}
    for path in sorted(root.rglob("*.md")):
        if any(part in skip_dirs for part in path.parts):
            continue
        yield path


def check_required_pages(root: Path, required: Sequence[str]) -> List[str]:
    errors: List[str] = []
    for rel in required:
        if not (root / rel).is_file():
            errors.append(f"missing required page: {rel}")
    return errors


def check_chrome(root: Path) -> List[str]:
    errors: List[str] = []
    for path in iter_markdown_files(root):
        if path.parts[0] == "_doc" or (len(path.parts) > 1 and path.parts[-2] == "_doc"):
            # Organiser docs may mention virtual chrome by name.
            rel = path.relative_to(root).as_posix()
            if rel.startswith("_doc/"):
                continue
        text = _read_text(path)
        rel = path.relative_to(root).as_posix()
        for marker, why in FORBIDDEN_CHROME:
            if marker in text:
                errors.append(f"{rel}: forbidden chrome {marker!r} ({why})")
    return errors


def check_config_year_dates(root: Path) -> List[str]:
    errors: List[str] = []
    config = root / "_config.yml"
    if not config.is_file():
        return ["missing _config.yml"]
    text = _read_text(config)
    year = _extract_conference_year(text)
    if year is None:
        errors.append("_config.yml: conference.year not found")
        return errors
    if PLACEHOLDER_YEAR_RE.search(year) or year == "20XX":
        return errors  # stub placeholders; year/date coherence N/A
    if not re.fullmatch(r"\d{4}", year):
        errors.append(f"_config.yml: conference.year is not a 4-digit year: {year!r}")
        return errors
    for entry in _extract_conference_dates(text):
        if entry.upper() in {"TBA", "TBD", ""}:
            continue
        found = YEAR_RE.findall(entry)
        for y in found:
            if y != year:
                errors.append(
                    f"_config.yml: conference.dates entry {entry!r} "
                    f"has year {y}, expected {year}"
                )
    return errors


def check_stub_placeholders(root: Path) -> List[str]:
    errors: List[str] = []
    config = root / "_config.yml"
    if not config.is_file():
        return ["missing _config.yml"]
    text = _read_text(config)
    if "20XX" not in text and "aistats20XX" not in text:
        errors.append("_config.yml: expected 20XX placeholders in stub template")
    year = _extract_conference_year(text)
    if year and re.fullmatch(r"\d{4}", year):
        errors.append(
            f"_config.yml: stub must keep placeholder year, found conference.year={year}"
        )
    for path in iter_markdown_files(root):
        rel = path.relative_to(root).as_posix()
        if rel.startswith("_doc/"):
            continue
        body = _read_text(path)
        for marker, why in STUB_FORBIDDEN:
            if marker in body:
                errors.append(f"{rel}: forbidden {marker!r} ({why})")
        for city in STUB_POLLUTION:
            if city in body:
                errors.append(f"{rel}: stub pollution {city!r} (use placeholders)")
    return errors


def run_checks(root: Path, mode: str) -> List[str]:
    errors: List[str] = []
    if mode == "stub":
        errors.extend(check_required_pages(root, REQUIRED_STUB_PAGES))
        errors.extend(check_chrome(root))
        errors.extend(check_stub_placeholders(root))
    else:
        errors.extend(check_required_pages(root, REQUIRED_YEAR_PAGES))
        errors.extend(check_chrome(root))
        errors.extend(check_config_year_dates(root))
    return errors


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root (default: cwd)",
    )
    parser.add_argument(
        "--mode",
        choices=("auto", "stub", "year"),
        default="auto",
        help="stub = template checks; year = archival site; auto detects from conference.year",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()
    mode = detect_mode(root, None if args.mode == "auto" else args.mode)
    print(f"check_year_site: root={root} mode={mode}")
    errors = run_checks(root, mode)
    if errors:
        print(f"FAILED ({len(errors)} issue(s)):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
