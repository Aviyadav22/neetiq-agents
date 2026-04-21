# MAKER — On-Demand Draft

**Trigger:** Avi sends "draft a post about X" via Dispatch (or says it in a Cowork session).
**Model:** Sonnet 4.6
**Duration:** 3–8 min

## Flow

1. stop-check + phase-check.
2. Read `brain/strategy.md` (this week's plan) + `brain/USER.md` (voice) + last 5 published_posts for the target channel.
3. Clarify ONCE if ambiguous:
   - Which channel? (Personal LI / Company LI / Twitter)
   - What's the hook? (stat / story / reaction)
   - Phase-appropriate scope?
   Ask at most one question. If Avi said "LinkedIn post about the Gujarat HC ruling", assume Personal LI (his voice), hook = the ruling, Phase 2 rules.
4. Draft 2 variants (not 1). Different opens, same point. ≤1,500 chars each for LI.
5. Voice-audit each.
6. Dispatch push:
   ```
   APPROVE — MAKER on-demand draft.
   Variant A: <first 80 chars>... [PASS]
   Variant B: <first 80 chars>... [PASS]
   Full text: outputs/drafts/ondemand_YYYY-MM-DD-HHMM.md
   Reply A, B, FIX, or BOTH.
   ```
7. On approval, queue for posting (same flow as weekly calendar).

## Log

```
2026-MM-DD HH:MM | MAKER | sonnet-4.6 | <phase> | on-demand draft | OK | outputs/drafts/ondemand_YYYY-MM-DD-HHMM.md
```

## Rules

- No question if you can make a reasonable default. Avi hates back-and-forth.
- Always 2 variants. Pick different angles (e.g., data-open vs story-open).
- Same voice audit rigor as weekly calendar. No shortcuts because it's "quick".
