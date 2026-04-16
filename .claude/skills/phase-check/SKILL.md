---
name: phase-check
description: Reads current_phase from brain/strategy.md. Returns the phase number and the rules for that phase. MAKER and CONNECT call this before generating any outward-facing content.
---

# Phase Check

Every content-producing agent must call this skill before generating output that will reach the public.

## Invocation

1. Read `brain/strategy.md` first 15 lines — parse the fenced block:
   ```
   STOP: false
   current_phase: 2
   ```
2. If `current_phase` is missing, malformed, or > 4, HALT and notify Avi. Do not generate content.
3. Return the phase number + the rules for that phase.

## Phase rules (reference)

### Phase 1 — "I'm Building Something" (Weeks 1–2)
- Goal: let people know Avi exists as a builder.
- ALLOWED: first-person stories, vulnerability, hint-dropping, "I've been building something".
- BANNED: any product name (ContraRed / Smriti / Legal OS), architecture claims ("zero hallucination", "source-traced"), industry commentary, competitor references by name.

### Phase 2 — "Here's the Problem" (Weeks 3–4)
- Goal: establish the problem NeetiQ solves; build credibility through insight.
- ALLOWED: data-driven problem deep-dives, DPDP stats, hallucination numbers, "I've been building something to fix this" with more authority.
- BANNED: still no product names, no "Legal OS", no architecture claims, no direct competitor names. Can reference "the biggest AI company" or "a recent Word add-in" without naming.

### Phase 3 — "The Product Reveal" (Week 5+)
- Goal: introduce ContraRed and Smriti by name. Show screenshots / demos.
- ALLOWED: product names, demos, before/after, side-by-side with Claude for Word, show DPDP scanning.
- BANNED: "Legal Operating System" framing (Phase 4), full architecture claims, industry-positioning thought leadership.

### Phase 4 — "Industry Authority" (Week 7+)
- Goal: position NeetiQ as an OS. Full thought leadership.
- ALLOWED: "The Legal Operating System", kernel language, hallucination data, architecture claims, industry commentary, named competitor comparisons (factual, not bashing).

## Output format

```
PHASE: 2
CONTRACT: Phase 2 — no product names, no Legal OS, no architecture claims
DRAFT_SCOPE: data-driven problem, India anchor required, "I've been building something" OK
BAN_LIST: ContraRed, Smriti, Legal OS, Legal Operating System, zero hallucination, source-traced, jurisdiction-native, kernel
ALLOW_LIST: DPDP, India courts, 55M cases, hallucination data, problem stats
```

If MAKER is about to generate Phase 3 content while `current_phase=2`, phase-check returns:

```
PHASE_MISMATCH
Requested: Phase 3 (product reveal)
Current: Phase 2 (problem awareness)
Action: HALT. Do not draft product-name content this week. Check strategy.md for transition date.
```

## Dependencies

- `brain/strategy.md` must exist and have the fenced STOP/phase block at the top.
- If malformed, halt and notify Avi via Dispatch or log.
