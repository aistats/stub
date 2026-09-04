# Syncing the year site with virtual.aistats.org

The **year site** (`aistats20XX` on GitHub Pages) is the long-term public record. [virtual.aistats.org](https://virtual.aistats.org/) is the live operations surface (registration checkout, interactive calendar, paper browser). Do not treat virtual as something that silently overwrites the year site.

Tooling lives in [`aistats/site-management`](https://github.com/aistats/site-management) under `scripts/sync_virtual/`. Commands and schema detail are in that package’s [README](https://github.com/aistats/site-management/blob/main/scripts/sync_virtual/README.md). This note is the organiser-facing workflow only.

Related timing bands (when to seed CFP, dates, invited talks, and so on) are sketched in site-management [CIP-0003](https://github.com/aistats/site-management/blob/main/cip/cip0003.md). Design and policy for the sync itself are in [CIP-0004](https://github.com/aistats/site-management/blob/main/cip/cip0004.md).

## Default: compare first (no overwrite)

From a checkout of `site-management`, with the year repo nearby:

```bash
.venv-vibesafe/bin/python scripts/sync_virtual/__main__.py sync \
  --manifest scripts/sync_virtual/manifests/aistats20XX.yml \
  --target-repo ../aistats20XX \
  --report-dir ../aistats20XX/sync-report
```

With no write flags, the tool only fetches or uses fixtures, converts, and writes a **report** under `sync-report/`:

| Artefact | Use |
|----------|-----|
| `summary.md` | What matched, drifted, or is missing |
| `diffs/*.diff` | Normalised body differences |
| `virtual-update-request.md` | Text you can send when the **year site** is right and virtual should catch up |

Read the report before changing anything. Prefer fixing year-site markdown and `_config.yml` by hand when the year site is already the better archive.

## Opt-in writes

These flags change the year repo. Use `--only` with explicit page ids.

| Flag | Effect |
|------|--------|
| `--fill-missing` | Create pages that are absent on the year site from the converted virtual candidate |
| `--apply-from-virtual` | Overwrite listed existing pages with the converted candidate (**requires `--only`**) |

Examples:

```bash
# Create only the pages that are missing
... sync --fill-missing --only call-for-papers,code-of-conduct,faqs ...

# Replace specific pages after you have read the diffs
... sync --apply-from-virtual --only call-for-papers,camera ...
```

Pages marked `on_drift: prefer_year` in the manifest (for example `dates`, `awards`, `index`) are **not** overwritten by `--apply-from-virtual`. Key dates should keep `{% include listdates.html %}` and parseable deadline values in `_config.yml`; award announcement prose must not be replaced by abstract cards from the virtual Award event list.

Never paraphrase virtual wording into the year site. Conversion is pandoc plus deterministic post-processing only.

## Virtual update request

When the year site is correct and virtual has drifted or lagged:

1. Run sync in default (report-only) mode.
2. Open `virtual-update-request.md`.
3. Send that document (or a trimmed version) to the corporate / virtual operator so they can align virtual with the year site.

Do not reverse the polarity: do not ask organisers to copy paraphrased virtual HTML back onto GitHub Pages as the archive.

## What not to import

Keep these as **links** from the year site; do not body-import them:

- Interactive calendar
- Papers list / OpenReview browser
- Registration checkout
- Sponsor application portal

## Checks

Before merging year-site PRs, Tier A `scripts/check_year_site.py` (see [site-contract.md](./site-contract.md)) checks inventory paths and config shape. Faithful conversion and live fetch remain in site-management, not in year-site CI.
