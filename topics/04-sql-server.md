# SQL Server & Databases

> The SQL round separates people who've memorized syntax from people who've
> actually debugged a slow production query. Wherever a question is "write a
> query", also be ready to say *why* it's fast or slow.

## Table of Contents

| No. | Question |
|-----|----------|
| 1 | [What is SQL Injection, and how do you prevent it?](#1-what-is-sql-injection-and-how-do-you-prevent-it) |
| 2 | [Joins and self-joins](#2-joins-and-self-joins) |
| 3 | [Inline query vs stored procedure](#3-inline-query-vs-stored-procedure) |
| 4 | [Stored procedure vs SQL function](#4-stored-procedure-vs-sql-function) |
| 5 | [How do you optimize a slow stored procedure?](#5-how-do-you-optimize-a-slow-stored-procedure) |
| 6 | [How would you handle billions of rows efficiently?](#6-how-would-you-handle-billions-of-rows-efficiently) |
| 7 | [How do you implement pagination in SQL?](#7-how-do-you-implement-pagination-in-sql) |
| 8 | [What are triggers, and when do you use one?](#8-what-are-triggers-and-when-do-you-use-one) |
| 9 | [What are indexes, and how do they get applied?](#9-what-are-indexes-and-how-do-they-get-applied) |
| 10 | [Filtered index vs non-clustered index](#10-filtered-index-vs-non-clustered-index) |
| 11 | [How does a B-tree index change read/write behavior?](#11-how-does-a-b-tree-index-change-readwrite-behavior) |
| 12 | [What is the "magic table" in SQL Server?](#12-what-is-the-magic-table-in-sql-server) |
| 13 | [What does `PARTITION BY` do?](#13-what-does-partition-by-do) |
| 14 | [Table variable vs temp table](#14-table-variable-vs-temp-table) |
| 15 | [What is a CTE?](#15-what-is-a-cte) |
| 16 | [What are Views, and when should you use one?](#16-what-are-views-and-when-should-you-use-one) |
| 17 | [What does `MERGE` do?](#17-what-does-merge-do) |
| 18 | [Should you run SQL Profiler on production?](#18-should-you-run-sql-profiler-on-production) |
| 19 | [`RANK()` vs `DENSE_RANK()`](#19-rank-vs-dense_rank) |
| 20 | [What are window functions? Write a running total.](#20-what-are-window-functions-write-a-running-total) |
| 21 | [What is a transaction, and how do you start one?](#21-what-is-a-transaction-and-how-do-you-start-one) |
| 22 | [How do you make a stored procedure parameter optional?](#22-how-do-you-make-a-stored-procedure-parameter-optional) |
| 23 | [How would you design a multi-tenant database schema?](#23-how-would-you-design-a-multi-tenant-database-schema) |
| 24 | [Find the 3rd-highest salary](#24-find-the-3rd-highest-salary) |
| 25 | [Find duplicate rows](#25-find-duplicate-rows) |
| 26 | [Find the manager with the most direct reports](#26-find-the-manager-with-the-most-direct-reports) |
| 27 | [Find employees whose DOB/DOJ is the last day of the month](#27-find-employees-whose-dobdoj-is-the-last-day-of-the-month) |
| 28 | [SQL Server vs RavenDB](#28-sql-server-vs-ravendb) |
| 29 | [General strategies for optimizing a slow query](#29-general-strategies-for-optimizing-a-slow-query) |

## 1. What is SQL Injection, and how do you prevent it?

SQL Injection is when untrusted input gets concatenated directly into a SQL
string, letting an attacker inject their own SQL:

```csharp
// vulnerable
var sql = $"SELECT * FROM Users WHERE Username = '{username}'";
// username = "' OR '1'='1" returns every row
```

**Prevention:** always use parameterized queries or an ORM that parameterizes for
you — never string-concatenate user input into SQL:

```csharp
var cmd = new SqlCommand("SELECT * FROM Users WHERE Username = @username", conn);
cmd.Parameters.AddWithValue("@username", username);
```

Also apply least-privilege database accounts, and validate/allow-list input where
it feeds into anything dynamic (like a sortable column name that can't itself be
parameterized).

**[⬆ Back to Top](#table-of-contents)**

## 2. Joins and self-joins

A **join** combines rows from two tables based on a related column
(`INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`). A **self-join** joins a
table to itself — the classic use case is a hierarchical relationship stored in
one table, like an `Employee` table where each row has a `ManagerId` that points
back to another row's `EmployeeId`:

```sql
SELECT e.EmpName AS Employee, m.EmpName AS Manager
FROM Employee e
LEFT JOIN Employee m ON e.ManagerId = m.EmpId;
```

**[⬆ Back to Top](#table-of-contents)**

## 3. Inline query vs stored procedure

| | Inline query | Stored procedure |
|---|---|---|
| Where it lives | Application code | Database |
| Execution plan | Ad-hoc, may recompile more often (though SQL Server does cache parameterized plans) | Precompiled/cached, generally more predictable |
| Deployment | Ships with app code | Deployed/versioned separately from the app |
| Security | Needs care to parameterize (injection risk) | Naturally parameterized; can grant execute rights without granting table access |
| Maintainability | Easy to keep next to the code using it | Centralizes logic, but spreads business rules into the DB layer |

**[⬆ Back to Top](#table-of-contents)**

## 4. Stored procedure vs SQL function

A **stored procedure** can perform DML (INSERT/UPDATE/DELETE), doesn't have to
return a value, can return multiple result sets, and can't be used directly
inside a `SELECT`. A **function** (scalar or table-valued) must return a value,
can't perform side-effecting operations like inserts, but *can* be composed
directly into a `SELECT`/`WHERE` clause — at the cost that scalar functions
called per-row can be a serious performance trap since they often can't use
indexes and get invoked once per row.

```sql
-- Stored procedure: can INSERT, can't be used inside a SELECT
CREATE PROCEDURE GetHighEarners @MinSalary DECIMAL
AS
BEGIN
    SELECT * FROM Employee WHERE Salary >= @MinSalary;
END
EXEC GetHighEarners @MinSalary = 50000;

-- Scalar function: must return a value, CAN be used inside a SELECT
CREATE FUNCTION dbo.YearsEmployed(@HireDate DATE)
RETURNS INT
AS
BEGIN
    RETURN DATEDIFF(YEAR, @HireDate, GETDATE());
END
SELECT Name, dbo.YearsEmployed(HireDate) AS Years FROM Employee;
```

**[⬆ Back to Top](#table-of-contents)**

## 5. How do you optimize a slow stored procedure?

1. Capture the **actual execution plan** and look for table scans where an index
   seek should be happening, expensive sort/hash operations, or a huge gap between
   estimated and actual row counts (a sign statistics are stale).
2. Check indexing on every column used in `WHERE`, `JOIN`, and `ORDER BY`.
3. Avoid `SELECT *` — only pull the columns actually needed.
4. Watch for implicit conversions (comparing a `varchar` column to an `nvarchar`
   parameter silently disables index usage).
5. Avoid scalar UDFs in the `SELECT`/`WHERE` list when called per row.
6. Update statistics / rebuild fragmented indexes if the plan looks stale.
7. Break an overly complex procedure into smaller steps with intermediate temp
   tables if the optimizer is choosing a bad plan for one giant query.

**How do you identify it's the problem in the first place?** SQL Profiler/Extended
Events (or Query Store) to find procedures with the highest cumulative duration or
worst average duration relative to call count — not just the slowest single call.

**[⬆ Back to Top](#table-of-contents)**

## 6. How would you handle billions of rows efficiently?

- **Indexing** aligned to actual query patterns (and only those — over-indexing
  slows writes).
- **Partitioning** the table (e.g. by date range) so queries and maintenance only
  touch the relevant partition.
- **Batching** large writes/deletes into chunks instead of one massive
  transaction, to avoid lock escalation and huge transaction log growth.
- **Pagination** for anything reading a subset (see below) instead of pulling the
  full set.
- Pushing aggregation down into the database (`GROUP BY`, indexed views) rather
  than pulling raw rows into the application to aggregate.
- Considering columnstore indexes for large analytical/reporting workloads.

**[⬆ Back to Top](#table-of-contents)**

## 7. How do you implement pagination in SQL?

```sql
-- SQL Server 2012+
SELECT *
FROM Orders
ORDER BY OrderDate
OFFSET (@PageNumber - 1) * @PageSize ROWS
FETCH NEXT @PageSize ROWS ONLY;
```

Older approach using `ROW_NUMBER()` (also portable to databases without
`OFFSET/FETCH`):

```sql
SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER (ORDER BY OrderDate) AS RowNum
    FROM Orders
) AS sub
WHERE RowNum BETWEEN (@PageNumber - 1) * @PageSize + 1 AND @PageNumber * @PageSize;
```

An `ORDER BY` is mandatory for either approach — without a deterministic order,
"page 2" isn't a well-defined concept.

**[⬆ Back to Top](#table-of-contents)**

## 8. What are triggers, and when do you use one?

A trigger is code that fires automatically in response to a DML event
(`INSERT`/`UPDATE`/`DELETE`) or DDL event on a table. Legitimate uses: auditing
(writing to a history table), enforcing complex cross-table business rules a
constraint can't express, or maintaining denormalized aggregates. Downsides worth
mentioning unprompted: triggers are invisible in application code, easy to forget
about, can cause surprising cascading behavior, and can hurt write performance —
so most teams prefer application-level logic or explicit stored-procedure calls
where practical.

**[⬆ Back to Top](#table-of-contents)**

## 9. What are indexes, and how do they get applied?

An index is a separate data structure (typically a B-tree) that stores a sorted
copy of one or more columns plus a pointer back to the full row, so the engine can
**seek** directly to matching rows instead of **scanning** the whole table. A
**clustered index** determines the physical storage order of the table itself
(one per table); a **non-clustered index** is a separate structure with a pointer
(the clustering key, or a row ID) back to the actual row. The optimizer decides
whether to use an index based on selectivity, statistics, and the query's `WHERE`/
`JOIN`/`ORDER BY` columns — an index that doesn't match how the table is actually
queried just adds write overhead without ever getting used.

```sql
-- Without an index: SQL Server scans every row in Employee to find matches
SELECT * FROM Employee WHERE Department = 'Engineering';

-- Add an index on the column used in WHERE/JOIN/ORDER BY
CREATE INDEX IX_Employee_Department ON Employee(Department);

-- Now the same query can SEEK directly to matching rows instead of scanning all of them
SELECT * FROM Employee WHERE Department = 'Engineering';
```

**[⬆ Back to Top](#table-of-contents)**

## 10. Filtered index vs non-clustered index

A **non-clustered index** covers all rows in the table for its indexed columns. A
**filtered index** is a non-clustered index with a `WHERE` clause, indexing only a
subset of rows — e.g. `WHERE IsActive = 1` — which keeps it smaller and faster
when queries consistently filter on that same condition, at the cost that it's
only usable for queries whose predicate is a subset of the filter.

**[⬆ Back to Top](#table-of-contents)**

## 11. How does a B-tree index change read/write behavior?

A B-tree keeps keys sorted in a balanced tree of pages, so a lookup, insert, or
delete takes roughly logarithmic time relative to the row count, instead of the
linear scan a heap table would need. Range queries (`BETWEEN`, `ORDER BY` on the
indexed column) are also fast because leaf pages are linked in sorted order.
The trade-off: every `INSERT`/`UPDATE`/`DELETE` has to keep the tree balanced and
every index up to date, so heavily-indexed tables pay a real cost on writes —
which is why indexing is a deliberate trade-off, not "add indexes everywhere".

**[⬆ Back to Top](#table-of-contents)**

## 12. What is the "magic table" in SQL Server?

The `inserted` and `deleted` pseudo-tables that exist only inside the scope of a
trigger, holding the before/after images of the affected rows — `inserted` holds
new/updated row values, `deleted` holds old/removed row values (an `UPDATE` shows
up in both, since SQL Server implements it as a delete + insert internally).

**[⬆ Back to Top](#table-of-contents)**

## 13. What does `PARTITION BY` do?

Used inside a window function to divide the result set into independent groups
that the window calculation resets for, without collapsing rows the way `GROUP BY`
does:

```sql
SELECT
    EmpId, Department, Salary,
    RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS DeptRank
FROM Employee;
```

Each department gets its own independent ranking, but every employee row is still
returned individually.

**[⬆ Back to Top](#table-of-contents)**

## 14. Table variable vs temp table

| | Table variable (`@Table`) | Temp table (`#Table`) |
|---|---|---|
| Scope | Current batch/procedure | Current session (and any nested calls) |
| Statistics | None kept (SQL Server assumes a fixed small row estimate historically) — can lead to bad plans on large data | Real statistics maintained, better plans for larger data |
| Indexes | Limited (constraints only, historically; modern SQL Server allows more) | Full index support |
| Transaction behavior | Not rolled back by an outer transaction rollback | Rolled back along with the transaction |
| Best for | Small row counts, simple logic | Larger intermediate result sets, anything needing real indexing |

```sql
-- Table variable
DECLARE @Temp TABLE (Id INT, Name NVARCHAR(50));
INSERT INTO @Temp VALUES (1, 'Sam');

-- Temp table
CREATE TABLE #Temp (Id INT, Name NVARCHAR(50));
INSERT INTO #Temp VALUES (1, 'Sam');
CREATE INDEX IX_Temp_Id ON #Temp(Id); -- full indexing support, unlike most @table variables
```

**[⬆ Back to Top](#table-of-contents)**

## 15. What is a CTE?

A **Common Table Expression** — a named, temporary result set defined with `WITH`,
scoped to the single statement that follows it. Useful for breaking a complex
query into readable steps, and it's also how you write a **recursive** query
(e.g. walking an org chart):

```sql
WITH OrgChart AS (
    SELECT EmpId, ManagerId, EmpName, 0 AS Level
    FROM Employee WHERE ManagerId IS NULL
    UNION ALL
    SELECT e.EmpId, e.ManagerId, e.EmpName, oc.Level + 1
    FROM Employee e
    JOIN OrgChart oc ON e.ManagerId = oc.EmpId
)
SELECT * FROM OrgChart;
```

**[⬆ Back to Top](#table-of-contents)**

## 16. What are Views, and when should you use one?

A **View** is a stored, named `SELECT` statement that can be queried like a table
— it doesn't store data itself (unless it's an **indexed/materialized view**), it
just wraps a query. Use views to simplify a frequently-repeated complex join for
consumers, to present a restricted/security-filtered slice of a table, or to keep
a stable interface over a schema that changes underneath it. They can hurt if
layered many views deep, since the optimizer has to unravel the whole nested
definition to build a plan.

```sql
CREATE VIEW vw_ActiveEmployees AS
SELECT e.EmpId, e.Name, d.DeptName
FROM Employee e
JOIN Department d ON e.DeptId = d.DeptId
WHERE e.IsActive = 1;

-- consumers query it exactly like a table, without repeating the join every time
SELECT * FROM vw_ActiveEmployees WHERE DeptName = 'Engineering';
```

**[⬆ Back to Top](#table-of-contents)**

## 17. What does `MERGE` do?

`MERGE` combines insert/update/delete into a single statement by comparing a
source and a target on a join condition — commonly used for **upserts**:

```sql
MERGE INTO Target AS t
USING Source AS s ON t.Id = s.Id
WHEN MATCHED THEN UPDATE SET t.Value = s.Value
WHEN NOT MATCHED BY TARGET THEN INSERT (Id, Value) VALUES (s.Id, s.Value)
WHEN NOT MATCHED BY SOURCE THEN DELETE;
```

Worth knowing as a caveat: `MERGE` has had documented concurrency-related edge
cases in SQL Server, so some teams deliberately avoid it under high concurrency in
favor of explicit `IF EXISTS ... UPDATE ELSE INSERT` logic.

**[⬆ Back to Top](#table-of-contents)**

## 18. Should you run SQL Profiler on production?

Generally **no**, or only with extreme care — classic SQL Profiler traces add
real overhead and can measurably slow down a busy production server. The modern
replacement, **Extended Events**, is far lighter-weight and is the recommended
tool for capturing diagnostic data on production instances; if Profiler must be
used, scope the trace tightly (specific events/columns, a filter, a time-boxed
run) rather than a broad, unfiltered capture.

**[⬆ Back to Top](#table-of-contents)**

## 19. `RANK()` vs `DENSE_RANK()`

Both assign a rank within an ordered partition, but they differ on ties:
`RANK()` leaves **gaps** after a tie (1, 2, 2, 4); `DENSE_RANK()` does **not**
(1, 2, 2, 3).

```sql
SELECT Name, Salary,
    RANK() OVER (ORDER BY Salary DESC) AS Rnk,
    DENSE_RANK() OVER (ORDER BY Salary DESC) AS DenseRnk
FROM Employee;
```

**[⬆ Back to Top](#table-of-contents)**

## 20. What are window functions? Write a running total.

Window functions compute a value across a set of rows **related to the current
row** (a "window") without collapsing the result set the way `GROUP BY` does —
each input row still produces one output row.

```sql
SELECT
    OrderId, OrderDate, OrderAmount,
    SUM(OrderAmount) OVER (ORDER BY OrderDate ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS RunningTotal
FROM Orders
ORDER BY OrderDate;
```

Other common window functions: `ROW_NUMBER()`, `LAG()`/`LEAD()` (compare a row to
the previous/next one), and moving averages via a bounded frame.

**[⬆ Back to Top](#table-of-contents)**

## 21. What is a transaction, and how do you start one?

A transaction groups multiple statements into a single all-or-nothing unit,
guaranteeing **ACID** properties (Atomicity, Consistency, Isolation, Durability).

```sql
BEGIN TRAN;
    UPDATE Accounts SET Balance = Balance - 100 WHERE Id = 1;
    UPDATE Accounts SET Balance = Balance + 100 WHERE Id = 2;
COMMIT TRAN;
-- or ROLLBACK TRAN; on failure
```

If the server crashes mid-transaction, or an error occurs and you `ROLLBACK`,
neither update is applied — the transfer never happens half-finished.

**[⬆ Back to Top](#table-of-contents)**

## 22. How do you make a stored procedure parameter optional?

Give it a default value; callers can omit it entirely:

```sql
CREATE PROCEDURE GetOrders
    @CustomerId INT = NULL
AS
BEGIN
    SELECT * FROM Orders
    WHERE (@CustomerId IS NULL OR CustomerId = @CustomerId);
END
```

**Watch-out:** that `OR @CustomerId IS NULL` pattern can defeat index usage
because the optimizer has to build one plan that covers both cases — for a
performance-critical procedure, consider `OPTION (RECOMPILE)` or splitting into
separate branches/dynamic SQL instead.

**[⬆ Back to Top](#table-of-contents)**

## 23. How would you design a multi-tenant database schema?

```sql
CREATE TABLE Tenants (TenantId INT PRIMARY KEY, TenantName NVARCHAR(100));

CREATE TABLE Users (
    UserId INT PRIMARY KEY,
    TenantId INT NOT NULL,
    UserName NVARCHAR(100),
    FOREIGN KEY (TenantId) REFERENCES Tenants(TenantId)
);
```

This is the **shared database, shared schema** model — every tenant-scoped table
carries a `TenantId`, and every query must filter by it (in EF Core, a global
query filter enforces this automatically so it can't be forgotten). See the
architecture file for the fuller comparison against separate-schema and
separate-database approaches.

**[⬆ Back to Top](#table-of-contents)**

## 24. Find the 3rd-highest salary

```sql
SELECT MIN(Salary) AS ThirdHighest
FROM (SELECT TOP 3 Salary FROM Employee ORDER BY Salary DESC) AS Top3;

-- or, handling ties more precisely with DENSE_RANK:
SELECT Salary FROM (
    SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS rnk
    FROM Employee
) t WHERE rnk = 3;
```

The `DENSE_RANK` version is the one to lead with if the interviewer asks a
follow-up about duplicate salaries — `TOP 3` alone can silently give the wrong
answer when there are ties.

**[⬆ Back to Top](#table-of-contents)**

## 25. Find duplicate rows

```sql
SELECT RollNo, COUNT(*) AS Occurrences
FROM Students
GROUP BY RollNo
HAVING COUNT(*) > 1;
```

`HAVING` (not `WHERE`) is required here because the filter applies to the
aggregated group, after `GROUP BY` has run.

**[⬆ Back to Top](#table-of-contents)**

## 26. Find the manager with the most direct reports

```sql
SELECT m.ManagerName, COUNT(e.EmployeeId) AS DirectReports
FROM Employee e
JOIN Manager m ON e.ManagerId = m.ManagerId
GROUP BY m.ManagerName
ORDER BY DirectReports DESC;
-- add: OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY  (or TOP 1) to return just the winner
```

**[⬆ Back to Top](#table-of-contents)**

## 27. Find employees whose DOB/DOJ is the last day of the month

```sql
SELECT *
FROM Employee
WHERE DOB = EOMONTH(DOB);
```

`EOMONTH()` returns the last day of the month for a given date, so comparing a
date to its own `EOMONTH()` result is a clean way to test "is this the last day
of its month" without manual date arithmetic.

**[⬆ Back to Top](#table-of-contents)**

## 28. SQL Server vs RavenDB

**SQL Server** is relational — strong schema, ACID transactions, mature tooling
for complex joins and reporting/BI; the right choice when data has clear
structure and relationships and consistency matters most. **RavenDB** is a
document (NoSQL) database — schema-flexible JSON documents, built for high
read/write throughput and horizontal scale, and a better fit when the data model
changes often or naturally maps to self-contained documents rather than normalized
tables. The decision usually comes down to how relational the data actually is and
how strict the consistency requirements are, not raw performance alone.

**[⬆ Back to Top](#table-of-contents)**

## 29. General strategies for optimizing a slow query

- Index the columns actually used in `WHERE`/`JOIN`/`ORDER BY`.
- Select only the columns you need — never `SELECT *` in production code.
- Prefer `JOIN`s over correlated subqueries where the optimizer can pick a better
  plan.
- Check the actual execution plan for scans, spills to tempdb, and bad row-count
  estimates (stale statistics).
- Avoid non-sargable predicates — wrapping an indexed column in a function
  (`WHERE YEAR(OrderDate) = 2026`) prevents an index seek; rewrite as a range
  (`WHERE OrderDate >= '2026-01-01' AND OrderDate < '2027-01-01'`).
- Cache results that don't need to be recomputed every request.
- Batch large writes instead of one giant transaction.

**[⬆ Back to Top](#table-of-contents)**
