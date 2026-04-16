# CEO Briefing — NeetiQ Agent System
> This file is the CEO's direct channel to ALL agents. Updated during Cowork sessions with Avi.
> ALL agents MUST read this file at the start of EVERY run, right after strategy.md.
> Treat directives here as top priority. They override campaign briefs when there's a conflict.
> Last updated: 2026-04-05

---

## How This File Works

The CEO (this Cowork session) manages all agents as a unified organization. This file is how strategic decisions, competitive intel, and action items flow from the top down. Agents should:
1. Read this file at the start of every run
2. Check the "Active Directives" section for standing orders
3. Check "Intel Drops" for competitive/market intelligence gathered outside the agent system
4. Check "Agent-Specific Notes" for anything addressed directly to them
5. After acting on a time-bound directive, note it in agent_log.md

---

## NeetiQ Agent Org Chart

```
CEO (Cowork Sessions)
│
├── STRATEGY (Sunday)
│   ├── Product Direction Bot (CPO) — Sun 6AM
│   ├── GTM Strategy Bot (CMO) — Sun 6:30AM
│   └── Admin Agent (COO) — Sun 7AM
│
├── EXECUTION (Daily)
│   ├── Research Agent (Analyst) — Daily 8AM
│   ├── Post Publisher (Content) — Daily 9AM
│   └── Outreach Agent (BD) — Weekdays 11AM
│
├── INTELLIGENCE (Weekly)
│   ├── Competitor Intel — Wed 10AM
│   └── Grants Scout — Mon 7AM
│
└── REPORTING
    ├── Daily Digest Email — Daily 8AM
    └── Weekly Strategy Email — Sun 8AM
```

## Communication Channels

| Channel | File | Who Writes | Who Reads | Purpose |
|---------|------|-----------|-----------|---------|
| CEO Directives | brain/ceo_briefing.md (THIS FILE) | CEO | All agents | Top-down strategy, intel, action items |
| Weekly Ops | brain/strategy.md | Admin Agent | Execution layer | Phase, content plan, agent directives |
| Brand Truth | brain/brand_identity.md | Admin Agent | Content agents | Voice, positioning, writing rules |
| Product Truth | brain/product_inventory.md | CEO (via Avi) | Direction bots | What's actually built |
| Competitive Intel | brain/competitive_watchlist.md | CEO + Competitor Intel + GTM Bot | All agents | Single source of truth on competitors |
| Activity Reports | brain/agent_log.md | All agents | All agents + CEO | Rolling 7-day log of all activity |
| Strategy Briefs | direction-briefs/ | Direction bots | Admin Agent | Weekly research and recommendations |
| Content Pipeline | drafts/ → published/ | Research Agent → Post Publisher | Post Publisher | Draft → publish flow |
| Target Pipeline | outreach/targets/ | Research + Intel + CEO | Outreach Agent | Who to reach out to |

---

## Active Directives

### D1: Agent Log Rotation (Standing Order)
Every agent: when writing to agent_log.md, check the file size first. If the file is over 500 lines, do NOT add more content. Instead, note "LOG FULL — see previous entries" and continue your work. The CEO will archive old entries weekly.

### D2: Published Content Tracking (Post Publisher)
After every successful publish, create a file in `published/` with format: `YYYY-MM-DD_channel_slug.md` containing the exact text that was posted, the channel, the URL if available, and timestamp. This is our audit trail.

### D3: Competitive Watchlist Updates (Competitor Intel + Research Agent)
When you discover a new competitor or significant competitor move, update `brain/competitive_watchlist.md` in addition to your regular outputs. The watchlist is the single source of truth — don't just mention competitors in your research files and hope someone notices.

### D4: Phase Check Before All Content
Every content-producing agent (Research, Post Publisher): before creating or publishing ANY content, read strategy.md and confirm the current phase. State the phase explicitly in your agent_log entry. If you're unsure about the phase, do NOT publish. Flag it in agent_log.md and wait.

### D5: No Duplicate Log Entries
If your run results in NO action taken (nothing published, no outreach sent, no new research), write a ONE-LINE entry to agent_log.md: "[Date] — [Agent Name] — No action. [One sentence reason]." Do NOT write multi-paragraph entries about doing nothing.

### D6: DPDP Command Center — Positioning Rules (NEW, Apr 5)
Avi built the DPDP Compliance Command Center for ContraRed. ALL agents MUST read `brain/dpdp_command_center_gtm.md` before any DPDP-related content, outreach, or strategy work. Key rules:
- **Phase 1-2:** DPDP urgency stats are OK (problem awareness). NO product names. NO feature descriptions.
- **Phase 3+:** Can name ContraRed and show DPDP scanning. Lead with contract scanning gap (nobody else does it).
- **NEVER publish the technical feature sheet** (5 agents, 22 endpoints, etc.). Internal only.
- **Lead with:** "Scan your contracts against 18 DPDP rules. Find gaps. Fix them in minutes."
- **Do NOT lead with:** Rights management, grievance handling, gap assessment questionnaire, penalty tracking.
- **Do NOT position against consent management tools.** They're adjacent, not competitive.
- Full GTM playbook, segment priorities, pricing guidance, and outreach rules are in the file.

### D7: Balanced Content — No DPDP Overweight (NEW, Apr 11)
CEO directive: We overcorrected toward DPDP after building the Command Center. NeetiQ is a two-product company built over 2 years. DPDP is a timely wedge, not the identity. ALL content-producing agents MUST follow this mix:
- **~1/3 Contract Intelligence pain** (ContraRed territory): 2-3 hour manual reviews, inconsistency across associates, no audit trails, playbook gaps. The problems ContraRed was built to solve BEFORE DPDP existed.
- **~1/3 Legal Research pain** (Smriti territory): lawyers researching on Google, hallucination crisis, case law chaos, 50M+ pending cases, zero reliable Indian legal AI. The problems Smriti solves.
- **~1/3 Regulatory/DPDP urgency**: Compliance gaps, enforcement timelines, penalties. Still important but ONE-THIRD, not two-thirds.
- **Outreach segments must also rebalance.** Don't ONLY target DPOs. Litigation associates, legal ops heads, corporate counsel dealing with contract volume are equally important.
- **Research Agent:** Produce drafts across ALL THREE pillars, not just DPDP. We need contract review pain drafts and legal research pain drafts.

### D8: India-First Content Targeting (NEW, Apr 11)
CEO directive: LinkedIn insights show 34% of post views are from US metros, only 5.4% from Delhi. We need India as the base audience, US as bonus.
- **Every post MUST include at least one India-specific anchor:** Indian court name, Indian statute, Indian company, Indian price point, MeitY, BCI, DPDP by name, "55 million pending cases in Indian courts." Make it impossible for LinkedIn's algorithm to ignore the India relevance.
- **Outreach connections should be 80%+ India-based.** DPOs at Indian fintechs, in-house counsel at Indian companies, Indian law firm associates.
- **Do NOT write "global legal tech thought leadership."** Write as someone building for the Indian legal market specifically. US audience will still engage if the content is good, but the primary pull should be India.
- **Hashtags:** Add #IndiaLegalTech, #IndianLaw, #DPDP alongside #LegalTech and #AI. India-specific tags help the algorithm.

---

## Intel Drops

### 2026-04-11: LinkedIn Audience Skew (CEO Analysis)
Source: Avi's LinkedIn post insights (Apr 11)

Post views by geography: NYC 11.9%, SF Bay 8.7%, LA 7.2%, Delhi 5.4%, Chicago area. DMs are mostly about DPDP, very few about legal research or contract review.

**Assessment:** Content is reaching US legal tech community but not the Indian ICP. Two causes: (1) content framing is too "global thought leadership" without India anchors, (2) DPDP overweight is attracting only compliance/DPO audience while ignoring contract review and litigation research audiences that are Smriti and ContraRed's core users.

**Action:** Directives D7 (balanced content) and D8 (India-first targeting) issued. All agents must rebalance immediately.


### 2026-04-03: Avish Sharma / Prodigy Legal (CRITICAL)
Source: Avi's debut LinkedIn post comment + CEO analysis

Avish Sharma is the founder of Prodigy Legal and GenLaw. He commented on Avi's debut post offering to "explore possibilities." Key facts:
- **8.5M+ Indian judgments indexed** (vs Smriti's 3K currently)
- **20+ years legal experience** as a practicing lawyer
- **Building BOTH sides**: GenLaw (research/litigation, like Smriti) + practice management (contracts, like ContraRed)
- **His UI looks AI-generated** — suggests the AI agents behind it may be less advanced
- **He's a senior in the space** — treat with respect, not as a junior competitor
- **Connection request sent** — Avi needs to reply to his comment manually

**Strategic assessment**: He is NOT just a research tool. He's building an OS competitor covering contracts + litigation, same as NeetiQ. Our moat is NOT broader coverage (he has that too). Our moat is DEEPER AI TECH — zero hallucination architecture, jurisdiction-native kernel, source-traced everything. His scale advantage (8.5M judgments) is real but our architectural advantage (zero hallucination by design) is harder to replicate.

**For Outreach Agent**: Avish is a peer, not a lead. Treat as "potential strategic relationship." Don't pitch. Be curious about his work.
**For Competitor Intel**: Add Prodigy Legal / GenLaw to competitive_watchlist.md. Monitor closely.
**For Research Agent**: When researching Indian legal AI, include Prodigy Legal in scans.

### 2026-04-03: Nyayanidhi — New Funded Competitor (CRITICAL)
Source: GTM Strategy Bot brief, Apr 1

Nyayanidhi (Bengaluru) raised $2M seed from 3one4 Capital. Building a "Litigation OS" for India with High Court pilots already running. This is the first FUNDED direct competitor to Smriti in India.

**For Competitor Intel**: Track Nyayanidhi as Tier 1 India competitor. Research their team, product, and customers.
**For GTM Bot**: Factor Nyayanidhi into competitive landscape.
**For Outreach Agent**: ~~Find Nyayanidhi founder on LinkedIn.~~ DONE (2026-04-04): "Pratik Pany" NOT FOUND on LinkedIn. Actual Nyayanidhi founders are **Adithya LHS** and **Chakshu Masag...** (from company People tab). Research Agent should verify full names and find their LinkedIn profiles.

### 2026-04-03: Google Cloud Credits Applied ($2K)
Applied to Google for Startups Cloud Program. $2,000 USD credits. Decision expected by April 10. Tracked in Notion VC & Funding Pipeline.

### 2026-04-03: Grants Scout Findings — Urgent Deadlines
- Google for Startups Accelerator: AI First India — deadline April 19 (requires incorporation)
- NIDHI-EIR Programme — no company needed, monthly stipend
- Youth Co:Lab Innovation Challenge — UNDP seed grant, no company needed
- Microsoft for Startups Founders Hub — up to $150K Azure credits, no registration

---

## Agent-Specific Notes

### To Admin Agent (next run: Sun Apr 5)
This is your first run with the new organizational structure. Key things for this run:
1. Read this entire ceo_briefing.md first
2. Read the Product Direction brief (brief_2026-04-06.md) and GTM brief (brief_2026-04-01-v2.md)
3. Assess Week 1 engagement data from LinkedIn (check metrics via Chrome)
4. Decide: stay in Phase 1 or advance to Phase 2? Criteria: 50+ new connections, genuine engagement, people asking "what are you building?"
5. Write Week 2 campaign brief with specific posts, channels, and dates
6. Archive agent_log.md entries older than 7 days (move to brain/agent_log_archive.md)
7. Update competitive_watchlist.md if direction briefs contain new competitor info

### To Post Publisher
1. After EVERY publish: save the exact posted text to published/ folder (see Directive D2)
2. Week 2 is NOW APPROVED. Publish per the campaign brief `campaigns/week_2026-04-13.md`.
3. **NEW: Read `brain/dpdp_command_center_gtm.md` before any DPDP content.** DPDP stats OK for Phase 1-2. No product names until Phase 3. Never publish the technical feature sheet.

### To Outreach Agent
1. Avish Sharma connection accepted. Peer message sent. Monitor for reply. Do NOT pitch.
2. ~~Find the Nyayanidhi founder~~ COMPLETED 2026-04-04: "Pratik Pany" does not exist. Actual founders: Adithya LHS, Chakshu Masagali. Research Agent needs to find their full names and LinkedIn URLs.
3. Rujhan Soni (Qdesq) is an ICP match sharing real pain points. Nurture carefully. Do NOT pitch ContraRed yet (Phase 1). **He is pilot customer #1 for DPDP scanning when Phase 3 hits.**
4. **NEW: Read `brain/dpdp_command_center_gtm.md` for DPDP outreach rules.** Phase 1-2: ask about DPDP challenges, don't mention ContraRed. Phase 3+: offer free DPDP contract audit.

### To Competitor Intel (next run: Wed Apr 8)
1. READ competitive_watchlist.md FIRST. It's the new source of truth.
2. Your primary mission this week: deep dive on Nyayanidhi (team, product, funding, customers, HC pilots)
3. Secondary: check Avish Sharma / Prodigy Legal / GenLaw product updates
4. UPDATE competitive_watchlist.md with findings (don't just dump in research files)

### To Grants Scout (next run: Mon Apr 7)
1. Check if Google Cloud credits decision came through (expected by Apr 10)
2. Prioritize verifying Microsoft for Startups Founders Hub — Avi should apply this week
3. Check NIDHI-EIR incubator associations in Delhi (IIT Delhi, NSRCEL, etc.)
