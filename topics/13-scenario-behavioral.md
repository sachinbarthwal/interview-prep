# Scenario-Based & Behavioral

> These questions test judgment, not memorized facts — there's rarely one
> "correct" answer. What interviewers are actually scoring is whether you reason
> through trade-offs out loud, and whether your behavioral answers have a real,
> specific example behind them rather than a generic platitude.

## Table of Contents

| No. | Question |
|-----|----------|
| 1 | [Concurrent update: User A's stale save overwrites User B's edit](#1-concurrent-update-user-as-stale-save-overwrites-user-bs-edit) |
| 2 | [Your JWT token gets stolen off an unattended laptop](#2-your-jwt-token-gets-stolen-off-an-unattended-laptop) |
| 3 | [1,000+ clients want conflicting business logic changes](#3-1000-clients-want-conflicting-business-logic-changes) |
| 4 | [An API that used to be fast is now over a minute slow](#4-an-api-that-used-to-be-fast-is-now-over-a-minute-slow) |
| 5 | [Code review: Singleton depending on Scoped](#5-code-review-singleton-depending-on-scoped) |
| 6 | [Describe a complex technical problem you solved](#6-describe-a-complex-technical-problem-you-solved) |
| 7 | [How do you troubleshoot performance issues in a distributed system?](#7-how-do-you-troubleshoot-performance-issues-in-a-distributed-system) |
| 8 | [How do you ensure code quality across a team?](#8-how-do-you-ensure-code-quality-across-a-team) |
| 9 | [How do you handle disagreements over technical decisions?](#9-how-do-you-handle-disagreements-over-technical-decisions) |
| 10 | [Walk through a project where you used Angular and .NET together](#10-walk-through-a-project-where-you-used-angular-and-net-together) |
| 11 | [What's the most challenging part of working with microservices?](#11-whats-the-most-challenging-part-of-working-with-microservices) |
| 12 | [How do you stay current with full-stack development?](#12-how-do-you-stay-current-with-full-stack-development) |
| 13 | [Describe a time you had to meet a tight deadline](#13-describe-a-time-you-had-to-meet-a-tight-deadline) |
| 14 | [How do you respond to constructive criticism in code review?](#14-how-do-you-respond-to-constructive-criticism-in-code-review) |
| 15 | [Walk through your role and responsibilities on a past project](#15-walk-through-your-role-and-responsibilities-on-a-past-project) |
| 16 | [An interviewer keeps probing deeper past your comfort zone](#16-an-interviewer-keeps-probing-deeper-past-your-comfort-zone) |

## 1. Concurrent update: User A's stale save overwrites User B's edit

**What's actually happening:** there's no concurrency control — the system reads
a row, and blindly writes it back based on what was read, regardless of whether
another write happened in between ("last write wins" by accident, not by
design).

**How to answer:**
1. Diagnose it as a classic **lost update** problem.
2. Fix it with **optimistic concurrency control** — add a version/timestamp
   column; on save, the `UPDATE` includes `WHERE Version = @originalVersion`,
   and if zero rows are affected, that tells you someone else changed it first
   (see the EF Core example in the [Entity Framework file](03-entity-framework-data-access.md#6-how-do-you-handle-concurrency-conflicts-in-ef-core)).
3. Decide the UX for the conflict: reject User B's save and ask them to
   re-review the current data (safest default), attempt a field-level merge if
   the changes don't overlap, or — for scenarios where losing the latest change
   is genuinely unacceptable — use **pessimistic locking** instead (lock the row
   for the duration of the edit), accepting the throughput cost that comes with
   it.

**[⬆ Back to Top](#table-of-contents)**

## 2. Your JWT token gets stolen off an unattended laptop

**Immediate response:** treat the token as compromised — if the system supports
revocation (a token blocklist, or a "security stamp"/version field checked on
each request), revoke it immediately; if not, at minimum rotate/invalidate the
associated refresh token so no new access token can be minted, and force a
re-login.

**Systemic fixes to mention, since this is really a "how do you design against
this" question:**
- Keep access token lifetimes **short** (minutes, not days) so a stolen token's
  exposure window is naturally small.
- Use **refresh tokens** that can be revoked server-side, rather than
  long-lived access tokens.
- Consider binding tokens to a device fingerprint or IP range where feasible, so
  a stolen token used from an unexpected context can be flagged/rejected.
- At the org level: enforce automatic screen lock, which is the actual root
  cause here, not a code-level fix.

**[⬆ Back to Top](#table-of-contents)**

## 3. 1,000+ clients want conflicting business logic changes

This is a **configuration/extensibility** design question, not a "just add an
if statement" question.

- **Feature flags/toggles** scoped per client/tenant, so the new behavior only
  activates for clients who opted in.
- **Strategy pattern** — extract the varying logic behind a common interface,
  with a per-client (or per-plan) implementation resolved at runtime, instead of
  branching on client ID inline throughout the codebase.
- **Per-tenant configuration** stored as data, not code, wherever the difference
  is genuinely just parameters (thresholds, rates) rather than fundamentally
  different logic.
- Explicitly avoid the trap of a single codebase riddled with
  `if (clientId == "Acme") { ... }` scattered across files — that's what makes a
  system unmaintainable at scale.

**[⬆ Back to Top](#table-of-contents)**

## 4. An API that used to be fast is now over a minute slow

Work this like a real investigation, out loud:

1. **Establish what actually changed** — data volume growth is the single most
   common cause (a query that was fine against 10K rows can fall over at 50M
   without a supporting index).
2. **Profile, don't guess** — get the actual execution plan/APM trace for a slow
   request; check whether the time is in the database, in application code, or
   in a downstream call.
3. **Common suspects for "this used to be fast":** a missing or now-ineffective
   index as data grew, stale statistics causing a bad query plan, an N+1 query
   introduced by a later code change, a downstream dependency that's slowed down,
   or a cache that used to exist and quietly stopped working.
4. **Fix and verify** — apply the targeted fix (index, query rewrite, caching,
   pagination) and confirm with the same profiling tool, not just "it feels
   faster."

**[⬆ Back to Top](#table-of-contents)**

## 5. Code review: Singleton depending on Scoped

See the full explanation with code in the
[.NET Core / Web API file](02-dotnet-aspnet-webapi.md#10-code-review-singleton-depending-on-scoped--whats-wrong) —
short version: it's a **captive dependency** bug. The `Singleton` captures one
instance of the `Scoped` service forever at first construction, so every request
after that shares stale (or, worse, disposed) state instead of getting the fresh
per-request instance it was registered for.

**[⬆ Back to Top](#table-of-contents)**

## 6. Describe a complex technical problem you solved

Use a **STAR** structure (Situation, Task, Action, Result), but keep it tight —
this shouldn't be a five-minute monologue:
- **Situation/Task** — one or two sentences of context on what was broken/needed
  and why it mattered.
- **Action** — the bulk of the answer: what *you* specifically did, the
  alternatives you considered and why you rejected them, not just the team's
  activity in general.
- **Result** — a concrete, ideally measurable outcome (latency dropped from X to
  Y, an incident class stopped recurring, a migration completed with zero
  downtime).

Prepare 2–3 of these in advance so you're not improvising the structure live —
have one that's clearly technical/architectural and one that involves a
people/process dimension.

**[⬆ Back to Top](#table-of-contents)**

## 7. How do you troubleshoot performance issues in a distributed system?

1. **Establish where the time is actually going** first — distributed tracing
   (a correlation ID through every hop) is the single highest-leverage tool
   here; don't start optimizing a service that isn't actually the bottleneck.
2. Check for the usual distributed-systems suspects: a downstream service with
   degraded latency, a lock/contention point shared across instances, a
   thundering-herd retry storm, or a connection-pool exhaustion issue.
3. **Reproduce it under load** if possible (a load test against a
   staging/pre-prod environment) rather than guessing from production metrics
   alone.
4. Fix the actual bottleneck, then re-measure with the same tracing/metrics to
   confirm the fix, not just "the ticket is closed."

**[⬆ Back to Top](#table-of-contents)**

## 8. How do you ensure code quality across a team?

Code reviews with real substance (not rubber-stamp approvals), automated checks
enforced in CI (linting, formatting, test coverage gates) so review time is spent
on design/logic rather than style nits, a shared and written-down set of
conventions so reviews aren't relitigating personal preference every time, and
pairing/mentoring junior engineers on trickier changes rather than only
reviewing after the fact. Mention a concrete practice you've personally driven,
not just a list of generic best practices.

**[⬆ Back to Top](#table-of-contents)**

## 9. How do you handle disagreements over technical decisions?

Lead with **data over opinion** — a benchmark, a prototype, a concrete trade-off
comparison beats "I think X is better." State the other person's position back
to them accurately before countering it, to make sure the disagreement is real
and not a miscommunication. If it's a genuine judgment call with no clearly
correct answer, default to whoever owns the long-term maintenance of that code,
or escalate to a lightweight decision (a time-boxed spike, or a tech lead's
call) rather than letting it stall the team. And be honest that you've been on
the losing side of one of these before, and it worked out fine — that's a more
credible answer than claiming you're always right.

**[⬆ Back to Top](#table-of-contents)**

## 10. Walk through a project where you used Angular and .NET together

Structure it as: what the app did, the shape of the architecture (Angular SPA
consuming a .NET Web API, how auth flowed between them, how the API was
structured), one specific technical decision you made and why (e.g. choosing
`OnPush` change detection for a data-heavy dashboard, or a particular caching
strategy on the API side), and a challenge you hit at the seam between the two —
CORS configuration, a serialization mismatch (`camelCase` vs `PascalCase`
JSON), or a shared type-contract problem between TypeScript and C# — and how you
resolved it.

**[⬆ Back to Top](#table-of-contents)**

## 11. What's the most challenging part of working with microservices?

A credible, specific answer usually lands on one of: **debugging across service
boundaries** (a single user-facing failure can originate several hops away, and
without good distributed tracing it's genuinely hard to find), **data
consistency** without a shared database/transaction, or **operational
complexity** (more deployments, more moving pieces, more places for
configuration drift). Pick one, give a concrete example of it biting you, and
say what practice you adopted in response (e.g. correlation IDs everywhere,
after a specific incident that was painful to trace without them).

**[⬆ Back to Top](#table-of-contents)**

## 12. How do you stay current with full-stack development?

Be specific rather than listing generic sources: a particular newsletter/blog
you actually read, release notes you follow for the frameworks you use daily
(.NET's, Angular's), a side project you use to try new features before adopting
them at work, or a conference talk/RFC that changed how you approach something.
"I read Hacker News" is not a differentiated answer; "I keep an eye on the .NET
release notes each cycle and try the preview SDK against a side project before
we adopt it at work" is.

**[⬆ Back to Top](#table-of-contents)**

## 13. Describe a time you had to meet a tight deadline

STAR again, but the interesting part interviewers are listening for is **what
you cut or triaged**, not that you worked longer hours. A strong answer names a
specific trade-off you made deliberately (deferred a nice-to-have, shipped
behind a flag, cut test coverage on a low-risk path *and said so explicitly to
the team*) rather than implying you simply did everything, faster.

**[⬆ Back to Top](#table-of-contents)**

## 14. How do you respond to constructive criticism in code review?

The strongest answer treats review feedback as a normal, low-stakes part of the
process — evaluate the feedback on its merits, ask a clarifying question if the
concern isn't clear rather than assuming you know what they meant, and change
your approach when they're right without treating it as a loss. If you disagree,
explain your reasoning rather than either capitulating silently or digging in —
and if you've ever been wrong and updated your approach based on review
feedback, that's a genuinely good, concrete example to have ready.

**[⬆ Back to Top](#table-of-contents)**

## 15. Walk through your role and responsibilities on a past project

Be concrete about scope: what you personally owned end-to-end (a specific
service, a feature area, a migration) versus what you contributed to as part of
a larger team effort — interviewers are listening for whether you can clearly
separate "the team did X" from "I specifically did Y." Mention the technologies
involved only in service of explaining the actual responsibility, not as a
keyword list.

**[⬆ Back to Top](#table-of-contents)**

## 16. An interviewer keeps probing deeper past your comfort zone

This happens in genuinely tough technical rounds — an interviewer asks you to
explain a concept, then keeps pushing ("what happens at a memory level," "how
does this compare to that other approach") past where your knowledge is solid.

**How to handle it:**
- It's completely fine, and more credible than bluffing, to say plainly: "I
  haven't gone that deep into it — my understanding stops around here, and in
  practice I'd look that specific detail up rather than rely on memory."
- Show your reasoning process on the parts you *do* know, rather than going
  silent — interviewers are often evaluating how you think under pressure at
  least as much as raw recall.
- If a term comes up that you can name but not fully explain, say so rather
  than guessing confidently and being wrong — a wrong confident answer reads
  worse than an honest "I'd need to check."
- Afterward, treat it as free diagnostic information: whatever they kept
  drilling into is exactly what to go deepen before the next interview.

**[⬆ Back to Top](#table-of-contents)**
