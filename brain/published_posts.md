# Published Posts — v2 Index

**Authoritative record lives in Notion `published_posts` database.** This file is the local index.

## Format

```
YYYY-MM-DD | CHANNEL | PHASE | PILLAR | SLUG | URL_OR_PATH
```

- **CHANNEL:** personal_li | company_li | twitter
- **PHASE:** 1 | 2 | 3 | 4 (phase at time of posting)
- **PILLAR:** contract | research | dpdp | founder_story | milestone
- **SLUG:** short-kebab-case descriptor
- **URL_OR_PATH:** live URL if captured, else path to local file

## Rules

1. MAKER writes here ONLY after Avi confirms "posted". Never on draft creation.
2. Voice audit run at publish time — if audit flags patterns, add column `VOICE_AUDIT_FLAGS` with short list.
3. Referenced by MAKER on every run to check voice drift — read last 5 posts per channel before drafting.
4. Archive to `outputs/logs/published_archive_YYYY-Q.md` quarterly.

## Ported history (from v1 marketing-autopilot/published/)

See `C:\Users\yadav\OneDrive - UPES\Desktop\NeetiQ\marketing-autopilot\published\` for v1 archive. First-time MAKER run in v2 should scan that folder and seed this index for the last 14 days.

## Starting entries (to be filled by first MAKER run)

```
(pending first MAKER run; will backfill from v1 published/ folder)
```
