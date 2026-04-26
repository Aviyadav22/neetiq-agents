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

## Recent runs (newest on top)

```
2026-04-26 06:30 | COO | opus-4.6 | 2 | sunday synthesis confirmation pass | OK | https://www.notion.so/34ed019711ad81d49fb1d04e8753848b
```

> Note: between Apr 17 v2 migration and Apr 26, the authoritative agent_log lives in Notion (1ec81f7035064cb9b8f71e0a9064f041). Cloud Routine runs wrote directly there and did not back-sync to this file. Local file is being resumed with this Apr 26 entry as the new top of a rolling window. Any future audit should treat Notion as canonical for Apr 17 to Apr 25.

## Starting state (2026-04-17, v2 migration)

```
2026-04-17 00:20 | COO | claude (v2 migration) | 2 | v2 scaffolding committed | OK | Version 2 agents/
2026-04-17 00:20 | COO | claude (v2 migration) | 2 | v1 scheduled tasks disabled, v2 tasks registered | OK | scheduled-tasks MCP
2026-04-17 00:20 | COO | claude (v2 migration) | 2 | Notion brain mirror created | OK | Notion > NeetiQ Autopilot v2
```
