# Notion Setup — NeetiQ Autopilot v2

## Workspace layout

```
NeetiQ Autopilot v2                              (parent page, 🧭)
├── 📋 Strategy                                  (page — STOP + phase + weekly plan)
├── 📘 Brand Identity                            (page — voice doctrine)
├── 🧱 Product Inventory                         (page — what's built)
├── 🎯 CEO Briefing                              (page — standing directives)
├── 👤 USER                                       (page — Avi profile)
├── 📆 Weekly Logs                                (page — container for Analytics reports)
├── 🗂 agent_log                                  (DB — rolling log of every run)
├── 📣 published_posts                            (DB — voice-drift reference)
├── 🗺 outreach_pipeline                          (DB — 11-stage funnel)
└── 🔭 competitive_watchlist                      (DB — competitor snapshots)
```

## Database schemas

### agent_log

| Column | Type |
|---|---|
| Timestamp | TITLE |
| Agent | SELECT('COO', 'INTEL', 'MAKER', 'CONNECT', 'ANALYTICS') |
| Model | SELECT('haiku-4.5', 'sonnet-4.6', 'opus-4.6') |
| Phase | NUMBER |
| Action | RICH_TEXT |
| Result | SELECT('OK', 'FAIL', 'SKIPPED', 'STOP') |
| Next | RICH_TEXT |
| Source | SELECT('cowork', 'cloud-routine', 'chrome', 'dispatch', 'github') |

### published_posts

| Column | Type |
|---|---|
| Title | TITLE |
| Channel | SELECT('Personal LI', 'Company LI', 'Twitter') |
| Pillar | SELECT('contract', 'research', 'dpdp', 'multi') |
| Phase | NUMBER |
| Published | DATE |
| URL | URL |
| Impressions | NUMBER |
| Reactions | NUMBER |
| Comments | NUMBER |
| Profile viewers | NUMBER |
| Replies | NUMBER |
| Notes | RICH_TEXT |

### outreach_pipeline

| Column | Type |
|---|---|
| Name | TITLE |
| Company | RICH_TEXT |
| Role | RICH_TEXT |
| LinkedIn URL | URL |
| Stage | SELECT (1–11 + Stale, Lapsed, Watch, AVI-MANAGED) |
| Segment | SELECT('DPO-compliance', 'litigation-ops', 'in-house-counsel', 'law-firm-associate', 'founder-peer', 'vc', 'other') |
| Personality tag | MULTI_SELECT('data-driven', 'story-driven', 'warm-intro-preferred', 'formal', 'casual', 'skeptical') |
| Pillar | SELECT('contract', 'research', 'dpdp', 'multi') |
| First touched | DATE |
| Last touched | DATE |
| Last action | RICH_TEXT |
| Source | SELECT('inbound', 'referral', 'cold', 'conference', 'content-reply') |
| Notes | RICH_TEXT |

### competitive_watchlist

| Column | Type |
|---|---|
| Name | TITLE |
| Category | SELECT('global-contract', 'india-contract', 'global-research', 'india-research', 'india-infra', 'adjacent') |
| Home URL | URL |
| Last activity | DATE |
| Last activity summary | RICH_TEXT |
| Threat level | SELECT('watch', 'active-competitor', 'direct-conflict', 'compression-risk') |
| India presence | SELECT('none', 'watching', 'active', 'primary') |
| Funding | RICH_TEXT |
| Notes | RICH_TEXT |

## Integration setup

1. Create a Notion **Internal Integration** at `notion.so/my-integrations`.
2. Share "NeetiQ Autopilot v2" parent page with the integration.
3. All sub-pages and DBs inherit the share.

## Editing etiquette

- Claude (all agents) writes to the Notion brain. Avi edits any of it any
  time — last-writer-wins. If Avi and Claude conflict, Avi wins; Claude
  re-reads on the next run.
- The local `brain/*.md` mirror is updated by COO on Sunday and Morning
  Brief. If Notion and the markdown diverge, **Notion is canonical** for
  strategy/USER/ceo_briefing. Brand identity + product inventory are
  canonical in the **markdown** (engineering sources).

## Links

Once the pages are created, capture the page IDs here:

```
NeetiQ Autopilot v2 (parent):   <fill in>
Strategy:                        <fill in>
Brand Identity:                  <fill in>
Product Inventory:               <fill in>
CEO Briefing:                    <fill in>
USER:                            <fill in>
Weekly Logs:                     <fill in>

agent_log (DB):                  <fill in>
published_posts (DB):            <fill in>
outreach_pipeline (DB):          <fill in>
competitive_watchlist (DB):      <fill in>
```

Save to `brain/.notion_ids.json` (gitignored). Agents read this at startup.
