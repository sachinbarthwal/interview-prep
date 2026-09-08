# Session log — resume here

Running prep with Claude for **RBC** (Senior .NET Dev, Direct Investing trading
platform, contract-to-hire) and **GlobalLogic** (.NET Technical Lead, remote
Canada). This file is the "where were we" marker so any machine can pick up.

## Consolidated prep guide (separate artifact)

https://claude.ai/code/artifact/42b87175-17db-43d5-bb04-cc6fe238da4b
— recruiter-screen prep, shared technical core, RBC vs GlobalLogic specifics.

## What's been added to this repo

- `topics/09-concurrency-async.md` §14–§21 — a ground-up rebuild of
  async / await / Task / return types, written plain-language with full code
  (no assumed methods). Covers: threads as workers, blocking vs awaiting,
  what each keyword does, `Task` without `async` (pass-through /
  `Task.FromResult` / `Task.Run`), a controller→service→repo thread walk,
  `SynchronizationContext` / `ConfigureAwait(false)`, `IActionResult` vs
  `ActionResult<T>` and why `async IActionResult` won't compile, `IQueryable`
  vs `IEnumerable`, EF Core async methods.

## Live mock interview — state

Format: interviewer asks one question, evaluates, pushes on shallow answers.

- **Q1 — async/await** (`.Result` in a controller, resumption, sync context):
  DONE. Answer was directionally right; gaps were the legacy-ASP.NET deadlock
  mechanism and the sync-context / `ConfigureAwait` story. Now written up in §14–§18.
- **Q2 — `IQueryable` vs `IEnumerable`** (`ToListAsync()` then `.Where()`):
  DONE. Diagnosis correct ("brings all data then filters"); needed the precise
  vocabulary — materialisation, expression trees, deferred execution. Written up in §20.
- **Q3 — SQL Server (OPEN — start here):**
  ```sql
  SELECT * FROM Orders WHERE CustomerId = 42 ORDER BY CreatedUtc DESC;
  ```
  20M rows. Non-clustered index on `CustomerId` exists. Query still slow and the
  plan sometimes ignores the index. Answer:
  1. Why would SQL Server ignore that non-clustered index?
  2. What is a covering index, and what would you build for this exact query?
  3. What does `SELECT *` cost you here specifically?

## Foundations roadmap (agreed order)

1. **C# language mechanics** — value vs reference types, `Order?` nullable refs,
   properties (`get`/`set`/`init`), interfaces & polymorphism, generics,
   delegates/`Func`/`Action`/lambdas, extension methods, expression trees.
2. **Async/await** — mostly covered now (§14–§18).
3. **LINQ** — `IEnumerable` vs `IQueryable`, deferred execution, operators
   (§20 covers the core).
4. **EF Core** — `DbContext`/`DbSet`/lifetimes, tracking vs `AsNoTracking`,
   `Include` / eager vs lazy, N+1, migrations.
5. **ASP.NET Core** — DI & service lifetimes, controllers/routing/model binding,
   middleware pipeline, `IActionResult`/`ActionResult<T>`/minimal APIs, filters, auth.
6. **SQL Server** — clustered/non-clustered/covering indexes, execution plans,
   isolation levels & locking, query tuning.

Then: system design, microservices, Kafka/Redis, Azure, design patterns, testing.

## Hands-on coding kata

Lives in the other repo (`C:\GitHub\Prep` — `Practice/`, `Practice.Tests/`,
`Practice.Solutions/`). 12 stubs, 39 xUnit tests, no AI. Write the code, ask for a
review of the finished attempt.
