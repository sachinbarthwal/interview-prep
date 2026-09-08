# Multithreading, Async & Concurrency

> This topic separates people who've used `async`/`await` from people who
> understand what it's actually doing to the thread pool. Lead with the mental
> model, not just syntax.

## Table of Contents

| No. | Question |
|-----|----------|
| 1 | [`Thread` vs `Task`](#1-thread-vs-task) |
| 2 | [Ways to create a thread in C#](#2-ways-to-create-a-thread-in-c) |
| 3 | [Thread safety and thread affinity](#3-thread-safety-and-thread-affinity) |
| 4 | [What is the Task Parallel Library (TPL)?](#4-what-is-the-task-parallel-library-tpl) |
| 5 | [What is the Task-based Asynchronous Pattern (TAP)?](#5-what-is-the-task-based-asynchronous-pattern-tap) |
| 6 | [What is a `ConcurrentDictionary`?](#6-what-is-a-concurrentdictionary) |
| 7 | [Worked example: print 1–10 using two threads](#7-worked-example-print-110-using-two-threads) |
| 8 | [How do you force async code to run synchronously — and why not to](#8-how-do-you-force-async-code-to-run-synchronously--and-why-not-to) |
| 9 | [How do you cancel a running Task?](#9-how-do-you-cancel-a-running-task) |
| 10 | [What should you consider when writing async code?](#10-what-should-you-consider-when-writing-async-code) |
| 11 | [What's the actual benefit of `async`/`await` over raw `Task`?](#11-whats-the-actual-benefit-of-asyncawait-over-raw-task) |
| 12 | [Multithreading vs concurrency](#12-multithreading-vs-concurrency) |
| 13 | [Encrypting/decrypting data, and encoding vs encrypting](#13-encryptingdecrypting-data-and-encoding-vs-encrypting) |
| 14 | [Ground-up: threads as workers, blocking vs awaiting](#14-ground-up-threads-as-workers-blocking-vs-awaiting) |
| 15 | [What `async`, `await`, `Task` and `Task<T>` each actually do](#15-what-async-await-task-and-taskt-each-actually-do) |
| 16 | [`Task` without `async`: pass-through, `Task.FromResult`, `Task.Run`](#16-task-without-async-pass-through-taskfromresult-taskrun) |
| 17 | [Walking one thread through a controller → service → repo chain](#17-walking-one-thread-through-a-controller--service--repo-chain) |
| 18 | [`SynchronizationContext` and `ConfigureAwait(false)` in plain terms](#18-synchronizationcontext-and-configureawaitfalse-in-plain-terms) |
| 19 | [Return types: `IActionResult` vs `ActionResult<T>` vs `Task<...>`, and why `async IActionResult` is illegal](#19-return-types-iactionresult-vs-actionresultt-vs-task-and-why-async-iactionresult-is-illegal) |
| 20 | [`IQueryable` vs `IEnumerable`, deferred execution, expression trees](#20-iqueryable-vs-ienumerable-deferred-execution-expression-trees) |
| 21 | [EF Core async query methods worth memorising](#21-ef-core-async-query-methods-worth-memorising) |

## 1. `Thread` vs `Task`

A **`Thread`** is a raw OS-level thread — you manage its lifecycle directly, and
it's relatively expensive to create. A **`Task`** is a higher-level abstraction
representing a unit of work that runs on the **thread pool** by default — the
runtime manages scheduling, reuses pooled threads instead of creating new OS
threads per task, and `Task` composes cleanly with `async`/`await`,
continuations (`ContinueWith`), and cancellation. In modern C#, you almost always
want `Task`, not a raw `Thread` — reach for `Thread` only when you specifically
need a dedicated, long-lived, foreground/background-controlled thread outside the
pool.

```csharp
Thread t = new Thread(() => Console.WriteLine("Raw OS thread"));
t.Start(); // you manage this thread's lifecycle yourself

Task task = Task.Run(() => Console.WriteLine("Runs on a pooled thread"));
await task; // the runtime schedules and reuses threads for you
```

**[⬆ Back to Top](#table-of-contents)**

## 2. Ways to create a thread in C#

```csharp
// Raw Thread
var t = new Thread(() => DoWork());
t.Start();

// ThreadPool (no Task wrapper)
ThreadPool.QueueUserWorkItem(_ => DoWork());

// Task (preferred in modern code)
Task.Run(() => DoWork());

// Parallel loops (internally use Tasks/the thread pool)
Parallel.For(0, 10, i => DoWork(i));
```

**[⬆ Back to Top](#table-of-contents)**

## 3. Thread safety and thread affinity

**Thread safety** means shared state behaves correctly when accessed from
multiple threads concurrently — usually achieved via locking (`lock`), immutable
data, or thread-safe collections (`ConcurrentDictionary`). **Thread affinity**
means some piece of code/resource must only ever be touched from one specific
thread — the classic example is UI frameworks (WinForms/WPF), where UI controls
can only be safely updated from the UI thread, and touching them from a
background thread throws a cross-thread-operation exception.

**[⬆ Back to Top](#table-of-contents)**

## 4. What is the Task Parallel Library (TPL)?

The `System.Threading.Tasks` library — `Task`/`Task<T>`, `Parallel.For`/
`Parallel.ForEach`, and the dataflow/continuation APIs — that provides
higher-level constructs for parallel and asynchronous programming on top of the
thread pool, so you rarely need to manage raw `Thread` objects directly.

**[⬆ Back to Top](#table-of-contents)**

## 5. What is the Task-based Asynchronous Pattern (TAP)?

The standard convention (superseding the older APM/EAP patterns) for exposing
asynchronous operations in .NET: a method named `XxxAsync` that returns a
`Task`/`Task<T>`, which callers can `await`, chain with continuations, or combine
with `Task.WhenAll`/`Task.WhenAny`. It's the pattern every modern async API in
.NET follows, which is what makes `async`/`await` interoperate cleanly across
the whole framework.

**[⬆ Back to Top](#table-of-contents)**

## 6. What is a `ConcurrentDictionary`?

A thread-safe dictionary implementation designed for high-concurrency scenarios —
multiple threads can read and write it simultaneously without external locking,
using fine-grained internal locking (or lock-free techniques) rather than a
single global lock. Use it instead of wrapping a plain `Dictionary` in your own
`lock` whenever multiple threads genuinely need concurrent read/write access; for
single-threaded or externally-synchronized access, a plain `Dictionary` is faster.

```csharp
var counts = new ConcurrentDictionary<string, int>();

// safe to call from many threads at once, no manual lock needed
Parallel.For(0, 1000, i =>
{
    counts.AddOrUpdate("hits", 1, (key, oldValue) => oldValue + 1);
});

Console.WriteLine(counts["hits"]); // reliably 1000 — a plain Dictionary here would corrupt or throw
```

**[⬆ Back to Top](#table-of-contents)**

## 7. Worked example: print 1–10 using two threads

```csharp
public class NumberPrinter
{
    private static int _current = 1;
    private static readonly object _lock = new();

    public static void Main()
    {
        Task t1 = Task.Run(PrintNumbers);
        Task t2 = Task.Run(PrintNumbers);
        Task.WaitAll(t1, t2);
    }

    private static void PrintNumbers()
    {
        while (true)
        {
            int numberToPrint;
            lock (_lock)
            {
                if (_current > 10) return;
                numberToPrint = _current++;
            }
            Console.WriteLine(numberToPrint); // outside the lock, see below
        }
    }
}
```

**Why is the counter and lock object `static`?** Both threads run the *same*
method on *conceptually separate* invocations, but they need to coordinate over
**one shared counter** — `static` is what makes `_current` and `_lock` a single
shared piece of state rather than per-call-instance state.

**Why `lock (_lock)`?** Without it, two threads could both read `_current`, both
compute the same "next" value, and print/increment based on stale data — a
classic race condition. The lock makes "read current value, then increment it"
atomic.

**Why is `Console.WriteLine` outside the lock?** To keep the critical section as
short as possible — the lock only needs to protect the shared counter, not the
(comparatively slow, and independent) act of writing to the console. Holding the
lock longer than necessary increases contention and hurts the whole point of
using two threads.

**[⬆ Back to Top](#table-of-contents)**

## 8. How do you force async code to run synchronously — and why not to

You can block on it with `.Result`, `.Wait()`, or `.GetAwaiter().GetResult()`:

```csharp
var result = SomeAsyncMethod().GetAwaiter().GetResult();
```

**Why this is usually a bad idea:** it defeats the entire purpose of being async
— you're blocking a thread waiting for work that was designed to free the thread
up. Worse, in contexts with a captured `SynchronizationContext` (classic ASP.NET,
UI apps), calling `.Result`/`.Wait()` synchronously from that same context can
**deadlock**, because the awaited continuation is trying to resume on the very
context that's currently blocked waiting for it. Modern ASP.NET Core doesn't have
that particular `SynchronizationContext` trap, but blocking on async code still
wastes a pool thread and hurts scalability either way — the fix is almost always
"make the caller async too," not to force synchronicity.

```csharp
// BAD: blocking on async code can deadlock in web/UI apps, and always wastes a thread
string data = GetDataAsync().Result;

// GOOD: await all the way up the call stack instead
string data = await GetDataAsync();
```

**[⬆ Back to Top](#table-of-contents)**

## 9. How do you cancel a running Task?

Via `CancellationToken`, cooperatively — the task has to check the token itself,
cancellation doesn't forcibly kill a thread:

```csharp
var cts = new CancellationTokenSource();

Task task = Task.Run(() =>
{
    for (int i = 0; i < 1000; i++)
    {
        cts.Token.ThrowIfCancellationRequested();
        DoWork();
    }
}, cts.Token);

cts.Cancel(); // requests cancellation
```

**[⬆ Back to Top](#table-of-contents)**

## 10. What should you consider when writing async code?

- Use `async` all the way up the call stack — don't mix blocking calls
  (`.Result`) into an otherwise-async chain.
- Use `ConfigureAwait(false)` in library code that doesn't need to resume on the
  original context, to avoid unnecessary context-switching overhead.
- Don't make a method `async` just because it calls something async — only if it
  actually needs to `await` and do something with the result/exception.
- Pass a `CancellationToken` through any long-running async operation.
- Avoid `async void` except for top-level event handlers — exceptions thrown
  from `async void` can't be caught by the caller the way `async Task` exceptions
  can.

**[⬆ Back to Top](#table-of-contents)**

## 11. What's the actual benefit of `async`/`await` over raw `Task`?

You *can* compose raw `Task` objects with `.ContinueWith()` chains, but it gets
unreadable fast, and exception handling across a chain of continuations is
awkward. `async`/`await` lets you write asynchronous code that **reads like
sequential code** — normal `try`/`catch`, normal control flow (`if`, loops)
around `await` points — while the compiler does the equivalent state-machine
transformation under the hood. The benefit is entirely about *readability and
correctness of the calling code*, not a different runtime execution model.

**[⬆ Back to Top](#table-of-contents)**

## 12. Multithreading vs concurrency

**Concurrency** is a broader concept — multiple tasks making progress over the
same time period, which doesn't necessarily require multiple threads (e.g.
`async`/`await` on a single thread interleaving I/O-bound work is concurrent, not
parallel). **Multithreading** is one specific *mechanism* for achieving
concurrency (and true parallelism on multi-core hardware) by literally running
code on multiple OS threads simultaneously. Async I/O achieves concurrency
without necessarily using extra threads at all; CPU-bound parallel work
(`Parallel.For`) genuinely needs multiple threads/cores to go faster.

**[⬆ Back to Top](#table-of-contents)**

## 13. Encrypting/decrypting data, and encoding vs encrypting

**Encoding** (Base64, UTF-8, URL-encoding) transforms data into another
representation for compatibility/transport — it's fully reversible by anyone,
with no secret involved, and provides **zero confidentiality**. **Encrypting**
transforms data so it's unreadable **without a secret key** — genuine
confidentiality. In .NET, symmetric encryption (AES, via
`System.Security.Cryptography.Aes`) is used for bulk data with a shared key;
asymmetric encryption (RSA) is used for scenarios like key exchange or digital
signatures where sender and receiver don't share a secret directly. A common
interview trap: someone describing Base64-encoding a password as "encrypting"
it — it isn't; it provides no protection at all.

**[⬆ Back to Top](#table-of-contents)**

---

# Ground-up deep dive (async / await / Task / return types)

> Added from a study session. This section assumes **nothing** — it rebuilds
> `async`/`await` from "what is a thread" up to controller return types, in plain
> language with complete code (no method left as "assume this exists").

## 14. Ground-up: threads as workers, blocking vs awaiting

A **thread** is one worker. A web server has a limited pool of them (realistically
you want to stay in the low hundreds, often far fewer). A request comes in, grabs
one worker, the worker runs your code line by line, then goes back to the pool for
the next request. If every worker is busy, request N+1 waits in line. **Workers
are precious — you never want one standing frozen doing nothing.**

The problem: your code calls the database, which takes ~200 ms to answer. During
those 200 ms the worker has nothing to do. Two ways to handle the wait:

- **Blocking** (`.Result`, `.Wait()`) — the worker stands frozen at the counter
  until the DB replies. It cannot do anything else.
- **Awaiting** (`await`) — the worker starts the DB call, then *lets go* and
  returns to the pool to serve other requests. When the DB replies, some worker
  (same or different — doesn't matter) picks the work back up and continues.

```csharp
// BAD: worker frozen for the whole DB round-trip
public List<Order> GetOrders()
{
    return _db.Orders.ToList();
}

// GOOD: worker released during the DB round-trip
public async Task<List<Order>> GetOrders()
{
    return await _db.Orders.ToListAsync();
}
```

Both return the same JSON. The difference is invisible for one request on a dev
box; it only shows under **concurrent load**. The blocking version runs out of
workers at ~20 simultaneous slow requests and everything queues. The async version
handles hundreds with the same 20 workers, because a request waiting on I/O holds
**zero** workers.

> Async does not make a single request faster — the client still waits 200 ms.
> It lets the server survive *many* concurrent requests with few threads.

**`.Result` on legacy ASP.NET / WPF / WinForms can deadlock** (see §18). On
**ASP.NET Core** it does not deadlock (there is no `SynchronizationContext`), but
it still causes thread-pool starvation under load. Either way: never block on
async — `await` all the way up.

**[⬆ Back to Top](#table-of-contents)**

## 15. What `async`, `await`, `Task` and `Task<T>` each actually do

**`Task` / `Task<T>` — a value that will exist *later*.**
A normal object (`Order`, `List<Order>`) is a value that exists *now*. A
`Task<Order>` is a handle to the eventual outcome of work still running — at the
moment you receive it, the `Order` does not exist yet. Think of the buzzer a
restaurant hands you: it is not the food, it is a claim you redeem later.

- `Task` = "work running, no result to collect — I'll signal when done."
- `Task<Order>` = "work running; when done you can collect an `Order`."

Internally a `Task<Order>` carries: a **status** (`WaitingForActivation`,
`Running`, `RanToCompletion`, `Faulted`, `Canceled`), a **result slot** (empty
until complete), an **exception slot** (if the work threw, it lands here and
re-throws on `await`), and a **continuation list** (callbacks to run on
completion). A plain `List<Order>` has none of that — it is just data. That is why
no DTO can stand in for `Task`: a DTO cannot be in the state "not done yet."

**`await` — pause here, release the worker, resume from this line when the Task completes.**
Everything *after* the `await` becomes the **continuation** — a callback the
awaited Task invokes when it finishes.

```csharp
public async Task<IActionResult> GetOrders()
{
    var orders = await _db.Orders.ToListAsync();   // split point
    return Ok(orders);                              // <-- the continuation
}
```

**`async` — a compiler instruction, not part of the method's contract.**
It tells the compiler to rewrite the method body into a state machine so `await`
can be used. Callers cannot tell a method is `async` — they only see the return
type. `async` with no `await` inside does nothing but warn.

An `async` method **always** returns `Task`, `Task<T>`, `ValueTask`,
`ValueTask<T>`, `void`, or `IAsyncEnumerable<T>`. There is no `public async Order
Foo()`. What you have seen everywhere is `public async Task<Order> Foo()` — the
`Task<>` is always there; inside you write `return someOrder;` and the compiler
wraps it into `Task<Order>` for you.

`Task<T>` does **not** guarantee a wait — it means "the result *may* be deferred."
A cache hit can complete without ever hitting an `await`:

```csharp
public async Task<Order> GetOrder(int id)
{
    if (_cache.TryGet(id, out var cached))
        return cached;                          // returns an ALREADY-COMPLETED Task, no waiting
    return await _db.Orders.FindAsync(id);      // this path actually waits
}
```

**[⬆ Back to Top](#table-of-contents)**

## 16. `Task` without `async`: pass-through, `Task.FromResult`, `Task.Run`

`async` is one way to *produce* a `Task`. It is not the only way. A method can
return a `Task<T>` with no `async` of its own:

```csharp
// WAY 1 — async + await: compiler builds the pause/resume machinery.
//         Use when you do work BEFORE returning, or await more than one thing,
//         or wrap the await in try/catch.
public async Task<Order?> GetOrderAsync(int id)
{
    var order = await _repo.GetByIdAsync(id);
    if (order != null) order.LastViewedUtc = DateTime.UtcNow;  // work after the wait -> async required
    return order;
}

// WAY 2 — pass-through: forward a Task someone else made. No await, no async.
//         Use when you add nothing — you just relay one call's result unchanged.
public Task<Order?> GetOrderAsync(int id)
{
    return _repo.GetByIdAsync(id);   // hand back the repo's Task as-is
}

// WAY 3 — Task.FromResult: you already hold the value, but your signature
//         promises a Task<T>. Wrap the ready value in a completed Task.
public Task<Order> GetOrderAsync(int id)
{
    if (_cache.TryGet(id, out var cached))
        return Task.FromResult(cached);   // no state machine, no warning
    return _repo.GetByIdAsync(id);
}

// WAY 4 — Task.Run: push CPU-heavy work onto a background pool thread.
//         NOT for I/O (I/O has its own ...Async methods). Rare in web apps.
public Task<Report> BuildAsync(int id)
{
    return Task.Run(() => _calculator.CrunchNumbers(id));
}
```

All four have the identical signature from the caller's side and are consumed the
same way: `var x = await service.GetOrderAsync(5);`

Why avoid `async`/`await` in the pass-through case:

```csharp
// Wasteful — unwrap the Task, then immediately re-wrap the same value in a new Task
public async Task<Order> GetOrder(int id) => await _repo.GetOrderAsync(id);

// Lean — the promise is already what you need
public Task<Order> GetOrder(int id) => _repo.GetOrderAsync(id);
```

The pass-through never *creates* the asynchrony — somewhere at the bottom of the
chain there is either an `async` method with a real `await`, or a framework I/O
method (`FindAsync`, `ToListAsync`, `HttpClient.GetAsync`) that builds the Task
with low-level machinery. The pass-through just carries the buzzer up.

Related helpers: `Task.CompletedTask` (a finished `Task` with no result),
`Task.WhenAll(t1, t2)` (await several in parallel), `Task.FromException(...)`.

**[⬆ Back to Top](#table-of-contents)**

## 17. Walking one thread through a controller → service → repo chain

```csharp
// LAYER 3 — Repository: the only place that talks to the DB
public class OrderRepository
{
    private readonly AppDbContext _db;
    public OrderRepository(AppDbContext db) { _db = db; }

    public async Task<Order?> GetByIdAsync(int id)
    {
        Order? order = await _db.Orders.FindAsync(id);  // the real ~200ms wait is here
        return order;
    }
}

// LAYER 2 — Service: business logic
public class OrderService
{
    private readonly OrderRepository _repo;
    public OrderService(OrderRepository repo) { _repo = repo; }

    public async Task<Order?> GetOrderAsync(int id)
    {
        Order? order = await _repo.GetByIdAsync(id);
        if (order != null) order.LastViewedUtc = DateTime.UtcNow;  // work after wait -> async
        return order;
    }
}

// LAYER 1 — Controller: HTTP
[ApiController]
[Route("orders")]
public class OrdersController : ControllerBase
{
    private readonly OrderService _service;
    public OrdersController(OrderService service) { _service = service; }

    [HttpGet("{id}")]
    public async Task<ActionResult<Order>> GetOrder(int id)
    {
        Order? order = await _service.GetOrderAsync(id);
        if (order == null) return NotFound();
        return order;
    }
}
```

`GET /orders/5` arrives; the pool assigns **Worker-1**.

1. Worker-1 runs `GetOrder` → calls `GetOrderAsync` → calls `GetByIdAsync` →
   calls `_db.Orders.FindAsync(5)`.
2. `FindAsync` fires the SQL and immediately returns an **incomplete** `Task<Order?>`.
3. `GetByIdAsync` hits `await` on it, stops, and returns its own **incomplete**
   `Task<Order?>` to the service.
4. `GetOrderAsync` was also at `await` → stops, returns its own incomplete Task to
   the controller.
5. `GetOrder` was also at `await` → stops, returns its incomplete
   `Task<ActionResult<Order>>` to ASP.NET.
6. Worker-1 has fully unwound → **back to the pool. Zero threads are now working
   on this request.** The DB is busy; nobody holds a thread.
7. ~200 ms later the DB replies. The pool grabs a free worker (maybe Worker-2) and
   runs the continuations bottom-up: `return order` in `GetByIdAsync` completes
   its Task → wakes `GetOrderAsync` (`order.LastViewedUtc = ...; return order`) →
   wakes `GetOrder` (`return order` / `NotFound`) → final Task completes → ASP.NET
   writes the HTTP response.

The win: the thread was free for the entire 200 ms the DB was working. The client
still waited 200 ms; the server burned no thread doing so.

**[⬆ Back to Top](#table-of-contents)**

## 18. `SynchronizationContext` and `ConfigureAwait(false)` in plain terms

**For ASP.NET Core web APIs you can ignore both.** They matter for desktop apps
(WPF/WinForms) and legacy .NET Framework ASP.NET.

A **`SynchronizationContext`** is an object whose one job is: given a piece of
work, decide *which thread* it runs on. Different app models plug in different
ones:

| App model | `SynchronizationContext.Current` | effect |
|---|---|---|
| WinForms / WPF | a UI-thread context | continuations resume on the single UI thread (required to touch controls) |
| Legacy ASP.NET (Framework) | a per-request context | one thread at a time per request; flows `HttpContext.Current` |
| **ASP.NET Core** | **`null`** | continuations just run on any free thread-pool thread |
| Console app | `null` | thread pool |

By default `await` captures `SynchronizationContext.Current` before suspending and
posts the continuation back onto it. That is how UI code automatically resumes on
the UI thread.

**The deadlock** (legacy ASP.NET / UI): a thread calls `.Result` and blocks while
*still holding* the single-thread context. The awaited operation's continuation
needs that same context to resume — but the only thread for it is blocked on
`.Result`. Circular wait, permanent hang. **ASP.NET Core has no such context, so
`.Result` there starves the pool but does not deadlock.**

**`ConfigureAwait(false)`** tells `await`: "don't capture the context — resume on
any thread-pool thread."

```csharp
var data = await httpClient.GetStringAsync(url).ConfigureAwait(false);
```

- **Library code:** use it everywhere — you don't know your caller, and not
  capturing avoids the deadlock risk and a needless thread hop.
- **UI event handlers:** don't — you need to be back on the UI thread.
- **ASP.NET Core controllers:** no-op (context is already `null`); harmless but
  pointless in your own code, common in shared libraries.

One sentence to remember: **`ConfigureAwait(false)` is a desktop/library concern;
in ASP.NET Core it does nothing.**

**[⬆ Back to Top](#table-of-contents)**

## 19. Return types: `IActionResult` vs `ActionResult<T>` vs `Task<...>`, and why `async IActionResult` is illegal

A controller-action signature answers **two independent questions**:

1. **What does the endpoint produce?** → `IActionResult`, `ActionResult<T>`, or a
   bare type like `List<Order>` / `string`.
2. **Is it ready when the method returns, or later?** → bare (ready now, sync) vs
   `Task<...>` (ready later, async).

**`IActionResult`** — "a response," you build it explicitly. Lets one method
return different status codes:

```csharp
public async Task<IActionResult> GetOrder(int id)
{
    var order = await _db.Orders.FindAsync(id);
    if (order == null) return NotFound();   // 404
    return Ok(order);                        // 200 + JSON
}
```

**bare `List<Order>` / `string`** — ASP.NET Core auto-wraps it in `200 OK` +
JSON. Fine when there are no error branches; you lose clean status-code control.

**`ActionResult<T>`** — best of both, recommended for APIs. Return `T` directly
*or* an action result:

```csharp
public async Task<ActionResult<Order>> GetOrder(int id)
{
    var order = await _db.Orders.FindAsync(id);
    if (order == null) return NotFound();   // IActionResult path
    return order;                            // T path -> 200 + JSON, no Ok(...)
}
```

It works via **implicit conversion operators** — no runtime magic:

```csharp
public sealed class ActionResult<TValue>
{
    public TValue?       Value  { get; }   // set when you return a T
    public ActionResult? Result { get; }   // set when you return NotFound() etc.

    public ActionResult(TValue value)        { Value  = value; }
    public ActionResult(ActionResult result) { Result = result; }

    public static implicit operator ActionResult<TValue>(TValue value)
        => new ActionResult<TValue>(value);
    public static implicit operator ActionResult<TValue>(ActionResult result)
        => new ActionResult<TValue>(result);
}
```

`return order;` → compiler inserts `new ActionResult<Order>(order)` (`Value` set).
`return NotFound();` → `new ActionResult<Order>(new NotFoundResult())` (`Result`
set). MVC then checks: `Result != null` → execute it; else wrap `Value` as
`ObjectResult` with status 200. So `return order;` and `return Ok(order);` produce
the identical response — `ActionResult<T>` also tells Swagger/OpenAPI the 200 body
type, which bare `IActionResult` hides.

**The four signature forms:**

| Form | Compiles? | `await` inside? | Use |
|---|---|---|---|
| `IActionResult Foo()` | yes | no | no I/O — constants, memory, CPU |
| `async Task<IActionResult> Foo()` | yes | yes | awaits I/O **and** has logic around it — the normal async action |
| `Task<IActionResult> Foo()` (no `async`) | yes | no | pure pass-through of one async call |
| `async IActionResult Foo()` | **NO** — CS1983 | — | illegal |

**Why `async IActionResult` is illegal:** `async` means the method returns to its
caller *before its body finishes* (at the first incomplete `await`). At that
moment the finished `IActionResult` does not exist yet — the only honest thing to
hand back is a *promise* of one, i.e. `Task<IActionResult>`. An `IActionResult` is
by definition a finished value; there is no "incomplete `IActionResult`." So the
compiler requires an `async` method to return a task-like type (or `void`).

Also: `await` without `async` on the method → CS4033. `async` and `await` are a
package deal.

**[⬆ Back to Top](#table-of-contents)**

## 20. `IQueryable` vs `IEnumerable`, deferred execution, expression trees

```csharp
// BUG: pulls EVERY order into memory, then filters in C#
var orders = await _db.Orders.ToListAsync();
return orders.Where(o => o.Total > 1000).ToList();

// FIX: filter before materialisation -> becomes SQL WHERE
return await _db.Orders.Where(o => o.Total > 1000).ToListAsync();
```

**`IEnumerable<T>`** — "a sequence you iterate in memory, now." Its LINQ operators
(`System.Linq.Enumerable`) take **compiled delegates** (`Func<T,bool>`) and run
**in your process**. Once you've called `ToList()` / `ToListAsync()` /
`AsEnumerable()`, you hold an in-memory collection and every later operation is
LINQ-to-Objects, running locally.

**`IQueryable<T>`** — "a *description* of a query against a remote source that has
not run yet." It adds an **`Expression`** (the query as a data structure) and a
**`Provider`**. Its operators (`System.Linq.Queryable`) take
**`Expression<Func<T,bool>>`** — code as data, e.g. `o => o.Total > 1000` becomes
a tree `GreaterThan(Property(o,"Total"), Constant(1000))`. EF Core's provider
walks that tree and **translates it to SQL**. A compiled `Func` cannot be
translated — it is opaque — which is why `IEnumerable` operations never become
SQL.

**Deferred execution** — chaining `.Where().Select().OrderBy()` on an `IQueryable`
executes nothing. The query runs only when you enumerate: `ToListAsync()`,
`FirstAsync()`, `CountAsync()`, `foreach`, etc. At that point EF translates the
whole accumulated expression tree into one SQL statement.

**Materialisation** — turning the rows that come back into `Order` objects. After
that you have `IEnumerable`/`List` and the DB is out of the picture.

**The trap to say out loud:** the moment you call `.ToList()` / `.AsEnumerable()`
/ `.ToListAsync()`, the type becomes `IEnumerable<T>` and every later LINQ call
runs in memory. Same `.Where()` — before materialisation it's a SQL `WHERE`, after
it's a C# loop over everything you already pulled.

**Related trap:** `_db.Orders.Where(o => MyHelper.IsBig(o))` — `MyHelper.IsBig` is
compiled code EF can't translate → runtime "could not be translated" exception.
Inline the logic so it's in the expression tree, or `.AsEnumerable()` first and
accept in-memory filtering deliberately.

**[⬆ Back to Top](#table-of-contents)**

## 21. EF Core async query methods worth memorising

All used as `await _db.Orders.XxxAsync(...)`. The `Async` suffix on your *own*
methods (`GetByIdAsync`) is just a naming convention signalling "returns a Task —
`await` me"; it is not a keyword and does nothing by itself.

| Method | Does |
|---|---|
| `ToListAsync()` | run the query, get all rows as `List<T>` |
| `ToArrayAsync()` / `ToDictionaryAsync(k => …)` | same, other shapes |
| `FirstOrDefaultAsync(pred)` | first matching row, or `null` |
| `SingleOrDefaultAsync(pred)` | exactly one match or `null`; throws if 2+ |
| `FindAsync(key)` | look up by primary key; checks already-tracked entities before hitting the DB |
| `AnyAsync(pred)` | `true`/`false` — cheap existence check |
| `CountAsync()` / `SumAsync(x)` / `MaxAsync(x)` / `AverageAsync(x)` | aggregates, computed in SQL |
| `SaveChangesAsync()` | commit pending inserts/updates/deletes |
| `ExecuteUpdateAsync(...)` / `ExecuteDeleteAsync()` | bulk update/delete without loading rows (EF Core 7+) |
| `AsNoTracking()` | (not async) skip change-tracking for read-only queries — faster, less memory |
| `Include(x => x.Nav)` | (not async) eager-load a related entity to avoid the N+1 problem |

**[⬆ Back to Top](#table-of-contents)**
