# RBC — Senior .NET Developer — Screener (9 Sep 2026)

**Role:** Senior .NET Developer, rebuild/modernization of the Direct Investing
trading platform. 155 Wellington W, 3 days/week on-site. Contract-to-hire, 4 openings.
**Stack in JD:** .NET Core / C#, RESTful APIs, SQL Server, Redis, Kafka, Docker,
Kubernetes, Azure and/or OpenShift (OCP), event-driven architecture, unit testing,
Git/GitHub, app security, WCAG.
**Interviewer:** senior technical screener on Trading Applications (long RBC tenure,
.NET + SQL Server background, ex-offshore tech lead — values clear communication,
requirements clarification, production-support mindset, practical engineering over
algorithm puzzles).
**Format:** ~30 min screener conversation + 2–3 live coding fundamentals.
**Outcome:** advanced. Next = **proctored technical assessment (~90 min, multiple
programming questions, no AI)**, then a **final round**.

**Read on performance:** conversation held up; on the three live coding problems the
interviewer had to lead to the answer each time (repeated "the array is sorted" →
binary search; walked from an O(n²) attempt to the two-pointer; nudged back to
DI/interface and then to `Dictionary`). He explicitly framed the assessment as the
place they check whether you can write fundamentals cold without AI, and asked
"are you doing the coding or are you the manager? what % of your day is coding?"
→ answer as a hands-on engineer (~70% coding), not a lead.

---

## Concept questions

### 1. What are the SOLID principles?

- **S — Single Responsibility:** a class has one job, one reason to change.
- **O — Open/Closed:** open to extension, closed to modification — add behaviour
  with a new class, not by editing a working one.
- **L — Liskov Substitution:** a subclass must work anywhere its base type is
  expected, with no surprises (classic violation: `Square : Rectangle`).
- **I — Interface Segregation:** many small focused interfaces beat one fat one;
  don't force a class to implement methods it doesn't use.
- **D — Dependency Inversion:** depend on abstractions (interfaces), not concrete
  classes; high-level code shouldn't depend on low-level details. This is why DI exists.

### 2. What else is the benefit of dependency injection? (beyond testability)

- Loose coupling — depend on `IOrderRepository`, not `SqlOrderRepository`.
- Swappable implementations — real / fake / different provider without touching consumers.
- Central configuration — everything wired in one place (`Program.cs`); whole graph visible.
- Lifetime & disposal management — container creates and disposes correctly.
- Clear contracts — a constructor lists exactly what a class needs.
- Enables cross-cutting concerns — logging/caching/retry via decorators around the interface.

### 3. Popular design patterns you have used

Pick 3–4 with a real example: **Repository** (wraps data access), **Factory**
(creates objects when construction is complex / concrete type chosen at runtime),
**Strategy** (swap an algorithm via an interface), **Decorator** (wrap a class to
add caching/logging), **Options pattern** (`IOptions<T>` for typed config),
**DI/IoC**. Prefer DI's singleton lifetime over the hand-rolled Singleton pattern.

### 4. Explain the Repository pattern

A class between business logic and the database, exposing `GetById` / `Add` /
`GetByCustomer` behind an interface.

```csharp
public interface IOrderRepository
{
    Task<Order?> GetByIdAsync(int id);
    Task<IReadOnlyList<Order>> GetByCustomerAsync(int customerId);
    Task AddAsync(Order order);
}
```

**Why:** keeps EF/SQL in one place; business code depends on the interface
(testable, swappable); shared query logic lives in one spot.
**Nuance to mention:** EF Core's `DbContext` + `DbSet` is already a
repository + unit-of-work, so re-wrapping it can be redundant — use a repository
to hide ORM specifics or centralise complex queries, not reflexively.

### 5. Dictionary vs List — the advantage

- **List:** find by value = linear scan, **O(n)**. Two parallel lists
  (`names[]`, `codes[]`) also risk drifting out of sync by index.
- **Dictionary:** hashes the key, jumps straight to the value, **O(1) average**;
  key and value bound in one entry.
- **List is still right when** you need order, duplicates, or only ever iterate.

**Soundbite:** "List lookup is O(n); Dictionary is a hash lookup, O(1) average.
For a name→code lookup called often, Dictionary — and it keeps key and value
together instead of two lists I keep aligned by index."

---

## Live coding questions

### 6. Search a 1,000,000-element **sorted** `int[]` for a number; return its
location or not-found. No built-in functions.

"Sorted" ⇒ **binary search**, O(log n) (~20 checks for 1M) vs O(n) linear scan.

```csharp
static int BinarySearch(int[] arr, int target)
{
    int low = 0, high = arr.Length - 1;

    while (low <= high)
    {
        int mid = low + (high - low) / 2;   // not (low+high)/2 — avoids int overflow

        if (arr[mid] == target) return mid;         // found — return index
        if (arr[mid] < target)  low  = mid + 1;     // go right
        else                    high = mid - 1;     // go left
    }
    return -1;                                       // not found
}
```

Say: "O(log n) time, O(1) space. Overflow-safe midpoint. For the *first*
occurrence with duplicates, keep searching left after a hit instead of returning."

### 7. Array of 1,000,000 elements, values only 0 or 1, random mix. Move all 0s to
the front. No built-in sort. Is it O(n) or O(n²)?

**Two pointers, one from each end, swap a misplaced pair. O(n) time, O(1) space, in place.**

```csharp
static void MoveZerosToFront(int[] arr)
{
    int left = 0, right = arr.Length - 1;

    while (left < right)
    {
        if (arr[left] == 0)         left++;      // already correct
        else if (arr[right] == 1)   right--;     // already correct
        else                                     // arr[left]==1 && arr[right]==0 → swap
        {
            (arr[left], arr[right]) = (arr[right], arr[left]);
            left++;
            right--;
        }
    }
}
```

**Why O(n), not O(n²):** `left` and `right` only ever move toward each other; every
iteration advances at least one; total work ≤ n. No restart, no nested loop.
**"Or even less":** count the 0s in one pass, then overwrite — same O(n) time,
fewer writes. Mention both; two-pointer is the standard answer.

---

## Design scenario

### 8. You're on a team building one ASP.NET Core solution (multiple projects).
You wrote a class; you want other projects/devs to use it. How?

Interviewer pushed past each first answer. The progression:

1. **Static class** — fine for a pure helper, but can't be mocked, can't be
   swapped, can't hold injected dependencies or per-environment config. He rejected this.
2. **Answer he wanted:** put the class in a **shared class library project**
   (`Common` / `Infrastructure`); other projects add a **project reference**;
   expose it via an **interface**; **register it in DI**; other devs **inject the
   interface** in their constructors — no `new`, no dependency on the concrete class.

```csharp
// shared library project
public interface ICountryCodeProvider
{
    bool TryGetCode(string country, out string code);
}

// registration (each app's Program.cs, or a shared AddCommon() extension)
services.AddSingleton<ICountryCodeProvider, CountryCodeProvider>();
```

### 9. Now write that function: given a list of ~250 country names and a list of
international dialling codes, return the code for a country. All in memory. How do
you organise the data and write the function?

**Organise as a `Dictionary`, not two parallel lists.**

```csharp
public class CountryCodeProvider : ICountryCodeProvider
{
    private static readonly Dictionary<string, string> _codes =
        new(StringComparer.OrdinalIgnoreCase)
        {
            ["India"] = "91",
            ["United States"] = "1",
            ["Canada"] = "1",
            // ...
        };

    public bool TryGetCode(string country, out string code)
        => _codes.TryGetValue(country, out code!);
}
```

- **Singleton** lifetime — data is static, read-only; dictionary reads are thread-safe.
- **`TryGetValue`** — handles "not found" without throwing or a second lookup.
- **`StringComparer.OrdinalIgnoreCase`** — `"india"` and `"India"` both resolve.
- **Why Dictionary over two lists:** O(1) lookup vs O(n) scan, and key+value can't
  drift out of sync.

---

## Behavioral

- **"Brief overview of your experience / yourself"** — have a tight 60–90s version.
- **Event-driven components you've built** — name only what you've actually used:
  ASP.NET Core Web APIs, `BackgroundService` workers consuming from
  Kafka / Azure Service Bus / RabbitMQ / Solace, idempotent message handlers,
  SignalR for live client updates. The final round will probe this.
- **"Are you coding or managing? What % of your day is coding?"** — answer as a
  hands-on engineer: "hands-on daily, ~70% coding, rest design / review / mentoring."
- **Contract-to-hire** — he wants people open to converting to FTE if performance
  is good; confirm you're fine with that.

---

## What to expect next

**Technical assessment (~90 min, proctored, no AI).** Likely shapes:
array/string manipulation, two-pointer, sliding window, hash map / `HashSet`
(frequency, dedupe, lookups), sorting & searching (binary search + variants),
maybe a small OOP design or a LINQ/collections question. **State time/space
complexity and justify it.** Drill these cold — no autocomplete.

**Final round.** Deeper technical + system design for the trading platform
(event-driven, Kafka, low latency, audit/compliance, WCAG) + behavioral +
contract-to-hire fit.
