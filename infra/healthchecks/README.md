# Healthchecks.io — External Watchdog

Every scheduled agent pings a unique URL at the end of a successful run.
If a ping is missed past the grace window, Healthchecks SMS/emails Avi.

This is the only thing that catches a silently-stuck system. Treat it as
non-optional.

## Accounts & billing

- Plan: Hobbyist (free). 20 checks, SMS via Twilio integration.
- If we outgrow 20 checks, upgrade to Supporter ($5/mo).

## Checks to create

Sign in → `healthchecks.io/checks/` → **Add Check** for each row. On each
check, open the **Schedule** tab → select **Cron** → paste the expression
→ set timezone to `Asia/Kolkata` → set grace from the table.

Healthchecks takes ONE cron per check, so schedules that fire on two
different clock times are split into two checks (intel daily vs saturday,
intel-feed weekday vs saturday).

| Name | Cron (Asia/Kolkata) | Grace | Tags |
|---|---|---|---|
| neetiq-v2-coo-sunday | `0 6 * * 0` | 45 | coo, weekly, critical |
| neetiq-v2-coo-morning | `30 8 * * 1-5` | 35 | coo, daily, critical |
| neetiq-v2-coo-evening | `0 18 * * 1-5` | 35 | coo, daily |
| neetiq-v2-intel-daily | `0 8 * * 1-5` | 30 | intel, daily |
| neetiq-v2-intel-saturday | `0 10 * * 6` | 30 | intel, daily |
| neetiq-v2-intel-wed | `0 10 * * 3` | 45 | intel, weekly |
| neetiq-v2-maker-weekly | `0 7 * * 0` | 60 | maker, weekly, critical |
| neetiq-v2-connect-daily-prompt | `0 11 * * 1-5` | 240 | connect, daily |
| neetiq-v2-analytics-weekly | `0 18 * * 5` | 45 | analytics, weekly |
| neetiq-v2-intel-feed-github-weekday | `30 7 * * 1-5` | 20 | intel, github, critical |
| neetiq-v2-intel-feed-github-sat | `30 9 * * 6` | 20 | intel, github, critical |

11 checks. Hobbyist (free) plan allows 20 so we're fine.

## Where the URLs live

After creating each check, Healthchecks gives a URL like
`https://hc-ping.com/<uuid>`. Save these as environment variables in
`Version 2 agents/brain/.env.local` (gitignored):

```
HEALTHCHECKS_URL_COO_SUNDAY=https://hc-ping.com/...
HEALTHCHECKS_URL_COO_MORNING=https://hc-ping.com/...
HEALTHCHECKS_URL_COO_EVENING=https://hc-ping.com/...
HEALTHCHECKS_URL_INTEL_DAILY=https://hc-ping.com/...
HEALTHCHECKS_URL_INTEL_SATURDAY=https://hc-ping.com/...
HEALTHCHECKS_URL_INTEL_WED=https://hc-ping.com/...
HEALTHCHECKS_URL_MAKER_WEEKLY=https://hc-ping.com/...
HEALTHCHECKS_URL_CONNECT=https://hc-ping.com/...
HEALTHCHECKS_URL_ANALYTICS=https://hc-ping.com/...
HEALTHCHECKS_URL_INTEL_FEED_WEEKDAY=https://hc-ping.com/...
HEALTHCHECKS_URL_INTEL_FEED_SAT=https://hc-ping.com/...
```

The two `INTEL_FEED_*` URLs ALSO go into the GitHub repo as
`secrets.HEALTHCHECKS_URL_INTEL_FEED_WEEKDAY` and
`secrets.HEALTHCHECKS_URL_INTEL_FEED_SAT` so the Actions workflow can read
them.

## How agents ping

Every agent prompt ends with a curl to its Healthchecks URL:

```bash
# Success ping at end of run
curl -fsS -m 10 --retry 3 "$HEALTHCHECKS_URL_<NAME>" >/dev/null
```

For failure pings (when the agent itself catches a handled error mid-run),
append `/fail`:

```bash
curl -fsS -m 10 --retry 3 "$HEALTHCHECKS_URL_<NAME>/fail" >/dev/null
```

For long-running agents (COO Sunday, MAKER Weekly) we also `/start`:

```bash
curl -fsS -m 10 --retry 3 "$HEALTHCHECKS_URL_<NAME>/start" >/dev/null
# ... work ...
curl -fsS -m 10 --retry 3 "$HEALTHCHECKS_URL_<NAME>" >/dev/null
```

## Notification integrations

Configure under `healthchecks.io/integrations/`:

1. **SMS (Twilio)** — primary for everything tagged `critical`.
2. **Email** to `aviyadav.personal@gmail.com` — for everything else.
3. **Slack webhook** — skip for now. Dispatch already covers.

Tag `critical` on: coo-morning, coo-sunday, maker-weekly,
intel-feed-github-weekday, intel-feed-github-sat.

## Grace window philosophy

- Grace > expected run time by ~50%, never less.
- CONNECT gets 4h because it's human-in-loop; Avi might not be at his desk
  at exactly 11 AM every weekday.
- Morning routines get 35 min: if brief doesn't ping by 09:05 IST, something
  is broken and Avi should know before the workday starts.

## When a check fires

Alert → Avi opens Cowork → runs the killswitch skill → investigates.

```
skill: killswitch
```

## Testing

Once set up, manually fail one check: open the check, hit "Test", confirm
SMS lands within 60s. Do this on `coo-morning` before relying on the
system.
