# Testing, TDD & Code Quality

> Often the most under-prepared topic, which makes it easy points — most
> candidates can talk architecture for an hour but go vague the moment testing
> comes up.

## Table of Contents

| No. | Question |
|-----|----------|
| 1 | [What is unit testing, and why does it matter?](#1-what-is-unit-testing-and-why-does-it-matter) |
| 2 | [What is Test-Driven Development (TDD)?](#2-what-is-test-driven-development-tdd) |
| 3 | [Arrange-Act-Assert](#3-arrange-act-assert) |
| 4 | [How do you unit test a method that returns `void`?](#4-how-do-you-unit-test-a-method-that-returns-void) |
| 5 | [What is mocking, and when should you use it?](#5-what-is-mocking-and-when-should-you-use-it) |
| 6 | [Stubs vs mocks vs fakes](#6-stubs-vs-mocks-vs-fakes) |
| 7 | [What is code coverage, and how is it measured?](#7-what-is-code-coverage-and-how-is-it-measured) |
| 8 | [What makes a unit test a good one?](#8-what-makes-a-unit-test-a-good-one) |
| 9 | [How do you handle external dependencies in a unit test?](#9-how-do-you-handle-external-dependencies-in-a-unit-test) |
| 10 | [Integration tests vs unit tests](#10-integration-tests-vs-unit-tests) |
| 11 | [How do you handle time-dependent code in a test?](#11-how-do-you-handle-time-dependent-code-in-a-test) |
| 12 | [How do you unit test code that uses Dependency Injection?](#12-how-do-you-unit-test-code-that-uses-dependency-injection) |

## 1. What is unit testing, and why does it matter?

A unit test verifies a small, isolated piece of code (typically one method or
one class) behaves correctly, independent of its real collaborators (database,
network, file system). It matters because it catches regressions immediately and
cheaply — a failing unit test points at the exact broken unit in seconds, versus
discovering the same bug in QA or production where it's far more expensive to
trace back.

**[⬆ Back to Top](#table-of-contents)**

## 2. What is Test-Driven Development (TDD)?

Write a failing test first, write the minimum code to make it pass, then
refactor — "red, green, refactor," repeated in small cycles. The claimed benefit
isn't really "more tests," it's that designing the test first forces you to think
about the API/contract from the caller's perspective before you've committed to
an implementation, which tends to produce more testable, more decoupled code.

**[⬆ Back to Top](#table-of-contents)**

## 3. Arrange-Act-Assert

The standard structure for a readable unit test:

```csharp
[Fact]
public void CalculateTotal_AppliesDiscountAndTax()
{
    // Arrange
    var order = new Order(subtotal: 100m);
    var calculator = new PriceCalculator(discountPercent: 10m, taxPercent: 5m);

    // Act
    var total = calculator.CalculateTotal(order);

    // Assert
    Assert.Equal(94.5m, total);
}
```

**Arrange** sets up the inputs/collaborators, **Act** invokes the thing under
test (ideally one call), **Assert** checks the outcome. Keeping these visually
separated is what makes a test scannable at a glance.

**[⬆ Back to Top](#table-of-contents)**

## 4. How do you unit test a method that returns `void`?

You can't assert on a return value, so you assert on **observable side effects**
instead:
- Verify a mocked dependency was called with the expected arguments
  (`mock.Verify(x => x.Save(It.IsAny<Order>()), Times.Once)`).
- Check that some observable state changed (a property on the object under test,
  a record now present in an in-memory fake repository).
- Assert that an expected event/exception was raised.

**[⬆ Back to Top](#table-of-contents)**

## 5. What is mocking, and when should you use it?

Mocking replaces a real dependency with a controllable substitute so you can
test a unit in isolation and verify *how* it interacted with that dependency.
Use it for dependencies that are slow, non-deterministic, or side-effecting
(a database, an HTTP call, the system clock, email sending) — not for simple,
fast, pure value objects, which you can just use directly.

```csharp
var mockRepo = new Mock<IOrderRepository>();
mockRepo.Setup(r => r.GetByIdAsync(1)).ReturnsAsync(new Order { Id = 1 });

var service = new OrderService(mockRepo.Object);
var result = await service.ProcessAsync(1);

mockRepo.Verify(r => r.GetByIdAsync(1), Times.Once);
```

**[⬆ Back to Top](#table-of-contents)**

## 6. Stubs vs mocks vs fakes

| Test double | Behavior | Use it to... |
|---|---|---|
| **Stub** | Returns canned answers to calls made during the test | Feed the unit under test fixed input data |
| **Mock** | Records calls made to it so you can *verify* interactions afterward | Assert that a specific method was/wasn't called, with what arguments |
| **Fake** | A real, working, but simplified implementation (e.g. an in-memory repository instead of a real database) | Stand in for a heavyweight dependency with realistic-enough behavior |
| **Dummy** | Passed around to satisfy a parameter list, never actually used | Fill required constructor arguments the test doesn't care about |

**[⬆ Back to Top](#table-of-contents)**

## 7. What is code coverage, and how is it measured?

The percentage of code (lines, branches, or methods) exercised by the test
suite, measured by instrumenting the build and tracking which lines execute
during a test run (tools like Coverlet for .NET, then visualized with
ReportGenerator or a CI dashboard). **The caveat worth stating unprompted:** high
coverage doesn't guarantee good tests — a test can execute a line without
actually asserting anything meaningful about its behavior. Coverage is a useful
signal for *finding untested code*, not a target to chase for its own sake.

**[⬆ Back to Top](#table-of-contents)**

## 8. What makes a unit test a good one?

- **Fast** — runs in milliseconds; a slow suite stops getting run.
- **Isolated** — doesn't depend on other tests' order or shared mutable state.
- **Deterministic** — same result every run; no reliance on the real clock,
  random values, or network calls.
- **Tests one behavior** — a failing test should tell you exactly what broke,
  not require digging through five assertions to find out.
- **Readable** — the test itself documents the expected behavior; a future
  reader shouldn't need the implementation open to understand what's being
  verified.

**[⬆ Back to Top](#table-of-contents)**

## 9. How do you handle external dependencies in a unit test?

Depend on **interfaces**, not concrete implementations, so a real database/HTTP
client/file system can be swapped for a mock or fake in the test. For code that's
hard to restructure this way (legacy code with concrete dependencies baked in),
wrap the external dependency behind a thin interface first (an "adapter"), which
is often the very first refactor needed before legacy code becomes testable at
all.

**[⬆ Back to Top](#table-of-contents)**

## 10. Integration tests vs unit tests

**Unit tests** isolate a single unit with all its dependencies faked/mocked —
fast, pinpoint failures, but don't prove the pieces actually work *together*.
**Integration tests** exercise real collaborators (a real database, typically via
a test container or a dedicated test database; a real HTTP call to a downstream
service, or at least a more realistic stand-in) to verify the wiring between
components is actually correct. A healthy test suite has many fast unit tests and
a smaller number of integration tests covering the critical seams — not one
extreme or the other.

**[⬆ Back to Top](#table-of-contents)**

## 11. How do you handle time-dependent code in a test?

Never call `DateTime.Now`/`DateTime.UtcNow` directly inside logic you want to
test deterministically — inject a time abstraction instead:

```csharp
public interface IClock { DateTime UtcNow { get; } }
public class SystemClock : IClock { public DateTime UtcNow => DateTime.UtcNow; }
```

In the test, supply a fake `IClock` returning a fixed date, so assertions like
"is this subscription expired" are deterministic regardless of when the test
actually runs. (.NET 8+ also ships `TimeProvider` as a built-in equivalent
abstraction.)

**[⬆ Back to Top](#table-of-contents)**

## 12. How do you unit test code that uses Dependency Injection?

You don't need the DI **container** at all for a unit test — that's exactly the
point of constructor injection. Just `new` up the class under test directly,
passing mocked/faked implementations of its interfaces by hand:

```csharp
var service = new OrderService(mockRepo.Object, mockLogger.Object);
```

Reserve spinning up the actual DI container (`WebApplicationFactory` in ASP.NET
Core) for integration tests that specifically want to verify the wiring itself,
not for ordinary unit tests.

**[⬆ Back to Top](#table-of-contents)**
