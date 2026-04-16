# Manual Setup — Things Only Avi Can Do

I've done everything I can do from Cowork. The following items require your hands on the keyboard / phone / browser. Do them in order. Each has a "you'll know it's done when" test.

## 1. Pair Dispatch (mobile Claude ↔ Windows Desktop)

**Why:** This is how you run MAKER / CONNECT / ad-hoc agent work from your phone without being at your desk.

1. Open Claude Desktop on Windows. Left sidebar → Dispatch → "Pair mobile".
2. On your iOS/Android Claude app: tap profile → Dispatch → scan QR.
3. Test from phone: "list files in Version 2 agents/". Watch the Windows Desktop run it.
4. Enable "Keep computer awake" toggle in Cowork settings.

**Done when:** a command sent from your phone shows up executing on your Windows machine.

## 2. Install Claude in Chrome — dedicated profile

**Why:** CONNECT agent drives LinkedIn through your real Chrome session. LinkedIn sees a normal user. No Playwright artifacts, no headless detection. Using a dedicated profile means NeetiQ automation never touches your banking / Gmail / personal logins.

1. Chrome → profile menu (top right) → Add → name it "NeetiQ Autopilot". Pick a distinct avatar color.
2. In the new profile, install Claude for Chrome extension.
3. Log into LinkedIn (your personal account) in this profile ONLY.
4. Do NOT log into email, banking, Twitter, GitHub, or personal services in this profile.

**Done when:** you have a Chrome profile labeled "NeetiQ Autopilot" that has LinkedIn logged in and nothing else sensitive.

## 3. Cap Extra Usage at $50/mo

**Why:** Weekly cap on Max 20x will bite if MAKER + INTEL + Claude Code sessions on Smriti/ContraRed all fire the same week. Extra usage converts to API rates automatically. Cap it or surprises happen.

1. claude.ai/settings/usage → Extra usage → Adjust limit.
2. Set to $50/mo. Save.

**Done when:** your settings page shows "Extra usage cap: $50/month".

## 4. Confirm Notion brain pages

**Why:** I created the brain mirror in your Notion workspace during this session. Verify they're where they should be.

Open Notion → search "NeetiQ Autopilot v2". You should see:
- Page: NeetiQ Autopilot v2 (parent)
  - Sub-page: strategy
  - Sub-page: brand_identity
  - Sub-page: product_inventory
  - Sub-page: ceo_briefing
  - Sub-page: USER
  - Database: competitive_watchlist
  - Database: outreach_pipeline
  - Database: agent_log
  - Database: published_posts

Each brain page has a "Last synced from local" timestamp in the first paragraph.

**Done when:** all 5 pages + 4 databases exist and are viewable on your phone via the Notion app.

## 5. Create private GitHub repo `neetiq-agents`

**Why:** Cloud Routines need a repo to mount. Also holds the intel-feed workflow (step 6).

1. github.com/new → Private → name: `neetiq-agents` → create.
2. Clone locally. Copy contents of `Version 2 agents/` into the repo root.
3. Commit + push.

**Done when:** `gh repo view yourusername/neetiq-agents` shows the repo.

## 6. Deploy intel-feed GitHub Action

**Why:** Polls Harvey + Jhana + Lexlegis blog RSS daily. Commits new entries to `outputs/intel-feed/` so INTEL Routine can react on-push.

1. Copy `infra/github-actions/intel-feed.yml` to `.github/workflows/intel-feed.yml` in the neetiq-agents repo.
2. Push. Actions tab should show the workflow.
3. Trigger manually once (Actions → intel-feed → Run workflow) to seed the feed.

**Done when:** `outputs/intel-feed/` has at least one JSON file committed by github-actions[bot].

## 7. Create 4 Claude Code Routines

**Why:** COO morning/evening, COO Sunday, INTEL daily, INTEL Wednesday, ANALYTICS Friday. These run in Anthropic's cloud, machine-off-OK.

For each, go to claude.ai/code/routines → New routine. Use the prompts from `agents/coo/`, `agents/intel/`, `agents/analytics/`. Set schedule per the table in `README.md`. Connect the `neetiq-agents` repo. Enable Notion + Gmail MCP connectors. Set model: Sonnet 4.6 (fall back to Haiku 4.5 for INTEL extraction per model policy in CLAUDE.md).

Cowork MAKER and CONNECT stay on your Windows machine (scheduled-tasks system already updated — see step 8).

**Done when:** `claude.ai/code/routines` lists 5 routines, all enabled.

## 8. Verify the cutover happened

I disabled all 11 v1 scheduled tasks and registered the v2 ones. Sanity check:

```
In Claude Desktop, open the Scheduled Tasks sidebar.
- v1 tasks (neetiq-daily-research, neetiq-post-publisher, neetiq-competitor-intel,
  neetiq-admin-agent, neetiq-outreach-agent, neetiq-product-market-direction,
  neetiq-gtm-outreach-direction, neetiq-daily-digest-email,
  neetiq-weekly-strategy-email, neetiq-grants-scout, neetiq-weekly-analytics):
  all show as disabled.
- v2 tasks (neetiq-v2-coo-sunday, neetiq-v2-coo-morning, neetiq-v2-coo-evening,
  neetiq-v2-maker-weekly, neetiq-v2-connect-daily-prompt,
  neetiq-v2-analytics-weekly, neetiq-v2-intel-daily, neetiq-v2-intel-wed):
  all show as enabled with next-run timestamps.
```

**Done when:** v1 rows are greyed out / disabled, v2 rows are green / enabled.

## 9. Healthchecks.io external watchdog (optional, recommended)

**Why:** If Cloud Routines silently fail to ping, Anthropic doesn't wake you up. Healthchecks does.

1. healthchecks.io → sign up (free tier) → create check "neetiq-coo-morning" → grace 35 min.
2. Copy the ping URL (`https://hc-ping.com/<uuid>`).
3. Edit `agents/coo/morning_brief.md` — replace `HEALTHCHECKS_URL_HERE` with your URL.
4. Add phone number to your Healthchecks account for SMS on missed pings.

**Done when:** you SMS-trigger a test ping and receive "[healthchecks.io] Test Notification" on your phone.

## 10. First live run

Don't wait for the schedule. Manually trigger:
1. COO Sunday Synthesis (preview what Sunday will do)
2. MAKER weekly calendar (see what it produces)
3. Review the drafts it pushes to Dispatch

If the drafts are AI-sounding or off-phase, tell me what needs fixing and I'll tune the skills.

---

**If something here is confusing, paste this doc into Claude and ask "what am I missing on step N?"**
