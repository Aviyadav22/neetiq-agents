# INTEL Daily — 2026-04-20

## Sources scanned: 13 (per run × 4 runs: Apr 16, 17, 18, 20)
## New items: 4 with content (3 Spellbook product/distribution, 1 new RBI circular)
## Severity: 0 critical, 0 high, 2 medium, 2 low

---

### Critical findings
None.

---

### High
None.

---

### Medium

**Spellbook — "What's New in Spellbook? March Releases"**
- URL: https://www.spellbook.legal/blog/whats-new-in-spellbook-march-2026
- Published: 2026-04-15
- Snippet: Empty (RSS feed returned no body text)
- Summary: Spellbook published their March 2026 product update recap. Content unknown without fetching the URL. Based on title, likely product changelog.
- NeetiQ implication: Spellbook continues active development. No detail available to assess direction. Market benchmarking competitor (not direct).

**Spellbook — "Channel Partner Program" launch**
- URL: https://www.spellbook.legal/blog/introducing-spellbook-channel-partner-program
- Published: 2026-02-14 (late to feed, appearing now)
- Summary: Spellbook launched a channel partner program, expanding distribution through resellers and partners. North America focus.
- NeetiQ implication: Spellbook accelerating distribution reach. Their market benchmarking (270+ clause benchmarks) is complementary to ContraRed, not competing, but wider distribution puts their framing in more lawyers' hands before ContraRed is known.

---

### Low

**Spellbook — "Meet Spicy Mode"**
- URL: https://www.spellbook.legal/blog/meet-spicy-mode
- Published: 2026-04-03
- Snippet: Empty. Name suggests an aggressive or opinionated review mode. Cannot assess without fetching.

**RBI Circular — NBFC Branch Authorization Amendment Directions, 2026**
- ID: 13370
- Summary: RBI updated NBFC branch authorization rules. Standard regulatory update.
- NeetiQ implication: NBFCs reviewing branch contracts may need compliance review. Background context for ContraRed banking/NBFC vertical, not urgent.

---

## SOURCE FAILURES — PERSISTENT SYSTEM ALERT

**7 of 13 sources have failed across ALL 4 runs (Apr 16, 17, 18, 20):**
1. harvey — CRITICAL competitor, dark for 4+ days
2. jhana — Top India competitor, dark for 4+ days
3. casetext_cocounsel — Global competitor, dark
4. lexoo — Watch list source, dark
5. meity_dpdp — CRITICAL regulatory source, dark for 4+ days
6. startup_india_seed — Grants scout source, dark
7. openai_grants — Grants source, dark

**Impact:** INTEL has been blind to Harvey and Jhana for at least 4 days, coinciding with the Phase 2/3 transition week. Any Harvey product updates, Jhana funding news, or MeitY DPDP rule changes during this window are UNDETECTED. The GitHub Actions RSS poller for these sources needs investigation and repair.

**Action required from Avi or COO:** Diagnose why these 7 sources are failing in the GitHub Actions workflow. Check `.github/workflows/` for connector errors.

---

## Watchlist updates
- Spellbook: Channel Partner Program noted (distribution expansion, Feb 2026)
- Spellbook: March Releases + Spicy Mode exist but no snippet content available

## Phase context
Today (2026-04-20) is the Phase 2 → Phase 3 transition target date per strategy.md. Phase 3 assets (demo videos, screenshots, custom playbooks) were due today. INTEL has no data from this week on whether competitors made any Phase 3-relevant announcements due to source failures.

## Dispatch sent: no (no critical competitor findings; source failures logged here)
