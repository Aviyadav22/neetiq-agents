# Migration from v1 → v2

## TL;DR

v1 (10 specialized agents, 11 scheduled tasks, flat scripts) → v2 (4 logical agents + ANALYTICS, Claude-native skills, brain mirrored in Notion + local md, human-in-loop for every outbound action).

Brain content is preserved verbatim. Scheduling and orchestration change.

## What changed

| Concern | v1 | v2 |
|---|---|---|
| Agent count | 10 role-specific bots | 4 logical agents + ANALYTICS |
| Orchestration | 11 scheduled Cowork tasks + manual prompts | 5 Cloud Routines + 3 Cowork tasks + skills + Dispatch approvals |
| Brain location | `marketing-autopilot/brain/*.md` only | Notion pages + `Version 2 agents/brain/*.md` (mirror) |
| Voice audit | Inline checks in agent prompts | `content-voice-audit` skill (109 banned words + 36 patterns) |
| Phase awareness | Read `strategy.md` every run | `phase-check` skill wraps the logic |
| Kill switch | Manual edit to brain files | `STOP: true` in strategy.md + Notion mirror + `killswitch` skill |
| Outreach automation | Queue-based, implied batch | Human-in-loop for EVERY action, 45–120s randomized delays, 5 conn/day hard cap |
| Intel gathering | Ad-hoc prompts per session | GitHub Actions polls RSS/pages daily, Claude reads output |
| Monitoring | None | Healthchecks.io pings per agent run |
| Posting | Auto-post via scheduled tasks | Drafts always; posting is a separate Dispatch trigger |

## What's unchanged (ported verbatim)

- `brain/brand_identity.md` — voice doctrine, banned words, ladder.
- `brain/product_inventory.md` — ContraRed + Smriti + DPDP Command Center specifics.
- `brain/competitive_watchlist.md` — Harvey, Jhana, Leegality, etc.
- `brain/ceo_briefing.md` — standing directives (D1–D10).
- `brain/dpdp_command_center_gtm.md` — April rollout GTM.
- `brain/strategy.md` — every week's plan (added STOP/phase fenced block at top; rest unchanged).

## What's new

- `brain/USER.md` — Avi's profile, working style, do-not-message list, banned phrases. Honcho replacement.
- `brain/agent_log.md` — single rolling log for all agents.
- `brain/published_posts.md` — voice-drift reference.
- `.claude/skills/{content-voice-audit, phase-check, stop-check, killswitch}` — reusable verbs.
- 4-agent prompt packages under `agents/{coo,intel,maker,connect,analytics}/`.
- `infra/github-actions/intel-feed.yml` + `poll.py` — external scraper.
- `infra/healthchecks/README.md` — watchdog setup.

## Scheduled task cutover

v1 tasks to **disable** (not delete — keep history):

```
neetiq-product-direction        Sun 06:00 IST
neetiq-gtm-strategy             Sun 06:30 IST
neetiq-admin-agent              Sun 07:00 IST
neetiq-research-daily           Weekdays 08:00 IST
neetiq-post-morning             Weekdays 09:00 IST
neetiq-post-lunch               Weekdays 13:00 IST
neetiq-post-evening             Weekdays 17:00 IST
neetiq-competitor-intel         Wed 10:00 IST
neetiq-outreach                 Weekdays 11:00 IST
neetiq-dpdp-gtm-check           Daily 19:00 IST
neetiq-weekly-review            Fri 18:00 IST
```

v2 tasks to **create**:

```
neetiq-v2-coo-sunday            Sun 06:00 IST   (COO Sunday Synthesis)
neetiq-v2-coo-morning           Weekdays 08:30  (COO Morning Brief)
neetiq-v2-coo-evening           Weekdays 18:00  (COO Evening Summary)
neetiq-v2-intel-daily           Mon–Fri 08:00 + Sat 10:00 (INTEL Daily Scan)
neetiq-v2-intel-wed             Wed 10:00       (INTEL Wednesday Deep Dive)
neetiq-v2-maker-weekly          Sun 07:00       (MAKER Weekly Calendar)
neetiq-v2-connect-daily-prompt  Weekdays 11:00  (prompts Avi to run CONNECT in Chrome)
neetiq-v2-analytics-weekly      Fri 18:00       (ANALYTICS Weekly Report)
```

The five Cloud Routines (COO morning/sunday/evening, INTEL daily/wed, ANALYTICS weekly) are ALSO scheduled as Cowork tasks as a cheap backup — if the Cloud Routine fails or the feature's unavailable, the local task catches it. MAKER + CONNECT only live in Cowork because they need the Windows machine + Chrome profile.

## What to tell Avi

1. Old tasks paused, not deleted — their logs stay in place for reference.
2. Nothing auto-posts in v2. Every outbound action needs Avi's APPROVE in Dispatch.
3. First live run is COO Morning Brief tomorrow 08:30 IST.
4. If anything feels wrong, reply `STOP` in Dispatch → killswitch kicks in → all agents idle.

## Rollback

```
1. Re-enable all 11 v1 tasks via mcp__scheduled-tasks__update_scheduled_task (enabled: true).
2. Disable the 8 v2 tasks (enabled: false).
3. Edit Version 2 agents/brain/strategy.md → set STOP: true.
4. Nothing in v1 reads from v2 files, so there is no data cleanup.
```

v1 folder stays untouched at `marketing-autopilot/`. Nothing is deleted.
