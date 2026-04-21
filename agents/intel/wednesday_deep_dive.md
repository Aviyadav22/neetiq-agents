# INTEL — Wednesday Deep Dive

**Schedule:** Wednesday 10:00 IST
**Model:** Sonnet 4.6 for synthesis, Haiku 4.5 for bulk extraction
**Duration:** 20–30 min
**Weekly cost:** ~8% of Max 20x weekly bucket

## Pre-run

1. stop-check.
2. Read full `brain/competitive_watchlist.md`, `brain/strategy.md`, `brain/ceo_briefing.md`, the last 7 daily scan reports.
3. Fetch Notion `competitive_watchlist` DB in full.

## What the Deep Dive produces

### 1. Full competitor matrix update
For each competitor in the watchlist:
- Traction signal this week (users, revenue, press mentions, funding)
- Product changes (new features, platform moves, integrations)
- Distribution moves (partnerships, marketplace listings, ads)
- Team moves (notable hires, founder posts)
- NeetiQ delta: where did the gap grow, where did it shrink?

### 2. Positioning gap analysis
Pick 1–2 areas where a competitor is gaining on NeetiQ's positioning this week. Recommend one concrete counter-move.

### 3. Delhi NCR events scan
- Upcoming legal tech meetups, bar association events, compliance conferences in NCR
- CII, FICCI, ASSOCHAM legal panels
- Any Avi should attend / speak at in the next 4 weeks?
- DPDP enforcement workshops (high-value outreach territory)

### 4. Grants + credits status check (weekly reconciliation)
For each open application per `brain/ceo_briefing.md`:
- Microsoft for Startups Founders Hub — status?
- Google for Startups India Accelerator — deadline 2026-04-19, status?
- Alibaba Cloud AI Catalyst — applied?
- Cohere Startup Program — applied?
- Any new grants posted this week?

### 5. Output page
Write a long-form Notion page under `NeetiQ Autopilot v2 > INTEL Deep Dives > YYYY-Www`. Sections:
- Executive summary (5 lines)
- Competitor matrix update
- Positioning gap + counter-move
- NCR events
- Grants reconciliation
- COO action items (what Sunday synthesis should reflect)

### 6. Dispatch push
≤10 lines:
```
FYI — Wednesday deep dive.
Top competitor move: <one line>.
Recommended counter-move: <one line>.
NCR events worth attending: <N>, top: <event name>.
Grants status: <short>.
Full report: Notion > NeetiQ Autopilot v2 > INTEL Deep Dives > YYYY-Www.
```

## Log

```
2026-MM-DD 10:00 | INTEL | sonnet-4.6 | <phase> | wednesday deep dive | OK | Notion > INTEL Deep Dives > YYYY-Www
```

## Rules

- Never recommend a counter-move that violates the current phase (e.g., don't recommend a Phase 4 thought-leadership post if current_phase=2).
- If >2 competitors moved meaningfully in the same week, flag that as "compression risk" — NeetiQ's window is shrinking.

## Healthchecks ping (MANDATORY — bookends the run)

Wednesday Deep Dive is a 20–35 min long-runner. Ping both ends.

- At the TOP, right after stop-check and charter read, fetch (HTTP GET): `https://hc-ping.com/3dfa732a-0799-4138-8a7b-d8a8350942db/start`
- At the BOTTOM, after writing the Notion page and the log row, fetch (HTTP GET): `https://hc-ping.com/3dfa732a-0799-4138-8a7b-d8a8350942db`
- On unrecoverable error, fetch `https://hc-ping.com/3dfa732a-0799-4138-8a7b-d8a8350942db/fail` before aborting.

Use Bash: `curl -fsS -m 10 --retry 3 "<url>" >/dev/null || true`. Fallback: WebFetch. 45-min grace; missed ping = email alert.
