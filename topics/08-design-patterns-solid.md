# Design Patterns & SOLID

> The trap on this topic is reciting definitions. Every answer here should end with
> a concrete violation-and-fix example — that's what interviewers are actually
> listening for.

## Table of Contents

| No. | Question |
|-----|----------|
| 1 | [Explain the SOLID principles, with a violation and a fix for each](#1-explain-the-solid-principles-with-a-violation-and-a-fix-for-each) |
| 2 | [Which SOLID principle is "L", and what does it mean?](#2-which-solid-principle-is-l-and-what-does-it-mean) |
| 3 | [Singleton pattern](#3-singleton-pattern) |
| 4 | [Factory pattern](#4-factory-pattern) |
| 5 | [Abstract class vs interface — the design-pattern angle](#5-abstract-class-vs-interface--the-design-pattern-angle) |
| 6 | [What design patterns have you actually used?](#6-what-design-patterns-have-you-actually-used) |
| 7 | [Memento pattern: undo/redo on a string](#7-memento-pattern-undoredo-on-a-string) |

## 1. Explain the SOLID principles, with a violation and a fix for each

- **S — Single Responsibility Principle:** a class should have one reason to
  change. *Violation:* an `Order` class that also formats an invoice PDF and
  sends an email. *Fix:* split into `Order`, `InvoicePdfGenerator`,
  `OrderNotifier` — each owns one concern and changes for one reason.

- **O — Open/Closed Principle:** open for extension, closed for modification.
  *Violation:* a `switch` on a `ShapeType` enum inside `CalculateArea()` that you
  have to edit every time a new shape is added. *Fix:* an `IShape` interface with
  a `CalculateArea()` method on each concrete shape — adding a new shape means
  adding a new class, not touching existing code.

- **L — Liskov Substitution Principle:** subtypes must be usable wherever the
  base type is expected, without breaking correctness. *Violation:* a `Square`
  that inherits from `Rectangle` and overrides `SetWidth`/`SetHeight` to keep
  both sides equal — code that sets width and height independently on a
  `Rectangle` now behaves unexpectedly when handed a `Square`. *Fix:* don't model
  `Square` as a `Rectangle` subtype at all; have both implement a common `IShape`
  interface instead.

- **I — Interface Segregation Principle:** don't force a class to implement
  methods it doesn't need. *Violation:* a fat `IWorker` interface with `Work()`
  and `Eat()` that a `RobotWorker` is forced to implement `Eat()` for (and throw
  `NotImplementedException`). *Fix:* split into `IWorkable` and `IFeedable`, and
  implement only what applies.

- **D — Dependency Inversion Principle:** depend on abstractions, not concrete
  implementations. *Violation:* a `NotificationService` that directly `new`s up a
  `SmtpEmailSender` inside it. *Fix:* inject an `INotificationSender` interface
  via the constructor — the high-level module no longer depends on (or needs to
  change for) a specific low-level implementation.

**[⬆ Back to Top](#table-of-contents)**

## 2. Which SOLID principle is "L", and what does it mean?

The **Liskov Substitution Principle** — named after Barbara Liskov. It says: if
`S` is a subtype of `T`, objects of type `T` should be replaceable with objects
of type `S` without altering the correctness of the program. In practice, it's a
check on whether an inheritance relationship is actually behaviorally sound, not
just structurally convenient — the classic Square/Rectangle example above is the
canonical violation to cite.

**[⬆ Back to Top](#table-of-contents)**

## 3. Singleton pattern

Guarantees a class has exactly one instance, with a global access point to it.

```csharp
public sealed class ConfigurationManager
{
    private static readonly Lazy<ConfigurationManager> _instance =
        new(() => new ConfigurationManager());

    public static ConfigurationManager Instance => _instance.Value;

    private ConfigurationManager() { /* load config */ }
}
```

Using `Lazy<T>` gives thread-safe, lazy initialization without hand-rolling
double-checked locking. **In a DI-based app, prefer registering the type as
`AddSingleton` in the container instead** of this hand-rolled pattern — it gets
you the same guarantee while staying testable/mockable, which the classic
static-instance Singleton is not.

**[⬆ Back to Top](#table-of-contents)**

## 4. Factory pattern

Centralizes object creation logic so callers depend on an interface, not a
concrete constructor — useful when the exact type to create depends on runtime
conditions:

```csharp
public interface INotificationSender { void Send(string message); }
public class EmailSender : INotificationSender { public void Send(string m) { } }
public class SmsSender : INotificationSender { public void Send(string m) { } }

public static class NotificationFactory
{
    public static INotificationSender Create(string channel) => channel switch
    {
        "email" => new EmailSender(),
        "sms" => new SmsSender(),
        _ => throw new ArgumentException("Unknown channel")
    };
}
```

**[⬆ Back to Top](#table-of-contents)**

## 5. Abstract class vs interface — the design-pattern angle

Beyond the mechanical differences (see the C# file), the design guidance is: use
an **interface** to define a role/capability that unrelated types can plug into
(this is what makes the Strategy, Factory, and Repository patterns work at all —
they all depend on programming to an interface). Use an **abstract class** when
there's real shared implementation to inherit, and the family of types is
genuinely related by "is-a", not just "can-do".

**[⬆ Back to Top](#table-of-contents)**

## 6. What design patterns have you actually used?

Answer this with real examples tied to a project, not a memorized list. A
credible, common combination for a typical .NET service:

- **Dependency Injection** everywhere via the built-in container.
- **Repository** (and sometimes Unit of Work) over EF Core for testability.
- **Strategy** for interchangeable business rules (e.g. different pricing rules
  per client, selected at runtime behind a common interface).
- **Factory** for constructing the right handler/strategy based on input.
- **Decorator** for cross-cutting concerns like caching or logging wrapped around
  a service without modifying it (`ICachedProductService` wrapping
  `IProductService`).
- **Circuit Breaker** (via Polly) for resilient outbound HTTP calls.

**[⬆ Back to Top](#table-of-contents)**

## 7. Memento pattern: undo/redo on a string

The Memento pattern captures an object's state so it can be restored later,
without exposing its internals:

```csharp
public class StringEditor
{
    private string _text = "";
    private readonly Stack<string> _history = new();

    public string Text
    {
        get => _text;
        set { _history.Push(_text); _text = value; }
    }

    public void Undo()
    {
        if (_history.Count > 0)
            _text = _history.Pop();
    }
}
```

Each mutation pushes the *previous* state onto a stack before applying the new
one; `Undo()` pops the last snapshot back. A full undo/redo implementation adds a
second "redo" stack that captures what `Undo()` just discarded, so a subsequent
`Redo()` can reapply it.

**[⬆ Back to Top](#table-of-contents)**
