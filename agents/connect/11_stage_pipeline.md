# CONNECT — 11-Stage Outreach Pipeline

Ported from the Hermes blueprint. Used by CONNECT and reflected in the Notion `outreach_pipeline` DB.

## Stages

| # | Stage | Action | Next action | Stuck if |
|---|-------|--------|-------------|----------|
| 1 | Identified | Added to DB with profile URL, segment, personality tag | Review profile, craft personalized connection-request note | Identified >14 days without stage 2 |
| 2 | Connection sent | Personalized note sent (<300 chars), within weekday cap | Wait for acceptance or decline | Pending >14 days → move to "Stale" |
| 3 | Connected | Accepted, relationship established | First DM within 48 hours | No DM sent 72h after accept |
| 4 | First message sent | Opening DM referencing something specific from their profile | Await reply (max 7 days) | No reply 10 days → "Lapsed" |
| 5 | Reply received | They responded, conversation active | Reply within 24 hours, move to "Conversation" | No follow-up 48h |
| 6 | Conversation active | Back-and-forth ≥2 rounds | Identify if buyer signal, peer signal, or social | 10 days silent |
| 7 | Buyer signal | Said something like "we have this problem", "show me", asked pricing | Offer demo, share Loom, schedule call | No move 5 days |
| 8 | Demo scheduled | Calendly booked or confirmed time | Run demo, log in pipeline notes | Demo cancelled |
| 9 | Post-demo followup | Demo complete, awaiting decision | Proposal or pilot offer | 7 days silent |
| 10 | Pilot / customer | Signed pilot terms or started free trial | Track usage + feedback | Pilot ended without conversion |
| 11 | Closed — conversion or decline | Paying customer OR politely declined | Reference in case study OR move to "Watch" list | n/a |

## Fields per prospect (Notion `outreach_pipeline` DB)

- name (title)
- company
- role
- linkedin_url (URL)
- stage (select: the 11 above + "Stale", "Lapsed", "Watch", "AVI-MANAGED")
- segment (select: DPO-compliance / litigation-ops / in-house-counsel / law-firm-associate / founder-peer / vc / other)
- personality_tag (multi-select: data-driven / story-driven / warm-intro-preferred / formal / casual / skeptical)
- pillar (select: contract / research / dpdp / multi)
- first_touched (date)
- last_touched (date)
- last_action (text)
- notes (rich text)
- source (text: inbound / referral / cold / conference / content-reply)

## Transition rules

- **Connection-request cap:** 5/day, 25/week (LinkedIn enforces weekly limits independently)
- **Never skip stages.** No cold pitches in first DM (stage 4 opener is relationship-open, not sale-open).
- **Stuck rescue:** when a prospect hits "Stuck if" threshold, CONNECT drops them to "Stale" and surfaces in a weekly review. Avi decides whether to revive with a different angle or close.
- **Declined prospects:** move to "Closed" with outcome = declined. Do NOT message again unless 90+ days later with a meaningfully different hook.
- **AVI-MANAGED flag:** set on prospects Avi wants to handle personally. CONNECT reads but never messages. Currently: Siddhant M Sharma, Apoorv Sharma, Shashank Pashine (for NCR JurisLPO introductions).

## Weekly targets (Phase 2 default; COO updates per week)

- 25 new connections sent
- 15 DMs to new connections
- 10 follow-ups on stages 4–7
- 3 revival messages on Stale/Lapsed
- 4 warm-intro asks via stage-10 customers (post-conversion)

## Scripts

Stored in `outreach_pipeline` DB as Notion sub-pages under each segment. Phase-aware. Updated by COO Sunday Synthesis based on strategy.md "To Outreach Agent" directive.

## Ethics

- Never use a fake pretext (e.g., "we met at X event" if not true).
- Always disclose if a message was AI-drafted when a prospect asks. Don't volunteer it unprompted.
- If prospect says "please don't message me", tag Closed/declined + block future touches forever.
- Do not scrape or export connection data for use outside this pipeline.
