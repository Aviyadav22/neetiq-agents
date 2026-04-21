# COO — Evening Summary

**Schedule:** Weekdays 18:00 IST
**Model:** Haiku 4.5
**Duration:** 2–5 min

## Pre-run

1. Run `.claude/skills/stop-check`.
2. Read: today's `brain/agent_log.md` rows (from 00:00 IST), today's `published_posts` rows, today's `outreach_pipeline` updates from Notion (new stages reached).

## Output

One Dispatch push, ≤8 lines.

Template:
```
FYI — Evening Summary, <Day MMM DD>.

Posted today: <N on Personal LI, N on Company, N on Twitter, or "none">.

Outreach today: <N connection requests, N DMs, N replies received>. New stage reached: <most-progressed prospect, one name, one stage>.

INTEL: <any significant overnight finding referenced, or "nothing flagged">.

Pending tomorrow: <N drafts awaiting approval, N outreach at 11 AM>.

Weekly cap: <% burned>. <"on track" / "watch" / "cut non-critical">.
```

## Log

```
2026-MM-DD 18:00 | COO | haiku-4.5 | <phase> | evening summary | OK | dispatch
```

## Rules

- Weekly cap check: if >65% by Wednesday evening, next morning brief must flag "cut non-critical INTEL" and COO Sunday must demote tasks for the rest of the week.
- If no MAKER or CONNECT runs happened today, say so explicitly — silence is a signal of system failure.

## Healthchecks ping (MANDATORY, final action)

After the Dispatch push and log row, fetch (HTTP GET): `https://hc-ping.com/6a99bc9e-e954-48f3-96bf-ee0804560cb4`

Use Bash: `curl -fsS -m 10 --retry 3 "https://hc-ping.com/6a99bc9e-e954-48f3-96bf-ee0804560cb4" >/dev/null || true`. Fallback: WebFetch.

On unrecoverable error, fetch `https://hc-ping.com/6a99bc9e-e954-48f3-96bf-ee0804560cb4/fail` before aborting. 35-min grace; missed ping = email to Avi (not SMS — evening is not tagged critical).
