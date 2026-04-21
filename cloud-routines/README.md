# Cloud Routine prompts — paste-ready

Cloud Routines (claude.ai-hosted scheduled prompts) can't read Avi's local
filesystem. So each routine needs a self-contained prompt that:

1. References Notion pages by name (Strategy, USER, CEO Briefing, etc.)
2. Uses Notion MCP to read/write instead of local files
3. Has the Healthchecks ping URL embedded
4. Sends a Dispatch push as the user-facing channel

The source-of-truth playbook for each agent is still the markdown file in
`agents/<agent>/<file>.md`. This folder is the Cloud Routine mirror,
condensed to fit a prompt textarea.

## The 7 Cloud Routines Avi manages at claude.ai

| Routine name (claude.ai)     | Paste from file              | Cron (Asia/Kolkata) |
|------------------------------|------------------------------|---------------------|
| NeetiQ — COO Sunday          | coo_sunday.md                | `0 6 * * 0`         |
| NeetiQ — COO Morning         | coo_morning.md               | `30 8 * * 1-5`      |
| NeetiQ — COO Evening         | coo_evening.md               | `0 18 * * 1-5`      |
| NeetiQ — INTEL Daily (wkdy)  | intel_daily.md               | `0 8 * * 1-5`       |
| NeetiQ — INTEL Saturday      | intel_saturday.md            | `0 10 * * 6`        |
| NeetiQ — INTEL Wed Deep Dive | intel_wed.md                 | `0 10 * * 3`        |
| NeetiQ — ANALYTICS Weekly    | analytics_weekly.md          | `0 18 * * 5`        |

## Tools each routine needs enabled at claude.ai

All 7: Notion connector, Gmail connector (for a couple), WebFetch (for
Healthchecks pings). No Bash needed — routines ping via WebFetch.

## Updating later

When a playbook changes here, regenerate the matching paste file below,
then re-paste into claude.ai. Do NOT edit the paste files in place hoping
the routine picks it up — the routine only sees what's pasted into its
prompt textarea.
