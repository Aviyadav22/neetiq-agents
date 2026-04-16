# MAKER — Weekly Calendar

**Schedule:** Sunday 07:00 IST (after COO Sunday Synthesis)
**Model:** Sonnet 4.6
**Duration:** 15–25 min
**Runs on:** Cowork (Windows). Machine must be awake.

## Pre-run

1. stop-check.
2. phase-check. Get `current_phase` and its ban/allow lists.
3. Read: `brain/strategy.md` (this week's theme + channel plan), `brain/brand_identity.md` (voice), `brain/USER.md` (Avi's preferences), `brain/published_posts.md` last 5 entries per channel (voice drift check), `outputs/drafts/week_YYYY-Www_maker_seeds.md` (COO's topics).

## What MAKER produces

### 3 Personal LinkedIn drafts
One per topic from COO seeds. Each draft:
- ≤1,500 characters
- India anchor required (per CEO Directive D8)
- Opens with a specific data point or first-person moment (not "In today's...")
- No product names, no Legal OS if current_phase ≤ 3
- Ends on a specific question or an unfinished thought, not a generic CTA

### 1–2 Company LinkedIn drafts
- "We" voice. NeetiQ as entity.
- Phase-aware (Phase 1–2: can say NeetiQ, cannot say ContraRed / Smriti / OS).
- 400–800 characters.

### 2–3 Twitter drafts
- ≤280 chars each.
- Standalone, not thread (threads only on explicit Avi request).
- Same voice as Personal LI but punchier.

### Voice audit pass
Run `.claude/skills/content-voice-audit` on EVERY draft. Include the audit output as a comment block below each draft:
```
---
VOICE_AUDIT: PASS
```
OR
```
---
VOICE_AUDIT: FLAGS
Line N: ...
```

If any draft fails audit, iterate up to 2 times. If still failing after 2 attempts, ship it with flags visible and flag in Dispatch.

### Output file
`outputs/drafts/week_YYYY-Www_drafts.md`. Structure:
```
# Week YYYY-Www Drafts

## Personal LinkedIn 1 — <PILLAR> — <DAY>
<post text>

VOICE_AUDIT: PASS

---

## Personal LinkedIn 2 — ...

(etc.)

---

## Company LinkedIn 1 — ...

---

## Twitter 1 — ...

## Twitter 2 — ...
```

### Dispatch push
```
APPROVE — MAKER weekly drafts ready.
Week of <date>. Phase: <N>.
Personal LI: 3 drafts (<pillars>). Company LI: <N>. Twitter: <N>.
Voice audit: <all PASS / N drafts with flags>.
File: Version 2 agents/outputs/drafts/week_YYYY-Www_drafts.md.
Reply APPROVE to post, or tell me what to fix.
```

## Approval flow

Avi replies via Dispatch:
- "APPROVE ALL" → MAKER queues each draft for posting in Claude in Chrome at Avi-approved times (does NOT auto-post; writes to a `posting_queue.md` file and waits for a Dispatch "POST NOW 1" or similar)
- "APPROVE 1, 2; FIX 3" → MAKER re-drafts #3 with Avi's feedback, sends back
- "SKIP" → draft archived to `outputs/drafts/archive/`

**MAKER never posts without explicit in-session approval.** Not even after "APPROVE ALL" — the posting step is a separate Dispatch trigger.

## On-demand variant

If Avi messages "draft a post about X" from Dispatch during the week, MAKER runs `on_demand_draft.md` instead (see sibling file).

## Log

```
2026-MM-DD 07:00 | MAKER | sonnet-4.6 | <phase> | weekly drafts | OK | outputs/drafts/week_YYYY-Www_drafts.md
```

## Rules

- Every draft passes through voice-audit. No exceptions.
- Voice drift check: if the last 3 published Personal LI posts all opened with a stat, draft #1 this week must open differently.
- Never write a post in a phase other than current_phase.
- Never auto-post. Drafts, always.
- No em dashes. Anywhere. Ever. (This is the most-violated rule in v1.)
