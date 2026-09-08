# Habit Tracker — Market Study & Business Requirements

**Status:** Draft v1
**Owner:** Mohamed Khadra
**Last updated:** 2026-08-23

---

## 1. Executive summary

Habit tracking is a crowded category with a brutal retention problem. Vendor and
practitioner reports converge on the same shape: most people abandon a habit
tracker within two to eight weeks. The apps are not failing because they lack
features — several are excellent. They fail because the *default design of a
habit tracker actively punishes the user for being human*.

The strongest evidence-backed lever in behaviour change is **social
accountability inside a small, trusted group** — which happens to be exactly the
use case this project starts from: a handful of friends who want to keep each
other honest.

**Product thesis**

> A habit tracker built for a small circle of friends, where the streak is
> forgiving by design and the accountability is social rather than punitive.

This document covers the failure modes this product is designed against (§2),
the requirements that follow from them (§5–8), and what is explicitly out of
scope (§11).

---

## 2. Why users quit (the actual problem)

Synthesised from the sources in §13. Each item below maps to a requirement later
in this document.

| # | Failure mode | What happens | Our counter-design |
|---|---|---|---|
| P1 | **Streak anxiety** | A 12-day streak breaks on a bad Tuesday, resets to 0, and the user quits rather than restart | Forgiving streak model (§6.2) |
| P2 | **Feature overload** | Dashboards, tags, categories, colour systems. Friction is fatal to a habit tool | Ruthless MVP scope (§8); ≤2 taps to log |
| P3 | **Notification fatigue** | Reminders shift from helpful to hostile around week 6 | Reminder budget + auto-decay (§6.4) |
| P4 | **No real accountability** | Nothing is at stake; the app is a private to-do list | Small-group visibility (§6.3) |
| P5 | **Self-deception** | Users tick "workout done" from the couch | Optional verification: notes, photo, or peer confirm (§6.3) |
| P6 | **All-or-nothing framing** | Binary done/not-done erases partial effort | Numeric and partial completion (§6.1) |
| P7 | **Post-honeymoon drop-off** | Enthusiasm carries ~4 days; the app must earn week 6 | Weekly review ritual (§6.5) |

> **On the statistics.** Most figures circulating in this category ("90% quit in
> 30 days", "you are 95% more likely to succeed with an accountability partner")
> originate in vendor blogs and a widely-miscited ASTD claim. Treat them as
> *directional*, not as evidence. The one genuinely useful dataset is stickK's
> observational data across 17,654 commitment contracts, which found large
> effects from stakes and from a designated referee — and even that is
> self-reported and self-selected. **Design for the mechanism, not the number.**

---

## 3. Positioning

**For** small groups of friends who already want the same habits,
**who** have tried and abandoned solo habit trackers,
**our product is** a shared habit tracker
**that** makes consistency visible to people whose opinion you actually care about, without punishing a missed day.

**Unlike** a solo tracker that resets your progress to zero the moment life
interferes, **we** treat a small group as the primary unit, and treat a missed
day as data rather than failure.

### Non-goals

Being the best app for everyone. This is a tool for **groups of 3–8 people who
know each other**. Every trade-off resolves in favour of that user.

---

## 4. Users

| Persona | Description | Primary need |
|---|---|---|
| **The Owner** (you) | Sets up the group, invites friends, cares about the data | Trustworthy tracking + a reason to keep coming back |
| **The Committed Friend** | Genuinely wants the habit, will log daily | Low-friction logging; visible progress |
| **The Casual Friend** | Joined because you asked | Almost zero friction, no guilt, easy re-entry after lapsing |
| **The Lapsed Returner** | Was active, disappeared for 10 days | A path back that does not feel like starting from zero |

**The Lapsed Returner is the most important persona.** Every competitor loses
this person. Designing for their return is the whole differentiator.

---

## 5. Product principles

1. **Logging must cost less than the habit.** If marking a habit takes longer than five seconds, it is broken.
2. **A missed day is information, not a verdict.** The system never uses shame.
3. **The group is the feature.** Anything that works better alone belongs in a different app.
4. **Honest by default, verifiable on request.** Verification is opt-in per habit, never global surveillance.
5. **Silence is a valid state.** Not logging is not the same as failing.
6. **Boring reliability beats clever features.** Sync that never loses a tick is worth more than any chart.

---

## 6. Functional requirements

Priority: **M** = Must (MVP), **S** = Should (v1.1), **C** = Could (later).

### 6.1 Habit definition

| ID | Requirement | Pri |
|---|---|---|
| FR-1.1 | Create a habit with a name, an icon/colour, and a schedule | M |
| FR-1.2 | Support habit types: **binary** (done/not), **numeric** (8 glasses), **duration** (30 min) | M |
| FR-1.3 | Schedules: every day, specific weekdays, N times per week, every N days | M |
| FR-1.4 | **N-times-per-week** must not care *which* days — this is the single most anti-anxiety scheduling primitive | M |
| FR-1.5 | Archive a habit without deleting its history | M |
| FR-1.6 | Partial completion recorded as a value, not a failure (e.g. 5 of 8 glasses) | M |
| FR-1.7 | Habits can be *building* (do more) or *breaking* (do less / abstain) | S |
| FR-1.8 | Habit templates so a friend can adopt an existing habit in one tap | S |

### 6.2 Tracking & the forgiving streak — *the core differentiator*

| ID | Requirement | Pri |
|---|---|---|
| FR-2.1 | Log a completion for today in **≤2 interactions** from the main screen | M |
| FR-2.2 | Backfill or edit any of the last 7 days | M |
| FR-2.3 | **Consistency score** (rolling % over 30 days) is the headline metric, *not* the streak | M |
| FR-2.4 | Streaks survive a configurable allowance (default: 1 miss per 7 days) | M |
| FR-2.5 | Explicit **"skip"** state for legitimate exceptions (illness, travel) — preserves the streak, excluded from the denominator | M |
| FR-2.6 | **Pause** a habit for a date range without ending it | S |
| FR-2.7 | On return after a lapse, show a re-entry view that surfaces lifetime consistency, never a zeroed counter | M |
| FR-2.8 | Optional per-habit note on any log entry | S |
| FR-2.9 | Optional photo attached to a log entry (verification, see FR-3.5) | C |

> **Design note (FR-2.3).** Making consistency the headline metric instead of the
> streak is the mechanical fix for P1. A 30-day rolling percentage degrades
> gracefully — one missed day moves 93% to 90%. A streak goes from 12 to 0. The
> streak is still shown, because people like it; it is just no longer the score.

### 6.3 Groups & accountability

| ID | Requirement | Pri |
|---|---|---|
| FR-3.1 | Create a group; invite by link; 2–12 members | M |
| FR-3.2 | A member chooses per habit whether it is **private** or **shared with the group** | M |
| FR-3.3 | Group feed showing shared completions (chronological, no algorithm) | M |
| FR-3.4 | React to a friend's entry (small fixed set of positive reactions only — no downvote) | M |
| FR-3.5 | Optional per-habit **peer verification**: a nominated group member confirms | C |
| FR-3.6 | Weekly group digest: who showed up, no leaderboard by default | S |
| FR-3.7 | **Nudge** a lapsed member — one tap, rate-limited to once per member per week | S |
| FR-3.8 | Shared group habits everyone tracks against the same definition | S |
| FR-3.9 | Opt-in leaderboard, off by default, disableable by the group owner | C |

> **Design note (FR-3.9).** Leaderboards help the person winning and harm
> everyone else. In a group of friends, that asymmetry costs you the Casual
> Friend persona. Ship it off by default or not at all.

### 6.4 Reminders

| ID | Requirement | Pri |
|---|---|---|
| FR-4.1 | Per-habit reminder at a chosen time | M |
| FR-4.2 | **Global reminder budget** — a hard cap on notifications per day (default 3) | M |
| FR-4.3 | Suppress a reminder if the habit is already logged | M |
| FR-4.4 | Auto-decay: if a reminder is ignored N times in a row, reduce frequency and tell the user | S |
| FR-4.5 | Quiet hours | S |

> **Design note.** FR-4.2 and FR-4.4 are the counter to P3. Almost no competitor
> caps its own notifications; it is a cheap, distinctive trust signal.

### 6.5 Insight & review

| ID | Requirement | Pri |
|---|---|---|
| FR-5.1 | Per-habit calendar heatmap | M |
| FR-5.2 | 30-day consistency trend per habit | M |
| FR-5.3 | **Weekly review**: what worked, what did not, one adjustment for next week | S |
| FR-5.4 | Best/worst weekday per habit ("you miss Saturdays") | S |
| FR-5.5 | Export all personal data as JSON and CSV | M |

### 6.6 Accounts & data

| ID | Requirement | Pri |
|---|---|---|
| FR-6.1 | Email + password auth, or OAuth (Google/GitHub) | M |
| FR-6.2 | A user belongs to zero or more groups | M |
| FR-6.3 | Full account deletion, cascading to all personal data | M |
| FR-6.4 | Timezone stored per user; "today" resolves in the user's local timezone | M |
| FR-6.5 | Configurable day boundary (default 00:00; allow e.g. 04:00 for night owls) | S |

---

## 7. Non-functional requirements

| ID | Requirement | Target |
|---|---|---|
| NFR-1 | Time to log a habit from app open | < 3 s on 4G |
| NFR-2 | Main dashboard interactive | < 1.5 s (p75, mobile) |
| NFR-3 | Works offline for logging; syncs on reconnect | Required by v1.1 |
| NFR-4 | Responsive: usable one-handed on a phone browser | Required at MVP |
| NFR-5 | Accessibility | WCAG 2.2 AA |
| NFR-6 | Data durability — a lost log entry is the worst possible bug | Nightly backups, no destructive migrations |
| NFR-7 | Privacy: no third-party analytics on habit content | Required |
| NFR-8 | Scale target | 100 groups / 500 users — deliberately small |
| NFR-9 | Installable as a PWA | v1.1 |

> **On NFR-8.** Designing for 500 users instead of 500,000 is a real decision.
> It permits a single Postgres instance, straightforward queries, and no caching
> layer. Revisit only when there is evidence to.

---

## 8. Scope & phasing

### MVP — "it works for the five of us"

Auth · create habits (binary + numeric) · daily/weekly schedules · log & backfill
7 days · consistency score · forgiving streak with skip · one group · shared/private
per habit · group feed with reactions · heatmap · data export.

**Definition of done:** you and four friends use it daily for three weeks
without anyone reverting to their old app.

### v1.1 — "it survives week six"

Reminders with budget and decay · offline logging + PWA · weekly review · nudges ·
habit templates · pause · duration habits · best/worst weekday.

### v2 — "other groups could use it"

Peer verification · shared group habits · optional leaderboard · integrations
(Apple Health / Google Fit) · multiple groups per user · public template library.

### Explicitly deferred

Native mobile apps · AI coaching · calendar integration · monetisation · web3/tokens ·
anything gamified beyond reactions.

---

## 9. Success metrics

The category's honest benchmark is retention, so measure that first.

| Metric | Definition | MVP target |
|---|---|---|
| **D30 retention** | % of users logging something in week 5 | > 60% (category norm ≈ 10–30%) |
| **Week-6 survival** | % still active at day 42 | > 50% |
| **Lapse recovery** | % of users inactive ≥5 days who log again | > 40% |
| Logging friction | Median seconds from open to first log | < 8 s |
| Group effect | D30 of grouped vs. solo users | Grouped materially higher |
| Notification trust | % of reminders leading to a log within 1 h | > 25% |

**Lapse recovery is the metric that proves the thesis.** If the forgiving design
works, it shows up there and nowhere else.

---

## 10. Domain model (first cut)

Feeds directly into the shared `@habit/shared` package. `User` is modelled in
full in [`data-modeling.dbml`](./data-modeling.dbml) — that file is the source of
truth; the sketch below is kept in step with it. The other entities are still a
first cut.

```
User        id, username, email, password?, role(user|admin), timezone,
            isAccountVerified, verificationToken?, verificationTokenExpiresAt?,
            resetPasswordToken?, resetPasswordTokenExpiresAt?, passwordChangedAt?,
            profileImage?, createdAt, updatedAt, deletedAt?
Group       id, name, ownerId, inviteCode, createdAt
Membership  userId, groupId, role(owner|member), joinedAt
Habit       id, userId, groupId?, name, icon, color, type(binary|numeric|duration),
            target, unit, schedule(json), visibility(private|group),
            allowedMissesPerWeek, archivedAt?
HabitEntry  id, habitId, date(local), status(done|partial|skipped|missed),
            value?, note?, loggedAt
Reaction    id, entryId, userId, kind
Reminder    id, habitId, timeLocal, enabled, consecutiveIgnores
```

### Modelling notes

- **`HabitEntry.date` is a local calendar date, not a timestamp.** Storing it as
  UTC is the classic bug in this domain: a user in Cairo logging at 01:00 gets
  credited to the previous day. Store the resolved local date, and keep
  `loggedAt` separately for auditing.
- **`missed` should be derived, not written.** Do not create rows for days
  nothing happened; compute absence from the schedule at read time. Writing
  "missed" rows makes backfill and schedule changes painful.
- **`skipped` is a first-class status, not a null.** It is what makes FR-2.5 work.
- **`User.timezone` is an IANA name** (`Africa/Cairo`), never a fixed offset —
  an offset breaks across DST and would silently corrupt FR-6.4.
- **`User.password` is nullable.** FR-6.1 permits OAuth signup, and an OAuth user
  has no password to store. Depends on how D3 resolves.
- **`User.role` is system-level** (`user|admin`) and is *not* the same thing as
  `Membership.role` (`owner|member`). Conflating the two is an easy mistake to
  make twice.
- **`User.deletedAt` is a soft delete.** FR-6.3 asks for a cascading hard delete;
  the open question is what that does to entries and reactions other people can
  see in the group feed. Soft delete keeps the option open — it is not the answer.
- **`dayBoundary` (FR-6.5) is not modelled yet**, and neither is a week-start
  preference, which FR-1.4 and FR-2.4 both need in order to agree on when a week
  begins. Both are per-user settings with nowhere to live at the moment.

---

## 11. Out of scope

Habit *coaching* content · therapy or medical claims · calorie/nutrition tracking ·
a full task manager · public social network features (followers, discovery, comments) ·
monetisation of any kind before the friend group is retained.

---

## 12. Open decisions

| # | Decision | Options | Recommendation |
|---|---|---|---|
| D1 | Database | Postgres vs. SQLite | **Postgres** — you need real dates, JSON schedules, and concurrent writers |
| D2 | ORM | Prisma vs. Drizzle | **Prisma** — better migration ergonomics for a solo dev; Nest integration is well-trodden |
| D3 | Auth | Roll your own vs. Auth.js vs. Supabase Auth | Decide before the first endpoint; auth retrofits are expensive |
| D4 | Offline strategy | Optimistic UI + queue vs. full CRDT | **Queue** — habit logs are append-mostly, conflicts are rare |
| D5 | Hosting | Vercel + managed Postgres vs. single VPS | Vercel for web; api needs a persistent host (Nest is not serverless-shaped) |

---

## 13. Sources

Behavioural claims above draw on the following. All are secondary
sources — several are vendor blogs with an interest in the conclusion, and are
treated as directional only (see the caveat in §2).

- [What Is the Problem with Habit Trackers? — Pattrn](https://pattrn.io/blog/what-is-the-problem-with-habit-trackers-and-how-you-can-solve-it)
- [Why Do 90% of People Quit Habit Trackers Within 30 Days? — Moore Momentum](https://mooremomentum.com/blog/why-do-90-of-people-quit-habit-trackers-within-30-days/)
- [Why Habit Trackers Stop Working After Week 6](https://qh88com.org/why-habit-trackers-stop-working-after-week-6-and-what-to-replace-them-with/)
- [Accountability Partner Apps: Ranked by Science — Accountablo](https://www.accountablo.com/blog/accountability-partner-app)
- [Friend Accountability Apps: Build Habits Together — Cohorty](https://www.cohorty.app/blog/friend-accountability-apps-build-habits-together-2025-guide)
- [Social Accountability in Habit Building — Happycado](https://happycado.app/en/social-accountability-habits)
