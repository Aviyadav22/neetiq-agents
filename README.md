# NeetiQ Autopilot v2

Claude-native port of the NeetiQ marketing + strategy system. Replaces the v1 Hermes/OpenClaw blueprint with 4 logical agents running on Cloud Routines, Cowork on Windows, and Claude in Chrome.

**Status:** v2 scaffolded. Scheduled tasks cut over from v1. Notion brain mirror created. Avi has manual steps to complete before the system is fully live. See `docs/MANUAL_SETUP_CHECKLIST.md`.

## The 4 agents (+ Analytics)

| Agent | When | Where | What |
|-------|------|-------|------|
| COO | Sun 6 AM + weekdays 8:30 AM + 6 PM | Cloud Routine (or Cowork) | Weekly synthesis, morning brief, evening retro |
| INTEL | Weekdays 8 AM + Wed 10 AM | Cloud Routine | Competitor scan + deep dive, writes to watchlist |
| MAKER | Sun 7 AM + on-demand via Dispatch | Cowork (Windows) | Drafts 3 posts/week, runs voice audit, pushes for approval |
| CONNECT | Weekdays 11 AM | Claude in Chrome | 11-stage outreach pipeline, hard-capped, human-in-loop |
| ANALYTICS | Fri 6 PM | Cloud Routine | Weekly report, Healthchecks ping, Dispatch summary |

## Folder layout

```
Version 2 agents/
├── CLAUDE.md                  # Governance, read on every run
├── README.md                  # This file
├── brain/                     # Local source of truth (versioned)
│   ├── strategy.md            # Current phase, STOP toggle, weekly ops
│   ├── brand_identity.md      # Voice, positioning, banned patterns
│   ├── product_inventory.md   # What's actually built
│   ├── ceo_briefing.md        # Directives from Avi
│   ├── USER.md                # Avi's preferences, decisions, style (Honcho replacement)
│   ├── competitive_watchlist.md
│   ├── agent_log.md           # Rolling 7-day log (Notion DB is canonical)
│   └── published_posts.md     # Index of everything published
├── agents/
│   ├── coo/{sunday_synthesis,morning_brief,evening_summary}.md
│   ├── intel/{daily_scan,wednesday_deep_dive}.md
│   ├── maker/{weekly_calendar,on_demand_draft}.md
│   ├── connect/{chrome_playbook,11_stage_pipeline}.md
│   └── analytics/weekly_report.md
├── .claude/skills/
│   ├── content-voice-audit/   # 109 banned words + 36 structural patterns
│   ├── phase-check/           # Reads strategy.current_phase, blocks if wrong phase
│   ├── stop-check/            # Reads strategy.STOP, aborts if true
│   └── killswitch/            # Triggered by "killswitch" from Dispatch
├── infra/
│   ├── github-actions/intel-feed.yml  # RSS poller for competitor blogs
│   └── healthchecks/README.md         # External watchdog setup
├── docs/
│   ├── MANUAL_SETUP_CHECKLIST.md      # What Avi must do himself
│   ├── MIGRATION_FROM_V1.md           # What carried over, what didn't
│   ├── NOTION_SETUP.md                # Page IDs, DB schemas
│   ├── DISPATCH_SETUP.md              # Pair mobile Claude to Windows
│   └── CHROME_PROFILE_SETUP.md        # Dedicated Claude-in-Chrome profile
└── outputs/
    ├── drafts/                # MAKER's output, awaiting approval
    ├── intel-feed/            # GitHub Actions writes here (RSS snapshots)
    └── logs/                  # Per-run trace logs
```

## How it reads on a typical day

```
Mon 8:00  INTEL Cloud Routine fires → reads intel-feed/ + Notion watchlist →
          writes new insights to watchlist → pings COO
Mon 8:30  COO Morning Brief fires → reads overnight INTEL, pending MAKER drafts,
          yesterday's published → pushes ≤10-line summary to Avi's phone
Mon 11:00 CONNECT session opens in Claude in Chrome → Avi approves pipeline →
          5 conn req + up to 15 DMs, 45–120s delays → updates outreach_pipeline
Mon 18:00 COO Evening Summary → retrospective, tees up tomorrow
Wed 10:00 INTEL Wednesday Deep Dive → full comp matrix, grants, NCR events
Fri 18:00 ANALYTICS → weekly report, Healthchecks ping, email to Avi
Sun 6:00  COO Sunday Synthesis → reads everything, writes new strategy.md,
          sets next week's MAKER calendar
Sun 7:00  MAKER Weekly Calendar → drafts 3 posts for the week, voice-audits
          each, Dispatch notification to Avi for approval
```

## Cost ceiling

- Claude Max 20x — $200/mo (all agent execution)
- Extra usage cap — $0–50/mo (only if weekly limits hit; cap hard in Settings → Usage)
- LiGo or equivalent LinkedIn MCP — $19/mo (optional, for API posting)
- Everything else free tier
- **Total ceiling: ~$269/mo**, well inside Avi's $250 comfort band with a little spillover if enabled.

## What v2 gives up from v1

- 10-agent hierarchy with CPO-S / CTO-S supervisors — collapsed to 4 agents
- Honcho dream cycles — replaced with `brain/USER.md` manual update pattern
- Self-hosted Mem0 + Obsidian — replaced with Claude Memory + Notion
- Playwright + residential proxy — replaced with Claude in Chrome
- VPS + systemd + Xvfb — replaced with Cloud Routines (no machine needed)
- "STOP ALL" single-command kill — replaced with killswitch skill triggered from Dispatch

See `docs/MIGRATION_FROM_V1.md` for the full delta.

## Start here

1. Open `docs/MANUAL_SETUP_CHECKLIST.md` — it lists the 8 things only Avi can do (pair Dispatch, install Chrome extension, set Extra usage cap, confirm Notion pages, etc.).
2. Read `CLAUDE.md` once. That's the contract every agent operates under.
3. Read `brain/strategy.md` — it's the live state of the business.
