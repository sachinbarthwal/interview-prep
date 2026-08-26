# Entity Framework, ADO.NET & Data Access

> Almost every .NET interview probes whether you understand what your ORM is doing
> *underneath* the LINQ syntax — because that's exactly where production incidents
> come from (N+1 queries, concurrency conflicts, a `DbContext` held open too long).

## Table of Contents

| No. | Question |
|-----|----------|
| 1 | [ADO.NET vs Entity Framework](#1-adonet-vs-entity-framework) |
| 2 | [What is Entity Framework, and how do Code First / DB First / Model First differ?](#2-what-is-entity-framework-and-how-do-code-first--db-first--model-first-differ) |
| 3 | [EF Core vs Dapper](#3-ef-core-vs-dapper) |
| 4 | [Lazy loading vs eager loading](#4-lazy-loading-vs-eager-loading) |
| 5 | [Multiple connections and multiple database instances with EF](#5-multiple-connections-and-multiple-database-instances-with-ef) |
| 6 | [How do you handle concurrency conflicts in EF Core?](#6-how-do-you-handle-concurrency-conflicts-in-ef-core) |
| 7 | [What is an EDMX file?](#7-what-is-an-edmx-file) |
| 8 | [What is Fluent API?](#8-what-is-fluent-api) |
| 9 | [What is tracing in Entity Framework?](#9-what-is-tracing-in-entity-framework) |
| 10 | [Which design pattern does Entity Framework implement?](#10-which-design-pattern-does-entity-framework-implement) |
| 11 | [What is the Repository pattern, and why add it on top of EF?](#11-what-is-the-repository-pattern-and-why-add-it-on-top-of-ef) |
| 12 | [Write a LINQ query: department with the highest average salary](#12-write-a-linq-query-department-with-the-highest-average-salary) |
| 13 | [How do you write a LEFT JOIN in LINQ?](#13-how-do-you-write-a-left-join-in-linq) |

## 1. ADO.NET vs Entity Framework

**ADO.NET** is the low-level data-access layer — you write raw SQL, manage
`SqlConnection`/`SqlCommand`/`DataReader` objects directly, and map results by
hand. **Entity Framework** is an ORM built on top of that idea — you work with
.NET objects and LINQ, and EF generates the SQL and maps rows back to objects for
you. Trade-off: ADO.NET gives full control and the best raw performance; EF gives
massive productivity at the cost of some abstraction overhead and less obvious SQL.

**[⬆ Back to Top](#table-of-contents)**

## 2. What is Entity Framework, and how do Code First / DB First / Model First differ?

Entity Framework is an **Object-Relational Mapper** — it translates LINQ queries
into SQL and maps rows back into strongly-typed .NET objects, tracking changes so
`SaveChanges()` can generate the right INSERT/UPDATE/DELETE statements.

- **Code First** — you write C# entity classes; EF generates the database schema
  (via migrations) from them. Best when the codebase is the source of truth.
- **Database First** — you point EF at an existing database; it scaffolds entity
  classes and a context from the existing schema. Best for legacy databases you
  don't want to redesign.
- **Model First** — you design a visual EDMX model, and EF generates both the
  database schema and the entity classes from it (largely legacy at this point,
  from the original EF/EDMX tooling).

**[⬆ Back to Top](#table-of-contents)**

## 3. EF Core vs Dapper

**EF Core** is a full ORM — change tracking, migrations, LINQ-to-SQL translation,
lazy/eager loading, relationship navigation. Great for productivity and complex
object graphs, at some performance cost. **Dapper** is a lightweight
**micro-ORM** — you write the SQL yourself, and Dapper just maps the result set
onto your objects, extremely fast, minimal overhead, no change tracking or
migrations. A common real-world pattern: EF Core for the bulk of CRUD/business
logic, Dapper for a handful of performance-critical read queries where hand-tuned
SQL and raw speed matter more than ORM convenience.

**[⬆ Back to Top](#table-of-contents)**

## 4. Lazy loading vs eager loading

- **Lazy loading** — related data is fetched **on first access** of the
  navigation property, as a separate query. Convenient, but easy to trigger the
  classic **N+1 query problem** — looping over 100 orders and touching
  `order.Customer` inside the loop fires 100 extra queries.
- **Eager loading** — related data is fetched **up front**, in the same query
  (or a small fixed number of queries), via `.Include()`:

```csharp
var orders = context.Orders
    .Include(o => o.Customer)
    .Include(o => o.Items)
    .ToList();
```

Default to eager loading when you know you'll need the related data; reach for
explicit/lazy loading only when it's genuinely optional per request.

**[⬆ Back to Top](#table-of-contents)**

## 5. Multiple connections and multiple database instances with EF

Yes — each `DbContext` instance manages its own connection, and nothing stops you
from having multiple `DbContext` instances (even to different databases) alive at
once, as long as each is scoped correctly (typically one per request/unit of
work). For **multiple database instances per region** (e.g. sharding by
geography), the common approach is a connection-string resolver keyed by
tenant/region that picks the right connection string before the `DbContext` is
constructed, so each request talks to the correct regional database transparently.

**[⬆ Back to Top](#table-of-contents)**

## 6. How do you handle concurrency conflicts in EF Core?

EF Core uses **optimistic concurrency** by default — it doesn't lock rows, it
detects conflicts when saving. Add a concurrency token (a `[Timestamp]`/
`RowVersion` column):

```csharp
public class MyEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    [Timestamp]
    public byte[] RowVersion { get; set; }
}

try
{
    context.SaveChanges();
}
catch (DbUpdateConcurrencyException ex)
{
    foreach (var entry in ex.Entries)
    {
        var databaseValues = entry.GetDatabaseValues();
        if (databaseValues != null)
        {
            // decide: overwrite with client values, reload and retry,
            // or surface a "someone else changed this" conflict to the user
            entry.OriginalValues.SetValues(databaseValues);
        }
    }
    context.SaveChanges();
}
```

This is the mechanism behind the classic "User A's stale save silently overwrites
User B's edit" interview scenario — without a concurrency token, EF has no way to
detect that the row changed between when it was read and when it's being saved.

**[⬆ Back to Top](#table-of-contents)**

## 7. What is an EDMX file?

An XML file (`.edmx`) from the original Entity Framework (EF6 and earlier) that
holds the conceptual model, storage model, and the mapping between them, along
with the visual designer's layout information — largely superseded by EF Core's
code-based `OnModelCreating`/Fluent API configuration, which has no visual
designer or XML mapping file at all.

**[⬆ Back to Top](#table-of-contents)**

## 8. What is Fluent API?

A code-based way to configure entity mappings (keys, relationships, constraints,
indexes, table/column names) inside `OnModelCreating`, as an alternative to Data
Annotation attributes on the entity classes themselves:

```csharp
protected override void OnModelCreating(ModelBuilder modelBuilder)
{
    modelBuilder.Entity<Order>()
        .HasOne(o => o.Customer)
        .WithMany(c => c.Orders)
        .HasForeignKey(o => o.CustomerId);

    modelBuilder.Entity<Order>()
        .Property(o => o.OrderNumber)
        .IsRequired()
        .HasMaxLength(20);
}
```

Fluent API can express mapping rules attributes can't (e.g. composite keys), and
keeps entity classes free of persistence-specific attributes.

**[⬆ Back to Top](#table-of-contents)**

## 9. What is tracing in Entity Framework?

Logging the actual SQL EF generates (and how long it took) so you can see what's
really being sent to the database — essential for diagnosing an unexpected N+1
query pattern or a slow LINQ query. In EF Core this is typically wired up via
`.LogTo(Console.WriteLine)` on the context options, or through the standard
`ILogger` integration in ASP.NET Core.

**[⬆ Back to Top](#table-of-contents)**

## 10. Which design pattern does Entity Framework implement?

`DbContext` itself is effectively a **Unit of Work** — it tracks every change
made across multiple entities and commits them together in one transaction on
`SaveChanges()`. Each `DbSet<T>` behaves like a **Repository** for that entity
type. This is exactly why hand-rolling an additional Repository/Unit-of-Work layer
on top of EF Core is often debated — EF Core already gives you both, and an extra
layer can just be indirection without new value, unless you specifically need to
abstract EF out entirely (e.g. to swap persistence technology, or to simplify
mocking in unit tests).

**[⬆ Back to Top](#table-of-contents)**

## 11. What is the Repository pattern, and why add it on top of EF?

A Repository exposes a collection-like interface (`GetById`, `Add`, `Remove`,
`Find`) over data access, hiding the underlying persistence mechanism from the
rest of the application:

```csharp
public interface IOrderRepository
{
    Task<Order> GetByIdAsync(int id);
    Task AddAsync(Order order);
}
```

Reasons to add it even over EF Core: it gives you a seam to mock in unit tests
without spinning up a real/in-memory database, it centralizes query logic instead
of scattering LINQ across services, and it insulates the rest of the app if you
ever need to change the underlying data access technology.

**[⬆ Back to Top](#table-of-contents)**

## 12. Write a LINQ query: department with the highest average salary

```csharp
public class Employee
{
    public string Name { get; set; }
    public string Department { get; set; }
    public decimal Salary { get; set; }
}

string department = employees
    .GroupBy(e => e.Department)
    .OrderByDescending(g => g.Average(e => e.Salary))
    .FirstOrDefault()
    ?.Key;
```

`GroupBy` buckets employees per department, `Average` computes the per-group
salary average, and `OrderByDescending` + `FirstOrDefault` picks the top one.

**[⬆ Back to Top](#table-of-contents)**

## 13. How do you write a LEFT JOIN in LINQ?

LINQ's `join` is an inner join by default; a left join needs `DefaultIfEmpty()`:

```csharp
var result =
    from d in departments
    join e in employees on d.DeptId equals e.DeptId into deptEmployees
    from emp in deptEmployees.DefaultIfEmpty()
    select new
    {
        d.DeptId,
        d.DeptName,
        EmployeeName = emp != null ? emp.Name : null
    };
```

The `into` clause creates a group join; `DefaultIfEmpty()` is what turns it into a
left join by supplying a `null` when a department has no matching employees.

**[⬆ Back to Top](#table-of-contents)**
