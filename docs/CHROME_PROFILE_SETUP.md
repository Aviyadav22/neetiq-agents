# Chrome Profile Setup — "NeetiQ Autopilot"

CONNECT runs inside Claude-in-Chrome. It MUST run in a dedicated Chrome
profile that is signed into LinkedIn as Avi. Never use the profile for
anything else.

## Why dedicated

- LinkedIn flags accounts that mix automation with normal browsing. A
  sterile profile (no other tabs, no ad trackers from your personal
  browsing, no extensions) keeps the account far from the threshold.
- If the profile gets flagged, we can kill it without nuking Avi's main
  Chrome.
- Claude-in-Chrome can only see the profile it's launched from. Keeping
  it isolated means Claude can't accidentally read other work/personal
  tabs.

## Steps

1. **Create the profile**
   - Chrome → profile icon (top-right) → **Add**.
   - Name: `NeetiQ Autopilot`.
   - Color: dark purple (so Avi never confuses it with personal).
   - Disable "sync everything" — keep it local.

2. **Sign in to LinkedIn only**
   - Open `linkedin.com`. Log in as Avi.
   - Do not sign in to Google, Gmail, or anything else in this profile.
   - Do not install any extensions except Claude for Chrome.

3. **Install Claude for Chrome**
   - `chrome.google.com/webstore` → search "Claude for Chrome".
   - Install inside the NeetiQ Autopilot profile only.

4. **Verify Claude for Chrome is bound to this profile**
   - Open Claude extension → settings → confirm it reports the
     NeetiQ Autopilot profile.

5. **Bookmark the four pages CONNECT uses**
   - LinkedIn homepage
   - LinkedIn messaging
   - LinkedIn notifications
   - LinkedIn connection-requests page
   No other bookmarks.

6. **Hardening**
   - Enable `chrome://settings/cookies` → block third-party cookies.
   - Enable `chrome://flags/#enable-quic` → default (don't change).
   - DO enable Safe Browsing (Enhanced protection is fine).
   - DO NOT install uBlock, Grammarly, or other content-script extensions.
     They inject into Claude's page and cause selector drift.

7. **Bookmark the CONNECT Chrome pre-session prompt**
   - The prompt is in
     `Version 2 agents/agents/connect/chrome_playbook.md` under
     "Pre-session". Copy it into a sticky note or a browser bookmark's
     description for fast paste.

## When Avi starts a CONNECT session

1. Open Chrome → switch to `NeetiQ Autopilot` profile.
2. Open Claude for Chrome extension (ALT+C or click icon).
3. Paste the pre-session prompt.
4. Wait for Claude to report queue + plan.
5. Approve actions one by one. ALWAYS review messages before send.
6. Close session. Confirm Claude logged the summary to Notion
   `agent_log`.

## What to do if LinkedIn shows a CAPTCHA or "unusual activity"

Stop the session immediately. Do not try to "just finish one more".

- In Cowork: run the killswitch skill targeted at CONNECT only.
- Wait 72 hours before resuming CONNECT.
- Review `brain/agent_log.md` for the last 20 actions. If there's a
  pattern (all DMs to the same segment? too-similar openers?), note it
  for MAKER to avoid.

## Daily sanity check

Before first CONNECT session of the day, Avi spends 30 seconds:

- Any LinkedIn notification banners warning of "unusual activity"?
- Profile thumbnail still looks right (LinkedIn hasn't silently
  restricted)?
- Message-send test on a known mutual (NOT a prospect) returns instantly?

If any of those is off, don't run CONNECT. Investigate first.
