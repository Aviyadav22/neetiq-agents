# Healthchecks.io — External Watchdog

Every scheduled agent pings a unique URL at the end of a successful run.
If a ping is missed past the grace window, Healthchecks SMS/emails Avi.

This is the only thing that catches a silently-stuck system. Treat it as
non-optional.

## Accounts & billing

- Plan: Hobbyist (free). 20 checks, SMS via Twilio integration.
- If we outgrow 20 checks, upgrade to Supporter ($5/mo).

## Checks to create

Sign in → `healthchecks.io/checks/` → **Add Check** for each row.

| Name | Schedule | Grace | Tag |
|---|---|---|---|
| neetiq-v2-coo-sunday | Every Sun 06:00 IST | 45 min | coo, weekly |
| neetiq-v2-coo-morning | Weekdays 08:30 IST | 35 min | coo, daily |
| neetiq-v2-coo-evening | Weekdays 18:00 IST | 35 min | coo, daily |
| neetiq-v2-intel-daily | Weekdays 08:00 IST + Sat 10:00 IST | 30 min | intel, daily |
| neetiq-v2-intel-wed | Wed 10:00 IST | 45 min | intel, weekly |
| neetiq-v2-maker-weekly | Sun 07:00 IST | 60 min | maker, weekly |
| neetiq-v2-connect-daily-prompt | Weekdays 11:00 IST | 240 min (humanloop) | connect, daily |
| neetiq-v2-analytics-weekly | Fri 18:00 IST | 45 min | analytics, weekly |
| neetiq-v2-intel-feed-github | Weekdays 07:30 IST + Sat 09:30 IST | 20 min | intel, github |

Cron schedule format: open the **Schedule** tab on each check and select
"Cron" — they're clock-based, not periodic.

## Where the URLs live

After creating each check, Healthchecks gives a URL like
`https://hc-ping.com/<uuid>`. Save these as environment variables in
`Version 2 agents/brain/.env.local` (gitignored):

```
HEALTHCHECKS_URL_COO_SUNDAY=https://hc-ping.com/...
HEALTHCHECKS_URL_COO_MORNING=https://hc-ping.com/...
HEALTHCHECKS_URL_COO_EVENING=https://hc-ping.com/...
HEALTHCHECKS_URL_INTEL_DAILY=https://hc-ping.com/...
HEALTHCHECKS_URL_INTEL_WED=https://hc-ping.com/...
HEALTHCHECKS_URL_MAKER_WEEKLY=https://hc-ping.com/...
HEALTHCHECKS_URL_CONNECT=https://hc-ping.com/...
HEALTHCHECKS_URL_ANALYTICS=https://hc-ping.com/...
HEALTHCHECKS_URL_INTEL=https://hc-ping.com/...   # GitHub Actions feed
```

The GitHub one ALSO gets added to the repo as
`secrets.HEALTHCHECKS_URL_INTEL` so the Actions workflow can read it.

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

Tag `critical` on: coo-morning, coo-sunday, intel-feed-github, maker-weekly.

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
