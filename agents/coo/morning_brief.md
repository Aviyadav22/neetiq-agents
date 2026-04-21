# COO — Morning Brief

**Schedule:** Weekdays 08:30 IST
**Model:** Haiku 4.5 for the scan, Sonnet 4.6 for the synthesis line
**Duration:** 2–5 min
**Expected daily cost:** ~1% of Max 20x weekly bucket per run

## Pre-run

1. Run `.claude/skills/stop-check`. If STOP engaged, exit.
2. Read: last 24 hours of `brain/agent_log.md`, last 24 hours of Notion `agent_log` database, `outputs/drafts/` (any pending approval), `outputs/intel-feed/` (any new overnight commits), `brain/ceo_briefing.md` (standing directives with deadlines).

## What Morning Brief produces

One Dispatch push to Avi, ≤10 lines. Hard ceiling.

Template:

```
REVIEW — Morning Brief, <Day MMM DD>.

Overnight: <1 line. What INTEL or GitHub Actions picked up. If nothing, say "nothing new".>

Pending approval: <count> draft(s) in outputs/drafts/. <most-urgent filename>.

Outreach today: <segment focus for the day per strategy.md>. <N> prospects queued.

Directive status: <any OVERDUE item from ceo_briefing.md>.

Top ask: <1 specific thing Avi should decide/do today. ONE thing.>
```

## Healthchecks ping (MANDATORY, final action)

As the last step after the Dispatch push goes out, fetch (HTTP GET): `https://hc-ping.com/07ad8b7c-1df3-4dad-9ec3-ca6dfe6bdf5b`

Use Bash: `curl -fsS -m 10 --retry 3 "https://hc-ping.com/07ad8b7c-1df3-4dad-9ec3-ca6dfe6bdf5b" >/dev/null || true`. Fallback: WebFetch.

If Dispatch fails or the briefing couldn't be built (missing inputs, Notion down), fetch `.../fail` instead: `https://hc-ping.com/07ad8b7c-1df3-4dad-9ec3-ca6dfe6bdf5b/fail`. 35-min grace; a missed or failed ping pages Avi by SMS.

## Log

```
2026-MM-DD 08:30 | COO | haiku-4.5 | <phase> | morning brief | OK | dispatch
```

## Rules

- Never include more than one "top ask". Avi ignores walls of text.
- If nothing is pending and nothing is overdue, push the brief anyway with "nothing urgent today" — the absence of the notification should not be how he learns the system is down.
- Never auto-approve anything. Review means Avi sees + decides.
