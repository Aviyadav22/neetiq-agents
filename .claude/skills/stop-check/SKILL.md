---
name: stop-check
description: Reads STOP toggle from brain/strategy.md. If STOP is true, abort the current run immediately with a one-line agent_log entry. Every agent calls this as its first action.
---

# STOP Check

## Invocation

Every agent's FIRST action on every run — before reading any other brain file, before any tool call.

## Logic

1. Read first 15 lines of `brain/strategy.md`.
2. Find the line matching `STOP: <value>`.
3. Normalize: strip whitespace, lowercase.
4. If value is exactly `false`, return `STOP_CHECK: CLEAR` and continue.
5. For any other value (`true`, `1`, `yes`, `stop`, `halt`, ANY text), return `STOP_CHECK: ENGAGED`.

## On ENGAGED

1. Write ONE line to `brain/agent_log.md`:
   ```
   YYYY-MM-DD HH:MM | <AGENT> | haiku-4.5 | <phase> | stopped by STOP toggle | STOP | none
   ```
2. Write the same row to Notion `agent_log` database.
3. Push Dispatch notification to Avi (once per session only, rate-limited to 1/hour):
   ```
   FYI — <AGENT> hit STOP toggle. Not running. Toggle in brain/strategy.md to resume.
   ```
4. Exit immediately. No further work.

## Cross-check: Notion mirror

Before deciding CLEAR, also fetch the Notion `strategy` page's STOP property (if MCP connector is available). If the two disagree, prefer the MORE RESTRICTIVE: ENGAGED wins. Notify Avi the two copies are out of sync.

## Permission

Only Avi can set STOP. Agents NEVER write `STOP: true` except via the explicit `killswitch` skill.

## Resume protocol

Avi sets STOP back to `false` in either the local strategy.md or the Notion page. COO Sunday Synthesis syncs the two. Agents resume on their next scheduled run automatically.
