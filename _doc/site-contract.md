# Year-site contract checks (Tier A)

PR CI runs [`scripts/check_year_site.py`](../scripts/check_year_site.py). It needs only Python 3 — no network, no pandoc, no Jekyll.

## What it checks

| Mode | When | Checks |
|------|------|--------|
| **stub** | `conference.year` is still `20XX` | Template pages present; no virtual chrome in `*.md`; placeholders kept; no leftover theme/venue pollution on public pages |
| **year** | `conference.year` is a real year | Archival pages from the CIP-0004 inventory present; no virtual chrome; `conference.dates` years match `conference.year` |

Mode is auto-detected; override with `--mode stub` or `--mode year`.

## Enable on a year repo

1. Copy `scripts/check_year_site.py` and `.github/workflows/site-contract.yml` from this stub (or keep them in sync when the stub template updates).
2. Open a PR: the **Site contract** workflow should run automatically.
3. Optional local run:

```bash
python3 scripts/check_year_site.py --root .
```

## What this does *not* check

Faithful virtual → markdown conversion, sync diffs, and live fetches are **Tier C** and live in [`aistats/site-management`](https://github.com/aistats/site-management) under `scripts/sync_virtual/`. Do not put those in year-site CI.
