# Interview Prep — .NET / Angular / SQL Server / Azure / Systems

Personal, living interview-preparation reference. Built from years of real interview
notes (Infosys, UKG, AVL, Nagarro, Centric Consulting, Policy Bazaar, Dayforce, Uplers,
PureSoftware/Saxo Bank, Fiserv, and more) plus deep-dive study notes on the
underlying concepts. Unlike a plain question dump, every topic file explains the
*concept*, shows a short example where it helps, and gives you a sense of what a
strong verbal answer sounds like — so you can actually study from this, not just
skim questions the night before.

## Practice quiz

[**Open the drill app →**](https://sachinbarthwal.github.io/interview-prep/) (live once
GitHub Pages is enabled on this repo — see below)

All 260 questions above are also playable as spaced-repetition flashcards: flip a
card, self-rate "Still learning" or "Got it", and missed cards resurface sooner
than ones you know cold. It tracks a daily streak, XP, and a per-topic mastery bar
— all stored only in your browser (`localStorage`), nothing leaves your device.

**To enable it** (one-time): repo → **Settings** → **Pages** → under "Build and
deployment", set **Source** to "Deploy from a branch", **Branch** to `main` /
`docs`, then save. The site publishes at `https://<your-username>.github.io/interview-prep/`.

**To regenerate it** after editing any file in `topics/`, run:

```bash
python scripts/build_quiz.py
```

This re-parses every topic file straight into `docs/index.html` — the quiz content
always mirrors the reference docs, so you only ever edit the Markdown.

## How to use this

1. **A week or more out:** read a topic file top to bottom. The "Core Concepts"
   section in each file is where the depth is — that's what separates a junior
   answer from a senior one.
2. **The night before / morning of:** skim the "Rapid-Fire Reference" table at the
   bottom of each file. It's a one-line-per-question cram sheet covering everything,
   including the more repetitive/company-specific questions.
3. **After every interview:** add anything new you got asked into the relevant file.
   This repo is meant to grow — it's cheaper to spend two minutes updating a file
   than to relearn the same gap next time.

## Topics

| # | File | Covers |
|---|------|--------|
| 1 | [C# & OOP Fundamentals](topics/01-csharp-oop.md) | OOP pillars, value/reference types, generics, delegates, GC, collections internals |
| 2 | [.NET Core, ASP.NET MVC & Web API](topics/02-dotnet-aspnet-webapi.md) | DI, middleware, filters, routing, REST design, auth (JWT/OAuth), WCF |
| 3 | [Entity Framework, ADO.NET & Data Access](topics/03-entity-framework-data-access.md) | EF Core vs Dapper, loading strategies, concurrency, migrations |
| 4 | [SQL Server & Databases](topics/04-sql-server.md) | Indexing, execution plans, CTEs, window functions, multi-tenant schema design |
| 5 | [Angular & Frontend](topics/05-angular-frontend.md) | Lifecycle, RxJS, change detection, state management, modern Angular (Signals, SSR, standalone) |
| 6 | [Cloud & Azure](topics/06-azure-cloud.md) | Storage, Service Bus vs Event Hubs, Key Vault, APIM, CI/CD, deployment models |
| 7 | [Microservices & System Architecture](topics/07-microservices-architecture.md) | Clean Architecture, data consistency (Saga/CQRS), inter-service comms, security |
| 8 | [Design Patterns & SOLID](topics/08-design-patterns-solid.md) | SOLID with real violations/fixes, Singleton/Factory/Repository/Memento |
| 9 | [Multithreading, Async & Concurrency](topics/09-concurrency-async.md) | Thread vs Task, TPL/TAP, locking, async/await internals |
| 10 | [Testing, TDD & Code Quality](topics/10-testing-quality.md) | Arrange-Act-Assert, mocks vs stubs vs fakes, testing DI code |
| 11 | [DevOps, Git & Agile](topics/11-devops-git-agile.md) | CI/CD pipelines, git conflict resolution, Agile/Scrum in practice |
| 12 | [Coding & Algorithm Challenges](topics/12-coding-challenges.md) | LRU cache, array/string problems, SQL algorithmic queries, worked solutions |
| 13 | [Scenario-Based & Behavioral](topics/13-scenario-behavioral.md) | Production-incident scenarios, system-design prompts, STAR-format behavioral answers |

## A study plan if you have 2 weeks

- **Days 1–3:** Files 1–3 (C#, .NET Core/Web API, EF) — this is the bulk of any
  .NET interview and most other topics build on it.
- **Days 4–5:** File 4 (SQL Server) — practice writing the queries by hand, not
  just reading them.
- **Days 6–7:** Files 5–6 (Angular, Azure) if the role needs them; skip if it's
  backend-only.
- **Days 8–9:** Files 7–9 (Architecture, Design Patterns, Concurrency) — this is
  what separates mid from senior answers.
- **Day 10:** Files 10–11 (Testing, DevOps/Agile) — usually quick, often skipped
  by candidates, easy points if you're solid.
- **Days 11–13:** File 12 (Coding) — actually write the code, don't just read it.
- **Day 14:** File 13 (Scenario/Behavioral) — rehearse out loud, not just in your head.

## Notes on sourcing

The original raw material was a mix of personal interview notes across ~10 companies,
generic prep checklists, and ChatGPT-assisted study sessions. Duplicate questions
across companies were merged; the content here is organized by *concept* rather than
by *company*, since the same 40–50 core ideas get asked everywhere with different
phrasing.
