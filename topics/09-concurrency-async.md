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
