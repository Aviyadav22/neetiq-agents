# Dispatch Setup — Phone ↔ Claude Channel

Dispatch is how every agent talks to Avi and how Avi approves / kills /
asks things mid-day. Treat it as a two-way radio, not a notification firehose.

## What Dispatch is

A Claude pairing that runs on Avi's phone (Claude mobile app) and sends
push messages from any Claude session (Cowork, Cloud Routine, Chrome) to
that phone. Avi replies in the thread; the reply is readable by the next
scheduled agent run.

If Dispatch isn't available in the Claude mobile app in your region yet,
the fallback is: all Dispatch pushes become **Gmail drafts** to
`aviyadav.personal@gmail.com` with subject `[NeetiQ v2 Dispatch] <topic>`,
and Avi replies by editing a file in the Cowork folder: `brain/inbox.md`.

## Setup steps

1. Install Claude on phone (iOS or Android).
2. Sign in with the same account that's paired with Cowork on the Windows
   machine.
3. In Claude settings → **Dispatch** → enable push notifications + reply.
4. On Windows Cowork, open the NeetiQ session. First message from any
   agent to Dispatch should arrive as a push within 30 seconds.

## Channels / topics

Messages from agents use a tag at the front so Avi can triage fast:

| Tag | Who sends | Response expected? |
|---|---|---|
| `APPROVE — ...` | MAKER, CONNECT | Yes, in Dispatch |
| `FYI — ...` | COO Evening, ANALYTICS, INTEL | No |
| `FLAG — ...` | Any agent catching something anomalous | Yes, Avi reads today |
| `KILL — ...` | Killswitch auto-notification | No (already acted on) |
| `MORNING — ...` | COO Morning Brief | Read-only |

## Reply grammar (what Avi types back)

Lowercase / uppercase both fine. Punctuation optional.

- `APPROVE ALL` — ship everything in the last APPROVE message
- `APPROVE 1, 3` — ship items 1 and 3, archive the rest
- `FIX 2: <feedback>` — redraft item 2 with this feedback
- `SKIP` — archive everything in the last APPROVE
- `STOP` — triggers killswitch. Sets strategy.md STOP: true.
- `RESUME` — clears STOP. Only Avi can send this.
- `PHASE <N>` — force phase transition (requires confirmation reply).
- `DRAFT <topic>` — asks MAKER to run on_demand_draft.md for this topic.
- `POST NOW <N>` — MAKER picks up post #N from this week's queue and
  prepares posting session.

## What Dispatch does NOT do

- Does not auto-act on replies. Replies sit in the thread; the next
  scheduled agent reads them.
- Does not carry the whole conversation history. Keep replies short and
  topic-tagged so the next agent can find them.
- Does not replace email. Weekly summary still goes to Gmail as a draft.

## Noise control

Hard rules, enforced by the `coo` and `killswitch` skills:

- Max 4 pushes per working day unless something breaks.
- Evenings after 19:00 IST: `FYI` and `MORNING` are suppressed. `FLAG`
  and `KILL` still fire.
- Weekends: only `KILL` fires. Everything else queues to Monday 08:30.
- Never two pushes within 2 minutes of each other — batch.

## Outages

If Dispatch is down:
1. Agents log the intended push to `brain/agent_log.md` with
   `DISPATCH_UNAVAILABLE` in the Result column.
2. `APPROVE` blockers pause the dependent work (MAKER won't send a draft
   for approval if there's no channel). MAKER just writes the draft file
   and moves on; Avi can read + approve manually in Cowork.
