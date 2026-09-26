# RBC Final Round: Senior .NET, Direct Investing

> Final-round prep for a Senior .NET Developer role rebuilding a Direct Investing
> trading platform (.NET Core, Kafka, Redis, SQL Server, Docker/OpenShift). Say each
> answer out loud in under a minute before revealing it. Sections: Your stories, Screener follow-ups, Kafka, Redis, .NET core, EF Core & SQL, API & security, Testing, Docker & OpenShift, System design, Behavioural, CodeSignal.

## Table of Contents

| No. | Section | Question |
|-----|---------|----------|
| 1 | Your stories | [Tell me about yourself.](#1-tell-me-about-yourself) |
| 2 | Your stories | [Walk me through one integration flow at Staples, end to end.](#2-walk-me-through-one-integration-flow-at-staples-end-to-end) |
| 3 | Your stories | [What happens at Staples if publishing to Event Hubs fails?](#3-what-happens-at-staples-if-publishing-to-event-hubs-fails) |
| 4 | Your stories | [Why do you publish in 15-minute batches instead of immediately?](#4-why-do-you-publish-in-15-minute-batches-instead-of-immediately) |
| 5 | Your stories | [What was the Bounteous / insightsoftware platform, and what was your role?](#5-what-was-the-bounteous--insightsoftware-platform-and-what-was-your-role) |
| 6 | Your stories | [How did you make the reports faster?](#6-how-did-you-make-the-reports-faster) |
| 7 | Your stories | [How did you find which queries were slow?](#7-how-did-you-find-which-queries-were-slow) |
| 8 | Your stories | [Why is SELECT * a problem?](#8-why-is-select--a-problem) |
| 9 | Your stories | [Tell me about a difficult legacy system you worked on.](#9-tell-me-about-a-difficult-legacy-system-you-worked-on) |
| 10 | Your stories | [What did you build with Kafka at Centric?](#10-what-did-you-build-with-kafka-at-centric) |
| 11 | Your stories | [Are you hands-on? What percentage of your day is coding?](#11-are-you-hands-on-what-percentage-of-your-day-is-coding) |
| 12 | Screener follow-ups | [Explain SOLID with a real example.](#12-explain-solid-with-a-real-example) |
| 13 | Screener follow-ups | [What are the benefits of dependency injection, beyond testing?](#13-what-are-the-benefits-of-dependency-injection-beyond-testing) |
| 14 | Screener follow-ups | [You wrote a class teammates need, in the same solution. How do you share it?](#14-you-wrote-a-class-teammates-need-in-the-same-solution-how-do-you-share-it) |
| 15 | Screener follow-ups | [Explain the Repository pattern. Isn't DbContext already one?](#15-explain-the-repository-pattern-isnt-dbcontext-already-one) |
| 16 | Screener follow-ups | [When would you use a Factory? Give an example.](#16-when-would-you-use-a-factory-give-an-example) |
| 17 | Screener follow-ups | [Find a number in a sorted array of 1 million ints, no built-ins.](#17-find-a-number-in-a-sorted-array-of-1-million-ints-no-built-ins) |
| 18 | Screener follow-ups | [Array of only 0s and 1s: move all 0s to the front in O(n).](#18-array-of-only-0s-and-1s-move-all-0s-to-the-front-in-on) |
| 19 | Screener follow-ups | [Country names and codes in two lists. Why a Dictionary?](#19-country-names-and-codes-in-two-lists-why-a-dictionary) |
| 20 | Screener follow-ups | [How does a Dictionary actually get O(1) lookups?](#20-how-does-a-dictionary-actually-get-o1-lookups) |
| 21 | Kafka | [Why use Kafka instead of calling the other service's API?](#21-why-use-kafka-instead-of-calling-the-other-services-api) |
| 22 | Kafka | [Explain topics, partitions, offsets and consumer groups.](#22-explain-topics-partitions-offsets-and-consumer-groups) |
| 23 | Kafka | [How do you keep one account's Buy and Cancel in order?](#23-how-do-you-keep-one-accounts-buy-and-cancel-in-order) |
| 24 | Kafka | [A consumer processes a message but crashes before committing the offset.](#24-a-consumer-processes-a-message-but-crashes-before-committing-the-offset) |
| 25 | Kafka | [Two consumers in the same group vs in different groups?](#25-two-consumers-in-the-same-group-vs-in-different-groups) |
| 26 | Kafka | [What's a dead-letter queue and when do you use it?](#26-whats-a-dead-letter-queue-and-when-do-you-use-it) |
| 27 | Kafka | [What's a rebalance?](#27-whats-a-rebalance) |
| 28 | Kafka | [Kafka vs a queue like MQ, RabbitMQ or Service Bus?](#28-kafka-vs-a-queue-like-mq-rabbitmq-or-service-bus) |
| 29 | Kafka | [Can more consumers than partitions make it faster?](#29-can-more-consumers-than-partitions-make-it-faster) |
| 30 | Kafka | [Is exactly-once delivery possible?](#30-is-exactly-once-delivery-possible) |
| 31 | Kafka | [Explain the transactional outbox pattern.](#31-explain-the-transactional-outbox-pattern) |
| 32 | Redis | [How do you implement caching with Redis?](#32-how-do-you-implement-caching-with-redis) |
| 33 | Redis | [How do you choose TTLs?](#33-how-do-you-choose-ttls) |
| 34 | Redis | [How do you invalidate the cache when data changes?](#34-how-do-you-invalidate-the-cache-when-data-changes) |
| 35 | Redis | [What's a cache stampede, and how do you prevent it?](#35-whats-a-cache-stampede-and-how-do-you-prevent-it) |
| 36 | Redis | [Redis goes down. What happens to your API?](#36-redis-goes-down-what-happens-to-your-api) |
| 37 | Redis | [Why shouldn't Redis be the source of truth for an account balance?](#37-why-shouldnt-redis-be-the-source-of-truth-for-an-account-balance) |
| 38 | Redis | [IMemoryCache vs Redis?](#38-imemorycache-vs-redis) |
| 39 | Redis | [What else is Redis used for besides caching?](#39-what-else-is-redis-used-for-besides-caching) |
| 40 | Redis | [What happens when Redis runs out of memory?](#40-what-happens-when-redis-runs-out-of-memory) |
| 41 | .NET core | [Transient vs Scoped vs Singleton?](#41-transient-vs-scoped-vs-singleton) |
| 42 | .NET core | [Why can't you inject a Scoped service into a Singleton?](#42-why-cant-you-inject-a-scoped-service-into-a-singleton) |
| 43 | .NET core | [How do you keep a Singleton thread-safe?](#43-how-do-you-keep-a-singleton-thread-safe) |
| 44 | .NET core | [What does async/await actually do? Does it create a thread?](#44-what-does-asyncawait-actually-do-does-it-create-a-thread) |
| 45 | .NET core | [Why is async void dangerous?](#45-why-is-async-void-dangerous) |
| 46 | .NET core | [What's wrong with .Result or .Wait()?](#46-whats-wrong-with-result-or-wait) |
| 47 | .NET core | [How do you run three independent calls in parallel?](#47-how-do-you-run-three-independent-calls-in-parallel) |
| 48 | .NET core | [Why use IHttpClientFactory?](#48-why-use-ihttpclientfactory) |
| 49 | .NET core | [IEnumerable vs IQueryable?](#49-ienumerable-vs-iqueryable) |
| 50 | .NET core | [What is middleware in ASP.NET Core?](#50-what-is-middleware-in-aspnet-core) |
| 51 | .NET core | [How do you handle exceptions globally in an API?](#51-how-do-you-handle-exceptions-globally-in-an-api) |
| 52 | .NET core | [How do you reduce memory allocations on large data?](#52-how-do-you-reduce-memory-allocations-on-large-data) |
| 53 | .NET core | [record vs class?](#53-record-vs-class) |
| 54 | EF Core & SQL | [What's the N+1 problem? How do you fix it?](#54-whats-the-n1-problem-how-do-you-fix-it) |
| 55 | EF Core & SQL | [What does AsNoTracking do, and when does it hurt?](#55-what-does-asnotracking-do-and-when-does-it-hurt) |
| 56 | EF Core & SQL | [Two users update the same balance at once. How do you stop a lost update?](#56-two-users-update-the-same-balance-at-once-how-do-you-stop-a-lost-update) |
| 57 | EF Core & SQL | [How do you deploy database changes safely?](#57-how-do-you-deploy-database-changes-safely) |
| 58 | EF Core & SQL | [Clustered vs nonclustered index? What's a key lookup?](#58-clustered-vs-nonclustered-index-whats-a-key-lookup) |
| 59 | EF Core & SQL | [Why would SQL Server ignore an index you created?](#59-why-would-sql-server-ignore-an-index-you-created) |
| 60 | EF Core & SQL | [What's parameter sniffing?](#60-whats-parameter-sniffing) |
| 61 | EF Core & SQL | [How do you prevent deadlocks in money transfers?](#61-how-do-you-prevent-deadlocks-in-money-transfers) |
| 62 | EF Core & SQL | [Add a NOT NULL column to a 50-million-row table without downtime.](#62-add-a-not-null-column-to-a-50-million-row-table-without-downtime) |
| 63 | EF Core & SQL | [Where should business logic live: stored procedures or C#?](#63-where-should-business-logic-live-stored-procedures-or-c) |
| 64 | EF Core & SQL | [Isolation levels, in one breath.](#64-isolation-levels-in-one-breath) |
| 65 | API & security | [What makes a RESTful API well designed?](#65-what-makes-a-restful-api-well-designed) |
| 66 | API & security | [POST vs PUT vs PATCH, and which are idempotent?](#66-post-vs-put-vs-patch-and-which-are-idempotent) |
| 67 | API & security | [Which status codes do you use, and when?](#67-which-status-codes-do-you-use-and-when) |
| 68 | API & security | [A client retries a timed-out order. How do you prevent a duplicate trade?](#68-a-client-retries-a-timed-out-order-how-do-you-prevent-a-duplicate-trade) |
| 69 | API & security | [How do you version an API?](#69-how-do-you-version-an-api) |
| 70 | API & security | [OAuth2 vs JWT?](#70-oauth2-vs-jwt) |
| 71 | API & security | [How does your API validate a JWT?](#71-how-does-your-api-validate-a-jwt) |
| 72 | API & security | [Name an OWASP risk you've mitigated.](#72-name-an-owasp-risk-youve-mitigated) |
| 73 | API & security | [How do you protect customer data and privacy?](#73-how-do-you-protect-customer-data-and-privacy) |
| 74 | API & security | [Where do secrets like connection strings go?](#74-where-do-secrets-like-connection-strings-go) |
| 75 | API & security | [What do you know about WCAG accessibility?](#75-what-do-you-know-about-wcag-accessibility) |
| 76 | Testing | [Unit test vs integration test: where's the line?](#76-unit-test-vs-integration-test-wheres-the-line) |
| 77 | Testing | [How do you unit test a class that publishes to Kafka?](#77-how-do-you-unit-test-a-class-that-publishes-to-kafka) |
| 78 | Testing | [How do you test an API end to end?](#78-how-do-you-test-an-api-end-to-end) |
| 79 | Testing | [What makes a good unit test?](#79-what-makes-a-good-unit-test) |
| 80 | Testing | [Mock vs stub vs fake?](#80-mock-vs-stub-vs-fake) |
| 81 | Testing | [Do you practise TDD?](#81-do-you-practise-tdd) |
| 82 | Docker & OpenShift | [Image vs container vs Docker?](#82-image-vs-container-vs-docker) |
| 83 | Docker & OpenShift | [How do you write a Dockerfile for a .NET API?](#83-how-do-you-write-a-dockerfile-for-a-net-api) |
| 84 | Docker & OpenShift | [Explain the core Kubernetes objects.](#84-explain-the-core-kubernetes-objects) |
| 85 | Docker & OpenShift | [OpenShift vs Kubernetes?](#85-openshift-vs-kubernetes) |
| 86 | Docker & OpenShift | [Liveness vs readiness probe?](#86-liveness-vs-readiness-probe) |
| 87 | Docker & OpenShift | [Walk me through a CI/CD pipeline you've built.](#87-walk-me-through-a-cicd-pipeline-youve-built) |
| 88 | Docker & OpenShift | [How do you handle config per environment?](#88-how-do-you-handle-config-per-environment) |
| 89 | System design | [Design order placement for our Direct Investing platform.](#89-design-order-placement-for-our-direct-investing-platform) |
| 90 | System design | [Why return 202 Accepted instead of waiting for the market?](#90-why-return-202-accepted-instead-of-waiting-for-the-market) |
| 91 | System design | [Kafka is down when an order is placed. What happens?](#91-kafka-is-down-when-an-order-is-placed-what-happens) |
| 92 | System design | [How would a regulator reconstruct what happened to one order?](#92-how-would-a-regulator-reconstruct-what-happened-to-one-order) |
| 93 | System design | [How do you keep data consistent across microservices?](#93-how-do-you-keep-data-consistent-across-microservices) |
| 94 | System design | [Circuit breaker vs retry vs bulkhead?](#94-circuit-breaker-vs-retry-vs-bulkhead) |
| 95 | System design | [How would you push live price or order updates to the UI?](#95-how-would-you-push-live-price-or-order-updates-to-the-ui) |
| 96 | System design | [How does your design scale?](#96-how-does-your-design-scale) |
| 97 | Behavioural | [Tell me about a disagreement with a teammate.](#97-tell-me-about-a-disagreement-with-a-teammate) |
| 98 | Behavioural | [Tell me about a mistake or a production incident.](#98-tell-me-about-a-mistake-or-a-production-incident) |
| 99 | Behavioural | [How do you mentor other developers?](#99-how-do-you-mentor-other-developers) |
| 100 | Behavioural | [Why RBC, and why this role?](#100-why-rbc-and-why-this-role) |
| 101 | Behavioural | [You're okay with contract-to-hire?](#101-youre-okay-with-contract-to-hire) |
| 102 | Behavioural | [What questions do you have for us?](#102-what-questions-do-you-have-for-us) |
| 103 | CodeSignal | [Walk me through your banking solution.](#103-walk-me-through-your-banking-solution) |
| 104 | CodeSignal | [How would you have implemented the scheduled transfer?](#104-how-would-you-have-implemented-the-scheduled-transfer) |
| 105 | CodeSignal | [What would you do differently on the assessment?](#105-what-would-you-do-differently-on-the-assessment) |

## 1. Tell me about yourself.

*Your stories*

> "I'm a senior .NET developer with about 10 years of experience, mostly C# and .NET Core backends with Angular or React front ends. Right now I'm at Staples on the middleware team, building .NET 8 services that connect systems owned by different teams and vendors (warehouse, transport, carriers) over REST APIs, Google Pub/Sub and Azure Event Hubs. Before that I was lead developer at Bounteous on an equity-compensation reporting platform for insightsoftware: ESOP, vesting and tax reports, where a lot of my work was performance. At Centric I built Kafka consumer services for an insurance platform. This role brings those together: event-driven .NET services in a financial domain."

**Follow-up:** Keep it to 60 to 90 seconds, then stop. Let them choose what to dig into.

**[⬆ Back to Top](#table-of-contents)**

## 2. Walk me through one integration flow at Staples, end to end.

*Your stories*

> "A customer creates a shipment by calling our API through Azure APIM. My service calls Centiro, the carrier platform, to pick the transport partner, and returns that in the same response. Then it raises two events: Google Pub/Sub so the WMS expects the package, and Azure Event Hubs so the TMS schedules delivery."

> "The carrier answer is synchronous because the customer needs it now. WMS and TMS get events because they don't need to block the customer. A slow WMS never slows the customer's call."

**Follow-up:** Why not call WMS and TMS directly? Coupling: if either is slow or down, the customer's request fails. Events let each team consume at its own pace.

**[⬆ Back to Top](#table-of-contents)**

## 3. What happens at Staples if publishing to Event Hubs fails?

*Your stories*

> "Messages are saved to a table first. A background service publishes them on a schedule, so a failed publish doesn't lose anything. The row stays pending, we retry with backoff, and after repeated failures Datadog alerts the team. Delivery is at-least-once, so consumers deduplicate on the message id."

This is an **outbox** pattern with batched publishing.

**Follow-up:** Improvements to mention: keep a status column instead of deleting rows (audit trail), and track status per destination so 'WMS sent, TMS failed' is visible.

**[⬆ Back to Top](#table-of-contents)**

## 4. Why do you publish in 15-minute batches instead of immediately?

*Your stories*

> "Fewer calls to partner systems, and WMS and TMS don't need the data within seconds. The trade-off is up to 15 minutes of delay. For a trading platform I'd shrink that to seconds or publish continuously, because order events can't wait."

**Follow-up:** The worker sends 50 of 100 rows and crashes? Those rows are still pending, so they're re-sent. Mark each row Sent right after it succeeds to keep duplicates small.

**[⬆ Back to Top](#table-of-contents)**

## 5. What was the Bounteous / insightsoftware platform, and what was your role?

*Your stories*

> "An equity-compensation reporting platform. Corporate clients used it to report on their employee stock plans: ESOP tax impact, vesting and unvesting schedules, grant reports. I was lead developer on the reporting team: building and changing reports end to end, API to database, and owning performance of the heavy ones."

**Follow-up:** Know a few domain words cold: grant, vesting schedule, cliff, exercise, unvested shares, fair market value.

**[⬆ Back to Top](#table-of-contents)**

## 6. How did you make the reports faster?

*Your stories*

1. **Diagnosis:** Datadog showed the API time was almost all inside the database call; the code path was already async.
1. **SELECT * → only needed columns.** Less I/O and network, and it lets indexes cover the query.
1. **Indexes** on the columns the reports filter and join on (client, grant date), checked in the execution plan.
1. **async/await end to end** so threads aren't blocked while waiting on SQL.
1. **Caching** data that rarely changes (plan definitions, reference data).

> "Heavy reports got significantly faster, roughly 40% on the worst ones."

**Follow-up:** Precision: async doesn't make one report faster. It improves throughput: the server handles many more concurrent report requests because threads aren't blocked.

**[⬆ Back to Top](#table-of-contents)**

## 7. How did you find which queries were slow?

*Your stories*

> "Datadog APM showed the time was spent in the database call, not in our code. Then I captured the slow queries with SQL Profiler and read their execution plans: table scans, key lookups, missing indexes."

**Follow-up:** Tooling: SQL Profiler is SQL Server only. On Oracle the equivalents are Explain Plan, AWR reports and SQL Trace/TKPROF.

**[⬆ Back to Top](#table-of-contents)**

## 8. Why is SELECT * a problem?

*Your stories*

- Reads and sends columns nobody uses: more I/O, network and memory.
- Prevents a covering index, so SQL does extra key lookups.
- Breaks or slows silently when someone adds a large column later.

**[⬆ Back to Top](#table-of-contents)**

## 9. Tell me about a difficult legacy system you worked on.

*Your stories*

> "Most business logic lived in stored procedures: thousands of lines of PL/SQL, procedures calling other procedures, with loops and cursors. The C# and Angular layers mostly just called them. It was hard to debug, hard to unit test and risky to change. It taught me why business logic belongs in the application layer, where it's testable, version-controlled and easy to scale, with SQL focused on data access."

**Follow-up:** Frame it as a lesson learned, not a complaint. If asked how you worked in it: trace the call chain, add logging, make small safe changes.

**[⬆ Back to Top](#table-of-contents)**

## 10. What did you build with Kafka at Centric?

*Your stories*

> "On an insurance platform, documents for different products were generated through Kafka. When a user requested a document, an event with the JSON payload was published to a topic per document type. I built consumer services that picked up the JSON, generated the PDF and stored it in Blob storage, where the UI read it from. The Kafka platform itself was set up by another team; my part was the consumers."

**Follow-up:** Likely follow-up: what if PDF generation fails halfway? Don't commit the offset until the PDF is stored. Retry, then dead-letter. Make it idempotent so a re-delivered message doesn't create a second document.

**[⬆ Back to Top](#table-of-contents)**

## 11. Are you hands-on? What percentage of your day is coding?

*Your stories*

> "Mostly hands-on. The majority of my day is design and coding; the rest is code reviews, sprint work with the team and mentoring. I like staying close to the code."

**[⬆ Back to Top](#table-of-contents)**

## 12. Explain SOLID with a real example.

*Screener follow-ups*

- **S**: one reason to change. `ShipmentService` runs the flow; `PubSubPublisher` only talks to Pub/Sub.
- **O**: extend without editing. A partner wants Kafka: add `KafkaPublisher`, nothing else changes.
- **L**: any implementation can replace another. A publisher that silently swallows errors would break the caller's retry logic.
- **I**: small interfaces. Publishing and consuming are separate interfaces.
- **D**: depend on `IEventPublisher`, never `new PubSubPublisher()`.

**[⬆ Back to Top](#table-of-contents)**

## 13. What are the benefits of dependency injection, beyond testing?

*Screener follow-ups*

- Loose coupling: callers depend on an interface, so implementations can be swapped.
- Dependencies are visible in the constructor instead of hidden.
- The container manages lifetimes (Transient, Scoped, Singleton) and disposal.
- Configuration lives in one place (Program.cs).
- And yes, unit tests can inject mocks.

**[⬆ Back to Top](#table-of-contents)**

## 14. You wrote a class teammates need, in the same solution. How do you share it?

*Screener follow-ups*

> "Within one solution, a project reference; NuGet is for sharing across solutions. For how teammates use it, I expose an interface and register the implementation in DI, so their code depends only on the contract, can be tested with mocks, and doesn't break when my implementation changes."

**Follow-up:** Why not a static class? Can't be mocked or swapped, hides dependencies, can't receive a DbContext or HttpClient. Static is fine for pure helpers like Math.Max.

**[⬆ Back to Top](#table-of-contents)**

## 15. Explain the Repository pattern. Isn't DbContext already one?

*Screener follow-ups*

> "A repository puts data access behind an interface, so services contain no EF or SQL, and I can mock it in tests. DbContext is already a unit of work and repository, so for simple CRUD I often use it directly. I add a repository when I want query logic in one place or EF out of the domain. I avoid a generic IRepository<T> that just wraps DbSet."

**Follow-up:** The repository doesn't call SaveChanges. The caller saves once per request so several changes commit together.

**[⬆ Back to Top](#table-of-contents)**

## 16. When would you use a Factory? Give an example.

*Screener follow-ups*

> "When which object to create depends on data at runtime. My example: a PublisherFactory. DI injects all IEventPublisher implementations, the factory stores them in a Dictionary by destination, and callers ask for 'WMS' or 'TMS'. Adding Kafka is one new class and one registration line."

**Follow-up:** Factory vs DI: DI when the type is known at startup, a factory when it depends on runtime data. They work together.

**[⬆ Back to Top](#table-of-contents)**

## 17. Find a number in a sorted array of 1 million ints, no built-ins.

*Screener follow-ups*

```csharp
int left = 0, right = arr.Length - 1;
while (left <= right)
{
    int mid = (left + right) / 2;
    if (arr[mid] == target) return mid;
    if (target < arr[mid]) right = mid - 1;
    else left = mid + 1;
}
return -1;
```

O(log n) time, about 20 checks for 1M. O(1) space.

**Follow-up:** Overflow: left + (right - left) / 2. Use <= or you skip the last element. mid ± 1 or it can loop forever.

**[⬆ Back to Top](#table-of-contents)**

## 18. Array of only 0s and 1s: move all 0s to the front in O(n).

*Screener follow-ups*

> "Two pointers, one at each end. A 0 on the left is in place, so move left forward. A 1 on the right is in place, so move right back. If both are wrong, swap them and move both. Each element is visited once: O(n) time, O(1) space, in place."

**Follow-up:** Mirror version (1s first): same algorithm with the value flipped, so pass the front value in as a parameter.

**[⬆ Back to Top](#table-of-contents)**

## 19. Country names and codes in two lists. Why a Dictionary?

*Screener follow-ups*

> "Build a Dictionary once, O(n). After that every lookup is O(1). With two lists, every lookup scans the list, O(n) each time, and the two lists can drift out of sync."

**Follow-up:** Bonus: new Dictionary(StringComparer.OrdinalIgnoreCase) so 'canada' matches 'Canada'.

**[⬆ Back to Top](#table-of-contents)**

## 20. How does a Dictionary actually get O(1) lookups?

*Screener follow-ups*

- It calls `GetHashCode()` on the key and maps it to a bucket.
- It goes straight to that bucket and confirms the key with `Equals()`.
- Different keys landing in one bucket are a collision; they're chained, so a lookup checks a few entries.
- When it fills up, it resizes and rehashes into a bigger array.

**Follow-up:** Worst case is O(n) if many keys collide. Never change a key object's fields after inserting it, or its hash changes and you can't find it.

**[⬆ Back to Top](#table-of-contents)**

## 21. Why use Kafka instead of calling the other service's API?

*Kafka*

> "Decoupling. The producer writes once and doesn't need to know who's listening or whether they're up. If a consumer is down, messages wait in Kafka and it catches up later. New consumers like audit or analytics can be added without touching the producer."

**[⬆ Back to Top](#table-of-contents)**

## 22. Explain topics, partitions, offsets and consumer groups.

*Kafka*

- **Topic**: a named stream, like `orders`.
- **Partition**: a topic is split into ordered logs for parallelism. On disk each is a folder of log segments.
- **Offset**: a message's position within a partition.
- **Consumer group**: consumers sharing the work. Each partition goes to one consumer in the group.

Messages stay until retention removes them. Reading doesn't delete them.

**[⬆ Back to Top](#table-of-contents)**

## 23. How do you keep one account's Buy and Cancel in order?

*Kafka*

> "Kafka only guarantees order within a partition. I use AccountId as the message key, and the same key always goes to the same partition, so each account's events stay in order while different accounts are processed in parallel."

**Follow-up:** Without a key, Cancel could be processed before Buy.

**[⬆ Back to Top](#table-of-contents)**

## 24. A consumer processes a message but crashes before committing the offset.

*Kafka*

> "After restart it resumes from the last committed offset, so that message is delivered again. That's at-least-once delivery. The consumer must be idempotent: store processed message ids with a unique constraint and skip duplicates."

**Follow-up:** Commit after processing, not before. Committing first risks losing the message if you crash mid-processing.

**[⬆ Back to Top](#table-of-contents)**

## 25. Two consumers in the same group vs in different groups?

*Kafka*

> "Same group: they split the partitions, which is load balancing. Different groups: each gets every message, which is broadcast, like an order service and an audit service both reading all orders."

**[⬆ Back to Top](#table-of-contents)**

## 26. What's a dead-letter queue and when do you use it?

*Kafka*

> "When a message keeps failing because of bad data or a bug, I don't retry forever and block the partition. After N retries I move it to a dead-letter topic, alert, and keep processing. Someone fixes the cause and replays it."

**[⬆ Back to Top](#table-of-contents)**

## 27. What's a rebalance?

*Kafka*

> "When a consumer joins or leaves a group, Kafka reassigns partitions. Processing pauses briefly, and uncommitted messages may be reprocessed, which is another reason consumers must be idempotent."

**[⬆ Back to Top](#table-of-contents)**

## 28. Kafka vs a queue like MQ, RabbitMQ or Service Bus?

*Kafka*

> "In a queue a message is removed once consumed and goes to one receiver. Kafka is a log: messages stay for the retention period, many groups read independently, and you can replay from an older offset. Queues fit commands and task distribution; Kafka fits event streams and high throughput."

**[⬆ Back to Top](#table-of-contents)**

## 29. Can more consumers than partitions make it faster?

*Kafka*

> "No. Each partition is read by one consumer per group, so extra consumers sit idle. The partition count is the maximum parallelism, so size it for future load."

**[⬆ Back to Top](#table-of-contents)**

## 30. Is exactly-once delivery possible?

*Kafka*

> "Inside Kafka, yes, with an idempotent producer and transactions. End to end across a database and external systems it's rare, so in practice teams build at-least-once delivery plus idempotent consumers. The result is effectively-once processing."

**[⬆ Back to Top](#table-of-contents)**

## 31. Explain the transactional outbox pattern.

*Kafka*

> "Writing to the database and publishing to Kafka are two separate systems, so one can succeed while the other fails. With an outbox, I write the business row and an outbox row in the same database transaction. A background worker publishes pending outbox rows and marks them sent. Nothing is lost if Kafka is down or the service crashes; delivery is at-least-once, so consumers are idempotent."

**[⬆ Back to Top](#table-of-contents)**

## 32. How do you implement caching with Redis?

*Redis*

**Cache-aside**, the most common pattern:

1. Read: check Redis. On a hit, return it.
1. On a miss, read from SQL, store it in Redis with a TTL, return it.
1. On a write: update SQL, then **delete** the cache key.

In .NET: `IDistributedCache` or `StackExchange.Redis`. In .NET 9+, `HybridCache` adds an in-memory layer and stampede protection.

**[⬆ Back to Top](#table-of-contents)**

## 33. How do you choose TTLs?

*Redis*

> "By how stale the data is allowed to be. Data that changes often gets a short TTL, around 5 minutes. Reference data that rarely changes gets an hour or more. I add a little random jitter so thousands of keys don't expire at the same moment."

**Follow-up:** First question to ask in any caching discussion: how stale can this data be? That drives the whole design.

**[⬆ Back to Top](#table-of-contents)**

## 34. How do you invalidate the cache when data changes?

*Redis*

> "On write, I update the database, then delete the key. The next read fetches fresh data. I delete rather than update the cached value, because two concurrent writers could otherwise leave a stale value in the cache. The TTL is a safety net. When another service changes the data, it publishes an event and our consumer evicts the key."

**[⬆ Back to Top](#table-of-contents)**

## 35. What's a cache stampede, and how do you prevent it?

*Redis*

> "A popular key expires and hundreds of requests miss at once, so they all hit the database together. I let one request rebuild the value while the others wait for its result, using a lock or request coalescing. I also add TTL jitter and refresh hot keys before they expire. HybridCache in .NET does the coalescing for you."

**[⬆ Back to Top](#table-of-contents)**

## 36. Redis goes down. What happens to your API?

*Redis*

> "The cache must be optional. Redis calls get short timeouts, and a failure falls back to the database. A circuit breaker stops us waiting on Redis for every call while it's down. Because the database suddenly takes all the load, I protect it with rate limiting, and monitoring alerts the team."

**[⬆ Back to Top](#table-of-contents)**

## 37. Why shouldn't Redis be the source of truth for an account balance?

*Redis*

> "A cache can be stale, evicted under memory pressure, or lose recent writes on failover. You can't approve a trade against a stale balance. SQL is the source of truth; Redis only speeds up reads where slightly old data is acceptable."

**[⬆ Back to Top](#table-of-contents)**

## 38. IMemoryCache vs Redis?

*Redis*

> "IMemoryCache lives inside one app instance: fastest, but each pod has its own copy and they can disagree. Redis is shared by all instances, so every pod sees the same data and the cache survives restarts. With several pods on Kubernetes, I use Redis, sometimes with a small in-memory layer in front."

**[⬆ Back to Top](#table-of-contents)**

## 39. What else is Redis used for besides caching?

*Redis*

- Sessions shared across instances
- Rate limiting with counters and expiry
- Distributed locks
- Sorted sets for leaderboards and rankings
- Pub/sub, for example as a SignalR backplane

**[⬆ Back to Top](#table-of-contents)**

## 40. What happens when Redis runs out of memory?

*Redis*

> "It evicts keys according to its maxmemory policy. allkeys-lru removes the least recently used keys; volatile-lru only removes keys that have a TTL. For a cache I'd use an LRU policy, always set TTLs, and monitor memory and hit rate."

**[⬆ Back to Top](#table-of-contents)**

## 41. Transient vs Scoped vs Singleton?

*.NET core*

- **Transient**: new instance every time. Lightweight stateless helpers.
- **Scoped**: one per HTTP request. DbContext, current user.
- **Singleton**: one for the app. Config, caches, Kafka producers.

**Follow-up:** Transient DbContext bug: two repositories get two DbContexts, so one SaveChanges doesn't include the other's changes.

**[⬆ Back to Top](#table-of-contents)**

## 42. Why can't you inject a Scoped service into a Singleton?

*.NET core*

> "The Singleton lives forever and keeps the Scoped DbContext it got from the first request. Every later request, on different threads, shares that one DbContext, which isn't thread-safe. It's a captive dependency. The fix is IServiceScopeFactory: create a scope when you need the DbContext."

**Follow-up:** Real example: a BackgroundService (always a Singleton) like an outbox worker creating a scope per batch.

**[⬆ Back to Top](#table-of-contents)**

## 43. How do you keep a Singleton thread-safe?

*.NET core*

> "Best is no mutable state. If it must hold state: ConcurrentDictionary for shared lookups, lock when several fields change together, Interlocked for counters. The danger is check-then-act: two threads both check 'not there' and both add."

**Follow-up:** count++ is read, add, write. Two threads both read 5 and both write 6, so an update is lost. That's a race condition.

**[⬆ Back to Top](#table-of-contents)**

## 44. What does async/await actually do? Does it create a thread?

*.NET core*

> "It doesn't create a thread. At an await on I/O, the thread goes back to the pool to serve other requests. When the I/O completes, a pool thread continues the method. That's how a server handles many more requests with the same threads."

**[⬆ Back to Top](#table-of-contents)**

## 45. Why is async void dangerous?

*.NET core*

> "It can't be awaited, so the caller doesn't know when it finishes, and an exception can crash the process because nothing can catch it. Always return Task. The only exception is event handlers."

**[⬆ Back to Top](#table-of-contents)**

## 46. What's wrong with .Result or .Wait()?

*.NET core*

> "It blocks a thread while waiting, which throws away the benefit of async and can cause thread-pool starvation. In older ASP.NET and UI apps it can deadlock. Go async all the way."

**[⬆ Back to Top](#table-of-contents)**

## 47. How do you run three independent calls in parallel?

*.NET core*

> "Start all three tasks, then await Task.WhenAll. Total time is the slowest call, not the sum."

**[⬆ Back to Top](#table-of-contents)**

## 48. Why use IHttpClientFactory?

*.NET core*

> "A new HttpClient per request exhausts sockets, because closed connections sit in TIME_WAIT. A single static client never picks up DNS changes. IHttpClientFactory pools and recycles handlers, so you avoid both problems."

**[⬆ Back to Top](#table-of-contents)**

## 49. IEnumerable vs IQueryable?

*.NET core*

> "IQueryable builds an expression that EF translates to SQL, so filtering happens in the database. IEnumerable works in memory on data already loaded. Calling ToList too early loads the whole table and filters in C#."

**Follow-up:** Deferred execution: building the query does nothing. It runs at ToList, First, Count or foreach.

**[⬆ Back to Top](#table-of-contents)**

## 50. What is middleware in ASP.NET Core?

*.NET core*

> "The request passes through an ordered pipeline of components: exception handling, authentication, authorization, logging. Each can act before and after the next one. Order matters: authentication before authorization. I've written custom middleware for correlation ids and global error handling."

**[⬆ Back to Top](#table-of-contents)**

## 51. How do you handle exceptions globally in an API?

*.NET core*

> "One place, not try/catch everywhere: exception-handling middleware, or IExceptionHandler in .NET 8. It logs the error with a correlation id and returns a consistent ProblemDetails response without leaking stack traces. Predictable conditions like 'not found' are handled explicitly, not with exceptions."

**[⬆ Back to Top](#table-of-contents)**

## 52. How do you reduce memory allocations on large data?

*.NET core*

- Stream data instead of loading everything into memory.
- `Span` / `ReadOnlySpan` to slice strings and arrays without copying.
- `StringBuilder` instead of string concatenation in loops.
- `ArrayPool` to reuse buffers.

Fewer allocations mean less GC work and fewer pauses.

**Follow-up:** GC basics: generations 0, 1, 2. Most objects die young in Gen 0. Objects over 85 KB go to the Large Object Heap, which is expensive to collect.

**[⬆ Back to Top](#table-of-contents)**

## 53. record vs class?

*.NET core*

> "A record has value equality (two records with the same data are equal) and is immutable by default, which makes it good for DTOs and events. A class has reference equality and is the choice for entities with behaviour and changing state."

**[⬆ Back to Top](#table-of-contents)**

## 54. What's the N+1 problem? How do you fix it?

*EF Core & SQL*

> "One query loads a list, then one extra query runs per item inside a loop: 100 orders become 101 database trips. Fix with Include, which loads the related data in the same query, or a Select projection when I only need a few fields."

**[⬆ Back to Top](#table-of-contents)**

## 55. What does AsNoTracking do, and when does it hurt?

*EF Core & SQL*

> "Normally EF keeps a copy of each loaded entity's original values and compares them on SaveChanges to generate updates. AsNoTracking skips that: faster and less memory, ideal for read-only queries. It hurts if you then change the entity and call SaveChanges, because nothing is saved."

**[⬆ Back to Top](#table-of-contents)**

## 56. Two users update the same balance at once. How do you stop a lost update?

*EF Core & SQL*

> "Optimistic concurrency. A rowversion column ([Timestamp] in EF). The update includes WHERE RowVersion = the value I read. If someone saved first, 0 rows are updated and EF throws DbUpdateConcurrencyException. I reload and retry, or tell the user."

**Follow-up:** Pessimistic alternative: lock the row when reading. Safer under heavy contention but blocks others.

**[⬆ Back to Top](#table-of-contents)**

## 57. How do you deploy database changes safely?

*EF Core & SQL*

> "EF Core migrations, reviewed in the PR like code. For production I generate an idempotent SQL script with dotnet ef migrations script --idempotent, and the pipeline or a DBA runs it. I don't let the app migrate itself on startup: several instances would race, and it would need admin permissions."

**[⬆ Back to Top](#table-of-contents)**

## 58. Clustered vs nonclustered index? What's a key lookup?

*EF Core & SQL*

> "The clustered index is the table itself, stored in key order, so there's one. A nonclustered index is a separate sorted copy of some columns with a pointer back to the row. If the query needs a column that isn't in the index, SQL jumps back to the table for every row: a key lookup. A covering index with INCLUDE removes it."

**[⬆ Back to Top](#table-of-contents)**

## 59. Why would SQL Server ignore an index you created?

*EF Core & SQL*

> "If the query matches many rows, thousands of key lookups cost more than one scan of the table, so the optimizer scans instead. There's no fixed percentage; it's a cost estimate and often a small fraction of rows. A covering index fixes it."

**Follow-up:** Every index slows inserts and updates and uses storage, so index the frequent, important queries, not everything.

**[⬆ Back to Top](#table-of-contents)**

## 60. What's parameter sniffing?

*EF Core & SQL*

> "SQL builds a plan using the first parameter value it sees and reuses it. If the first call returned 10 rows, the plan suits small results, and a later call returning a million rows reuses that bad plan. The sign is: fast in SSMS, slow in the app. Fixes: OPTION (RECOMPILE), OPTIMIZE FOR, or a covering index."

**[⬆ Back to Top](#table-of-contents)**

## 61. How do you prevent deadlocks in money transfers?

*EF Core & SQL*

> "A deadlock is a circle: A holds account 1 and wants 2, B holds 2 and wants 1. I always lock in the same order, lower account id first, so a circle can't form; the second transfer just waits. I also keep transactions short. To diagnose, I read the deadlock graph from Extended Events."

**[⬆ Back to Top](#table-of-contents)**

## 62. Add a NOT NULL column to a 50-million-row table without downtime.

*EF Core & SQL*

1. Add it as nullable. Instant, metadata only.
1. Deploy code that always writes the new column.
1. Backfill old rows in batches of a few thousand so locks stay short.
1. Switch the column to NOT NULL.

**[⬆ Back to Top](#table-of-contents)**

## 63. Where should business logic live: stored procedures or C#?

*EF Core & SQL*

> "In the application layer. There it's unit-testable, version-controlled, debuggable, and scales by adding app instances instead of loading the database. Stored procedures still make sense for heavy set-based data work close to the data. I've seen the opposite: thousands of lines of nested PL/SQL that nobody could safely change."

**[⬆ Back to Top](#table-of-contents)**

## 64. Isolation levels, in one breath.

*EF Core & SQL*

> "The default is Read Committed: you only see committed data, but readers can wait on writers. Read Committed Snapshot lets readers see the last committed version without blocking. Serializable is safest but blocks most. For balances I prefer short transactions plus optimistic concurrency."

**[⬆ Back to Top](#table-of-contents)**

## 65. What makes a RESTful API well designed?

*API & security*

- Resources as nouns, correct verbs: `GET /accounts/42/orders`.
- Correct status codes and consistent errors (ProblemDetails).
- Versioning, so existing clients never break.
- Pagination and filtering for lists.
- Idempotency for retries, validation, and authentication on every endpoint.

**[⬆ Back to Top](#table-of-contents)**

## 66. POST vs PUT vs PATCH, and which are idempotent?

*API & security*

> "POST creates and isn't idempotent: two calls create two things. PUT replaces the whole resource and is idempotent. PATCH changes part of it. GET, PUT and DELETE are idempotent. For POSTs that must be safe to retry, like placing an order, I use an Idempotency-Key header."

**[⬆ Back to Top](#table-of-contents)**

## 67. Which status codes do you use, and when?

*API & security*

- **200** OK · **201** Created · **202** Accepted (processing later) · **204** No Content
- **400** bad input · **401** not authenticated · **403** authenticated but not allowed · **404** not found
- **409** conflict (concurrency, duplicate) · **422** valid format, fails business rules · **429** rate limited
- **500** server error · **503** dependency down

**Follow-up:** 401 vs 403 is a classic: 401 = who are you? 403 = I know who you are, and you can't do this.

**[⬆ Back to Top](#table-of-contents)**

## 68. A client retries a timed-out order. How do you prevent a duplicate trade?

*API & security*

> "The client sends an Idempotency-Key, unique per order attempt. I store it with the order under a unique constraint. On a retry with the same key, I return the original result instead of placing a second order."

**[⬆ Back to Top](#table-of-contents)**

## 69. How do you version an API?

*API & security*

> "Usually in the URL, like /v1/orders, because it's explicit and easy to route in APIM. Existing versions never get breaking changes; breaking changes go in a new version, and the old one is deprecated with notice to consumers."

**[⬆ Back to Top](#table-of-contents)**

## 70. OAuth2 vs JWT?

*API & security*

> "OAuth2 is the authorization framework: how a client gets a token from an identity provider like Microsoft Entra ID. A JWT is a token format: a signed JSON token carrying claims like user id, roles and expiry. OAuth2 commonly issues JWTs as access tokens."

**[⬆ Back to Top](#table-of-contents)**

## 71. How does your API validate a JWT?

*API & security*

- `AddAuthentication().AddJwtBearer()` checks the signature with the identity provider's public keys.
- It validates issuer, audience and expiry.
- `[Authorize]` policies check roles or scopes.
- APIM can also validate the JWT at the gateway before the request reaches the service.

**[⬆ Back to Top](#table-of-contents)**

## 72. Name an OWASP risk you've mitigated.

*API & security*

> "Broken access control is the big one for banking. Checking that someone is logged in isn't enough; for GET /accounts/123 I verify account 123 belongs to the caller, otherwise anyone can change the id and read other people's data. Also SQL injection, prevented with parameterized queries and EF, and secrets kept out of code in Key Vault."

**[⬆ Back to Top](#table-of-contents)**

## 73. How do you protect customer data and privacy?

*API & security*

- Collect and return only what's needed.
- Never log account numbers, SINs, tokens or passwords; mask them.
- TLS in transit, encryption at rest (TDE).
- Least-privilege access, and secrets in Key Vault with managed identity.

**[⬆ Back to Top](#table-of-contents)**

## 74. Where do secrets like connection strings go?

*API & security*

> "Never in appsettings or Git. Azure Key Vault or OpenShift/Kubernetes secrets, and ideally managed identity so there's no password to store at all."

**[⬆ Back to Top](#table-of-contents)**

## 75. What do you know about WCAG accessibility?

*API & security*

> "It's the standard for making apps usable by everyone: keyboard navigation, alt text, enough color contrast, proper labels and ARIA for screen readers. On the front end I check with tools like Lighthouse or axe. On the API side, it means returning clear, structured error messages the UI can present accessibly."

**[⬆ Back to Top](#table-of-contents)**

## 76. Unit test vs integration test: where's the line?

*Testing*

> "A unit test checks one class's logic with its dependencies mocked: fast, no database, no network. An integration test checks that real pieces work together: API, database, Kafka. Business rules get unit tests; queries, serialization and wiring get integration tests."

**[⬆ Back to Top](#table-of-contents)**

## 77. How do you unit test a class that publishes to Kafka?

*Testing*

> "The class depends on an IEventPublisher interface, not the Kafka client. In the test I inject a Moq mock, run the method, and verify PublishAsync was called once with the expected event. No Kafka needed."

```csharp
var publisher = new Mock<IEventPublisher>();
var service = new ShipmentService(publisher.Object);

await service.CreateAsync(shipment);

publisher.Verify(p => p.PublishAsync(It.IsAny<ShipmentEvent>()), Times.Once);
```

**[⬆ Back to Top](#table-of-contents)**

## 78. How do you test an API end to end?

*Testing*

> "WebApplicationFactory starts the real API in memory, and the test calls it with HttpClient. For real dependencies, Testcontainers starts SQL Server, Redis or Kafka in Docker for the test run, so it's close to production and runs in CI."

**[⬆ Back to Top](#table-of-contents)**

## 79. What makes a good unit test?

*Testing*

- Arrange, Act, Assert.
- Tests one behaviour; the name says what it checks.
- Fast and deterministic: no real clock, network or random values.
- Covers edge cases, not just the happy path.

**[⬆ Back to Top](#table-of-contents)**

## 80. Mock vs stub vs fake?

*Testing*

> "A stub returns canned answers. A mock also lets you verify how it was called. A fake is a simple working implementation, like an in-memory repository."

**[⬆ Back to Top](#table-of-contents)**

## 81. Do you practise TDD?

*Testing*

> "For business rules, yes: write a failing test, make it pass, refactor. It's most useful where the logic has many edge cases. For plumbing code I usually write the tests right after."

**[⬆ Back to Top](#table-of-contents)**

## 82. Image vs container vs Docker?

*Docker & OpenShift*

> "An image is the immutable package: compiled app, runtime and OS files. A container is a running instance of an image. Docker builds images and runs containers on one machine. Kubernetes or OpenShift runs them at scale across many."

**[⬆ Back to Top](#table-of-contents)**

## 83. How do you write a Dockerfile for a .NET API?

*Docker & OpenShift*

> "Multi-stage. The first stage uses the .NET SDK image to restore, build and publish. The final stage copies only the published output into the smaller ASP.NET runtime image. The production image has no SDK or source code, is much smaller, and runs as a non-root user."

**[⬆ Back to Top](#table-of-contents)**

## 84. Explain the core Kubernetes objects.

*Docker & OpenShift*

- **Pod**: one or more containers running together.
- **Deployment**: keeps N replicas running and does rolling updates.
- **Service**: a stable address in front of changing pods.
- **Ingress** (Route in OpenShift): external traffic in.
- **ConfigMap / Secret**: configuration and secrets.
- **HPA**: scales pods on CPU or other metrics.

**[⬆ Back to Top](#table-of-contents)**

## 85. OpenShift vs Kubernetes?

*Docker & OpenShift*

> "OpenShift is Red Hat's enterprise Kubernetes, so pods, deployments and services all carry over. It adds stricter security by default (containers can't run as root, via Security Context Constraints), Routes for external traffic, Projects as namespaces with extra controls, a built-in image registry and builds, and the oc CLI alongside kubectl."

**[⬆ Back to Top](#table-of-contents)**

## 86. Liveness vs readiness probe?

*Docker & OpenShift*

> "Readiness: is this pod ready for traffic? If not, it's taken out of the load balancer, for example while it warms up or loses the database. Liveness: is it still alive? If not, Kubernetes restarts it. In .NET I expose them with health checks via MapHealthChecks."

**[⬆ Back to Top](#table-of-contents)**

## 87. Walk me through a CI/CD pipeline you've built.

*Docker & OpenShift*

1. On a PR: build, unit tests, code and dependency scans.
1. On merge: build the Docker image, tag it and push to the registry.
1. Deploy to dev automatically, then higher environments with approvals.
1. Rolling deployment with health checks, and rollback to the previous image if checks fail.

The same image moves through every environment; only configuration changes.

**[⬆ Back to Top](#table-of-contents)**

## 88. How do you handle config per environment?

*Docker & OpenShift*

> "One image for all environments. Settings come from appsettings.{Environment}.json overridden by environment variables or ConfigMaps, and secrets come from Key Vault or Kubernetes secrets. Nothing environment-specific is baked into the image."

**[⬆ Back to Top](#table-of-contents)**

## 89. Design order placement for our Direct Investing platform.

*System design*

Ask first: orders per second? Placement only, or cancel and modify too?

```csharp
Client -> APIM -> Order API
  -> [Orders + Outbox, one transaction]
  -> worker -> Kafka "orders" (key = AccountId)
  -> Router (to market) / Notifications / Audit
```

- Idempotency-Key stops duplicate trades on retry.
- Return 202 Accepted with the order id.
- Keyed by AccountId, so Buy and Cancel stay in order.
- Redis for fast reads, SQL as the source of truth.
- Every state change stored as an audit event.

**[⬆ Back to Top](#table-of-contents)**

## 90. Why return 202 Accepted instead of waiting for the market?

*System design*

> "Reaching the market and getting filled can take a while and depends on systems we don't control. Holding the client's connection open wastes server resources and risks timeouts, which cause retries. So I accept the order, return 202 with the order id, and push status updates as it moves: sent, filled, rejected."

**[⬆ Back to Top](#table-of-contents)**

## 91. Kafka is down when an order is placed. What happens?

*System design*

> "The order and its outbox row are already saved in one transaction, so the client still gets 202. The worker keeps retrying and publishes once Kafka is back. Nothing is lost, and order intake doesn't depend on Kafka being up."

**[⬆ Back to Top](#table-of-contents)**

## 92. How would a regulator reconstruct what happened to one order?

*System design*

> "Every state change (received, validated, sent, filled, cancelled) is written as an immutable, append-only event with timestamp, user and source. A correlation id follows the order across every service and log. Replaying one order's events shows exactly what happened and when."

**[⬆ Back to Top](#table-of-contents)**

## 93. How do you keep data consistent across microservices?

*System design*

> "Each service owns its database, so there are no distributed transactions. Services communicate with events via an outbox, and multi-step processes use a saga with compensating actions: reserve cash, place the order, and if the market rejects it, release the cash. It's eventually consistent, and every step is idempotent."

**[⬆ Back to Top](#table-of-contents)**

## 94. Circuit breaker vs retry vs bulkhead?

*System design*

- **Retry** with backoff: for brief glitches.
- **Circuit breaker**: after repeated failures, stop calling for a while so you don't pile onto a failing dependency.
- **Bulkhead**: cap concurrent calls to one dependency so it can't use up all your threads.

In .NET: Polly or Microsoft.Extensions.Http.Resilience. On one critical dependency, use all three together.

**[⬆ Back to Top](#table-of-contents)**

## 95. How would you push live price or order updates to the UI?

*System design*

> "SignalR over WebSockets. The server pushes updates instead of the client polling. With several API instances, SignalR needs a backplane, like Redis or Azure SignalR Service, so a message reaches the client whichever instance it's connected to."

**[⬆ Back to Top](#table-of-contents)**

## 96. How does your design scale?

*System design*

> "The Order API is stateless, so I add instances behind the gateway, with autoscaling on OpenShift or AKS. Kafka scales with partitions and consumers. Reads come from Redis and SQL read replicas, and writes stay on the primary."

**[⬆ Back to Top](#table-of-contents)**

## 97. Tell me about a disagreement with a teammate.

*Behavioural*

**STAR, about 90 seconds.** Situation, Task, Action, Result.

What they check: you listen, argue with data, and commit to the team decision.

> Shape: "We disagreed about X. I understood their concern about Y, proposed we compare Z, and we agreed on… The result was…"

**Follow-up:** Use a real example. A good one is technical: where logic should live, sync vs events, or a code review.

**[⬆ Back to Top](#table-of-contents)**

## 98. Tell me about a mistake or a production incident.

*Behavioural*

What they check: ownership, calm diagnosis, prevention.

> Shape: "Something broke. I owned it, found the cause with logs or Datadog, fixed it, and then added a test, alert or process so it can't happen again."

**Follow-up:** End on what you changed afterwards. That's the part they remember.

**[⬆ Back to Top](#table-of-contents)**

## 99. How do you mentor other developers?

*Behavioural*

> "Mostly through code reviews: explaining why, not just what to change, and pairing on tricky pieces. When someone's stuck, I help them debug rather than fixing it for them, so they learn the approach."

**[⬆ Back to Top](#table-of-contents)**

## 100. Why RBC, and why this role?

*Behavioural*

> "It's a rebuild of a large trading platform, which is rare: modern .NET, Kafka, Redis and containers in a domain where correctness really matters. It lines up with what I've done, event-driven integration at Staples and financial reporting at insightsoftware, and I want to go deeper into capital markets."

**[⬆ Back to Top](#table-of-contents)**

## 101. You're okay with contract-to-hire?

*Behavioural*

> "Yes, completely. I'm looking for a long-term role, and I'm happy to prove myself during the contract and convert."

**Follow-up:** Answer without hesitation.

**[⬆ Back to Top](#table-of-contents)**

## 102. What questions do you have for us?

*Behavioural*

- What does the target architecture of the rebuild look like, and what stage is it at?
- How is the team split across the 4 openings?
- What does success look like in the first 3 months?
- What's the biggest technical challenge right now?

**[⬆ Back to Top](#table-of-contents)**

## 103. Walk me through your banking solution.

*CodeSignal*

- **Dictionary<accountId, Account>** for O(1) lookups.
- Validate everything before changing state: accounts exist, amount positive, enough balance.
- Transfer changes both balances only after every check passes, so it's all or nothing.
- Top spenders: track each account's total outgoing, sort descending with an id tie-break, then format the output.

**[⬆ Back to Top](#table-of-contents)**

## 104. How would you have implemented the scheduled transfer?

*CodeSignal*

> "Store scheduled transfers ordered by execution time, in a list or a PriorityQueue keyed by time. Before handling any operation at timestamp T, process every scheduled transfer due at or before T, in order. Check the balance when it executes, not when it's scheduled; if it's insufficient, mark it failed. Give each one an id so it can be cancelled."

**Follow-up:** Why process due transfers first? So every operation sees the correct balance at its timestamp.

**[⬆ Back to Top](#table-of-contents)**

## 105. What would you do differently on the assessment?

*CodeSignal*

> "I'd move faster through the first levels by setting up the data model for later requirements from the start, a dictionary of account objects with history, instead of refactoring each level. That would have left time for the scheduled transfers."

**[⬆ Back to Top](#table-of-contents)**
