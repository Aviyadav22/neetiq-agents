# CONNECT — Claude in Chrome Playbook

**Schedule:** Weekdays 11:00 IST (human-in-loop; scheduled task pings Avi with a prompt, then Avi runs the session in Claude in Chrome)
**Surface:** Claude for Chrome extension, dedicated "NeetiQ Autopilot" Chrome profile
**Duration:** 30 min max per session
**Hard caps (do not exceed, ever):**
- 5 connection requests / day
- 15 messages / day
- 40 total actions / day (connections + messages + comments + profile views)
- 45–120s randomized delay between any two actions

## Pre-session (Avi runs this as the first Claude in Chrome prompt)

```
Read Version 2 agents/brain/strategy.md first. Check STOP and current_phase.
Then read Version 2 agents/agents/connect/11_stage_pipeline.md for stage definitions.
Then read Notion > NeetiQ Autopilot v2 > outreach_pipeline for today's prospect queue.
Tell me: (1) how many are in each stage, (2) which 5–10 are highest-priority this session, (3) today's stage focus (connection requests / DMs / follow-ups / replies).
```

## Session flow

### 1. Concurrent-session guard
Before opening LinkedIn, check Notion `agent_log` for any row in the last 10 minutes with `source=linkedin`. If present, abort. "MAKER might be posting right now."

### 2. Announce intent
Tell Avi what this session will do in ≤5 lines:
```
Session plan: 3 connection requests (DPDP segment), 5 follow-up DMs (contract review segment), review 2 replies received. 
Est duration: 18 min. 
Est actions: 10. Safe under 40/day cap.
Stop me anytime — "STOP", "PAUSE", "SKIP THIS ONE".
```

### 3. Execute one prospect at a time
For each prospect:
1. Open their profile (tab or nav, not both).
2. Read their last 3 posts / recent activity.
3. Craft a message referencing something specific (not "I saw your profile").
4. Show the message to Avi for approval before sending (ALWAYS, every action).
5. On approval, perform the action (connect request with note / DM / comment).
6. Wait randomized 45–120s before next action.
7. Update Notion `outreach_pipeline` row: stage, last_touched, notes.
8. Log to `brain/agent_log.md` after each action: `HH:MM | CONNECT | <action> | <prospect-first-name> | <stage>`.

### 4. Session close
- Summarize actions taken vs plan.
- Update session total in `brain/agent_log.md`:
  ```
  YYYY-MM-DD 11:45 | CONNECT | sonnet-4.6 | <phase> | linkedin session closed | OK | N actions, <breakdown>
  ```
- If ANY reply arrived during the session, flag it in a final Dispatch push.

## Prospect prioritization

Today's 5–10 picks = top of this ordering:
1. Active conversations (stage 4–9) awaiting a response from Avi
2. New connections (stage 2) accepted in last 48 hours, ready for first DM
3. Warm intros from existing prospects (stage 3) not yet messaged
4. Cold prospects at stage 1 for this day's segment focus
5. Lapsed conversations (last_touched > 7 days in stage 4–7) — revive message

**NEVER message these people via CONNECT (handled by Avi):**
- Siddhant M Sharma (TRION LAW)
- Apoorv Sharma (college friend)
- Anyone flagged "AVI-MANAGED" in Notion `outreach_pipeline`

## Segment focus by day

| Day | Segment | Pillar |
|-----|---------|--------|
| Mon | DPOs / compliance heads at Indian fintechs | DPDP |
| Tue | Litigation associates / legal ops, Indian mid-size firms | Research |
| Wed | In-house counsel at Indian companies with contract volume | Contract |
| Thu | Reply handling + active conversation progression | ALL |
| Fri | Warm intro asks + week-end nudges on pending replies | ALL |

Rotate the Monday focus every 3 weeks to avoid overfishing.

## Message templates (phase-aware)

See `brain/strategy.md` "To Outreach Agent" section for the current week's message framing. Use that verbatim as the scaffold, personalize per prospect.

Phase 1–2: "I've been building something to fix this" / problem-aware curiosity. NO product names.

Phase 3+: Can name ContraRed + Smriti. Can offer 30-day pilot. Can offer free DPDP contract audit.

## Response handling

If a prospect replies during the session:
1. Read the reply.
2. Classify: positive (asking more) / neutral (ack) / negative (no thanks) / ambiguous.
3. For positive replies, draft a follow-up but DO NOT send — push to Avi via the session for his review ("Here's what I'd reply, OK?").
4. For neutral, ack-and-close.
5. For negative, update pipeline stage to "Declined" and move on. No further messages.
6. For ambiguous, flag for Avi to handle personally.

## Failure modes

- LinkedIn shows CAPTCHA: stop the session immediately. Do not retry. Flag Avi.
- "You've reached the weekly invitation limit": stop connection requests for the week. DMs still OK if under message cap.
- Profile not found: skip and log.
- Account flag warning ("unusual activity"): stop session, trigger killswitch for CONNECT only, flag Avi.

## Rules

- Every single action requires Avi's in-session approval. Never send unreviewed.
- Dignity-first messaging. If the personalization feels generic, rewrite before asking Avi.
- Hard caps are ceiling, not target. Aim for 3/3/3 on a typical day (3 conns + 3 DMs + 3 replies).
- Delays are non-negotiable. 45–120s randomized. Don't batch.
- "Once in the DM, always in the DM" — don't parallel-message someone on Instagram, X, or email after starting a LinkedIn thread, unless Avi directs.
