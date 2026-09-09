# C# & OOP Fundamentals

> This is the topic every interview opens with, and it's also where candidates lose
> points on autopilot. Answer with a one-sentence definition, then immediately follow
> it with "...and the gotcha is". That's what separates a memorized answer from one
> that shows you've actually hit these edge cases in real code.

## Table of Contents

| No. | Question |
|-----|----------|
| 1 | [What are the four pillars of OOP?](#1-what-are-the-four-pillars-of-oop) |
| 2 | [Abstract class vs interface — what's the difference and when do you use each?](#2-abstract-class-vs-interface--whats-the-difference-and-when-do-you-use-each) |
| 3 | [How does explicit interface implementation work when two interfaces share a method name?](#3-how-does-explicit-interface-implementation-work-when-two-interfaces-share-a-method-name) |
| 4 | [What's the difference between method hiding (`new`) and overriding (`override`)?](#4-whats-the-difference-between-method-hiding-new-and-overriding-override) |
| 5 | [Predict the output: virtual/override polymorphism](#5-predict-the-output-virtualoverride-polymorphism) |
| 6 | [Overloading vs overriding](#6-overloading-vs-overriding) |
| 7 | [What is a sealed class?](#7-what-is-a-sealed-class) |
| 8 | [`const` vs `static readonly` vs `readonly`](#8-const-vs-static-readonly-vs-readonly) |
| 9 | [Static class vs a class with static methods](#9-static-class-vs-a-class-with-static-methods) |
| 10 | [Static vs Singleton](#10-static-vs-singleton) |
| 11 | [Why can't a static constructor take parameters?](#11-why-cant-a-static-constructor-take-parameters) |
| 12 | [What are private constructors used for?](#12-what-are-private-constructors-used-for) |
| 13 | [What is constructor chaining?](#13-what-is-constructor-chaining) |
| 14 | [Shallow copy vs deep copy](#14-shallow-copy-vs-deep-copy) |
| 15 | [Copying an array vs cloning it](#15-copying-an-array-vs-cloning-it) |
| 16 | [What is boxing and unboxing?](#16-what-is-boxing-and-unboxing) |
| 17 | [Value type vs reference type](#17-value-type-vs-reference-type) |
| 18 | [Is a struct a value type or a reference type?](#18-is-a-struct-a-value-type-or-a-reference-type) |
| 19 | [`var` vs `dynamic`, and what is the DLR?](#19-var-vs-dynamic-and-what-is-the-dlr) |
| 20 | [Managed vs unmanaged code](#20-managed-vs-unmanaged-code) |
| 21 | [How do you handle exceptions in C#?](#21-how-do-you-handle-exceptions-in-c) |
| 22 | [What is a delegate?](#22-what-is-a-delegate) |
| 23 | [`Action`, `Func`, and `event` — how do they differ?](#23-action-func-and-event--how-do-they-differ) |
| 24 | [What are generics, and why use them?](#24-what-are-generics-and-why-use-them) |
| 25 | [What is an extension method?](#25-what-is-an-extension-method) |
| 26 | [Named parameters vs optional parameters](#26-named-parameters-vs-optional-parameters) |
| 27 | [Anonymous types vs anonymous methods](#27-anonymous-types-vs-anonymous-methods) |
| 28 | [What is reflection?](#28-what-is-reflection) |
| 29 | [`yield return` vs `return`](#29-yield-return-vs-return) |
| 30 | [What are record types?](#30-what-are-record-types) |
| 31 | [What is covariance and contravariance?](#31-what-is-covariance-and-contravariance) |
| 32 | [What are the CLR, MSIL, and .NET assemblies?](#32-what-are-the-clr-msil-and-net-assemblies) |
| 33 | [How does the Garbage Collector work?](#33-how-does-the-garbage-collector-work) |
| 34 | [`Dispose()` vs `Finalize()`](#34-dispose-vs-finalize) |
| 35 | [Hashtable vs Dictionary, and how do they work internally?](#35-hashtable-vs-dictionary-and-how-do-they-work-internally) |
| 36 | [`IEnumerable` vs `IQueryable`](#36-ienumerable-vs-iqueryable) |
| 37 | [`==` vs `.Equals()`](#37--vs-equals) |
| 38 | [Mutable vs immutable — how do you design an immutable class?](#38-mutable-vs-immutable--how-do-you-design-an-immutable-class) |
| 39 | [What ASP.NET state-management options are there?](#39-what-aspnet-state-management-options-are-there) |
| 40 | [`Response.Write` vs `Response.Output.Write`](#40-responsewrite-vs-responseoutputwrite) |
| 41 | [`Server.Transfer` vs `Response.Redirect`](#41-servertransfer-vs-responseredirect) |
| 42 | [What is Cross-Page Posting?](#42-what-is-cross-page-posting) |
| 43 | [What is Delay Signing?](#43-what-is-delay-signing) |
| 44 | [In what type/format should you store and return dates?](#44-in-what-typeformat-should-you-store-and-return-dates) |
| 45 | [`DataSet` vs `DataReader`](#45-dataset-vs-datareader) |
| 46 | [What is serialization/deserialization?](#46-what-is-serializationdeserialization) |
| 47 | [.NET Framework vs .NET Core](#47-net-framework-vs-net-core) |
| 48 | [What are the ASP.NET page life-cycle events?](#48-what-are-the-aspnet-page-life-cycle-events) |
| 49 | [How do you force all validation controls to run?](#49-how-do-you-force-all-validation-controls-to-run) |
| 50 | [IEnumerable vs List — deferred execution vs eager loading](#50-ienumerable-vs-list--deferred-execution-vs-eager-loading) |

## 1. What are the four pillars of OOP?

- **Encapsulation** — hiding internal state behind a controlled interface (`private`
  fields + `public` properties/methods). The real point isn't "using `private`", it's
  that the object can enforce its own invariants — e.g. a `BankAccount` can guarantee
  its balance never goes negative because nothing outside can touch the field
  directly.
- **Abstraction** — exposing *what* something does without *how*. Interfaces and
  abstract classes are the mechanism; the goal is that callers depend on a contract,
  not an implementation.
- **Inheritance** — an "is-a" relationship for reuse. The gotcha: overuse creates
  fragile hierarchies; prefer composition when the relationship is really "has-a" or
  "can-do".
- **Polymorphism** — one interface, many implementations, resolved either at
  compile time (overloading) or runtime (overriding via `virtual`/`override`).

**[⬆ Back to Top](#table-of-contents)**

## 2. Abstract class vs interface — what's the difference and when do you use each?

The single most-asked question on this list. Give the mechanical differences, then
the design guidance.

| | Abstract class | Interface |
|---|---|---|
| State | Can hold fields and constructors | Cannot hold instance fields (C# 8+ default method *bodies* are allowed, not state) |
| Multiple inheritance | A class can inherit only one | A class can implement many |
| Access modifiers | Members can be `private`/`protected` | Members are implicitly `public` |
| Versioning | Adding a member breaks nothing (give it a body) | C# 8+ default interface methods let you add members without breaking implementers |
| Use it when | A family of related types shares real state/behavior | Unrelated types opt into the same capability (`IDisposable`, `IComparable`) |

**How to phrase it out loud:** "An abstract class answers 'what is it' — it's a base
for related types that share state and behavior. An interface answers 'what can it
do' — unrelated types can implement the same interface. I reach for an interface by
default because it keeps things loosely coupled, and only pull in an abstract class
when there's real shared implementation to avoid duplicating it."

**[⬆ Back to Top](#table-of-contents)**

## 3. How does explicit interface implementation work when two interfaces share a method name?

When a class implements two interfaces that expose the same method signature, you
disambiguate with explicit implementation:

```csharp
interface I1 { void Method(); }
interface I2 { void Method(); }

class A : I1, I2
{
    void I1.Method() { /* I1's version */ }
    void I2.Method() { /* I2's version */ }
}

A a = new A();
((I1)a).Method(); // calls I1's version
((I2)a).Method(); // calls I2's version
// a.Method();     <-- doesn't compile; explicit implementations aren't public on A itself
```

**[⬆ Back to Top](#table-of-contents)**

## 4. What's the difference between method hiding (`new`) and overriding (`override`)?

This shows up constantly as a "predict the output" question. The key rule: **virtual
dispatch only kicks in through `override`; `new` is resolved by the *compile-time*
type of the reference, not the runtime type.**

```csharp
class BaseClass
{
    public void Func1() => Console.WriteLine("Base.Func1");
    public virtual void Func2() => Console.WriteLine("Base.Func2");
    public virtual void Func3() => Console.WriteLine("Base.Func3");
}

class DerivedClass : BaseClass
{
    public new void Func1() => Console.WriteLine("Derived.Func1");
    public override void Func2() => Console.WriteLine("Derived.Func2");
    public new void Func3() => Console.WriteLine("Derived.Func3");
}

BaseClass b = new DerivedClass();
b.Func1(); // "Base.Func1"    <- new hides, but the reference type is BaseClass, so base wins
b.Func2(); // "Derived.Func2" <- override => runtime type wins, regardless of reference type
b.Func3(); // "Base.Func3"    <- same as Func1: `new` is resolved by reference type
```

**Say this out loud:** "`override` gives you real polymorphism — the call is
dispatched based on the actual object type at runtime. `new` just hides the base
member for that reference type; if you access the object through a base-typed
reference, you get the base version back. It's a common bug source when someone
'overrides' a non-virtual method with `new`, expecting polymorphic behavior."

**[⬆ Back to Top](#table-of-contents)**

## 5. Predict the output: virtual/override polymorphism

```csharp
class A { public virtual void Show() => Console.WriteLine("Base!"); }
class B : A { public override void Show() => Console.WriteLine("Derived!"); }

A a1 = new A(); a1.Show();      // "Base!"
B b1 = new B(); b1.Show();      // "Derived!"
A a2 = new B(); a2.Show();      // "Derived!"  <- virtual dispatch, runtime type wins
// B b2 = new A(); <-- doesn't compile: can't implicitly downcast A to B
```

**[⬆ Back to Top](#table-of-contents)**

## 6. Overloading vs overriding

- **Overloading** — same method name, different signature (parameter types/count),
  resolved at **compile time**. Not true polymorphism, just convenience.
- **Overriding** — same signature, subclass replaces base behavior, resolved at
  **runtime**, requires `virtual`/`override` (or `abstract`).

```csharp
class Calculator
{
    // Overloading: same name "Add", different parameter lists — picked at compile time
    public int Add(int a, int b) => a + b;
    public double Add(double a, double b) => a + b;
}

class Shape
{
    public virtual double Area() => 0;
}
class Circle : Shape
{
    // Overriding: same signature as base, replaces behavior — picked at runtime
    public override double Area() => 3.14 * 5 * 5;
}
```

**[⬆ Back to Top](#table-of-contents)**

## 7. What is a sealed class?

`sealed class Foo {}` prevents further inheritance. Use it when a class's design
isn't meant to be extended (immutable value-like types, or a small performance win —
the JIT can devirtualize calls on sealed types slightly more aggressively). `sealed`
can also be applied to an individual `override` to stop further overriding in a
deeper subclass.

```csharp
public sealed class DiscountCalculator { /* ... */ }

// public class BetterDiscountCalculator : DiscountCalculator { } // compile error — sealed
```

**[⬆ Back to Top](#table-of-contents)**

## 8. `const` vs `static readonly` vs `readonly`

| | `const` | `static readonly` | `readonly` (instance) |
|---|---|---|
| When is the value set | Compile time | Runtime (in a static constructor or inline) | Runtime (in a constructor or inline) |
| Shared or per-instance | Shared, inlined into IL at every call site | Shared, one copy per type | One copy per instance |
| Can hold a computed value | No — must be a compile-time literal | Yes | Yes |
| Gotcha | Changing a `const` in a referenced library requires recompiling *every* consumer, since the value is baked in | None of that problem | — |

```csharp
public class Config
{
    public const int MaxRetries = 3;                 // fixed forever, baked into IL
    public static readonly DateTime StartedAt = DateTime.UtcNow; // set once, at runtime
    public readonly string InstanceId;                // set once per instance, in the constructor

    public Config() { InstanceId = Guid.NewGuid().ToString(); }
}
```

**[⬆ Back to Top](#table-of-contents)**

## 9. Static class vs a class with static methods

A **static class** (`static class Utils`) can't be instantiated and can only contain
static members — good for pure helper/utility functions with no state
(`Math`, `Console`-style APIs). A regular class can simply *have* static methods
alongside instance methods; that's a design choice for utility methods that don't
need instance state, not a language restriction.

```csharp
public static class MathUtils           // can never be instantiated
{
    public static int Square(int x) => x * x;
}

public class OrderService              // a normal class, but with one static helper
{
    public static bool IsValidOrderNumber(string s) => s.StartsWith("ORD-");
    public void Process(Order order) { /* uses instance state */ }
}
```

**[⬆ Back to Top](#table-of-contents)**

## 10. Static vs Singleton

They solve different problems and get confused constantly:
- A **static class** has no instance at all — no state lifecycle, no interfaces, no DI.
- A **Singleton** *is* an instance — just guaranteed to be the only one. It can
  implement interfaces, be lazily created, be swapped for a test double, and
  participate in a DI container (`services.AddSingleton<IFoo, Foo>()`).

**How to phrase it:** "I use `static` for stateless utility logic. I use Singleton
when I need exactly one instance of something that has state or needs to satisfy an
interface — e.g. a configuration cache — because it stays testable and DI-friendly
in a way a static class never can."

```csharp
public static class MathUtils { public static int Square(int x) => x * x; } // no instance, ever

public interface IConfigCache { string Get(string key); }
public sealed class ConfigCache : IConfigCache      // a Singleton — still an object
{
    private static readonly Lazy<ConfigCache> _instance = new(() => new ConfigCache());
    public static ConfigCache Instance => _instance.Value;
    public string Get(string key) => "value";       // could be mocked via IConfigCache in tests
}
```

**[⬆ Back to Top](#table-of-contents)**

## 11. Why can't a static constructor take parameters?

Because the CLR calls it automatically, exactly once, the first time the type is
touched (first instantiation or first static member access) — there's no call site
for you to pass arguments from. It exists purely to initialize static state once,
safely, and the runtime guarantees it happens before you can observe an
uninitialized static field, even under concurrent access.

```csharp
class Logger
{
    private static readonly string _logPath;
    static Logger() // no parameters possible
    {
        _logPath = ConfigurationManager.AppSettings["LogPath"] ?? "logs.txt";
    }
}
```

**[⬆ Back to Top](#table-of-contents)**

## 12. What are private constructors used for?

To prevent external instantiation — the classic use case is the Singleton pattern,
or a class that should only be created through a static factory method (so the
factory can validate, cache, or pool instances).

```csharp
public class DatabaseConnection
{
    private DatabaseConnection(string connStr) { /* ... */ }

    // callers can only get an instance through this validated factory method
    public static DatabaseConnection Create(string connStr)
    {
        if (string.IsNullOrWhiteSpace(connStr)) throw new ArgumentException("Connection string required");
        return new DatabaseConnection(connStr);
    }
}
// var db = new DatabaseConnection("..."); // compile error — constructor is private
var db = DatabaseConnection.Create("Server=...");
```

**[⬆ Back to Top](#table-of-contents)**

## 13. What is constructor chaining?

One constructor calling another on the same class (`: this(...)`) or the base class
(`: base(...)`) to avoid duplicating initialization logic:

```csharp
class Person
{
    public Person(string name) : this(name, 0) { }
    public Person(string name, int age) { Name = name; Age = age; }
}
```

**[⬆ Back to Top](#table-of-contents)**

## 14. Shallow copy vs deep copy

- **Shallow copy** — copies the top-level fields; if a field is a reference type,
  both the original and the copy point at the *same* nested object. Mutating the
  nested object through one reflects in the other.
- **Deep copy** — recursively copies referenced objects too, so the copy is fully
  independent.

`MemberwiseClone()` gives a shallow copy. A copy constructor is the typical way to
implement a deep copy explicitly, field by field.

```csharp
public class Address { public string City; }
public class Person
{
    public string Name;
    public Address Home;

    public Person ShallowCopy() => (Person)MemberwiseClone(); // Home is SHARED with the copy

    public Person DeepCopy() => new Person
    {
        Name = Name,
        Home = new Address { City = Home.City } // a genuinely separate Address
    };
}

var p1 = new Person { Name = "Sam", Home = new Address { City = "Delhi" } };
var shallow = p1.ShallowCopy();
shallow.Home.City = "Mumbai";
Console.WriteLine(p1.Home.City); // "Mumbai" — shallow copy shared the same Address object!
```

**[⬆ Back to Top](#table-of-contents)**

## 15. Copying an array vs cloning it

Assignment (`arr2 = arr1`) just copies the reference — both variables point at the
same array. `arr.Clone()` produces a genuinely new array object, but it's still a
**shallow** copy of the elements — reference-type elements in the cloned array still
point at the same underlying objects as the original.

```csharp
int[] original = { 1, 2, 3 };

int[] alias = original;       // same array — mutating one mutates both
alias[0] = 99;
Console.WriteLine(original[0]); // 99

int[] copy = (int[])original.Clone(); // a genuinely new array
copy[0] = 5;
Console.WriteLine(original[0]);       // still 99 — unaffected
```

**[⬆ Back to Top](#table-of-contents)**

## 16. What is boxing and unboxing?

Boxing wraps a value type on the heap as an `object`; unboxing extracts it back.

```csharp
int i = 42;
object boxed = i;         // boxing — heap allocation
int unboxed = (int)boxed; // unboxing — must cast back to the exact original type
```

The cost is the interview point: boxing allocates on the managed heap and adds GC
pressure, which is why generic collections (`List<int>` vs the old `ArrayList`)
matter — generics avoid boxing entirely for value types.

**[⬆ Back to Top](#table-of-contents)**

## 17. Value type vs reference type

Value types (`struct`, `int`, `bool`, enums) live on the stack (or inline inside
whatever contains them) and are copied by value on assignment. Reference types
(`class`, arrays, delegates, strings) live on the heap, and the variable holds a
reference — assignment copies the reference, not the object.

```csharp
// Value type: assignment copies the data
int x = 5;
int y = x;
y = 10;
Console.WriteLine(x); // 5 — x is untouched

// Reference type: assignment copies the pointer, not the object
List<int> a = new List<int> { 1, 2, 3 };
List<int> b = a;      // b and a now point at the exact same List in memory
a.Add(4);
Console.WriteLine(string.Join(",", b)); // "1,2,3,4" — b sees the change made through a
```

**Gotcha worth mentioning:** `string` is a reference type but *behaves* immutably —
every "mutation" produces a new string, so equality comparisons use value semantics
even though it's heap-allocated.

**[⬆ Back to Top](#table-of-contents)**

## 18. Is a struct a value type or a reference type?

Value type, always. It's allocated inline (on the stack if it's a local, or inline
inside its containing object if it's a field). This is exactly why passing a large
struct around by value can hurt performance — each pass is a full copy — which is
why you'll sometimes see `in`/`ref` parameters used with structs.

**[⬆ Back to Top](#table-of-contents)**

## 19. `var` vs `dynamic`, and what is the DLR?

`var` is resolved by the compiler at compile time — it's still static typing, just
with inferred syntax; IntelliSense and compile errors work normally. `dynamic`
defers type resolution to **runtime** via the **DLR (Dynamic Language Runtime)** —
the compiler emits a call site that resolves the actual member/operator at runtime
using reflection-like binding, which is slower and loses compile-time safety, but is
useful for interop (COM, dynamic JSON, `ExpandoObject`).

```csharp
var name = "Sam";        // compiler infers `string` — still fully type-checked
// name = 5;             // compile error: cannot convert int to string

dynamic value = "Sam";   // type resolved at runtime
value = 5;               // fine — dynamic can hold anything
value.NonExistentMethod(); // compiles! but throws a RuntimeBinderException when it runs
```

**[⬆ Back to Top](#table-of-contents)**

## 20. Managed vs unmanaged code

Managed code runs under the CLR — memory is garbage-collected, type safety and
bounds checks are enforced, exceptions are structured. Unmanaged code (raw C/C++,
Win32 API calls) manages its own memory and isn't verified by the CLR; C# reaches it
via P/Invoke or `unsafe` blocks, and at that point you're responsible for cleanup
(hence `IDisposable`/finalizers wrapping unmanaged handles).

**[⬆ Back to Top](#table-of-contents)**

## 21. How do you handle exceptions in C#?

```csharp
try
{
    // risky operation
}
catch (SqlException ex) when (ex.Number == 2601)
{
    // narrowest, most specific exception type first, optionally with a filter
}
catch (Exception ex)
{
    // broad catch-all last
    throw; // preserves the original stack trace — never `throw ex;`
}
finally
{
    // always runs — cleanup, even if an exception propagates
}
```

**Interview trap:** `throw;` vs `throw ex;` — the former preserves the original
stack trace, the latter resets it to the current line, hiding where the exception
actually originated.

```csharp
catch (Exception ex)
{
    Logger.Log(ex);
    throw ex;   // BAD  — stack trace now starts here, you lose where it really failed
    throw;      // GOOD — original stack trace (exact file/line of the real failure) is kept
}
```

**[⬆ Back to Top](#table-of-contents)**

## 22. What is a delegate?

A type-safe function pointer — a reference to a method with a matching signature
that can be invoked indirectly, passed as a parameter, or combined (multicast).

```csharp
public delegate int Operation(int a, int b);

Operation add = (a, b) => a + b;
int result = add(3, 4); // 7
```

**[⬆ Back to Top](#table-of-contents)**

## 23. `Action`, `Func`, and `event` — how do they differ?

- **`Action<T...>`** — a delegate that returns `void`.
- **`Func<T..., TResult>`** — a delegate that returns `TResult` (the last type
  parameter).
- **`event`** — a wrapper around a multicast delegate that restricts external code
  to only `+=`/`-=` (subscribe/unsubscribe) — it can't be invoked or reassigned from
  outside the declaring class, which is what makes it safe for the classic
  publisher/subscriber pattern.

```csharp
Action<string> print = msg => Console.WriteLine(msg);   // takes a string, returns void
print("hello");                                          // prints "hello"

Func<int, int, int> add = (a, b) => a + b;               // takes two ints, returns an int
int sum = add(2, 3);                                      // 5

public class Button
{
    public event Action Clicked;             // external code can only += / -= this
    public void SimulateClick() => Clicked?.Invoke();
}
var btn = new Button();
btn.Clicked += () => Console.WriteLine("Clicked!");
btn.SimulateClick(); // "Clicked!"
```

**[⬆ Back to Top](#table-of-contents)**

## 24. What are generics, and why use them?

Generics let you write a type or method parameterized by type, with compile-time
type safety and no boxing for value types:

```csharp
public class Repository<T> where T : class, IEntity
{
    public T GetById(int id) { /* ... */ }
}
```

The `where T : ...` constraint restricts what `T` can be (`class`, `struct`, a base
type/interface, `new()`).

**[⬆ Back to Top](#table-of-contents)**

## 25. What is an extension method?

A static method in a static class, written so it *looks* like it's an instance
method on the extended type — the compiler resolves it via the `this` modifier on
the first parameter. LINQ (`.Where()`, `.Select()`) is entirely built on this.

```csharp
public static class StringExtensions
{
    public static bool IsNullOrBlank(this string s) => string.IsNullOrWhiteSpace(s);
}
// usage: myString.IsNullOrBlank();
```

**[⬆ Back to Top](#table-of-contents)**

## 26. Named parameters vs optional parameters

```csharp
void CreateUser(string name, int age = 18, string role = "User") { }

CreateUser("Sam");                       // age=18, role="User"
CreateUser("Sam", role: "Admin");        // named parameter skips age
```

Optional parameters supply a default so callers can omit them; named parameters let
callers pass arguments out of order by name — the two are usually used together.

**[⬆ Back to Top](#table-of-contents)**

## 27. Anonymous types vs anonymous methods

Don't conflate these — they're two different features:

- **Anonymous type** — a compiler-generated read-only class inferred from an object
  initializer: `var p = new { Name = "Sam", Age = 30 };`
- **Anonymous method/lambda** — an inline, unnamed function:
  `Func<int,int> square = x => x * x;`

**[⬆ Back to Top](#table-of-contents)**

## 28. What is reflection?

The ability to inspect and manipulate types, members, and metadata at runtime
(`Type.GetType()`, `GetProperties()`, `Activator.CreateInstance()`). Common uses:
building generic serializers, dependency injection containers, ORMs, and plugin
systems. It costs performance, so it's typically cached rather than repeated per
call.

**[⬆ Back to Top](#table-of-contents)**

## 29. `yield return` vs `return`

`yield return` produces a value from an **iterator block** without exiting the
method — the compiler rewrites the method into a state machine implementing
`IEnumerable<T>`, and execution resumes exactly where it left off on the next
`MoveNext()`. Regular `return` exits immediately and produces one final value. This
is how you get lazy, streaming enumeration instead of building a full list up
front.

```csharp
public static IEnumerable<int> GetNumbersUpTo(int max)
{
    for (int i = 1; i <= max; i++)
    {
        Console.WriteLine($"producing {i}");
        yield return i; // pauses here, resumes on the next MoveNext()
    }
}

foreach (var n in GetNumbersUpTo(3))
{
    Console.WriteLine($"consuming {n}");
}
// Output interleaves: producing 1, consuming 1, producing 2, consuming 2, producing 3, consuming 3
// (a `return List<int>` version would print all three "producing" lines up front instead)
```

**[⬆ Back to Top](#table-of-contents)**

## 30. What are record types?

Reference types (or, with `record struct`, value types) with built-in
**value-based equality**, `ToString()`, and support for non-destructive mutation via
`with` expressions:

```csharp
public record Point(int X, int Y);
var p1 = new Point(1, 2);
var p2 = p1 with { Y = 5 }; // new record, X copied, Y changed
p1 == p2; // false — but two records with the same values are `==` even though they're different instances
```

Good fit for immutable DTOs and value objects.

**[⬆ Back to Top](#table-of-contents)**

## 31. What is covariance and contravariance?

- **Covariance** (`out T`) — lets you use a more derived type than originally
  specified; `IEnumerable<out T>` means `IEnumerable<string>` can be assigned to an
  `IEnumerable<object>` variable, because you only ever *read* `T` out of it.
- **Contravariance** (`in T`) — lets you use a more generic type than originally
  specified; `Action<in T>` means an `Action<object>` can be used where an
  `Action<string>` is expected, because you only ever *pass* `T` in.

**[⬆ Back to Top](#table-of-contents)**

## 32. What are the CLR, MSIL, and .NET assemblies?

The **CLR** (Common Language Runtime) is the execution engine — JIT compilation,
garbage collection, type safety, exception handling. C# source compiles to
**MSIL** (Microsoft Intermediate Language), a CPU-independent bytecode, packaged
into an **assembly** (a `.dll`/`.exe` plus a manifest). At runtime, the JIT compiler
turns MSIL into native machine code, method by method, on first call.

**[⬆ Back to Top](#table-of-contents)**

## 33. How does the Garbage Collector work?

The GC tracks object reachability from a set of roots (static fields, thread stacks,
CPU registers) and reclaims anything unreachable. It's generational — Gen 0
(short-lived objects, collected most often/cheaply), Gen 1 (a buffer), Gen 2
(long-lived objects, collected least often, most expensively), plus a separate Large
Object Heap for allocations over ~85KB. This is why churning lots of small,
short-lived objects is usually fine (Gen 0 collections are fast) while large
allocations or objects that survive into Gen 2 are the ones that hurt.

**[⬆ Back to Top](#table-of-contents)**

## 34. `Dispose()` vs `Finalize()`

- **`Dispose()`** (via `IDisposable`) is **deterministic** — you (or a `using`
  block) call it explicitly to release unmanaged resources (file handles, DB
  connections, sockets) right away.
- **`Finalize()`** (a C# destructor, `~ClassName()`) is called by the GC
  **non-deterministically**, as a safety net, and is more expensive because
  finalizable objects need an extra GC pass.

The standard pattern: implement `IDisposable`, and have the finalizer call the same
cleanup as a backstop, guarded by `GC.SuppressFinalize(this)` in `Dispose()` so the
finalizer doesn't run twice.

```csharp
public class ResourceHolder : IDisposable
{
    private bool _disposed;
    public void Dispose()
    {
        if (_disposed) return;
        // release unmanaged resource here (file handle, socket, etc.)
        _disposed = true;
        GC.SuppressFinalize(this); // finalizer no longer needed, we already cleaned up
    }
    ~ResourceHolder() { Dispose(); } // safety net if someone forgets to call Dispose()
}
```

**Why do you still need the `using` statement if `IDisposable` already exists?**
Because `Dispose()` only runs if something actually calls it — `using` guarantees
that call happens automatically, wrapped in a hidden `try`/`finally`, even if an
exception is thrown partway through the block:

```csharp
using (var stream = new FileStream("file.txt", FileMode.Open))
{
    // read the file — stream.Dispose() runs automatically here,
    // even if an exception is thrown above
}

// equivalent to what the compiler actually generates:
var stream2 = new FileStream("file.txt", FileMode.Open);
try { /* read the file */ }
finally { stream2.Dispose(); }
```

**[⬆ Back to Top](#table-of-contents)**

## 35. Hashtable vs Dictionary, and how do they work internally?

Both are hash-table based key/value stores. `Dictionary<TKey,TValue>` is the
modern, generic, type-safe version — no boxing for value-type keys/values, and it
throws `KeyNotFoundException` on a missing key via the indexer. `Hashtable` is the
older, non-generic collection — everything is stored as `object`, so value types get
boxed, and a missing key via the indexer just returns `null` instead of throwing.

**Internally**, both hash the key to compute a bucket index into an internal array,
then handle collisions by chaining entries that land in the same bucket. Average
case is `O(1)` for get/insert/delete; **worst case degrades toward `O(n)`** if the
hash function distributes poorly and many keys collide into the same bucket. The
table resizes (and rehashes everything) once the load factor crosses a threshold.

```csharp
// Throws KeyNotFoundException if missing:
var v = dict["key"];

// Safe:
if (dict.TryGetValue("key", out var value)) { /* use value */ }
```

**[⬆ Back to Top](#table-of-contents)**

## 36. `IEnumerable` vs `IQueryable`

- **`IEnumerable<T>`** — iterates an **in-memory** sequence. LINQ operators
  (`.Where()`, `.Select()`) compile to delegates and execute **in process**, item by
  item, as you enumerate.
- **`IQueryable<T>`** — represents a **not-yet-executed query** as an expression
  tree. LINQ operators build up the expression tree instead of running immediately;
  the provider (e.g. EF Core) translates the whole tree into a single SQL statement
  only when you enumerate it (`.ToList()`, `foreach`, etc.).

**The classic bug this causes:** chaining `.Where()` calls on an `IQueryable` from
EF, then accidentally calling `.AsEnumerable()` or `.ToList()` too early — every
filter after that point runs in application memory instead of the database, pulling
far more rows across the wire than intended.

```csharp
IQueryable<Order> query = dbContext.Orders;        // nothing has run yet
query = query.Where(o => o.Status == "Pending");   // still just building an expression tree
var results = query.ToList();                       // NOW it runs — translated to one SQL query:
                                                      // SELECT * FROM Orders WHERE Status = 'Pending'

IEnumerable<Order> inMemory = dbContext.Orders.ToList(); // pulls ALL rows into memory here
inMemory = inMemory.Where(o => o.Status == "Pending");   // filters in C#, not in SQL
```

**[⬆ Back to Top](#table-of-contents)**

## 37. `==` vs `.Equals()`

For value types and `string`, both check value equality out of the box. For
reference types, the default behavior of both is **reference equality** (same
object in memory) *unless* the type overrides `Equals()`/operator `==` to provide
value equality (which `string` and `record` types do). The safest general rule:
`.Equals()` is virtual and can be overridden per-type; `==` is a static operator
resolved at compile time based on the *declared* type of the operands, which is why
casting to `object` can change the answer:

```csharp
string a = "hi", b = new string("hi".ToCharArray());
a == b;                 // true  — string overloads == for value equality
((object)a).Equals(b);  // true — Equals is still value equality
```

**[⬆ Back to Top](#table-of-contents)**

## 38. Mutable vs immutable — how do you design an immutable class?

An immutable object's state can't change after construction — which makes it
inherently thread-safe and easy to reason about.

```csharp
public sealed class ImmutablePoint
{
    public int X { get; }
    public int Y { get; }
    public ImmutablePoint(int x, int y) { X = x; Y = y; }
    // no setters, no mutating methods; any "change" returns a new instance
}
```

Watch for reference-type fields — if a property returns a mutable collection
directly, callers can still mutate it; return a copy or a read-only wrapper instead.

**[⬆ Back to Top](#table-of-contents)**

## 39. What ASP.NET state-management options are there?

ViewState, Session State, Application State, Cookies, Query Strings, Hidden Fields,
and Cache — each trades off scope (per-user vs. app-wide), persistence, and payload
size differently. For **session state specifically**, the store can be InProc,
StateServer, SQL Server, or a custom provider — trading speed for durability and
support for scaling out across multiple servers.

**[⬆ Back to Top](#table-of-contents)**

## 40. `Response.Write` vs `Response.Output.Write`

`Response.Write` takes a plain string/object. `Response.Output.Write` is a
`TextWriter` that supports formatted output (like `String.Format`-style
placeholders) directly.

**[⬆ Back to Top](#table-of-contents)**

## 41. `Server.Transfer` vs `Response.Redirect`

`Server.Transfer` happens server-side, preserves the original URL in the browser,
and is faster (no round trip) — but only works within the same application.
`Response.Redirect` sends an HTTP 302 to the browser, which then makes a brand-new
request — works across applications/domains, but costs an extra round trip and
changes the URL bar.

**[⬆ Back to Top](#table-of-contents)**

## 42. What is Cross-Page Posting?

A page posts to a *different* page (via `PostBackUrl`) instead of itself; the
target page reads the source page's controls through the `PreviousPage` property.

**[⬆ Back to Top](#table-of-contents)**

## 43. What is Delay Signing?

A strong-naming technique where the public key is embedded at build time but the
private-key signing step is deferred to a later, separate, restricted process — used
so most developers don't need access to the actual signing key during day-to-day
builds.

**[⬆ Back to Top](#table-of-contents)**

## 44. In what type/format should you store and return dates?

Store dates as `DateTime`/`DateTimeOffset` (`DateTimeOffset` if time zone matters,
which it usually does for anything user-facing or distributed) and serialize them in
**ISO 8601** format (e.g. `2026-08-25T14:30:00Z`) — it's unambiguous, sortable as a
string, and every serializer/client understands it natively.

**[⬆ Back to Top](#table-of-contents)**

## 45. `DataSet` vs `DataReader`

`DataReader` is a fast, forward-only, read-only stream over a live connection — low
memory, but the connection must stay open while you read. `DataSet` loads the
entire result (potentially multiple tables, with relationships) into an in-memory,
disconnected structure you can pass around, cache, or serialize — more overhead, but
no connection dependency after the initial fetch.

**[⬆ Back to Top](#table-of-contents)**

## 46. What is serialization/deserialization?

**Serialization** converts an in-memory object into a storable/transmittable format
(JSON, XML, binary); **deserialization** reverses it, rebuilding the object graph
from that format. Used constantly for API payloads, caching, and persisting state
across process boundaries.

**[⬆ Back to Top](#table-of-contents)**

## 47. .NET Framework vs .NET Core

The **.NET Framework** is the original, Windows-only runtime and base class library.
**.NET Core** (now unified as modern **.NET 5+**) is cross-platform (Windows,
macOS, Linux), open-source, more modular, and generally faster — built for cloud and
containerized workloads. New development targets modern .NET; the Framework is
effectively legacy-maintenance-only at this point.

**[⬆ Back to Top](#table-of-contents)**

## 48. What are the ASP.NET page life-cycle events?

`Init` → `Load` → validation → postback event handling → `PreRender` → `Render` →
`Unload`. Knowing the order matters most for control state timing — e.g. why you
can't reliably read a dynamically-added control's postback value if it wasn't
re-added by `Init` on every request.

**[⬆ Back to Top](#table-of-contents)**

## 49. How do you force all validation controls to run?

Call `Page.Validate()` explicitly (optionally with a specific `ValidationGroup`), or
make sure the triggering button's `ValidationGroup` matches the validators you want
to run — a button with `CausesValidation="false"` will skip validation entirely,
which is a common source of "why didn't my validators fire" bugs.

**[⬆ Back to Top](#table-of-contents)**

## 50. IEnumerable vs List — deferred execution vs eager loading

`List<T>` is a concrete, fully-materialized collection sitting in memory right now.
`IEnumerable<T>` is a *sequence* that may not have produced any values yet — LINQ
methods like `.Where()`/`.Select()` on an `IEnumerable<T>` build up a **query
definition** that only actually runs when you enumerate it (`foreach`, `.ToList()`,
`.Count()`, etc.). This is called **deferred execution**, and it causes a genuinely
surprising bug if you're not expecting it:

```csharp
List<int> numbers = new List<int> { 1, 2, 3 };

IEnumerable<int> query = numbers.Where(n => n > 1); // NOT executed yet — just a definition
numbers.Add(4);                                      // mutate the source before enumerating

foreach (var n in query) Console.WriteLine(n);
// Prints 2, 3, 4 — the "4" is included because the filter only ran just now,
// during the foreach, against the list's CURRENT contents.

List<int> eager = numbers.Where(n => n > 1).ToList(); // executes immediately, snapshot taken now
numbers.Add(5);
// `eager` still only has {2, 3, 4} — it was materialized before the Add(5)
```

**How to phrase it:** "`IEnumerable` queries are lazy — nothing runs until you
enumerate them, which is efficient but means the results can change if the
underlying source changes before you do. Calling `.ToList()` forces immediate,
eager execution and locks in a snapshot at that exact moment."

**[⬆ Back to Top](#table-of-contents)**
