---
name: content-voice-audit
description: Audits any draft text (LinkedIn post, Twitter post, outreach DM, email) against NeetiQ's banned patterns and Avi's voice rules. Returns PASS or a list of flags with line numbers and rewrite suggestions.
---

# Content Voice Audit

This skill is MANDATORY before MAKER pushes any draft for approval and before CONNECT sends any outreach DM.

## Invocation

Run the skill by reading `banned_words.md` and `structural_patterns.md` in this folder, then applying the rules below.

## Inputs

A block of draft text (≤2,000 characters for LinkedIn, ≤280 chars for Twitter, ≤600 for DMs).

Also read these context files:
- `brain/brand_identity.md` — the full voice doctrine
- `brain/strategy.md` — current_phase (must match the draft's phase scope)
- `brain/published_posts.md` — last 5 posts per channel (voice drift check)

## Checks (in order)

### 1. Phase-gate check
If `current_phase == 1` or `2`:
- Flag any mention of: ContraRed, Smriti, "Legal OS", "Legal Operating System", "zero hallucination", "jurisdiction-native", "source-traced", "kernel"

If `current_phase == 3`:
- Product names OK. Flag "Legal OS" / "Legal Operating System" (still Phase 4).

If `current_phase == 4`:
- All positioning OK.

### 2. Banned-word scan (109 words)
Load `banned_words.md`. Flag any match (case-insensitive, whole-word). For each flag: return the word, line number, one rewrite suggestion.

### 3. Structural pattern scan (36 patterns)
Load `structural_patterns.md`. Each pattern is either a regex or a description. Flag matches.

### 4. Em-dash and semicolon check
Any `—`, `–`, ` -- `, or `;` in a social post = automatic flag. Zero tolerance.

### 5. Opening check
First sentence must not start with any of: "In today's", "I'm thrilled", "Excited to announce", "Proud to share", "Here's the thing:", "Let me be clear:", "Let that sink in."

### 6. Closing check
Last 2 sentences must not be a generic CTA ("What do you think?", "Would love your thoughts", "Agree?", "DM me for more").

### 7. India-anchor check (per CEO Directive D8)
Posts must include ≥1 India-specific anchor: Indian court, Indian statute, Indian company name, MeitY/BCI/DPDP/RBI/SEBI/CCI, or "₹X lakh/crore", or an Indian city. Flag if missing.

### 8. Bullet-list check
Social posts may not contain bullet lists (lines starting with `-`, `*`, `•`, or numbered `1.` / `2.`). Twitter threads are exempt.

### 9. Voice drift check
Compare the draft against `brain/published_posts.md` last 5 posts on the same channel. Flag if the draft substantially matches the opening structure of a recent post (same hook type 3 posts in a row = drift).

### 10. "Would a human write this?" final sniff
Read the draft out loud (mentally). If any sentence makes you pause because "a real person wouldn't say it that way", flag it.

## Output format

Return one of:

```
VOICE_AUDIT: PASS
```

OR

```
VOICE_AUDIT: FLAGS

Line 3: "navigate the landscape" → banned word "navigate" + banned phrase "the landscape"
  Rewrite: "work in this space" or just drop the sentence

Line 7: em dash "—"
  Rewrite: period + new sentence

Line 12: generic CTA "What do you think?"
  Rewrite: end on the specific thing you want them to answer, or delete

[Phase gate] Line 5: "Legal OS" mentioned but current_phase=2
  Fix: cut the whole paragraph or move to Phase 4 queue

[India anchor] Missing.
  Fix: add one of DPDP / SC / BCI / ₹ / Delhi / Mumbai / a named Indian company
```

Do NOT auto-rewrite. MAKER shows flags to Avi for decision.

## Failure modes

- If `banned_words.md` or `structural_patterns.md` is missing, HALT and notify Avi. Do not let drafts through without audit.
- If the draft is in a language other than English or Hindi, flag "unsupported language, human review".
