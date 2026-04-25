# Agent Log — v2

**Authoritative log lives in Notion `agent_log` database.** This file is the local mirror, maintained as a rolling 7-day window by COO Sunday Synthesis.

## Format

One row per run. Order: newest on top. Fields:

```
YYYY-MM-DD HH:MM | AGENT | MODEL | PHASE | ACTION | RESULT | NEXT
```

- **AGENT:** COO | INTEL | MAKER | CONNECT | ANALYTICS
- **MODEL:** sonnet-4.6 | haiku-4.5 | opus-4.6
- **PHASE:** 1 | 2 | 3 | 4 (should match brain/strategy.md current_phase)
- **ACTION:** 1–5 words describing what the run did
- **RESULT:** OK | PARTIAL | FAIL | STOP (if aborted by STOP toggle) | SKIPPED (if no-action)
- **NEXT:** file path or Notion link where output landed, or "none" for no-action

## Rules

1. **One row per run.** No multi-paragraph entries.
2. **No-action runs still log.** Write one line: `[time] | [agent] | haiku-4.5 | [phase] | no action | SKIPPED | reason: [one sentence]`
3. **STOP-triggered aborts.** Write one line: `[time] | [agent] | haiku-4.5 | [phase] | stopped by STOP toggle | STOP | none`
4. **Failures.** Write one line plus a pointer to `outputs/logs/YYYY-MM-DD_agent_trace.log` for details. Never dump stack traces in the log.
5. **Rotation.** When the file hits 200 lines, COO Sunday Synthesis moves the oldest half to `outputs/logs/agent_log_archive_YYYY-Www.md`.

## Log (newest first)

2026-04-25 18:00 | COO | haiku-4.5 | 2 | evening summary — 0 posts, 0 outreach, INTEL feed 404 (D12 day 6), 3 drafts pending approval, CONNECT queued Mon Apr 27; Dispatch draft staged | OK | Notion agent_log + Gmail draft r-7437365903125558370
2026-04-25 10:00 | INTEL | sonnet-4.6 | 2 | daily scan (saturday) — 0 new items, feed 404, fallback 2026-04-24.json, 7 sources dark (D12 day 6), Gmail draft staged | OK | Notion agent_log
2026-04-25 08:30 | COO | haiku-4.5 | 2 | morning brief — Gmail draft sent; Gmail MCP re-auth needed, D3/D4 OVERDUE Mon Apr 27, 3 drafts pending approval, Tanya stage-7 buyer signal active | OK | Notion agent_log

## Starting state (2026-04-17, v2 migration)

```
2026-04-17 00:20 | COO | claude (v2 migration) | 2 | v2 scaffolding committed | OK | Version 2 agents/
2026-04-17 00:20 | COO | claude (v2 migration) | 2 | v1 scheduled tasks disabled, v2 tasks registered | OK | scheduled-tasks MCP
2026-04-17 00:20 | COO | claude (v2 migration) | 2 | Notion brain mirror created | OK | Notion > NeetiQ Autopilot v2
```
