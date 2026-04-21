# ANALYTICS — Weekly Report

**Schedule:** Friday 18:00 IST
**Model:** Sonnet 4.6
**Duration:** 10–15 min

## Pre-run

1. stop-check.
2. Read: last 7 days of `brain/agent_log.md` + Notion `agent_log`, `brain/published_posts.md` + Notion `published_posts`, Notion `outreach_pipeline` (stage distribution snapshot), `brain/competitive_watchlist.md`, Notion `strategy` page (current_phase + KPIs), `brain/ceo_briefing.md` (directive status).

## What ANALYTICS produces

### 1. Content performance
For each post this week:
- Channel, pillar, phase, impressions, reactions, comments, profile viewers attributed, replies
- If engagement data isn't available (Claude in Chrome limitations), note "awaiting manual capture"
- Best-performing post of the week (+ why you think so)
- Underperformer (+ diagnosis: topic, timing, opener, format)

### 2. Outreach metrics
- Connection requests sent / accepted / pending
- DMs sent / replied / ignored
- Stage transitions: who moved forward, who stalled
- Buyer signals count (stage 7+)
- Warm leads active (stages 5–9)
- Avi-managed conversations status (flag only, don't analyze content)

### 3. Competitor moves
- Summary of the week's competitive_watchlist updates
- Any "compression risk" flagged by INTEL Wednesday Deep Dive
- Grants / credits status changes

### 4. System health
- Total agent runs: N
- Failures: N (list)
- Weekly cap burn: X% (rough, from claude.ai/settings/usage if Avi updates a file; else estimate from run count)
- Healthchecks status: last miss

### 5. Recommendations for next week (3 max)
- Ranked by impact. "Do X, cut Y, monitor Z."
- Tie each to data from the week.

### 6. Output
Write a Notion page under `NeetiQ Autopilot v2 > Analytics > Week-YYYY-Www`. Mirror to `outputs/logs/analytics_YYYY-Www.md`.

### 7. Email digest to Avi
Use Gmail MCP to create a draft (NOT send) to aviyadav.personal@gmail.com:
- Subject: `[NeetiQ v2] Weekly Report — Week YYYY-Www`
- Body: the Executive Summary section + links to the Notion page
- ≤300 words in the email body. Full detail lives in Notion.
- LEAVE AS DRAFT. Avi sends if he wants, or ignores.

### 8. Dispatch push
```
FYI — Weekly Report ready.
Top stat this week: <one line>.
Best post: <pillar + channel>.
Warm leads active: <N>.
Top recommendation: <one line>.
Full: Notion > NeetiQ Autopilot v2 > Analytics > Week-YYYY-Www.
```

## Healthchecks ping (MANDATORY — bookends the run)

- At the TOP, right after stop-check, fetch (HTTP GET): `https://hc-ping.com/8c5be281-4ac9-45ab-abd1-74b8a531a821/start`
- At the BOTTOM, after writing the Notion page, Gmail draft, Dispatch push, and log row, fetch (HTTP GET): `https://hc-ping.com/8c5be281-4ac9-45ab-abd1-74b8a531a821`
- On unrecoverable error, fetch `https://hc-ping.com/8c5be281-4ac9-45ab-abd1-74b8a531a821/fail` before aborting.

Use Bash: `curl -fsS -m 10 --retry 3 "<url>" >/dev/null || true`. Fallback: WebFetch. 45-min grace, email alert on miss.

## Log

```
2026-MM-DD 18:00 | ANALYTICS | sonnet-4.6 | <phase> | weekly report | OK | Notion > Analytics > Week-YYYY-Www
```

## Rules

- Every recommendation must cite at least one data row. No gut calls in the written report.
- If a recommendation conflicts with a standing CEO directive, flag the conflict — let Avi resolve.
- Never suggest actions that require Avi's hours on the weekend. Weekend asks = deal breakers in USER.md.
- If a week had no posts (MAKER failed or Avi didn't approve), say so. Silence is a signal.
