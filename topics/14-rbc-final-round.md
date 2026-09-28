# RBC Final Round: Senior .NET, Direct Investing

> Final-round prep for a Senior .NET Developer role rebuilding a Direct Investing
> trading platform (.NET Core, Kafka, Redis, SQL Server, Docker/OpenShift). Say each
> answer out loud in under a minute before revealing it. Sections: Your stories, Screener follow-ups, Basics, Snippets, Kafka, Redis, .NET core, EF Core & SQL, API & security, Testing, Docker & OpenShift, Git, Azure, System design, Frontend, Behavioural, CodeSignal.

## Table of Contents

| No. | Section | Question |
|-----|---------|----------|
| 1 | Your stories | [Tell me about yourself.](#1-tell-me-about-yourself) |
| 2 | Your stories | [Walk me through one integration flow at Staples, end to end.](#2-walk-me-through-one-integration-flow-at-staples-end-to-end) |
| 3 | Your stories | [Draw the Staples shipment flow: sync vs async, retries, idempotency.](#3-draw-the-staples-shipment-flow-sync-vs-async-retries-idempotency) |
| 4 | Your stories | [What happens at Staples if publishing to Event Hubs fails?](#4-what-happens-at-staples-if-publishing-to-event-hubs-fails) |
| 5 | Your stories | [Why do you publish in 15-minute batches instead of immediately?](#5-why-do-you-publish-in-15-minute-batches-instead-of-immediately) |
| 6 | Your stories | [How do you keep stock consistent across multiple order management systems?](#6-how-do-you-keep-stock-consistent-across-multiple-order-management-systems) |
| 7 | Your stories | [If the inventory service is the source of truth, why publish stock updates at all?](#7-if-the-inventory-service-is-the-source-of-truth-why-publish-stock-updates-at-all) |
| 8 | Your stories | [What was the Bounteous / insightsoftware platform, and what was your role?](#8-what-was-the-bounteous--insightsoftware-platform-and-what-was-your-role) |
| 9 | Your stories | [Explain the equity-compensation domain you worked in at insightsoftware.](#9-explain-the-equity-compensation-domain-you-worked-in-at-insightsoftware) |
| 10 | Your stories | [How did you make the reports faster?](#10-how-did-you-make-the-reports-faster) |
| 11 | Your stories | [How did you find which queries were slow?](#11-how-did-you-find-which-queries-were-slow) |
| 12 | Your stories | [Why is SELECT * a problem?](#12-why-is-select--a-problem) |
| 13 | Your stories | [Tell me about a difficult legacy system you worked on.](#13-tell-me-about-a-difficult-legacy-system-you-worked-on) |
| 14 | Your stories | [What did you build with Kafka at Centric?](#14-what-did-you-build-with-kafka-at-centric) |
| 15 | Your stories | [Are you hands-on? What percentage of your day is coding?](#15-are-you-hands-on-what-percentage-of-your-day-is-coding) |
| 16 | Screener follow-ups | [Explain SOLID with a real example.](#16-explain-solid-with-a-real-example) |
| 17 | Screener follow-ups | [Give a SOLID VIOLATION example for each letter.](#17-give-a-solid-violation-example-for-each-letter) |
| 18 | Screener follow-ups | [DI vs IoC vs Dependency Inversion?](#18-di-vs-ioc-vs-dependency-inversion) |
| 19 | Screener follow-ups | [Constructor vs method vs property injection?](#19-constructor-vs-method-vs-property-injection) |
| 20 | Screener follow-ups | [What are the benefits of dependency injection, beyond testing?](#20-what-are-the-benefits-of-dependency-injection-beyond-testing) |
| 21 | Screener follow-ups | [You wrote a class teammates need, in the same solution. How do you share it?](#21-you-wrote-a-class-teammates-need-in-the-same-solution-how-do-you-share-it) |
| 22 | Screener follow-ups | [Explain the Repository pattern. Isn't DbContext already one?](#22-explain-the-repository-pattern-isnt-dbcontext-already-one) |
| 23 | Screener follow-ups | [When would you use a Factory? Give an example.](#23-when-would-you-use-a-factory-give-an-example) |
| 24 | Screener follow-ups | [Find a number in a sorted array of 1 million ints, no built-ins.](#24-find-a-number-in-a-sorted-array-of-1-million-ints-no-built-ins) |
| 25 | Screener follow-ups | [Array of only 0s and 1s: move all 0s to the front in O(n).](#25-array-of-only-0s-and-1s-move-all-0s-to-the-front-in-on) |
| 26 | Screener follow-ups | [Country names and codes in two lists. Why a Dictionary?](#26-country-names-and-codes-in-two-lists-why-a-dictionary) |
| 27 | Screener follow-ups | [How does a Dictionary actually get O(1) lookups?](#27-how-does-a-dictionary-actually-get-o1-lookups) |
| 28 | Screener follow-ups | [Your country Dictionary lives in a Singleton and a nightly job reloads it while requests read. What goes wrong, and how do you fix it?](#28-your-country-dictionary-lives-in-a-singleton-and-a-nightly-job-reloads-it-while-requests-read-what-goes-wrong-and-how-do-you-fix-it) |
| 29 | Screener follow-ups | [If the lookup is a Singleton, how can Reload create a new Dictionary?](#29-if-the-lookup-is-a-singleton-how-can-reload-create-a-new-dictionary) |
| 30 | Basics | [IOptions vs IOptionsSnapshot vs IOptionsMonitor?](#30-ioptions-vs-ioptionssnapshot-vs-ioptionsmonitor) |
| 31 | Basics | [Abstract class vs interface?](#31-abstract-class-vs-interface) |
| 32 | Basics | [const vs readonly?](#32-const-vs-readonly) |
| 33 | Basics | [class vs struct?](#33-class-vs-struct) |
| 34 | Basics | [Why is string immutable, and when do you use StringBuilder?](#34-why-is-string-immutable-and-when-do-you-use-stringbuilder) |
| 35 | Basics | [ref vs out?](#35-ref-vs-out) |
| 36 | Basics | [What does using do with IDisposable?](#36-what-does-using-do-with-idisposable) |
| 37 | Basics | [== vs Equals()?](#37--vs-equals) |
| 38 | Basics | [Task vs Thread?](#38-task-vs-thread) |
| 39 | Basics | [virtual/override vs new?](#39-virtualoverride-vs-new) |
| 40 | Basics | [Filters vs middleware?](#40-filters-vs-middleware) |
| 41 | Basics | [What are the MVC filter types, in order?](#41-what-are-the-mvc-filter-types-in-order) |
| 42 | Basics | [How do model binding and validation work?](#42-how-do-model-binding-and-validation-work) |
| 43 | Basics | [[FromBody] vs [FromQuery] vs [FromRoute]?](#43-frombody-vs-fromquery-vs-fromroute) |
| 44 | Basics | [What is Kestrel?](#44-what-is-kestrel) |
| 45 | Basics | [What is CORS?](#45-what-is-cors) |
| 46 | Basics | [Minimal APIs vs controllers?](#46-minimal-apis-vs-controllers) |
| 47 | Basics | [Where does ASP.NET Core configuration come from, and in what order?](#47-where-does-aspnet-core-configuration-come-from-and-in-what-order) |
| 48 | Basics | [How do you log properly in .NET?](#48-how-do-you-log-properly-in-net) |
| 49 | Basics | [IActionResult vs ActionResult<T>?](#49-iactionresult-vs-actionresultt) |
| 50 | Basics | [What is a correlation ID?](#50-what-is-a-correlation-id) |
| 51 | Basics | [Write a minimal API endpoint.](#51-write-a-minimal-api-endpoint) |
| 52 | Basics | [How do you handle a question you haven't prepared?](#52-how-do-you-handle-a-question-you-havent-prepared) |
| 53 | Screener follow-ups | [Strategy pattern?](#53-strategy-pattern) |
| 54 | Screener follow-ups | [Decorator pattern?](#54-decorator-pattern) |
| 55 | Screener follow-ups | [Mediator / MediatR / CQRS?](#55-mediator--mediatr--cqrs) |
| 56 | Screener follow-ups | [Observer pattern?](#56-observer-pattern) |
| 57 | Screener follow-ups | [Singleton pattern?](#57-singleton-pattern) |
| 58 | Screener follow-ups | [Find the first non-repeating character in a string (e.g. "swiss" gives 'w'). No LINQ.](#58-find-the-first-non-repeating-character-in-a-string-eg-swiss-gives-w-no-linq) |
| 59 | Screener follow-ups | [An array holds 1 to 100 with one number missing, in any order. Find it. No built-ins.](#59-an-array-holds-1-to-100-with-one-number-missing-in-any-order-find-it-no-built-ins) |
| 60 | Screener follow-ups | [Two-sum: return the indexes of the two numbers that add up to a target.](#60-two-sum-return-the-indexes-of-the-two-numbers-that-add-up-to-a-target) |
| 61 | Screener follow-ups | [Reverse the words in a sentence ("I love coding" gives "coding love I"). No Split, no Reverse.](#61-reverse-the-words-in-a-sentence-i-love-coding-gives-coding-love-i-no-split-no-reverse) |
| 62 | Screener follow-ups | [Return all numbers that appear more than once ([4,3,2,7,8,2,3,1] gives [2,3]).](#62-return-all-numbers-that-appear-more-than-once-43278231-gives-23) |
| 63 | Basics | [What does string.Join do?](#63-what-does-stringjoin-do) |
| 64 | Basics | [What does GroupBy actually return? Visualise it.](#64-what-does-groupby-actually-return-visualise-it) |
| 65 | Basics | [Write a basic API controller.](#65-write-a-basic-api-controller) |
| 66 | Basics | [Write a custom middleware.](#66-write-a-custom-middleware) |
| 67 | Screener follow-ups | [Walk me through a layered API: controller, service, repository, ORM. What goes where?](#67-walk-me-through-a-layered-api-controller-service-repository-orm-what-goes-where) |
| 68 | Screener follow-ups | [Show the code for each layer of a repository-pattern API.](#68-show-the-code-for-each-layer-of-a-repository-pattern-api) |
| 69 | Screener follow-ups | [QUICK REFERENCE: Tony's screener questions in one table.](#69-quick-reference-tonys-screener-questions-in-one-table) |
| 70 | Screener follow-ups | [QUICK REFERENCE: repeats, counts and pairs means Dictionary or HashSet.](#70-quick-reference-repeats-counts-and-pairs-means-dictionary-or-hashset) |
| 71 | Screener follow-ups | [Walk me through a full API request: middleware, filter, controller, service, cache, repository, EF.](#71-walk-me-through-a-full-api-request-middleware-filter-controller-service-cache-repository-ef) |
| 72 | Snippets | [class Foo<T> { public static int bar; } Foo<int>.bar++; what does Foo<double>.bar print?](#72-class-foot--public-static-int-bar--foointbar-what-does-foodoublebar-print) |
| 73 | Snippets | [Static constructor, instance constructor and Print(): what's the output of new Test().Print()?](#73-static-constructor-instance-constructor-and-print-whats-the-output-of-new-testprint) |
| 74 | Snippets | [Main calls an async method (with await Task.Delay) WITHOUT awaiting, then prints the value. What happens?](#74-main-calls-an-async-method-with-await-taskdelay-without-awaiting-then-prints-the-value-what-happens) |
| 75 | Kafka | [Why use Kafka instead of calling the other service's API?](#75-why-use-kafka-instead-of-calling-the-other-services-api) |
| 76 | Kafka | [Explain topics, partitions, offsets and consumer groups.](#76-explain-topics-partitions-offsets-and-consumer-groups) |
| 77 | Kafka | [How do you keep one account's Buy and Cancel in order?](#77-how-do-you-keep-one-accounts-buy-and-cancel-in-order) |
| 78 | Kafka | [A consumer processes a message but crashes before committing the offset.](#78-a-consumer-processes-a-message-but-crashes-before-committing-the-offset) |
| 79 | Kafka | [Why add a version number to events if Kafka keeps order?](#79-why-add-a-version-number-to-events-if-kafka-keeps-order) |
| 80 | Kafka | [Two consumers in the same group vs in different groups?](#80-two-consumers-in-the-same-group-vs-in-different-groups) |
| 81 | Kafka | [What's a dead-letter queue and when do you use it?](#81-whats-a-dead-letter-queue-and-when-do-you-use-it) |
| 82 | Kafka | [What's a rebalance?](#82-whats-a-rebalance) |
| 83 | Kafka | [Kafka vs a queue like MQ, RabbitMQ or Service Bus?](#83-kafka-vs-a-queue-like-mq-rabbitmq-or-service-bus) |
| 84 | Kafka | [Can more consumers than partitions make it faster?](#84-can-more-consumers-than-partitions-make-it-faster) |
| 85 | Kafka | [Is exactly-once delivery possible?](#85-is-exactly-once-delivery-possible) |
| 86 | Kafka | [Explain the transactional outbox pattern.](#86-explain-the-transactional-outbox-pattern) |
| 87 | Redis | [How do you implement caching with Redis?](#87-how-do-you-implement-caching-with-redis) |
| 88 | Redis | [How do you choose TTLs?](#88-how-do-you-choose-ttls) |
| 89 | Redis | [How do you invalidate the cache when data changes?](#89-how-do-you-invalidate-the-cache-when-data-changes) |
| 90 | Redis | [What's a cache stampede, and how do you prevent it?](#90-whats-a-cache-stampede-and-how-do-you-prevent-it) |
| 91 | Redis | [Redis goes down. What happens to your API?](#91-redis-goes-down-what-happens-to-your-api) |
| 92 | Redis | [In a trading platform, where would you use Redis, and what would you never trust a cache for?](#92-in-a-trading-platform-where-would-you-use-redis-and-what-would-you-never-trust-a-cache-for) |
| 93 | Redis | [Why shouldn't Redis be the source of truth for an account balance?](#93-why-shouldnt-redis-be-the-source-of-truth-for-an-account-balance) |
| 94 | Redis | [IMemoryCache vs Redis?](#94-imemorycache-vs-redis) |
| 95 | Redis | [What else is Redis used for besides caching?](#95-what-else-is-redis-used-for-besides-caching) |
| 96 | Redis | [What happens when Redis runs out of memory?](#96-what-happens-when-redis-runs-out-of-memory) |
| 97 | .NET core | [Transient vs Scoped vs Singleton?](#97-transient-vs-scoped-vs-singleton) |
| 98 | .NET core | [Why can't you inject a Scoped service into a Singleton?](#98-why-cant-you-inject-a-scoped-service-into-a-singleton) |
| 99 | .NET core | [How do you keep a Singleton thread-safe?](#99-how-do-you-keep-a-singleton-thread-safe) |
| 100 | .NET core | [What does async/await actually do? Does it create a thread?](#100-what-does-asyncawait-actually-do-does-it-create-a-thread) |
| 101 | .NET core | [Why is async void dangerous?](#101-why-is-async-void-dangerous) |
| 102 | .NET core | [What's wrong with .Result or .Wait()?](#102-whats-wrong-with-result-or-wait) |
| 103 | .NET core | [How do you run three independent calls in parallel?](#103-how-do-you-run-three-independent-calls-in-parallel) |
| 104 | .NET core | [Process 1000 messages, max 10 at a time, and start the next as soon as one finishes. How?](#104-process-1000-messages-max-10-at-a-time-and-start-the-next-as-soon-as-one-finishes-how) |
| 105 | .NET core | [Why use IHttpClientFactory?](#105-why-use-ihttpclientfactory) |
| 106 | .NET core | [IEnumerable vs IQueryable?](#106-ienumerable-vs-iqueryable) |
| 107 | .NET core | [What is middleware in ASP.NET Core?](#107-what-is-middleware-in-aspnet-core) |
| 108 | .NET core | [How do you handle exceptions globally in an API?](#108-how-do-you-handle-exceptions-globally-in-an-api) |
| 109 | .NET core | [How do you reduce memory allocations on large data?](#109-how-do-you-reduce-memory-allocations-on-large-data) |
| 110 | .NET core | [record vs class?](#110-record-vs-class) |
| 111 | EF Core & SQL | [What's the N+1 problem? How do you fix it?](#111-whats-the-n1-problem-how-do-you-fix-it) |
| 112 | EF Core & SQL | [What does AsNoTracking do, and when does it hurt?](#112-what-does-asnotracking-do-and-when-does-it-hurt) |
| 113 | EF Core & SQL | [Two users update the same balance at once. How do you stop a lost update?](#113-two-users-update-the-same-balance-at-once-how-do-you-stop-a-lost-update) |
| 114 | EF Core & SQL | [How do you deploy database changes safely?](#114-how-do-you-deploy-database-changes-safely) |
| 115 | EF Core & SQL | [Clustered vs nonclustered index? What's a key lookup?](#115-clustered-vs-nonclustered-index-whats-a-key-lookup) |
| 116 | EF Core & SQL | [Why would SQL Server ignore an index you created?](#116-why-would-sql-server-ignore-an-index-you-created) |
| 117 | EF Core & SQL | [What's parameter sniffing?](#117-whats-parameter-sniffing) |
| 118 | EF Core & SQL | [Two orders try to reserve the last unit at the same moment. How do you stop both succeeding?](#118-two-orders-try-to-reserve-the-last-unit-at-the-same-moment-how-do-you-stop-both-succeeding) |
| 119 | EF Core & SQL | [Does SQL Server lock rows by itself?](#119-does-sql-server-lock-rows-by-itself) |
| 120 | EF Core & SQL | [How do you prevent deadlocks in money transfers?](#120-how-do-you-prevent-deadlocks-in-money-transfers) |
| 121 | EF Core & SQL | [Add a NOT NULL column to a 50-million-row table without downtime.](#121-add-a-not-null-column-to-a-50-million-row-table-without-downtime) |
| 122 | EF Core & SQL | [Where should business logic live: stored procedures or C#?](#122-where-should-business-logic-live-stored-procedures-or-c) |
| 123 | EF Core & SQL | [Isolation levels, in one breath.](#123-isolation-levels-in-one-breath) |
| 124 | EF Core & SQL | [SQL: types of JOIN?](#124-sql-types-of-join) |
| 125 | EF Core & SQL | [SQL: WHERE vs HAVING?](#125-sql-where-vs-having) |
| 126 | EF Core & SQL | [SQL: DELETE vs TRUNCATE?](#126-sql-delete-vs-truncate) |
| 127 | EF Core & SQL | [SQL: UNION vs UNION ALL?](#127-sql-union-vs-union-all) |
| 128 | EF Core & SQL | [SQL: what's a CTE?](#128-sql-whats-a-cte) |
| 129 | EF Core & SQL | [SQL: ROW_NUMBER vs RANK vs DENSE_RANK?](#129-sql-rownumber-vs-rank-vs-denserank) |
| 130 | EF Core & SQL | [SQL: find the second-highest salary.](#130-sql-find-the-second-highest-salary) |
| 131 | EF Core & SQL | [SQL: delete duplicate rows but keep one.](#131-sql-delete-duplicate-rows-but-keep-one) |
| 132 | EF Core & SQL | [SQL: temp table vs table variable?](#132-sql-temp-table-vs-table-variable) |
| 133 | EF Core & SQL | [SQL: stored procedure vs function?](#133-sql-stored-procedure-vs-function) |
| 134 | EF Core & SQL | [SQL: what is ACID?](#134-sql-what-is-acid) |
| 135 | EF Core & SQL | [SQL: what is normalization?](#135-sql-what-is-normalization) |
| 136 | API & security | [What makes a RESTful API well designed?](#136-what-makes-a-restful-api-well-designed) |
| 137 | API & security | [POST vs PUT vs PATCH, and which are idempotent?](#137-post-vs-put-vs-patch-and-which-are-idempotent) |
| 138 | API & security | [Which status codes do you use, and when?](#138-which-status-codes-do-you-use-and-when) |
| 139 | API & security | [A client retries a timed-out order. How do you prevent a duplicate trade?](#139-a-client-retries-a-timed-out-order-how-do-you-prevent-a-duplicate-trade) |
| 140 | API & security | [How do you version an API?](#140-how-do-you-version-an-api) |
| 141 | API & security | [OAuth2 vs JWT?](#141-oauth2-vs-jwt) |
| 142 | API & security | [A partner system calls your API through APIM. Walk me through how it's secured.](#142-a-partner-system-calls-your-api-through-apim-walk-me-through-how-its-secured) |
| 143 | API & security | [How do users log in through the UI and call your API?](#143-how-do-users-log-in-through-the-ui-and-call-your-api) |
| 144 | API & security | [What does rotating secrets mean?](#144-what-does-rotating-secrets-mean) |
| 145 | API & security | [How do you implement authorization in .NET?](#145-how-do-you-implement-authorization-in-net) |
| 146 | API & security | [How does your API validate a JWT?](#146-how-does-your-api-validate-a-jwt) |
| 147 | API & security | [Name an OWASP risk you've mitigated.](#147-name-an-owasp-risk-youve-mitigated) |
| 148 | API & security | [How do you protect customer data and privacy?](#148-how-do-you-protect-customer-data-and-privacy) |
| 149 | API & security | [Where do secrets like connection strings go?](#149-where-do-secrets-like-connection-strings-go) |
| 150 | API & security | [What do you know about WCAG accessibility?](#150-what-do-you-know-about-wcag-accessibility) |
| 151 | Testing | [How do you test a service that consumes events and writes to a database?](#151-how-do-you-test-a-service-that-consumes-events-and-writes-to-a-database) |
| 152 | Testing | [Unit test vs integration test: where's the line?](#152-unit-test-vs-integration-test-wheres-the-line) |
| 153 | Testing | [How do you unit test a class that publishes to Kafka?](#153-how-do-you-unit-test-a-class-that-publishes-to-kafka) |
| 154 | Testing | [How do you test an API end to end?](#154-how-do-you-test-an-api-end-to-end) |
| 155 | Testing | [What makes a good unit test?](#155-what-makes-a-good-unit-test) |
| 156 | Testing | [Mock vs stub vs fake?](#156-mock-vs-stub-vs-fake) |
| 157 | Testing | [Do you practise TDD?](#157-do-you-practise-tdd) |
| 158 | Docker & OpenShift | [Image vs container vs Docker?](#158-image-vs-container-vs-docker) |
| 159 | Docker & OpenShift | [How do you write a Dockerfile for a .NET API?](#159-how-do-you-write-a-dockerfile-for-a-net-api) |
| 160 | Docker & OpenShift | [Explain the core Kubernetes objects.](#160-explain-the-core-kubernetes-objects) |
| 161 | Docker & OpenShift | [OpenShift vs Kubernetes?](#161-openshift-vs-kubernetes) |
| 162 | Docker & OpenShift | [Liveness vs readiness probe?](#162-liveness-vs-readiness-probe) |
| 163 | Docker & OpenShift | [Walk me through a CI/CD pipeline you've built.](#163-walk-me-through-a-cicd-pipeline-youve-built) |
| 164 | Docker & OpenShift | [How do you handle config per environment?](#164-how-do-you-handle-config-per-environment) |
| 165 | Git | [Git: merge vs rebase?](#165-git-merge-vs-rebase) |
| 166 | Git | [Git: what's your branching strategy?](#166-git-whats-your-branching-strategy) |
| 167 | Git | [Git: how do you resolve a merge conflict?](#167-git-how-do-you-resolve-a-merge-conflict) |
| 168 | Git | [What do you look for in a code review?](#168-what-do-you-look-for-in-a-code-review) |
| 169 | Git | [Git: revert vs reset?](#169-git-revert-vs-reset) |
| 170 | Azure | [Azure: App Service vs AKS vs Azure Functions?](#170-azure-app-service-vs-aks-vs-azure-functions) |
| 171 | Azure | [Azure: Event Hubs vs Service Bus vs Event Grid?](#171-azure-event-hubs-vs-service-bus-vs-event-grid) |
| 172 | Azure | [Azure: what is APIM for?](#172-azure-what-is-apim-for) |
| 173 | Azure | [Azure: Key Vault and Managed Identity?](#173-azure-key-vault-and-managed-identity) |
| 174 | Azure | [Azure: what does Application Insights give you?](#174-azure-what-does-application-insights-give-you) |
| 175 | Azure | [Azure: storage types?](#175-azure-storage-types) |
| 176 | Azure | [Azure: Table Storage vs Cosmos DB vs Azure SQL?](#176-azure-table-storage-vs-cosmos-db-vs-azure-sql) |
| 177 | Azure | [Azure: what is ACR?](#177-azure-what-is-acr) |
| 178 | Azure | [Azure: how does a request reach your AKS service?](#178-azure-how-does-a-request-reach-your-aks-service) |
| 179 | Azure | [Azure: what are deployment slots?](#179-azure-what-are-deployment-slots) |
| 180 | Azure | [Azure: how do you scale?](#180-azure-how-do-you-scale) |
| 181 | Azure | [How do you implement Event Hubs in .NET?](#181-how-do-you-implement-event-hubs-in-net) |
| 182 | Azure | [What is Google Pub/Sub and how does it work?](#182-what-is-google-pubsub-and-how-does-it-work) |
| 183 | Azure | [What is AKS, and who decides the number of pods?](#183-what-is-aks-and-who-decides-the-number-of-pods) |
| 184 | Azure | [Walk me through an Azure DevOps pipeline you built.](#184-walk-me-through-an-azure-devops-pipeline-you-built) |
| 185 | System design | [Microservices vs monolith?](#185-microservices-vs-monolith) |
| 186 | System design | [How would you build a microservice?](#186-how-would-you-build-a-microservice) |
| 187 | System design | [A client clicks 'Buy 100 shares'. Design what happens until the order reaches the market.](#187-a-client-clicks-buy-100-shares-design-what-happens-until-the-order-reaches-the-market) |
| 188 | System design | [Does the Direct Investing platform match buyers and sellers?](#188-does-the-direct-investing-platform-match-buyers-and-sellers) |
| 189 | System design | [Broker domain terms: exchange, market vs limit order, fill, buying power?](#189-broker-domain-terms-exchange-market-vs-limit-order-fill-buying-power) |
| 190 | System design | [Draw the journey of one 'Buy 100 AAPL' order.](#190-draw-the-journey-of-one-buy-100-aapl-order) |
| 191 | System design | [Order follow-ups: partial fill, client cancel, exchange reject?](#191-order-follow-ups-partial-fill-client-cancel-exchange-reject) |
| 192 | System design | [Why return 202 Accepted instead of waiting for the market?](#192-why-return-202-accepted-instead-of-waiting-for-the-market) |
| 193 | System design | [Kafka is down when an order is placed. What happens?](#193-kafka-is-down-when-an-order-is-placed-what-happens) |
| 194 | System design | [How would a regulator reconstruct what happened to one order?](#194-how-would-a-regulator-reconstruct-what-happened-to-one-order) |
| 195 | System design | [How do you keep data consistent across microservices?](#195-how-do-you-keep-data-consistent-across-microservices) |
| 196 | System design | [Circuit breaker vs retry vs bulkhead?](#196-circuit-breaker-vs-retry-vs-bulkhead) |
| 197 | System design | [How would you push live price or order updates to the UI?](#197-how-would-you-push-live-price-or-order-updates-to-the-ui) |
| 198 | System design | [How does your design scale?](#198-how-does-your-design-scale) |
| 199 | Frontend | [Frontend: how do you position yourself if they go deep?](#199-frontend-how-do-you-position-yourself-if-they-go-deep) |
| 200 | Frontend | [Angular: component vs service? Lifecycle hooks?](#200-angular-component-vs-service-lifecycle-hooks) |
| 201 | Frontend | [Angular: Observables, the async pipe and switchMap?](#201-angular-observables-the-async-pipe-and-switchmap) |
| 202 | Frontend | [Angular: HTTP interceptor and route guard?](#202-angular-http-interceptor-and-route-guard) |
| 203 | Frontend | [Angular: change detection, OnPush, and modern Angular?](#203-angular-change-detection-onpush-and-modern-angular) |
| 204 | Frontend | [React: props vs state, useState, useEffect, virtual DOM?](#204-react-props-vs-state-usestate-useeffect-virtual-dom) |
| 205 | Behavioural | [Tell me about a disagreement with a teammate.](#205-tell-me-about-a-disagreement-with-a-teammate) |
| 206 | Behavioural | [Tell me about a production incident or a hard problem you solved.](#206-tell-me-about-a-production-incident-or-a-hard-problem-you-solved) |
| 207 | Behavioural | [Working with another team or an external vendor whose system didn't do what you needed?](#207-working-with-another-team-or-an-external-vendor-whose-system-didnt-do-what-you-needed) |
| 208 | Behavioural | [Tell me about delivering under a tight deadline.](#208-tell-me-about-delivering-under-a-tight-deadline) |
| 209 | Behavioural | [Tell me about a hard technical challenge you overcame.](#209-tell-me-about-a-hard-technical-challenge-you-overcame) |
| 210 | Behavioural | [How do you use AI in your work?](#210-how-do-you-use-ai-in-your-work) |
| 211 | Behavioural | [Other likely behavioural questions: quick starting points.](#211-other-likely-behavioural-questions-quick-starting-points) |
| 212 | Behavioural | [How do you mentor other developers?](#212-how-do-you-mentor-other-developers) |
| 213 | Behavioural | [Why RBC, and why this role?](#213-why-rbc-and-why-this-role) |
| 214 | Behavioural | [You're okay with contract-to-hire?](#214-youre-okay-with-contract-to-hire) |
| 215 | Behavioural | [What questions do you have for us?](#215-what-questions-do-you-have-for-us) |
| 216 | CodeSignal | [Walk me through your banking solution, level by level.](#216-walk-me-through-your-banking-solution-level-by-level) |
| 217 | CodeSignal | [Level 3: show the transfer and the traps.](#217-level-3-show-the-transfer-and-the-traps) |
| 218 | CodeSignal | [Level 4: top spenders, and the traps.](#218-level-4-top-spenders-and-the-traps) |
| 219 | CodeSignal | [How would you have implemented the scheduled transfer?](#219-how-would-you-have-implemented-the-scheduled-transfer) |
| 220 | CodeSignal | [Why call ProcessDue in every method instead of a background service?](#220-why-call-processdue-in-every-method-instead-of-a-background-service) |
| 221 | CodeSignal | [How would you improve your CodeSignal solution?](#221-how-would-you-improve-your-codesignal-solution) |

## 1. Tell me about yourself.

*Your stories*

**About 75 seconds.** Bold words are hooks that lead to prepared answers.

> "I'm a senior .NET developer with about ten years of experience, mostly C# and .NET Core backends.

> At Staples I'm on the middleware team. Staples runs on a lot of third-party platforms, like **Centiro** for carriers and **Manhattan** for the warehouse, and my job is making them talk to each other and to our systems. A typical flow: a customer calls our API through **APIM**, we call Centiro synchronously to pick the carrier, then publish **events** to the warehouse and transport systems over **Pub/Sub and Event Hubs**, with **retries** so nothing is lost. On inventory, we built a **single source of truth** for stock, and I relay its updates to each system in the format it needs: events for some, REST APIs for others.

> Before that I was a **full-stack** lead developer at Accolite on a **capital markets** reporting platform for insightsoftware. About 70% of my work was **report calculations**, like vesting and equity-compensation figures, plus **performance tuning**; the rest was typical full-stack work: admin features like **feature flags**, data validation and the UI.

> What excites me about this role is that it's exactly that combination (event-driven .NET, performance, financial data) on a platform being rebuilt."

**[⬆ Back to Top](#table-of-contents)**

## 2. Walk me through one integration flow at Staples, end to end.

*Your stories*

> "A customer creates a shipment by calling our API through Azure APIM. My service calls Centiro, the carrier platform, to pick the transport partner, and returns that in the same response. Then it raises two events: Google Pub/Sub so the WMS expects the package, and Azure Event Hubs so the TMS schedules delivery."

> "The carrier answer is synchronous because the customer needs it now. WMS and TMS get events because they don't need to block the customer. A slow WMS never slows the customer's call."

**Follow-up:** Why not call WMS and TMS directly? Coupling: if either is slow or down, the customer's request fails. Events let each team consume at its own pace.

**[⬆ Back to Top](#table-of-contents)**

## 3. Draw the Staples shipment flow: sync vs async, retries, idempotency.

*Your stories*

```csharp
Customer --POST /shipments--> APIM --> Your .NET 8 API
   SYNCHRONOUS (customer waits)
     --> Centiro: which carrier? --> "Purolator, $12.40"
     --> save shipment + messages to table (one transaction)
     --> respond 200: carrier + tracking

   ASYNCHRONOUS (customer doesn't wait)
   Background service reads pending rows:
     --> Google Pub/Sub  --> Manhattan WMS: expect this package
     --> Azure Event Hubs --> TMS: schedule delivery
   failure? stays Pending, retry with backoff, Datadog alert after N failures
```

> "Customer-facing work is synchronous; everything else is events, saved first, retried with backoff, and processed idempotently."

**Follow-up:** WMS down for an hour? The customer isn't affected. We publish to Pub/Sub, not to the WMS, so the publish SUCCEEDS and messages wait in the subscription; the WMS processes everything it hasn't acknowledged when it's back. Retries + Datadog alerts are for the OTHER case: the broker itself unreachable, so rows stay pending in our table. Pub/Sub uses acks, Kafka uses offsets, Event Hubs uses checkpoints: same idea. What's backoff? Waiting longer between retries (1s, 2s, 4s, 8s) so you don't overwhelm a struggling system. Exact idempotency check: a ProcessedMessages table with the message id as a unique key, insert + process in one transaction; a duplicate insert fails, so skip.

**[⬆ Back to Top](#table-of-contents)**

## 4. What happens at Staples if publishing to Event Hubs fails?

*Your stories*

> "Messages are saved to a table first. A background service publishes them on a schedule, so a failed publish doesn't lose anything. The row stays pending, we retry with backoff, and after repeated failures Datadog alerts the team. Delivery is at-least-once, so consumers deduplicate on the message id."

This is an **outbox** pattern with batched publishing.

**Follow-up:** Improvements to mention: keep a status column instead of deleting rows (audit trail), and track status per destination so 'WMS sent, TMS failed' is visible.

**[⬆ Back to Top](#table-of-contents)**

## 5. Why do you publish in 15-minute batches instead of immediately?

*Your stories*

> "Fewer calls to partner systems, and WMS and TMS don't need the data within seconds. The trade-off is up to 15 minutes of delay. For a trading platform I'd shrink that to seconds or publish continuously, because order events can't wait."

**Follow-up:** The worker sends 50 of 100 rows and crashes? Those rows are still pending, so they're re-sent. Mark each row Sent right after it succeeds to keep duplicates small.

**[⬆ Back to Top](#table-of-contents)**

## 6. How do you keep stock consistent across multiple order management systems?

*Your stories*

> "The key is one source of truth. Our inventory service owns the stock numbers, the single pool of inventory, and the order management systems don't calculate stock themselves; they receive it.

> Every stock change is published as an event keyed by SKU, so changes for one product are processed in order. Each event carries a version number, so a late, older update is ignored instead of overwriting newer data. Consumers are idempotent, so a redelivered event doesn't change stock twice.

> Events can still fail, so a reconciliation pipeline periodically compares each system's stock with ours, fixes differences and alerts when drift crosses a threshold. Failing messages go to a dead-letter queue. So it's eventually consistent, with reconciliation as the safety net."

**Pattern:** one owner, then ordered and versioned events, then idempotent consumers, then reconciliation.

**Follow-up:** Why not one shared database for all systems? They're owned by different teams and vendors. A shared database couples them, so one team's schema change breaks everyone. Events keep them independent.

**[⬆ Back to Top](#table-of-contents)**

## 7. If the inventory service is the source of truth, why publish stock updates at all?

*Your stories*

> "The source of truth decides the numbers, but other systems still need to know them: the website shows availability on every page, and order systems check stock before accepting an order. They can't call us millions of times, so each keeps a read-only copy that our events keep current and reconciliation checks. Their copy never decides stock; ours wins."

Analogy: the bank is the source of truth, and your banking app shows a copy.

**[⬆ Back to Top](#table-of-contents)**

## 8. What was the Bounteous / insightsoftware platform, and what was your role?

*Your stories*

> "An equity-compensation reporting platform. Corporate clients used it to report on their employee stock plans: ESOP tax impact, vesting and unvesting schedules, grant reports. I was lead developer on the reporting team: building and changing reports end to end, API to database, and owning performance of the heavy ones."

**Follow-up:** Know a few domain words cold: grant, vesting schedule, cliff, exercise, unvested shares, fair market value.

**[⬆ Back to Top](#table-of-contents)**

## 9. Explain the equity-compensation domain you worked in at insightsoftware.

*Your stories*

- **Grant**: a company awards shares or options to an employee.
- **Vesting schedule**: when the employee actually earns them, e.g. over 4 years.
- **Cliff**: nothing vests until a first milestone (e.g. 1 year), then a chunk vests at once.
- **Vested / unvested**: earned so far vs still pending.
- **Stock option**: the right to buy shares at a fixed **strike price**.
- **RSU**: Restricted Stock Units, actual shares given once vested, no purchase needed.
- **Exercise**: using an option to buy the shares at the strike price.
- **FMV**: Fair Market Value of the share on a date, used for tax calculations.
- **ESOP tax report**: tax impact for company and employee when options vest or are exercised.

> "At insightsoftware, clients used our platform to manage employee equity plans. I worked on the calculations behind reports like vesting schedules and the tax impact of grants and exercises, which depend on things like FMV on the vesting date."

**[⬆ Back to Top](#table-of-contents)**

## 10. How did you make the reports faster?

*Your stories*

1. **Diagnosis:** Datadog showed the API time was almost all inside the database call; the code path was already async.
1. **SELECT * → only needed columns.** Less I/O and network, and it lets indexes cover the query.
1. **Indexes** on the columns the reports filter and join on (client, grant date), checked in the execution plan.
1. **async/await end to end** so threads aren't blocked while waiting on SQL.
1. **Caching** data that rarely changes (plan definitions, reference data).

> "Heavy reports got significantly faster, roughly 40% on the worst ones."

**Follow-up:** Precision: async doesn't make one report faster. It improves throughput: the server handles many more concurrent report requests because threads aren't blocked.

**[⬆ Back to Top](#table-of-contents)**

## 11. How did you find which queries were slow?

*Your stories*

> "Datadog APM showed the time was spent in the database call, not in our code. Then I captured the slow queries with SQL Profiler and read their execution plans: table scans, key lookups, missing indexes."

**Follow-up:** Tooling: SQL Profiler is SQL Server only. On Oracle the equivalents are Explain Plan, AWR reports and SQL Trace/TKPROF.

**[⬆ Back to Top](#table-of-contents)**

## 12. Why is SELECT * a problem?

*Your stories*

- Reads and sends columns nobody uses: more I/O, network and memory.
- Prevents a covering index, so SQL does extra key lookups.
- Breaks or slows silently when someone adds a large column later.

**[⬆ Back to Top](#table-of-contents)**

## 13. Tell me about a difficult legacy system you worked on.

*Your stories*

> "Most business logic lived in stored procedures: thousands of lines of PL/SQL, procedures calling other procedures, with loops and cursors. The C# and Angular layers mostly just called them. It was hard to debug, hard to unit test and risky to change. It taught me why business logic belongs in the application layer, where it's testable, version-controlled and easy to scale, with SQL focused on data access."

**Follow-up:** Frame it as a lesson learned, not a complaint. If asked how you worked in it: trace the call chain, add logging, make small safe changes.

**[⬆ Back to Top](#table-of-contents)**

## 14. What did you build with Kafka at Centric?

*Your stories*

> "On an insurance platform, documents for different products were generated through Kafka. When a user requested a document, an event with the JSON payload was published to a topic per document type. I built consumer services that picked up the JSON, generated the PDF and stored it in Blob storage, where the UI read it from. The Kafka platform itself was set up by another team; my part was the consumers."

**Follow-up:** Likely follow-up: what if PDF generation fails halfway? Don't commit the offset until the PDF is stored. Retry, then dead-letter. Make it idempotent so a re-delivered message doesn't create a second document.

**[⬆ Back to Top](#table-of-contents)**

## 15. Are you hands-on? What percentage of your day is coding?

*Your stories*

> "Mostly hands-on. The majority of my day is design and coding; the rest is code reviews, sprint work with the team and mentoring. I like staying close to the code."

**[⬆ Back to Top](#table-of-contents)**

## 16. Explain SOLID with a real example.

*Screener follow-ups*

- **S**: one reason to change. `ShipmentService` runs the flow; `PubSubPublisher` only talks to Pub/Sub.
- **O**: extend without editing. A partner wants Kafka: add `KafkaPublisher`, nothing else changes.
- **L**: any implementation can replace another. A publisher that silently swallows errors would break the caller's retry logic.
- **I**: small interfaces. Publishing and consuming are separate interfaces.
- **D**: depend on `IEventPublisher`, never `new PubSubPublisher()`.

**[⬆ Back to Top](#table-of-contents)**

## 17. Give a SOLID VIOLATION example for each letter.

*Screener follow-ups*

- **S:** a ShipmentService that also builds JSON, calls Centiro and writes log files.
- **O:** a switch (destination) inside the service that you edit for every new partner.
- **L:** a publisher that silently swallows failures, breaking the caller's retry logic.
- **I:** one IMessaging with 15 methods where most classes throw NotImplementedException.
- **D:** var p = new PubSubPublisher(); inside the service instead of injecting IEventPublisher.

**[⬆ Back to Top](#table-of-contents)**

## 18. DI vs IoC vs Dependency Inversion?

*Screener follow-ups*

> "Dependency Inversion is the principle: depend on abstractions. Inversion of Control is the broader idea that a framework creates your objects and calls your code, instead of you doing it. Dependency Injection is the technique that implements it: dependencies are passed in, usually through the constructor, and the DI container builds them."

**[⬆ Back to Top](#table-of-contents)**

## 19. Constructor vs method vs property injection?

*Screener follow-ups*

> "Constructor injection is the default: dependencies are required and visible. Method injection is for something only one call needs, like [FromServices] on an action. Property injection is rare in .NET's built-in container."

**[⬆ Back to Top](#table-of-contents)**

## 20. What are the benefits of dependency injection, beyond testing?

*Screener follow-ups*

- Loose coupling: callers depend on an interface, so implementations can be swapped.
- Dependencies are visible in the constructor instead of hidden.
- The container manages lifetimes (Transient, Scoped, Singleton) and disposal.
- Configuration lives in one place (Program.cs).
- And yes, unit tests can inject mocks.

**[⬆ Back to Top](#table-of-contents)**

## 21. You wrote a class teammates need, in the same solution. How do you share it?

*Screener follow-ups*

> "Within one solution, a project reference; NuGet is for sharing across solutions. For how teammates use it, I expose an interface and register the implementation in DI, so their code depends only on the contract, can be tested with mocks, and doesn't break when my implementation changes."

**Follow-up:** Why not a static class? Can't be mocked or swapped, hides dependencies, can't receive a DbContext or HttpClient. Static is fine for pure helpers like Math.Max.

**[⬆ Back to Top](#table-of-contents)**

## 22. Explain the Repository pattern. Isn't DbContext already one?

*Screener follow-ups*

> "A repository puts data access behind an interface, so services contain no EF or SQL, and I can mock it in tests. DbContext is already a unit of work and repository, so for simple CRUD I often use it directly. I add a repository when I want query logic in one place or EF out of the domain. I avoid a generic IRepository<T> that just wraps DbSet."

**Follow-up:** The repository doesn't call SaveChanges. The caller saves once per request so several changes commit together.

**[⬆ Back to Top](#table-of-contents)**

## 23. When would you use a Factory? Give an example.

*Screener follow-ups*

> "When which object to create depends on data at runtime. My example: a PublisherFactory. DI injects all IEventPublisher implementations, the factory stores them in a Dictionary by destination, and callers ask for 'WMS' or 'TMS'. Adding Kafka is one new class and one registration line."

**Follow-up:** Factory vs DI: DI when the type is known at startup, a factory when it depends on runtime data. They work together.

**[⬆ Back to Top](#table-of-contents)**

## 24. Find a number in a sorted array of 1 million ints, no built-ins.

*Screener follow-ups*

**With library:** `int index = Array.BinarySearch(arr, target);` returns the index, or a negative number if not found. O(log n).

**Without library:**

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

## 25. Array of only 0s and 1s: move all 0s to the front in O(n).

*Screener follow-ups*

**With library:** `Array.Sort(bits);` works but is O(n log n). Faster built-in-ish: count the zeros, then fill. The two-pointer swap is O(n) in one pass.

**Without library:**

> "Two pointers, one at each end. A 0 on the left is in place, so move left forward. A 1 on the right is in place, so move right back. If both are wrong, swap them and move both. Each element is visited once: O(n) time, O(1) space, in place."

**Follow-up:** Mirror version (1s first): same algorithm with the value flipped, so pass the front value in as a parameter.

**[⬆ Back to Top](#table-of-contents)**

## 26. Country names and codes in two lists. Why a Dictionary?

*Screener follow-ups*

**With library:** `var lookup = names.Zip(codes).ToDictionary(p => p.First, p => p.Second);` Zip pairs the two lists item by item.

**Without library:** a for loop adding names[i] to codes[i].

> "Build a Dictionary once, O(n). After that every lookup is O(1). With two lists, every lookup scans the list, O(n) each time, and the two lists can drift out of sync."

**Follow-up:** Bonus: new Dictionary(StringComparer.OrdinalIgnoreCase) so 'canada' matches 'Canada'.

**[⬆ Back to Top](#table-of-contents)**

## 27. How does a Dictionary actually get O(1) lookups?

*Screener follow-ups*

- It calls `GetHashCode()` on the key and maps it to a bucket.
- It goes straight to that bucket and confirms the key with `Equals()`.
- Different keys landing in one bucket are a collision; they're chained, so a lookup checks a few entries.
- When it fills up, it resizes and rehashes into a bigger array.

**Follow-up:** Worst case is O(n) if many keys collide. Never change a key object's fields after inserting it, or its hash changes and you can't find it.

**[⬆ Back to Top](#table-of-contents)**

## 28. Your country Dictionary lives in a Singleton and a nightly job reloads it while requests read. What goes wrong, and how do you fix it?

*Screener follow-ups*

**Problem 1:** a plain Dictionary isn't safe for reads during writes. A reader can get an exception, a wrong result, or (older .NET) an infinite loop.

**Problem 2, the trap:** even ConcurrentDictionary gives wrong answers if the job does Clear() then re-adds. Between Clear and Add("India"), a lookup says India doesn't exist.

**Fix: build a new dictionary on the side, then swap the reference in one step.**

```csharp
private volatile Dictionary<string, string> _countries = new Dictionary<string, string>();

public string? GetCode(string countryName)
{
    Dictionary<string, string> current = _countries;
    if (current.TryGetValue(countryName, out string? code))
    {
        return code;
    }
    return null;
}

public void Reload(List<string> names, List<string> codes)
{
    var fresh = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
    for (int i = 0; i < names.Count; i++)
    {
        fresh[names[i]] = codes[i];
    }
    _countries = fresh;   // one atomic swap
}
```

> "Readers always see a complete old or new version, with no locking on the read path. A lock or ReaderWriterLockSlim would also work, but they make every read pay for a rare nightly write."

**Follow-up:** Bonus: in .NET 8, FrozenDictionary for the snapshot, immutable and optimized for reads. Why volatile? So every thread sees the new reference right after the swap.

**[⬆ Back to Top](#table-of-contents)**

## 29. If the lookup is a Singleton, how can Reload create a new Dictionary?

*Screener follow-ups*

The **service** is the Singleton: one CountryLookup object, never replaced. Only the **data it holds** is replaced: its field points to a new Dictionary after the reload.

```csharp
CountryLookup (one object, same forever)
   _countries -> Dictionary #1
after Reload():
   _countries -> Dictionary #2   (#1 is discarded)
```

Picture a notice board: one board, and every night you pin up a new sheet instead of rewriting the old sheet while people read it.

**[⬆ Back to Top](#table-of-contents)**

## 30. IOptions vs IOptionsSnapshot vs IOptionsMonitor?

*Basics*

- **IOptions**: reads config once at startup, never changes. Singleton.
- **IOptionsSnapshot**: re-reads per request. Scoped, so not usable in a Singleton.
- **IOptionsMonitor**: always current (`CurrentValue`) plus `OnChange`. Singleton-safe, for background services.

**[⬆ Back to Top](#table-of-contents)**

## 31. Abstract class vs interface?

*Basics*

> "An interface is a contract with no state. An abstract class can hold shared code and fields. A class can implement many interfaces but inherit only one class."

**[⬆ Back to Top](#table-of-contents)**

## 32. const vs readonly?

*Basics*

> "const is fixed at compile time and baked into calling code. readonly is set once, at declaration or in the constructor, so it can hold runtime values."

**[⬆ Back to Top](#table-of-contents)**

## 33. class vs struct?

*Basics*

> "A class is a reference type on the heap. A struct is a value type copied on assignment, good for small immutable values like a point or an amount."

**[⬆ Back to Top](#table-of-contents)**

## 34. Why is string immutable, and when do you use StringBuilder?

*Basics*

> "Every change creates a new string. Concatenating in a loop creates thousands of throwaway strings; StringBuilder edits one buffer."

**[⬆ Back to Top](#table-of-contents)**

## 35. ref vs out?

*Basics*

> "Both pass by reference. ref must be initialised before the call; out must be assigned inside the method, like TryGetValue."

**[⬆ Back to Top](#table-of-contents)**

## 36. What does using do with IDisposable?

*Basics*

> "It guarantees Dispose() runs even if an exception happens, releasing connections and file handles immediately instead of waiting for the GC."

**[⬆ Back to Top](#table-of-contents)**

## 37. == vs Equals()?

*Basics*

> "For classes, == checks whether it's the same object unless overridden; string overrides it to compare text. Equals can be overridden for value equality, and records do it automatically."

**[⬆ Back to Top](#table-of-contents)**

## 38. Task vs Thread?

*Basics*

> "A Thread is an OS thread, which is expensive. A Task is a unit of work scheduled on the thread pool, lighter and awaitable. Modern code almost always uses Tasks."

**[⬆ Back to Top](#table-of-contents)**

## 39. virtual/override vs new?

*Basics*

> "override replaces the base behaviour even when called through a base reference. new only hides it, so calling through the base type still runs the base version."

**[⬆ Back to Top](#table-of-contents)**

## 40. Filters vs middleware?

*Basics*

> "Middleware wraps every request in the pipeline, even ones that never reach MVC. Filters run inside MVC around controllers and actions, so they know which action is running. Filters suit validation or action-level logging."

**[⬆ Back to Top](#table-of-contents)**

## 41. What are the MVC filter types, in order?

*Basics*

Authorization, Resource, Action, Exception, Result. Action filters are the ones you write most, to validate input or log timing.

**[⬆ Back to Top](#table-of-contents)**

## 42. How do model binding and validation work?

*Basics*

> "Model binding maps route, query, body and header values onto action parameters. Data annotations like [Required] or [Range] validate them, and with [ApiController] an invalid model automatically returns 400 with the errors."

**[⬆ Back to Top](#table-of-contents)**

## 43. [FromBody] vs [FromQuery] vs [FromRoute]?

*Basics*

Where the value comes from: the JSON body, the query string (`?page=2`), or the URL path (`/orders/{id}`).

**[⬆ Back to Top](#table-of-contents)**

## 44. What is Kestrel?

*Basics*

> "The cross-platform web server built into ASP.NET Core. In containers it serves traffic directly, usually behind a load balancer or ingress."

**[⬆ Back to Top](#table-of-contents)**

## 45. What is CORS?

*Basics*

> "Browsers block a page from calling an API on another domain unless the API allows it. CORS configures which origins, methods and headers are allowed. It's a browser protection, so server-to-server calls aren't affected."

**[⬆ Back to Top](#table-of-contents)**

## 46. Minimal APIs vs controllers?

*Basics*

> "Minimal APIs map endpoints directly in Program.cs with less ceremony, good for small services. Controllers suit larger APIs with filters, conventions and more structure."

**[⬆ Back to Top](#table-of-contents)**

## 47. Where does ASP.NET Core configuration come from, and in what order?

*Basics*

appsettings.json, then appsettings.{Environment}.json, then user secrets (dev), then environment variables, then command-line args. Later sources override earlier ones, which is why env vars and ConfigMaps override JSON in Kubernetes.

**[⬆ Back to Top](#table-of-contents)**

## 48. How do you log properly in .NET?

*Basics*

> "Inject ILogger<T> and use structured logging, like LogInformation("Order {OrderId} placed", orderId), not string concatenation, so tools like Datadog can search by OrderId. Add a correlation id to trace one request across services."

**[⬆ Back to Top](#table-of-contents)**

## 49. IActionResult vs ActionResult<T>?

*Basics*

> "ActionResult<T> lets you return either the data or a status result like NotFound(), and tells Swagger the response type. It's the modern default for APIs."

**[⬆ Back to Top](#table-of-contents)**

## 50. What is a correlation ID?

*Basics*

> "A unique ID created when a request first enters the system, usually at the gateway. It's passed in a header to every service the request touches and included in every log line, so in Datadog I can search one ID and see the whole journey of that request across services."

**Follow-up:** Answer from what you do daily. Describing your real usage IS the best answer.

**[⬆ Back to Top](#table-of-contents)**

## 51. Write a minimal API endpoint.

*Basics*

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddScoped<IOrderService, OrderService>();
var app = builder.Build();

app.MapGet("/orders/{id}", async (int id, IOrderService service) =>
{
    Order? order = await service.GetAsync(id);
    if (order == null)
        return Results.NotFound();
    return Results.Ok(order);
});

app.Run();
```

DI still works: services are injected straight into the handler's parameters.

**[⬆ Back to Top](#table-of-contents)**

## 52. How do you handle a question you haven't prepared?

*Basics*

1. **Start from the purpose:** "Filters exist so you can run code around an action without repeating it..."
1. **Connect to experience:** "We used an action filter to log request timing..."
1. **Reason out loud** about the uncertain part: "I believe X runs before Y, but I'd confirm in the docs."
1. **Be honest about the edge:** "I haven't gone deep on that, but based on how the pipeline works I'd expect..."

They grade how you think, not perfect recall.

**[⬆ Back to Top](#table-of-contents)**

## 53. Strategy pattern?

*Screener follow-ups*

> "Swap an algorithm at runtime behind one interface, like IShippingRateStrategy with an implementation per carrier. It removes big if/else chains."

**[⬆ Back to Top](#table-of-contents)**

## 54. Decorator pattern?

*Screener follow-ups*

> "Wrap an object to add behaviour without changing it, like a caching or logging wrapper around a repository with the same interface. Polly's retry around HttpClient is the same idea."

**[⬆ Back to Top](#table-of-contents)**

## 55. Mediator / MediatR / CQRS?

*Screener follow-ups*

> "Controllers send a command or query object and one handler processes it, keeping controllers thin. CQRS separates writes (commands) from reads (queries) so each can be optimised, like reads from a replica or cache."

**[⬆ Back to Top](#table-of-contents)**

## 56. Observer pattern?

*Screener follow-ups*

> "Subscribers are notified when something changes. C# events are the built-in form; Kafka consumers are the distributed version of the same idea."

**[⬆ Back to Top](#table-of-contents)**

## 57. Singleton pattern?

*Screener follow-ups*

> "One instance for the whole app. In modern .NET I register it with AddSingleton and let DI manage it, which keeps it testable. Hand-written, I'd use Lazy<T> for thread-safe initialisation."

**[⬆ Back to Top](#table-of-contents)**

## 58. Find the first non-repeating character in a string (e.g. "swiss" gives 'w'). No LINQ.

*Screener follow-ups*

**With library:** `char? first = text.GroupBy(c => c).Where(g => g.Count() == 1).Select(g => (char?)g.Key).FirstOrDefault();` GroupBy keeps first-appearance order, so this finds the first. O(n).

**Without library:**

```csharp
public static char? FirstNonRepeating(string text)
{
    var counts = new Dictionary<char, int>();

    foreach (char c in text)            // pass 1: count
    {
        if (counts.ContainsKey(c))
            counts[c]++;
        else
            counts[c] = 1;
    }

    foreach (char c in text)            // pass 2: first with count 1
    {
        if (counts[c] == 1)
            return c;
    }

    return null;
}
```

> "Brute force compares every pair, O(n squared). I count each character in a Dictionary in one pass, then walk the string again in order and return the first with a count of 1. O(n) time; space is the number of distinct characters."

**Follow-up:** Pattern: two nested loops to find repeats means reach for a Dictionary to count. Brute-force traps: compare chars[i] == chars[j], not i == j; check ALL other positions, not only later ones ('aab' should give 'b').

**[⬆ Back to Top](#table-of-contents)**

## 59. An array holds 1 to 100 with one number missing, in any order. Find it. No built-ins.

*Screener follow-ups*

**With library:** `int missing = Enumerable.Range(1, n).Except(numbers).First();` Or with the formula: `n * (n + 1) / 2 - numbers.Sum()`.

**Progression to say out loud:**

1. Sort, then scan: O(n log n).
1. HashSet: add all, then check 1 to n for the one not contained. O(n) time, O(n) space.
1. **Sum formula**: O(n) time, **O(1)** space. The best.

```csharp
public static int FindMissing(int[] numbers, int n)
{
    int expectedSum = n * (n + 1) / 2;    // 5050 for 100

    int actualSum = 0;
    foreach (int number in numbers)
    {
        actualSum += number;
    }

    return expectedSum - actualSum;
}
```

**HashSet version** (fine to lead with):

```csharp
int n = numbers.Length + 1;
var seen = new HashSet<int>();
foreach (int number in numbers)
{
    seen.Add(number);
}
for (int i = 1; i <= n; i++)
{
    if (!seen.Contains(i))
        return i;
}
```

> "1 to n always adds up to n(n+1)/2. I sum what's actually there, and the difference is the missing number. O(n) time, O(1) space."

**Follow-up:** Is n*(n+1)/2 safe with int division? Yes: it multiplies first (100*101 = 10100) then halves, and n*(n+1) is always even. If n isn't given, n = numbers.Length + 1. The formula is a trick; the HashSet answer is a perfectly good interview answer. Overflow for huge n: use long.

**[⬆ Back to Top](#table-of-contents)**

## 60. Two-sum: return the indexes of the two numbers that add up to a target.

*Screener follow-ups*

**With library:** there's no built-in for two-sum; the Dictionary one-pass IS the standard answer.

```csharp
public static int[]? TwoSum(int[] nums, int target)
{
    var seen = new Dictionary<int, int>();     // number -> index

    for (int i = 0; i < nums.Length; i++)
    {
        int partner = target - nums[i];

        if (seen.ContainsKey(partner))
            return new int[] { seen[partner], i };

        seen[nums[i]] = i;                     // store THIS number
    }

    return null;
}
```

> "Brute force checks every pair, O(n squared). One pass with a Dictionary from number to index: for each number I check whether its partner, target minus the number, was already seen. O(n) time, O(n) space."

**Follow-up:** Common bug: storing the partner and searching for the partner. Store the number, search for the partner. Why for, not foreach? You need the index. Why check before adding? A number can't pair with itself, and [3,3] target 6 still works.

**[⬆ Back to Top](#table-of-contents)**

## 61. Reverse the words in a sentence ("I love coding" gives "coding love I"). No Split, no Reverse.

*Screener follow-ups*

```csharp
public static string ReverseWords(string sentence)
{
    var result = new StringBuilder();
    int wordEnd = sentence.Length;

    for (int i = sentence.Length - 1; i >= 0; i--)
    {
        if (sentence[i] == ' ')
        {
            result.Append(sentence.Substring(i + 1, wordEnd - (i + 1)));
            result.Append(' ');
            wordEnd = i;
        }
    }

    result.Append(sentence.Substring(0, wordEnd));   // first word
    return result.ToString();
}
```

**Your order:** 1) "Simplest: Split by space, swap words from both ends, Join. O(n)." 2) If he says no Split, use your own words:

> "Walk backwards and check for a space. When I find one, take the substring from space + 1 up to the end of the current word, then move the end to that space and repeat. The first word is left at the end. O(n), with a StringBuilder."

**Follow-up:** Lead with the practical version: string.Join(" ", sentence.Split(' ').Reverse()), which is O(n) (three single passes, no nested loop). If no built-ins: Split, then swap words with two pointers (like the 0/1 problem), then Join. Reverse the word ORDER only, not the letters. Traps: i > 0 skips index 0; string += in a loop is O(n squared).

**[⬆ Back to Top](#table-of-contents)**

## 62. Return all numbers that appear more than once ([4,3,2,7,8,2,3,1] gives [2,3]).

*Screener follow-ups*

**With library:** `numbers.GroupBy(n => n).Where(g => g.Count() > 1).Select(g => g.Key).ToList();` GroupBy puts equal numbers together; keep groups with more than one item.

**Without library** (O(n) time, O(n) space):

```csharp
var counts = new Dictionary<int, int>();
foreach (int n in numbers)
{
    if (counts.ContainsKey(n))
        counts[n]++;
    else
        counts[n] = 1;
}

var duplicates = new List<int>();
foreach (KeyValuePair<int, int> pair in counts)
{
    if (pair.Value > 1)
        duplicates.Add(pair.Key);
}
return duplicates;
```

> "Count each number in a Dictionary, then collect the ones with a count above 1. I return a List because I don't know the size in advance."

**Follow-up:** foreach over a Dictionary gives KeyValuePair items: use pair.Key and pair.Value.

**[⬆ Back to Top](#table-of-contents)**

## 63. What does string.Join do?

*Basics*

Takes every element of a collection and puts the separator BETWEEN them (not at the ends).

```csharp
string.Join(" ", new[] { "coding", "love", "I" })   // "coding love I"
string.Join(", ", new[] { "a", "b", "c" })           // "a, b, c"
```

**[⬆ Back to Top](#table-of-contents)**

## 64. What does GroupBy actually return? Visualise it.

*Basics*

Buckets, not counts. Each group has a **Key** plus the **items** in it, like Dictionary<key, List<items>>.

```csharp
[4, 3, 2, 7, 8, 2, 3, 1].GroupBy(n => n)

Key 4 -> [4]
Key 3 -> [3, 3]
Key 2 -> [2, 2]
Key 7 -> [7]
Key 8 -> [8]
Key 1 -> [1]

.Where(g => g.Count() > 1)   -> Key 3 [3,3], Key 2 [2,2]
.Select(g => g.Key)          -> 3, 2
.ToList()                    -> [3, 2]   (runs HERE: deferred execution)
```

Group by anything: `trades.GroupBy(t => t.Symbol).Select(g => new { Symbol = g.Key, Total = g.Sum(t => t.Quantity) })` gives total quantity per stock.

**Follow-up:** Count isn't stored; g.Count() counts the items in the bucket. In Tony's interview: lead with LINQ, then have the Dictionary loop ready for 'now without LINQ'.

**[⬆ Back to Top](#table-of-contents)**

## 65. Write a basic API controller.

*Basics*

```csharp
[ApiController]
[Route("api/orders")]
public class OrdersController : ControllerBase
{
    private readonly IOrderService _service;
    public OrdersController(IOrderService service) { _service = service; }

    [HttpGet("{id}")]
    public async Task<ActionResult<Order>> Get(int id)
    {
        Order? order = await _service.GetAsync(id);
        if (order == null) return NotFound();
        return Ok(order);
    }
}
```

**[⬆ Back to Top](#table-of-contents)**

## 66. Write a custom middleware.

*Basics*

```csharp
public class CorrelationIdMiddleware
{
    private readonly RequestDelegate _next;
    public CorrelationIdMiddleware(RequestDelegate next) { _next = next; }

    public async Task InvokeAsync(HttpContext context)
    {
        string id = context.Request.Headers["X-Correlation-ID"].FirstOrDefault() ?? Guid.NewGuid().ToString();
        context.Response.Headers["X-Correlation-ID"] = id;
        await _next(context);      // pass to the next middleware
    }
}
// Program.cs: app.UseMiddleware<CorrelationIdMiddleware>();
```

Shape: constructor takes next; InvokeAsync does its work, then awaits _next(context).

**[⬆ Back to Top](#table-of-contents)**

## 67. Walk me through a layered API: controller, service, repository, ORM. What goes where?

*Screener follow-ups*

```csharp
HTTP request
  OrdersController  -> HTTP only: routes, status codes. No logic.
  OrderService      -> BUSINESS LOGIC: rules, calculations, decisions
  OrderRepository   -> DATA ACCESS only: queries, saving
  AppDbContext      -> the ORM (EF Core): C# to SQL
  SQL Server
```

> "The controller handles HTTP, the service holds the business rules, the repository does data access through EF Core, and each depends on the interface below it, registered as Scoped in DI."

Why: one job per layer (S), depend on interfaces (D), and the service is unit-testable by mocking the repository.

**Follow-up:** Why Scoped? The DbContext is Scoped (one per request), so whatever holds it must be Scoped too. A Singleton holding it is a captive dependency. Files: Dockerfile (not YAML), Kubernetes and azure-pipelines are YAML, appsettings is JSON.

**[⬆ Back to Top](#table-of-contents)**

## 68. Show the code for each layer of a repository-pattern API.

*Screener follow-ups*

```csharp
// Order.cs (entity = table)
public class Order
{
    public int Id { get; set; }
    public string AccountId { get; set; } = "";
    public string Symbol { get; set; } = "";
    public int Quantity { get; set; }
    public string Status { get; set; } = "Pending";
}

// PlaceOrderRequest.cs (DTO)
public class PlaceOrderRequest
{
    [Required] public string AccountId { get; set; } = "";
    [Required] public string Symbol { get; set; } = "";
    [Range(1, 1000000)] public int Quantity { get; set; }
}

// AppDbContext.cs (ORM)
public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }
    public DbSet<Order> Orders { get; set; }
}

// OrderRepository.cs (data access only)
public class OrderRepository : IOrderRepository
{
    private readonly AppDbContext _db;
    public OrderRepository(AppDbContext db) { _db = db; }

    public async Task<Order?> GetByIdAsync(int id)
    {
        return await _db.Orders.FirstOrDefaultAsync(o => o.Id == id);
    }
    public async Task AddAsync(Order order) { await _db.Orders.AddAsync(order); }
    public async Task SaveChangesAsync() { await _db.SaveChangesAsync(); }
}

// OrderService.cs (business logic)
public class OrderService : IOrderService
{
    private readonly IOrderRepository _repo;
    public OrderService(IOrderRepository repo) { _repo = repo; }

    public async Task<Order?> GetAsync(int id) { return await _repo.GetByIdAsync(id); }

    public async Task<Order> PlaceAsync(PlaceOrderRequest request)
    {
        // business rules: buying power, market hours, limits...
        var order = new Order
        {
            AccountId = request.AccountId,
            Symbol = request.Symbol.ToUpper(),
            Quantity = request.Quantity,
            Status = "Pending"
        };
        await _repo.AddAsync(order);
        await _repo.SaveChangesAsync();
        return order;
    }
}

// OrdersController.cs (HTTP only)
[ApiController]
[Route("api/orders")]
public class OrdersController : ControllerBase
{
    private readonly IOrderService _service;
    public OrdersController(IOrderService service) { _service = service; }

    [HttpGet("{id}")]
    public async Task<ActionResult<Order>> Get(int id)
    {
        Order? order = await _service.GetAsync(id);
        if (order == null) return NotFound();
        return Ok(order);
    }

    [HttpPost]
    public async Task<ActionResult<Order>> Place(PlaceOrderRequest request)
    {
        Order order = await _service.PlaceAsync(request);
        return CreatedAtAction(nameof(Get), new { id = order.Id }, order);
    }
}

// Program.cs
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("Default")));
builder.Services.AddScoped<IOrderRepository, OrderRepository>();
builder.Services.AddScoped<IOrderService, OrderService>();
builder.Services.AddControllers();
```

**[⬆ Back to Top](#table-of-contents)**

## 69. QUICK REFERENCE: Tony's screener questions in one table.

*Screener follow-ups*

> "Sorted means halve the range. Each element visited once, in place. Two lists means an O(n) scan per lookup and can drift out of sync. NuGet is for other solutions."

**[⬆ Back to Top](#table-of-contents)**

## 70. QUICK REFERENCE: repeats, counts and pairs means Dictionary or HashSet.

*Screener follow-ups*

**Rule:** nested loops looking for repeats or pairs means reach for a Dictionary. Say the Big-O before he asks.

**[⬆ Back to Top](#table-of-contents)**

## 71. Walk me through a full API request: middleware, filter, controller, service, cache, repository, EF.

*Screener follow-ups*

```csharp
HTTP request
  ExceptionHandlingMiddleware   catches any crash -> clean 500 (ProblemDetails)
  CorrelationIdMiddleware       request ID in every log line + response header
  Routing -> OrdersController
    [ApiController]             invalid DTO -> automatic 400
    TimingActionFilter          times the action
      OrdersController          HTTP only: 200 / 201 / 404 / 409 / 422
        OrderService            BUSINESS LOGIC + cache-aside (IDistributedCache)
          OrderRepository       DATA ACCESS only
            AppDbContext        EF Core -> database
```

**Program.cs order:** register (Configure<OrderSettings>, AddDbContext, AddDistributedMemoryCache, AddScoped repo + service, AddControllers with the global filter), then pipeline: exception middleware FIRST, correlation id, (authentication, authorization), MapControllers.

**Cache:** Get = cache-aside with a TTL; Cancel = update DB then delete the key. Redis is one line: AddStackExchangeRedisCache; the service doesn't change because it depends on IDistributedCache.

**Rules:** predictable business conditions return a result (422/409), not exceptions; exceptions are for the unexpected (500).

Runnable: `C:GitHubPrepSampleApi`, `dotnet run`. The log shows cache miss ~45 ms vs hit ~1 ms.

**Follow-up:** Why exception middleware first? It must wrap everything after it to catch any crash. Filter vs middleware: the filter knows which action runs; middleware wraps every request.

**[⬆ Back to Top](#table-of-contents)**

## 72. class Foo<T> { public static int bar; } Foo<int>.bar++; what does Foo<double>.bar print?

*Snippets*

```csharp
class Foo<T> { public static int bar; }

Foo<int>.bar++;
Console.WriteLine(Foo<double>.bar);   // 0
Console.WriteLine(Foo<int>.bar);      // 1
```

> "It prints 0. Each closed generic type, Foo<int>, Foo<double>, is a separate type at runtime with its own copy of every static field."

**Follow-up:** Not about reference vs value types: Foo and Foo also have separate statics. Used on purpose as a per-type cache: static class Cache { public static T Value; }.

**[⬆ Back to Top](#table-of-contents)**

## 73. Static constructor, instance constructor and Print(): what's the output of new Test().Print()?

*Snippets*

```csharp
class Test
{
    static Test() { Console.WriteLine("Static constructor"); }
    public Test() { Console.WriteLine("Instance constructor"); }
    public void Print() { Console.WriteLine("Print"); }
}

var t = new Test();
t.Print();
// Static constructor
// Instance constructor
// Print
```

> "The static constructor runs once, automatically, before the type is first used; then the instance constructor on each new; then the method. A second new Test() prints only 'Instance constructor'."

**Follow-up:** With inheritance: static ctors run derived first, then base; instance ctors run base first, then derived.

**[⬆ Back to Top](#table-of-contents)**

## 74. Main calls an async method (with await Task.Delay) WITHOUT awaiting, then prints the value. What happens?

*Snippets*

```csharp
static async Task<int> GetValueAsync()
{
    await Task.Delay(1000);
    return 42;
}

// A: no await, print the returned Task
var result = GetValueAsync();
Console.WriteLine(result);     // System.Threading.Tasks.Task`1[System.Int32]

// B: method sets a variable after the delay, Main prints it without awaiting
LoadAsync();
Console.WriteLine(value);      // 0 (default)

// C: correct
int r = await GetValueAsync(); // 42, after 1 second
```

> "Inside the method, code after await Task.Delay always runs, after the delay; await pauses the method, not the thread. Without an await in the caller, Main carries on immediately: it prints the Task's type name, or a default value. It doesn't throw; you get the wrong output. In a console app the rest may never run if Main exits first. Fix: async Task Main and await."

**Follow-up:** The trap is saying it will fail: it prints the wrong value, it does not throw. It's the runtime that moves on, not the compiler.

**[⬆ Back to Top](#table-of-contents)**

## 75. Why use Kafka instead of calling the other service's API?

*Kafka*

> "Decoupling. The producer writes once and doesn't need to know who's listening or whether they're up. If a consumer is down, messages wait in Kafka and it catches up later. New consumers like audit or analytics can be added without touching the producer."

**[⬆ Back to Top](#table-of-contents)**

## 76. Explain topics, partitions, offsets and consumer groups.

*Kafka*

- **Topic**: a named stream, like `orders`.
- **Partition**: a topic is split into ordered logs for parallelism. On disk each is a folder of log segments.
- **Offset**: a message's position within a partition.
- **Consumer group**: consumers sharing the work. Each partition goes to one consumer in the group.

Messages stay until retention removes them. Reading doesn't delete them.

**[⬆ Back to Top](#table-of-contents)**

## 77. How do you keep one account's Buy and Cancel in order?

*Kafka*

> "Kafka only guarantees order within a partition. I use AccountId as the message key, and the same key always goes to the same partition, so each account's events stay in order while different accounts are processed in parallel."

**Follow-up:** Without a key, Cancel could be processed before Buy.

**[⬆ Back to Top](#table-of-contents)**

## 78. A consumer processes a message but crashes before committing the offset.

*Kafka*

> "After restart it resumes from the last committed offset, so that message is delivered again. That's at-least-once delivery. The consumer must be idempotent: store processed message ids with a unique constraint and skip duplicates."

**Follow-up:** Commit after processing, not before. Committing first risks losing the message if you crash mid-processing.

**[⬆ Back to Top](#table-of-contents)**

## 79. Why add a version number to events if Kafka keeps order?

*Kafka*

> "Kafka only guarantees order within a partition. Retries, replays or a second producer can still deliver an older update late. With a version, the consumer ignores anything older than what it already has."

Example: v2 (stock 8) arrives, then v1 (stock 10) arrives late. The consumer already has v2, so it ignores v1. Without the version, stock jumps back to 10 and you oversell.

**Follow-up:** The version must be assigned by the owner of the data, such as a counter in the inventory database. Versions invented by different producers can't be compared.

**[⬆ Back to Top](#table-of-contents)**

## 80. Two consumers in the same group vs in different groups?

*Kafka*

> "Same group: they split the partitions, which is load balancing. Different groups: each gets every message, which is broadcast, like an order service and an audit service both reading all orders."

**[⬆ Back to Top](#table-of-contents)**

## 81. What's a dead-letter queue and when do you use it?

*Kafka*

> "When a message keeps failing because of bad data or a bug, I don't retry forever and block the partition. After N retries I move it to a dead-letter topic, alert, and keep processing. Someone fixes the cause and replays it."

**[⬆ Back to Top](#table-of-contents)**

## 82. What's a rebalance?

*Kafka*

> "When a consumer joins or leaves a group, Kafka reassigns partitions. Processing pauses briefly, and uncommitted messages may be reprocessed, which is another reason consumers must be idempotent."

**[⬆ Back to Top](#table-of-contents)**

## 83. Kafka vs a queue like MQ, RabbitMQ or Service Bus?

*Kafka*

> "In a queue a message is removed once consumed and goes to one receiver. Kafka is a log: messages stay for the retention period, many groups read independently, and you can replay from an older offset. Queues fit commands and task distribution; Kafka fits event streams and high throughput."

**[⬆ Back to Top](#table-of-contents)**

## 84. Can more consumers than partitions make it faster?

*Kafka*

> "No. Each partition is read by one consumer per group, so extra consumers sit idle. The partition count is the maximum parallelism, so size it for future load."

**[⬆ Back to Top](#table-of-contents)**

## 85. Is exactly-once delivery possible?

*Kafka*

> "Inside Kafka, yes, with an idempotent producer and transactions. End to end across a database and external systems it's rare, so in practice teams build at-least-once delivery plus idempotent consumers. The result is effectively-once processing."

**[⬆ Back to Top](#table-of-contents)**

## 86. Explain the transactional outbox pattern.

*Kafka*

> "Writing to the database and publishing to Kafka are two separate systems, so one can succeed while the other fails. With an outbox, I write the business row and an outbox row in the same database transaction. A background worker publishes pending outbox rows and marks them sent. Nothing is lost if Kafka is down or the service crashes; delivery is at-least-once, so consumers are idempotent."

**[⬆ Back to Top](#table-of-contents)**

## 87. How do you implement caching with Redis?

*Redis*

**Cache-aside**, the most common pattern:

1. Read: check Redis. On a hit, return it.
1. On a miss, read from SQL, store it in Redis with a TTL, return it.
1. On a write: update SQL, then **delete** the cache key.

In .NET: `IDistributedCache` or `StackExchange.Redis`. In .NET 9+, `HybridCache` adds an in-memory layer and stampede protection.

**[⬆ Back to Top](#table-of-contents)**

## 88. How do you choose TTLs?

*Redis*

> "By how stale the data is allowed to be. Data that changes often gets a short TTL, around 5 minutes. Reference data that rarely changes gets an hour or more. I add a little random jitter so thousands of keys don't expire at the same moment."

**Follow-up:** First question to ask in any caching discussion: how stale can this data be? That drives the whole design.

**[⬆ Back to Top](#table-of-contents)**

## 89. How do you invalidate the cache when data changes?

*Redis*

> "On write, I update the database, then delete the key. The next read fetches fresh data. I delete rather than update the cached value, because two concurrent writers could otherwise leave a stale value in the cache. The TTL is a safety net. When another service changes the data, it publishes an event and our consumer evicts the key."

**[⬆ Back to Top](#table-of-contents)**

## 90. What's a cache stampede, and how do you prevent it?

*Redis*

> "A popular key expires and hundreds of requests miss at once, so they all hit the database together. I let one request rebuild the value while the others wait for its result, using a lock or request coalescing. I also add TTL jitter and refresh hot keys before they expire. HybridCache in .NET does the coalescing for you."

**[⬆ Back to Top](#table-of-contents)**

## 91. Redis goes down. What happens to your API?

*Redis*

> "The cache must be optional. Redis calls get short timeouts, and a failure falls back to the database. A circuit breaker stops us waiting on Redis for every call while it's down. Because the database suddenly takes all the load, I protect it with rate limiting, and monitoring alerts the team."

**[⬆ Back to Top](#table-of-contents)**

## 92. In a trading platform, where would you use Redis, and what would you never trust a cache for?

*Redis*

**Rule: Redis for display, the source of truth for decisions.**

> "I'd use Redis for data that's read constantly where a tiny delay is fine: user profiles and preferences, reference data like instrument details, and live quotes for display, which the market data feed pushes into Redis on every tick so it's always current.

> What I'd never rely on a cache for is anything that moves money: buying power and balances when approving an order, positions when checking whether a client can sell, and order status transitions. Those come from the source of truth, and the execution price comes from the market at trade time, not a cached quote."

**Follow-up:** Common mistake: saying you'd never cache stock prices. Live quotes are a classic Redis use; the point is not to make trading decisions from them. Holdings can be cached for the portfolio screen, invalidated by fill events, but the sell check reads the database.

**[⬆ Back to Top](#table-of-contents)**

## 93. Why shouldn't Redis be the source of truth for an account balance?

*Redis*

> "A cache can be stale, evicted under memory pressure, or lose recent writes on failover. You can't approve a trade against a stale balance. SQL is the source of truth; Redis only speeds up reads where slightly old data is acceptable."

**[⬆ Back to Top](#table-of-contents)**

## 94. IMemoryCache vs Redis?

*Redis*

> "IMemoryCache lives inside one app instance: fastest, but each pod has its own copy and they can disagree. Redis is shared by all instances, so every pod sees the same data and the cache survives restarts. With several pods on Kubernetes, I use Redis, sometimes with a small in-memory layer in front."

**[⬆ Back to Top](#table-of-contents)**

## 95. What else is Redis used for besides caching?

*Redis*

- Sessions shared across instances
- Rate limiting with counters and expiry
- Distributed locks
- Sorted sets for leaderboards and rankings
- Pub/sub, for example as a SignalR backplane

**[⬆ Back to Top](#table-of-contents)**

## 96. What happens when Redis runs out of memory?

*Redis*

> "It evicts keys according to its maxmemory policy. allkeys-lru removes the least recently used keys; volatile-lru only removes keys that have a TTL. For a cache I'd use an LRU policy, always set TTLs, and monitor memory and hit rate."

**[⬆ Back to Top](#table-of-contents)**

## 97. Transient vs Scoped vs Singleton?

*.NET core*

- **Transient**: new instance every time. Lightweight stateless helpers.
- **Scoped**: one per HTTP request. DbContext, current user.
- **Singleton**: one for the app. Config, caches, Kafka producers.

**Follow-up:** Transient DbContext bug: two repositories get two DbContexts, so one SaveChanges doesn't include the other's changes.

**[⬆ Back to Top](#table-of-contents)**

## 98. Why can't you inject a Scoped service into a Singleton?

*.NET core*

> "The Singleton lives forever and keeps the Scoped DbContext it got from the first request. Every later request, on different threads, shares that one DbContext, which isn't thread-safe. It's a captive dependency. The fix is IServiceScopeFactory: create a scope when you need the DbContext."

**Follow-up:** Real example: a BackgroundService (always a Singleton) like an outbox worker creating a scope per batch.

**[⬆ Back to Top](#table-of-contents)**

## 99. How do you keep a Singleton thread-safe?

*.NET core*

> "Best is no mutable state. If it must hold state: ConcurrentDictionary for shared lookups, lock when several fields change together, Interlocked for counters. The danger is check-then-act: two threads both check 'not there' and both add."

**Follow-up:** count++ is read, add, write. Two threads both read 5 and both write 6, so an update is lost. That's a race condition.

**[⬆ Back to Top](#table-of-contents)**

## 100. What does async/await actually do? Does it create a thread?

*.NET core*

> "It doesn't create a thread. At an await on I/O, the thread goes back to the pool to serve other requests. When the I/O completes, a pool thread continues the method. That's how a server handles many more requests with the same threads."

**[⬆ Back to Top](#table-of-contents)**

## 101. Why is async void dangerous?

*.NET core*

> "It can't be awaited, so the caller doesn't know when it finishes, and an exception can crash the process because nothing can catch it. Always return Task. The only exception is event handlers."

**[⬆ Back to Top](#table-of-contents)**

## 102. What's wrong with .Result or .Wait()?

*.NET core*

> "It blocks a thread while waiting, which throws away the benefit of async and can cause thread-pool starvation. In older ASP.NET and UI apps it can deadlock. Go async all the way."

**[⬆ Back to Top](#table-of-contents)**

## 103. How do you run three independent calls in parallel?

*.NET core*

> "Start all three tasks, then await Task.WhenAll. Total time is the slowest call, not the sum."

**[⬆ Back to Top](#table-of-contents)**

## 104. Process 1000 messages, max 10 at a time, and start the next as soon as one finishes. How?

*.NET core*

**Batches of 10 (underutilized):** each batch waits for its slowest message.

```csharp
foreach (var batch in messages.Chunk(10))
{
    await Task.WhenAll(batch.Select(m => ProcessAsync(m)));
}
```

**SemaphoreSlim: always 10 in flight, next starts immediately:**

```csharp
var gate = new SemaphoreSlim(10);

var tasks = messages.Select(async m =>
{
    await gate.WaitAsync();          // take a slot
    try
    {
        await ProcessAsync(m);
    }
    finally
    {
        gate.Release();              // free it, even on error
    }
});

await Task.WhenAll(tasks);
```

**.NET 6+, simplest:**

```csharp
var options = new ParallelOptions { MaxDegreeOfParallelism = 10 };
await Parallel.ForEachAsync(messages, options, async (m, ct) =>
{
    await ProcessAsync(m);
});
```

> "Batching with WhenAll wastes slots because each batch waits for its slowest message. A SemaphoreSlim with 10 slots keeps 10 in flight: each message takes a slot and releases it in a finally, so the next starts as soon as one finishes. Parallel.ForEachAsync with MaxDegreeOfParallelism = 10 does the same more simply."

**Follow-up:** Kafka: parallel processing breaks per-key ordering, so parallelise across keys or partitions, not within one.

**[⬆ Back to Top](#table-of-contents)**

## 105. Why use IHttpClientFactory?

*.NET core*

> "A new HttpClient per request exhausts sockets, because closed connections sit in TIME_WAIT. A single static client never picks up DNS changes. IHttpClientFactory pools and recycles handlers, so you avoid both problems."

**[⬆ Back to Top](#table-of-contents)**

## 106. IEnumerable vs IQueryable?

*.NET core*

> "IQueryable builds an expression that EF translates to SQL, so filtering happens in the database. IEnumerable works in memory on data already loaded. Calling ToList too early loads the whole table and filters in C#."

**Follow-up:** Deferred execution: building the query does nothing. It runs at ToList, First, Count or foreach.

**[⬆ Back to Top](#table-of-contents)**

## 107. What is middleware in ASP.NET Core?

*.NET core*

> "The request passes through an ordered pipeline of components: exception handling, authentication, authorization, logging. Each can act before and after the next one. Order matters: authentication before authorization. I've written custom middleware for correlation ids and global error handling."

**[⬆ Back to Top](#table-of-contents)**

## 108. How do you handle exceptions globally in an API?

*.NET core*

> "One place, not try/catch everywhere: exception-handling middleware, or IExceptionHandler in .NET 8. It logs the error with a correlation id and returns a consistent ProblemDetails response without leaking stack traces. Predictable conditions like 'not found' are handled explicitly, not with exceptions."

**[⬆ Back to Top](#table-of-contents)**

## 109. How do you reduce memory allocations on large data?

*.NET core*

- Stream data instead of loading everything into memory.
- `Span` / `ReadOnlySpan` to slice strings and arrays without copying.
- `StringBuilder` instead of string concatenation in loops.
- `ArrayPool` to reuse buffers.

Fewer allocations mean less GC work and fewer pauses.

**Follow-up:** GC basics: generations 0, 1, 2. Most objects die young in Gen 0. Objects over 85 KB go to the Large Object Heap, which is expensive to collect.

**[⬆ Back to Top](#table-of-contents)**

## 110. record vs class?

*.NET core*

> "A record has value equality (two records with the same data are equal) and is immutable by default, which makes it good for DTOs and events. A class has reference equality and is the choice for entities with behaviour and changing state."

**[⬆ Back to Top](#table-of-contents)**

## 111. What's the N+1 problem? How do you fix it?

*EF Core & SQL*

> "One query loads a list, then one extra query runs per item inside a loop: 100 orders become 101 database trips. Fix with Include, which loads the related data in the same query, or a Select projection when I only need a few fields."

**[⬆ Back to Top](#table-of-contents)**

## 112. What does AsNoTracking do, and when does it hurt?

*EF Core & SQL*

> "Normally EF keeps a copy of each loaded entity's original values and compares them on SaveChanges to generate updates. AsNoTracking skips that: faster and less memory, ideal for read-only queries. It hurts if you then change the entity and call SaveChanges, because nothing is saved."

**[⬆ Back to Top](#table-of-contents)**

## 113. Two users update the same balance at once. How do you stop a lost update?

*EF Core & SQL*

> "Optimistic concurrency. A rowversion column ([Timestamp] in EF). The update includes WHERE RowVersion = the value I read. If someone saved first, 0 rows are updated and EF throws DbUpdateConcurrencyException. I reload and retry, or tell the user."

**Follow-up:** Pessimistic alternative: lock the row when reading. Safer under heavy contention but blocks others.

**[⬆ Back to Top](#table-of-contents)**

## 114. How do you deploy database changes safely?

*EF Core & SQL*

> "EF Core migrations, reviewed in the PR like code. For production I generate an idempotent SQL script with dotnet ef migrations script --idempotent, and the pipeline or a DBA runs it. I don't let the app migrate itself on startup: several instances would race, and it would need admin permissions."

**[⬆ Back to Top](#table-of-contents)**

## 115. Clustered vs nonclustered index? What's a key lookup?

*EF Core & SQL*

> "The clustered index is the table itself, stored in key order, so there's one. A nonclustered index is a separate sorted copy of some columns with a pointer back to the row. If the query needs a column that isn't in the index, SQL jumps back to the table for every row: a key lookup. A covering index with INCLUDE removes it."

**[⬆ Back to Top](#table-of-contents)**

## 116. Why would SQL Server ignore an index you created?

*EF Core & SQL*

> "If the query matches many rows, thousands of key lookups cost more than one scan of the table, so the optimizer scans instead. There's no fixed percentage; it's a cost estimate and often a small fraction of rows. A covering index fixes it."

**Follow-up:** Every index slows inserts and updates and uses storage, so index the frequent, important queries, not everything.

**[⬆ Back to Top](#table-of-contents)**

## 117. What's parameter sniffing?

*EF Core & SQL*

> "SQL builds a plan using the first parameter value it sees and reuses it. If the first call returned 10 rows, the plan suits small results, and a later call returning a million rows reuses that bad plan. The sign is: fast in SSMS, slow in the app. Fixes: OPTION (RECOMPILE), OPTIMIZE FOR, or a covering index."

**[⬆ Back to Top](#table-of-contents)**

## 118. Two orders try to reserve the last unit at the same moment. How do you stop both succeeding?

*EF Core & SQL*

An **atomic conditional update**: the check and the change in ONE statement.

```sql
UPDATE Stock SET Qty = Qty - 1
WHERE Sku = @sku AND Qty >= 1
```

- Order A locks the row, sees Qty 1, sets it to 0 and commits: 1 row updated.
- Order B waited on the lock, then sees Qty 0: 0 rows updated, so it's out of stock.

> "If 0 rows are updated, the reservation failed. The check and the change can't be separated, so two orders can't both win."

**Follow-up:** The unsafe version: read Qty in C#, check it, then write. Both orders read 1 and both write 0, like count++. The gap between read and write is the bug.

**[⬆ Back to Top](#table-of-contents)**

## 119. Does SQL Server lock rows by itself?

*EF Core & SQL*

> "Yes, automatically. An UPDATE, INSERT or DELETE takes an exclusive lock on the rows it changes and holds it until the transaction commits. Anyone else changing those rows waits, and under the default Read Committed, readers wait too, so nobody sees a half-finished change. That's why a single conditional UPDATE is atomic."

**[⬆ Back to Top](#table-of-contents)**

## 120. How do you prevent deadlocks in money transfers?

*EF Core & SQL*

> "A deadlock is a circle: A holds account 1 and wants 2, B holds 2 and wants 1. I always lock in the same order, lower account id first, so a circle can't form; the second transfer just waits. I also keep transactions short. To diagnose, I read the deadlock graph from Extended Events."

**[⬆ Back to Top](#table-of-contents)**

## 121. Add a NOT NULL column to a 50-million-row table without downtime.

*EF Core & SQL*

1. Add it as nullable. Instant, metadata only.
1. Deploy code that always writes the new column.
1. Backfill old rows in batches of a few thousand so locks stay short.
1. Switch the column to NOT NULL.

**[⬆ Back to Top](#table-of-contents)**

## 122. Where should business logic live: stored procedures or C#?

*EF Core & SQL*

> "In the application layer. There it's unit-testable, version-controlled, debuggable, and scales by adding app instances instead of loading the database. Stored procedures still make sense for heavy set-based data work close to the data. I've seen the opposite: thousands of lines of nested PL/SQL that nobody could safely change."

**[⬆ Back to Top](#table-of-contents)**

## 123. Isolation levels, in one breath.

*EF Core & SQL*

> "The default is Read Committed: you only see committed data, but readers can wait on writers. Read Committed Snapshot lets readers see the last committed version without blocking. Serializable is safest but blocks most. For balances I prefer short transactions plus optimistic concurrency."

**[⬆ Back to Top](#table-of-contents)**

## 124. SQL: types of JOIN?

*EF Core & SQL*

> "INNER returns only matching rows. LEFT returns everything from the left with NULLs where there's no match. RIGHT is the mirror. FULL returns everything from both. CROSS gives every combination."

**[⬆ Back to Top](#table-of-contents)**

## 125. SQL: WHERE vs HAVING?

*EF Core & SQL*

> "WHERE filters rows before grouping. HAVING filters groups after GROUP BY, like HAVING COUNT(*) > 5."

**[⬆ Back to Top](#table-of-contents)**

## 126. SQL: DELETE vs TRUNCATE?

*EF Core & SQL*

> "DELETE removes rows one by one, can use WHERE, fires triggers and is fully logged. TRUNCATE removes all rows at once, is minimally logged, resets identity, and can't use WHERE."

**[⬆ Back to Top](#table-of-contents)**

## 127. SQL: UNION vs UNION ALL?

*EF Core & SQL*

> "UNION removes duplicates, which needs a sort, so it's slower. UNION ALL keeps everything and is faster; I use it unless I need duplicates removed."

**[⬆ Back to Top](#table-of-contents)**

## 128. SQL: what's a CTE?

*EF Core & SQL*

> "A named temporary result set defined with WITH, to make complex queries readable or to write recursive queries like walking an org hierarchy."

**[⬆ Back to Top](#table-of-contents)**

## 129. SQL: ROW_NUMBER vs RANK vs DENSE_RANK?

*EF Core & SQL*

For scores 100, 90, 90, 80:

- ROW_NUMBER: 1, 2, 3, 4
- RANK: 1, 2, 2, 4 (skips)
- DENSE_RANK: 1, 2, 2, 3 (no gap)

**[⬆ Back to Top](#table-of-contents)**

## 130. SQL: find the second-highest salary.

*EF Core & SQL*

```sql
SELECT Salary
FROM (SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS Rnk
      FROM Employees) AS Ranked
WHERE Rnk = 2;
```

DENSE_RANK handles ties: if two share the top salary, the next distinct one is still rank 2.

**[⬆ Back to Top](#table-of-contents)**

## 131. SQL: delete duplicate rows but keep one.

*EF Core & SQL*

```csharp
WITH Dupes AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY Email ORDER BY Id) AS Rn
    FROM Customers
)
DELETE FROM Dupes WHERE Rn > 1;
```

Number rows within each duplicate group, delete everything after the first.

**[⬆ Back to Top](#table-of-contents)**

## 132. SQL: temp table vs table variable?

*EF Core & SQL*

> "A temp table (#Temp) lives in tempdb, can have indexes and statistics, so it's better for larger data. A table variable (@T) is lighter, but the optimizer assumes few rows, so it's for small sets."

**[⬆ Back to Top](#table-of-contents)**

## 133. SQL: stored procedure vs function?

*EF Core & SQL*

> "A procedure can modify data, return multiple result sets and manage transactions. A function returns a value or table, can be used inside a SELECT, and can't modify data."

**[⬆ Back to Top](#table-of-contents)**

## 134. SQL: what is ACID?

*EF Core & SQL*

> "Atomic: all or nothing. Consistent: constraints always hold. Isolated: concurrent transactions don't see each other's unfinished work. Durable: once committed, it survives a crash."

**[⬆ Back to Top](#table-of-contents)**

## 135. SQL: what is normalization?

*EF Core & SQL*

> "Organising tables so each fact is stored once and linked by keys. Up to 3NF is normal for transactional systems; reporting databases are often denormalized for fast reads."

**[⬆ Back to Top](#table-of-contents)**

## 136. What makes a RESTful API well designed?

*API & security*

- Resources as nouns, correct verbs: `GET /accounts/42/orders`.
- Correct status codes and consistent errors (ProblemDetails).
- Versioning, so existing clients never break.
- Pagination and filtering for lists.
- Idempotency for retries, validation, and authentication on every endpoint.

**[⬆ Back to Top](#table-of-contents)**

## 137. POST vs PUT vs PATCH, and which are idempotent?

*API & security*

> "POST creates and isn't idempotent: two calls create two things. PUT replaces the whole resource and is idempotent. PATCH changes part of it. GET, PUT and DELETE are idempotent. For POSTs that must be safe to retry, like placing an order, I use an Idempotency-Key header."

**[⬆ Back to Top](#table-of-contents)**

## 138. Which status codes do you use, and when?

*API & security*

- **200** OK · **201** Created · **202** Accepted (processing later) · **204** No Content
- **400** bad input · **401** not authenticated · **403** authenticated but not allowed · **404** not found
- **409** conflict (concurrency, duplicate) · **422** valid format, fails business rules · **429** rate limited
- **500** server error · **503** dependency down

**Follow-up:** 401 vs 403 is a classic: 401 = who are you? 403 = I know who you are, and you can't do this.

**[⬆ Back to Top](#table-of-contents)**

## 139. A client retries a timed-out order. How do you prevent a duplicate trade?

*API & security*

> "The client sends an Idempotency-Key, unique per order attempt. I store it with the order under a unique constraint. On a retry with the same key, I return the original result instead of placing a second order."

**[⬆ Back to Top](#table-of-contents)**

## 140. How do you version an API?

*API & security*

> "Usually in the URL, like /v1/orders, because it's explicit and easy to route in APIM. Existing versions never get breaking changes; breaking changes go in a new version, and the old one is deprecated with notice to consumers."

**[⬆ Back to Top](#table-of-contents)**

## 141. OAuth2 vs JWT?

*API & security*

> "OAuth2 is the authorization framework: how a client gets a token from an identity provider like Microsoft Entra ID. A JWT is a token format: a signed JSON token carrying claims like user id, roles and expiry. OAuth2 commonly issues JWTs as access tokens."

**[⬆ Back to Top](#table-of-contents)**

## 142. A partner system calls your API through APIM. Walk me through how it's secured.

*API & security*

**OAuth2 client credentials flow** (a system calling, not a person).

1. We register the client in Entra ID and give it a client ID plus a secret, or preferably a certificate.
1. The client sends them to **Entra's token endpoint** with our API's scope and gets a short-lived **access token (JWT)**, about an hour.
1. **No refresh token** in this flow: the client caches the token and requests a new one when it expires.
1. The client calls APIM with `Authorization: Bearer `.
1. APIM's **validate-jwt** policy checks signature (Entra public keys), issuer, audience, expiry and app roles, and applies rate limiting.
1. The API validates again (defence in depth) and checks the role per endpoint.

Secrets are rotated and stored in Key Vault, never in code.

**Follow-up:** Common mistake: saying client credentials get a refresh token. They don't; refresh tokens only exist when a user logged in.

**[⬆ Back to Top](#table-of-contents)**

## 143. How do users log in through the UI and call your API?

*API & security*

**Authorization code flow with PKCE**, through Entra ID.

1. The UI redirects the user to **Microsoft's login page**. Our app never sees the password; MFA and lockout are handled by Entra.
1. Entra redirects back with a **one-time authorization code**.
1. The app exchanges the code for three tokens: an **ID token** (who the user is, for the UI), an **access token** (sent to the API), and a **refresh token** (gets new access tokens without logging in again).
1. Every API call carries the access token; the API validates it and checks roles.

Refresh token stored server-side and encrypted. If the access token is in a cookie, the cookie is **HttpOnly, Secure, SameSite**. The ID token is never sent to the API.

**Follow-up:** PKCE: the app sends a hashed random secret with the login, then proves it has the original when exchanging the code, so a stolen code is useless. Why not localStorage? Any script can read it, so one XSS bug leaks the token.

**[⬆ Back to Top](#table-of-contents)**

## 144. What does rotating secrets mean?

*API & security*

A client secret is like a password and expires in Entra. Rotating means replacing it on a schedule, before it expires or leaks:

1. Create a new secret (an app can hold two at once).
1. Put it in Key Vault and switch the client to it.
1. Delete the old one.

> "Two valid secrets during the switch means no downtime. Better still: certificates or managed identity, so there's no secret to leak."

**[⬆ Back to Top](#table-of-contents)**

## 145. How do you implement authorization in .NET?

*API & security*

**Authentication** = who are you. **Authorization** = what may you do. Three layers:

**1. Role or policy based** (can this caller use this endpoint?):

```csharp
builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("CanPlaceOrders", policy => policy.RequireRole("Orders.Write"));
});

[Authorize(Policy = "CanPlaceOrders")]
[HttpPost("orders")]
public async Task<IActionResult> PlaceOrder(OrderRequest request) { ... }
```

Roles are Entra ID app roles, arriving in the token's `roles` claim.

**2. Resource based** (can this user touch THIS account?):

```csharp
string userId = User.FindFirst("oid").Value;
Account account = await _repo.GetAccountAsync(accountId);

if (account.OwnerId != userId)
    return Forbid();   // 403
```

**3. Deny by default:** a fallback policy requires authentication on every endpoint, so a forgotten [Authorize] doesn't leave one open.

**Follow-up:** Skipping layer 2 is broken access control, the #1 OWASP risk: change /accounts/123 to /accounts/124 and read someone else's account.

**[⬆ Back to Top](#table-of-contents)**

## 146. How does your API validate a JWT?

*API & security*

- `AddAuthentication().AddJwtBearer()` checks the signature with the identity provider's public keys.
- It validates issuer, audience and expiry.
- `[Authorize]` policies check roles or scopes.
- APIM can also validate the JWT at the gateway before the request reaches the service.

**[⬆ Back to Top](#table-of-contents)**

## 147. Name an OWASP risk you've mitigated.

*API & security*

> "Broken access control is the big one for banking. Checking that someone is logged in isn't enough; for GET /accounts/123 I verify account 123 belongs to the caller, otherwise anyone can change the id and read other people's data. Also SQL injection, prevented with parameterized queries and EF, and secrets kept out of code in Key Vault."

**[⬆ Back to Top](#table-of-contents)**

## 148. How do you protect customer data and privacy?

*API & security*

- Collect and return only what's needed.
- Never log account numbers, SINs, tokens or passwords; mask them.
- TLS in transit, encryption at rest (TDE).
- Least-privilege access, and secrets in Key Vault with managed identity.

**[⬆ Back to Top](#table-of-contents)**

## 149. Where do secrets like connection strings go?

*API & security*

> "Never in appsettings or Git. Azure Key Vault or OpenShift/Kubernetes secrets, and ideally managed identity so there's no password to store at all."

**[⬆ Back to Top](#table-of-contents)**

## 150. What do you know about WCAG accessibility?

*API & security*

> "It's the standard for making apps usable by everyone: keyboard navigation, alt text, enough color contrast, proper labels and ARIA for screen readers. On the front end I check with tools like Lighthouse or axe. On the API side, it means returning clear, structured error messages the UI can present accessibly."

**[⬆ Back to Top](#table-of-contents)**

## 151. How do you test a service that consumes events and writes to a database?

*Testing*

> "Take a flow I'm working on now: MDM publishes an event when a SKU changes, and my service maps it to the B2B format and sends it to the B2B team.

> Unit tests cover the mapping logic, where the business rules live. I build test events for each scenario (colour change, quantity change, missing fields, invalid values), mock the dependencies like the B2B publisher and repository with Moq, and assert that the output is correct and that the publisher was or wasn't called.

> I specifically test failure cases: a duplicate event is processed once, an older event doesn't overwrite newer data, and a malformed message is dead-lettered instead of crashing the consumer.

> Integration tests run the service against a real database in a Docker container to catch query, serialization and configuration problems. Everything runs on every PR, and a failing test blocks the merge."

```csharp
var publisher = new Mock<IB2BPublisher>();
var handler = new SkuChangedHandler(publisher.Object);

await handler.HandleAsync(new SkuChangedEvent { Sku = "ABC123", Colour = "Blue" });

publisher.Verify(p => p.SendAsync(It.Is<B2BProduct>(b => b.Colour == "Blue")), Times.Once);
```

**Follow-up:** Terminology: Moq is the mocking library; the sample values are test data. Mock the boundaries (database, publishers, HTTP), never the logic under test. Is 150 tests a good metric? The count isn't the goal; covering business rules and failure cases is.

**[⬆ Back to Top](#table-of-contents)**

## 152. Unit test vs integration test: where's the line?

*Testing*

> "A unit test checks one class's logic with its dependencies mocked: fast, no database, no network. An integration test checks that real pieces work together: API, database, Kafka. Business rules get unit tests; queries, serialization and wiring get integration tests."

**[⬆ Back to Top](#table-of-contents)**

## 153. How do you unit test a class that publishes to Kafka?

*Testing*

> "The class depends on an IEventPublisher interface, not the Kafka client. In the test I inject a Moq mock, run the method, and verify PublishAsync was called once with the expected event. No Kafka needed."

```csharp
var publisher = new Mock<IEventPublisher>();
var service = new ShipmentService(publisher.Object);

await service.CreateAsync(shipment);

publisher.Verify(p => p.PublishAsync(It.IsAny<ShipmentEvent>()), Times.Once);
```

**[⬆ Back to Top](#table-of-contents)**

## 154. How do you test an API end to end?

*Testing*

> "WebApplicationFactory starts the real API in memory, and the test calls it with HttpClient. For real dependencies, Testcontainers starts SQL Server, Redis or Kafka in Docker for the test run, so it's close to production and runs in CI."

**[⬆ Back to Top](#table-of-contents)**

## 155. What makes a good unit test?

*Testing*

- Arrange, Act, Assert.
- Tests one behaviour; the name says what it checks.
- Fast and deterministic: no real clock, network or random values.
- Covers edge cases, not just the happy path.

**[⬆ Back to Top](#table-of-contents)**

## 156. Mock vs stub vs fake?

*Testing*

> "A stub returns canned answers. A mock also lets you verify how it was called. A fake is a simple working implementation, like an in-memory repository."

**[⬆ Back to Top](#table-of-contents)**

## 157. Do you practise TDD?

*Testing*

> "For business rules, yes: write a failing test, make it pass, refactor. It's most useful where the logic has many edge cases. For plumbing code I usually write the tests right after."

**[⬆ Back to Top](#table-of-contents)**

## 158. Image vs container vs Docker?

*Docker & OpenShift*

> "An image is the immutable package: compiled app, runtime and OS files. A container is a running instance of an image. Docker builds images and runs containers on one machine. Kubernetes or OpenShift runs them at scale across many."

**[⬆ Back to Top](#table-of-contents)**

## 159. How do you write a Dockerfile for a .NET API?

*Docker & OpenShift*

> "Multi-stage. The first stage uses the .NET SDK image to restore, build and publish. The final stage copies only the published output into the smaller ASP.NET runtime image. The production image has no SDK or source code, is much smaller, and runs as a non-root user."

**[⬆ Back to Top](#table-of-contents)**

## 160. Explain the core Kubernetes objects.

*Docker & OpenShift*

- **Pod**: one or more containers running together.
- **Deployment**: keeps N replicas running and does rolling updates.
- **Service**: a stable address in front of changing pods.
- **Ingress** (Route in OpenShift): external traffic in.
- **ConfigMap / Secret**: configuration and secrets.
- **HPA**: scales pods on CPU or other metrics.

**[⬆ Back to Top](#table-of-contents)**

## 161. OpenShift vs Kubernetes?

*Docker & OpenShift*

> "OpenShift is Red Hat's enterprise Kubernetes, so pods, deployments and services all carry over. It adds stricter security by default (containers can't run as root, via Security Context Constraints), Routes for external traffic, Projects as namespaces with extra controls, a built-in image registry and builds, and the oc CLI alongside kubectl."

**[⬆ Back to Top](#table-of-contents)**

## 162. Liveness vs readiness probe?

*Docker & OpenShift*

> "Readiness: is this pod ready for traffic? If not, it's taken out of the load balancer, for example while it warms up or loses the database. Liveness: is it still alive? If not, Kubernetes restarts it. In .NET I expose them with health checks via MapHealthChecks."

**[⬆ Back to Top](#table-of-contents)**

## 163. Walk me through a CI/CD pipeline you've built.

*Docker & OpenShift*

1. On a PR: build, unit tests, code and dependency scans.
1. On merge: build the Docker image, tag it and push to the registry.
1. Deploy to dev automatically, then higher environments with approvals.
1. Rolling deployment with health checks, and rollback to the previous image if checks fail.

The same image moves through every environment; only configuration changes.

**[⬆ Back to Top](#table-of-contents)**

## 164. How do you handle config per environment?

*Docker & OpenShift*

> "One image for all environments. Settings come from appsettings.{Environment}.json overridden by environment variables or ConfigMaps, and secrets come from Key Vault or Kubernetes secrets. Nothing environment-specific is baked into the image."

**[⬆ Back to Top](#table-of-contents)**

## 165. Git: merge vs rebase?

*Git*

> "Merge combines branches with a merge commit and keeps full history. Rebase replays my commits on top of the latest main for a clean, straight history. I rebase my own feature branch, but never a shared branch, because it rewrites history others depend on."

**[⬆ Back to Top](#table-of-contents)**

## 166. Git: what's your branching strategy?

*Git*

> "Trunk-based with short-lived feature branches: branch from main, PR, review, CI must pass, merge, and the pipeline deploys. Long-lived branches cause painful merges."

**[⬆ Back to Top](#table-of-contents)**

## 167. Git: how do you resolve a merge conflict?

*Git*

> "Pull the latest main, understand both changes, talk to the other developer if it's not obvious, combine them, run the tests, then commit. Never blindly pick mine."

**[⬆ Back to Top](#table-of-contents)**

## 168. What do you look for in a code review?

*Git*

> "Correctness and edge cases first, then security like validation and authorization, then readability, tests and performance issues like N+1. I explain why in comments so it's a learning moment."

**[⬆ Back to Top](#table-of-contents)**

## 169. Git: revert vs reset?

*Git*

> "Revert creates a new commit that undoes an earlier one, safe on shared branches. Reset moves the branch pointer back and rewrites history, only for local unpushed work."

**[⬆ Back to Top](#table-of-contents)**

## 170. Azure: App Service vs AKS vs Azure Functions?

*Azure*

> "App Service is the simplest way to host a web app or API: deploy code, Azure manages servers. AKS is managed Kubernetes for many containerised microservices, with fine control over scaling and networking. Functions are event-driven and serverless: pay per execution, good for small background jobs."

**[⬆ Back to Top](#table-of-contents)**

## 171. Azure: Event Hubs vs Service Bus vs Event Grid?

*Azure*

- **Event Hubs**: high-throughput event streaming with partitions and replay. Azure's Kafka; supports the Kafka protocol.
- **Service Bus**: reliable enterprise messaging: queues, topics, sessions for ordering, dead-lettering, transactions. For commands like "process this order".
- **Event Grid**: lightweight event notification, like "a blob was uploaded", pushed to subscribers.

Your example: "At Staples we use Event Hubs for high-throughput integration events to the TMS."

**[⬆ Back to Top](#table-of-contents)**

## 172. Azure: what is APIM for?

*Azure*

> "A gateway in front of our APIs: JWT validation, rate limiting and quotas, versioning, request transformation, and a developer portal for partners. One secure front door for all APIs."

**[⬆ Back to Top](#table-of-contents)**

## 173. Azure: Key Vault and Managed Identity?

*Azure*

> "Key Vault stores secrets, keys and certificates. Managed Identity gives the app its own Azure identity, so it reads Key Vault without any stored password. That removes the problem of where to keep the secret that unlocks the secrets."

**[⬆ Back to Top](#table-of-contents)**

## 174. Azure: what does Application Insights give you?

*Azure*

> "Azure's APM: request rates, failures, dependency calls with timings, exceptions and distributed traces across services. It's how you find that time is going into a slow SQL call, the same way we use Datadog at Staples."

**[⬆ Back to Top](#table-of-contents)**

## 175. Azure: storage types?

*Azure*

- **Blob**: files like PDFs.
- **Table Storage**: cheap NoSQL key-value (used at Staples).
- **Queue Storage**: simple queuing.
- **Files**: SMB file shares.

**[⬆ Back to Top](#table-of-contents)**

## 176. Azure: Table Storage vs Cosmos DB vs Azure SQL?

*Azure*

> "Azure SQL is relational with joins, transactions and strong consistency, what you want for money. Cosmos DB is globally distributed NoSQL with low latency and flexible schemas. Table Storage is the cheapest key-value option for simple lookups at scale."

**[⬆ Back to Top](#table-of-contents)**

## 177. Azure: what is ACR?

*Azure*

> "Azure Container Registry: the private Docker image registry. The pipeline pushes images there and AKS pulls from it."

**[⬆ Back to Top](#table-of-contents)**

## 178. Azure: how does a request reach your AKS service?

*Azure*

DNS, then Azure Front Door or Application Gateway (WAF, TLS), then APIM, then the AKS ingress controller, then the Kubernetes Service, then the pods.

**[⬆ Back to Top](#table-of-contents)**

## 179. Azure: what are deployment slots?

*Azure*

> "An App Service feature: deploy to a staging slot, warm it up, then swap with production for near-zero downtime, and swap back if something breaks."

**[⬆ Back to Top](#table-of-contents)**

## 180. Azure: how do you scale?

*Azure*

> "Scale up means a bigger machine; scale out means more instances. App Service autoscales on rules like CPU; AKS uses the Horizontal Pod Autoscaler for pods and the cluster autoscaler for nodes."

**[⬆ Back to Top](#table-of-contents)**

## 181. How do you implement Event Hubs in .NET?

*Azure*

> "An Event Hubs namespace with an event hub inside, like a Kafka topic, split into partitions. The producer sends JSON using a connection string or, better, managed identity. Consumers read through a consumer group and save checkpoints in Blob storage, so after a restart they continue where they left off, like Kafka offsets."

```csharp
// Producer
var producer = new EventHubProducerClient(connectionString, "shipments");
EventDataBatch batch = await producer.CreateBatchAsync();
batch.TryAdd(new EventData(JsonSerializer.SerializeToUtf8Bytes(shipment)));
await producer.SendAsync(batch);

// Consumer
var checkpoints = new BlobContainerClient(blobConnectionString, "checkpoints");
var processor = new EventProcessorClient(checkpoints, "$Default", connectionString, "shipments");
processor.ProcessEventAsync += async args =>
{
    Shipment? shipment = JsonSerializer.Deserialize<Shipment>(args.Data.EventBody.ToArray());
    // handle it idempotently
    await args.UpdateCheckpointAsync();
};
processor.ProcessErrorAsync += args => { return Task.CompletedTask; };
await processor.StartProcessingAsync();
```

**[⬆ Back to Top](#table-of-contents)**

## 182. What is Google Pub/Sub and how does it work?

*Azure*

> "A publisher sends messages to a topic; each subscription gets its own copy, like consumer groups. Subscribers pull messages or have them pushed to an endpoint, and must acknowledge each one; unacknowledged messages are redelivered. So it's at-least-once, and consumers are idempotent."

**[⬆ Back to Top](#table-of-contents)**

## 183. What is AKS, and who decides the number of pods?

*Azure*

> "AKS is Azure's managed Kubernetes: Azure runs the control plane, and we define deployments (image and replica count), services and autoscaling rules. Kubernetes restarts failed pods and rolls out new versions without downtime. Docker builds the image; Kubernetes runs and scales it."

**Follow-up:** Common mistake: pod count is NOT set in Docker. It's replicas in the deployment YAML, and the Horizontal Pod Autoscaler scales it.

**[⬆ Back to Top](#table-of-contents)**

## 184. Walk me through an Azure DevOps pipeline you built.

*Azure*

> "An azure-pipelines.yml file in the repo, triggered on every push to main. Stages: build and unit tests, then build the Docker image and push it to ACR, then deploy to AKS, dev automatically and prod with approval."

```csharp
trigger:
  - main
stages:
  - stage: Build
    jobs:
      - job: Build
        steps:
          - task: DotNetCoreCLI@2
            inputs: { command: 'test' }
          - task: Docker@2
            inputs: { command: 'buildAndPush', repository: 'shipments-api', containerRegistry: 'our-acr' }
  - stage: DeployDev
    jobs:
      - deployment: Deploy
        environment: dev
        strategy:
          runOnce:
            deploy:
              steps:
                - task: KubernetesManifest@1
                  inputs: { action: 'deploy', manifests: 'k8s/deployment.yaml' }
```

**[⬆ Back to Top](#table-of-contents)**

## 185. Microservices vs monolith?

*System design*

> "A monolith is one application and one deployment: everything is released together, and one bug can take down everything. Microservices split the system into small services around business capabilities, like orders, inventory and shipping, each with its own database, deployed and scaled independently, talking over APIs or events. The trade-off: more flexibility and resilience, but more complexity in networking, monitoring and data consistency."

**[⬆ Back to Top](#table-of-contents)**

## 186. How would you build a microservice?

*System design*

> "An ASP.NET Core API that owns one business capability and its own database, never shared. Others talk to it through its API or events, never its tables. It gets a Dockerfile, a pipeline, health checks for Kubernetes, structured logs with correlation ids, and it's deployed independently to AKS."

**[⬆ Back to Top](#table-of-contents)**

## 187. A client clicks 'Buy 100 shares'. Design what happens until the order reaches the market.

*System design*

**Two halves:** synchronous during the click, asynchronous after.

> "During the click: the gateway routes to the Order API, which validates it: authenticated, account belongs to the user, valid symbol and quantity, market open. Then in ONE database transaction it checks and reserves buying power with a conditional update, saves the order as Accepted and writes an outbox event, and returns 202 with the order id. An Idempotency-Key stops a retried click placing a second order.

> After the click: a worker publishes the outbox event to Kafka keyed by account, and the order router sends the order to the market, where the matching happens. When the execution report comes back, a consumer updates in one transaction the order status, the client's positions and cash, and releases any unused reservation. A rejection releases the reservation.

> The client sees each status pushed live through SignalR. Every step goes to an append-only audit trail. Balances and positions always come from the database, never a cache."

```csharp
Client -> Gateway -> Order API
  -> [reserve cash + Order + Outbox, one transaction] -> 202
  -> worker -> Kafka (key = AccountId) -> Order Router -> MARKET
  <- execution report -> update order + positions + cash -> SignalR
```

**Follow-up:** Why reserve cash, not just check it? Two orders could both see $10,000 and both spend it. Partial fill (60 of 100)? PartiallyFilled, add 60 shares, charge for 60, keep the rest reserved. Only mention scaling (stateless APIs, partitions, read replicas) if asked.

**[⬆ Back to Top](#table-of-contents)**

## 188. Does the Direct Investing platform match buyers and sellers?

*System design*

> "No. Direct Investing is a broker, not an exchange. Matching happens on the market (TSX, NYSE and so on). The broker's system validates the order, reserves the client's cash, routes the order to the market, and processes the execution report that comes back. The other side of the trade is another market participant, not one of our clients."

**Follow-up:** This is why execution is asynchronous: a limit order can fill hours later, or never, so it can't happen inside one API call.

**[⬆ Back to Top](#table-of-contents)**

## 189. Broker domain terms: exchange, market vs limit order, fill, buying power?

*System design*

- **Exchange** (TSX, NYSE): where buyers and sellers are matched. RBC doesn't run one.
- **Broker** (RBC Direct Investing): takes the client's order, checks it, sends it to the exchange, updates the account when done.
- **Market order**: buy now at the current price. Usually fills in seconds.
- **Limit order**: buy only at $180 or less. Might fill hours later, or never.
- **Fill / execution report**: the exchange's reply, "Filled 100 at $182.50". Can be partial (60 of 100).
- **Buying power**: cash available to trade with.
- **FIX protocol**: the industry-standard message format between brokers and exchanges.

**[⬆ Back to Top](#table-of-contents)**

## 190. Draw the journey of one 'Buy 100 AAPL' order.

*System design*

```csharp
PART 1: THE CLICK (synchronous)
Client --POST /orders (Idempotency-Key)--> APIM --> Order API
  1. Validate: logged in, own account, valid symbol, market open
  2. ONE transaction:
     - reserve cash: UPDATE Accounts SET Reserved = Reserved + @cost
                     WHERE Id = @acct AND Cash - Reserved >= @cost
     - INSERT Orders (Accepted)
     - INSERT Outbox (OrderAccepted)
  3. Return 202 + orderId

PART 2: AFTER THE CLICK (asynchronous)
Outbox worker --> Kafka "orders" (key = AccountId)
  --> Order Router --> EXCHANGE (matching happens here)
  <-- execution report "Filled 100 @ 182.50"
  Fill consumer, ONE transaction:
     Order -> Filled, Positions +100, Cash -18,250, release reservation
  --> SignalR push: client sees "Filled"
```

> "The click only reserves money and records the order. Everything involving the market happens afterwards, through events."

**Follow-up:** Why reserve instead of charging at fill? Two orders can't spend the same cash, and the money stays held however long a limit order takes to fill.

**[⬆ Back to Top](#table-of-contents)**

## 191. Order follow-ups: partial fill, client cancel, exchange reject?

*System design*

- **Partial fill (60 of 100):** status PartiallyFilled, positions +60, charge for 60, keep the other 40 reserved until they fill or the order is cancelled.
- **Client cancels while at the exchange:** send a cancel request, mark CancelPending. Only when the exchange confirms: Cancelled and release cash, because it might fill in the meantime.
- **Exchange rejects:** status Rejected, release the reservation, notify the client.
- **How does the router talk to the exchange?** Usually FIX: translate our order into FIX messages and read execution reports back.
- **Where's Redis?** Quotes and the portfolio screen. Reservations and positions always come from SQL.

**[⬆ Back to Top](#table-of-contents)**

## 192. Why return 202 Accepted instead of waiting for the market?

*System design*

> "Reaching the market and getting filled can take a while and depends on systems we don't control. Holding the client's connection open wastes server resources and risks timeouts, which cause retries. So I accept the order, return 202 with the order id, and push status updates as it moves: sent, filled, rejected."

**[⬆ Back to Top](#table-of-contents)**

## 193. Kafka is down when an order is placed. What happens?

*System design*

> "The order and its outbox row are already saved in one transaction, so the client still gets 202. The worker keeps retrying and publishes once Kafka is back. Nothing is lost, and order intake doesn't depend on Kafka being up."

**[⬆ Back to Top](#table-of-contents)**

## 194. How would a regulator reconstruct what happened to one order?

*System design*

> "Every state change (received, validated, sent, filled, cancelled) is written as an immutable, append-only event with timestamp, user and source. A correlation id follows the order across every service and log. Replaying one order's events shows exactly what happened and when."

**[⬆ Back to Top](#table-of-contents)**

## 195. How do you keep data consistent across microservices?

*System design*

> "Each service owns its database, so there are no distributed transactions. Services communicate with events via an outbox, and multi-step processes use a saga with compensating actions: reserve cash, place the order, and if the market rejects it, release the cash. It's eventually consistent, and every step is idempotent."

**[⬆ Back to Top](#table-of-contents)**

## 196. Circuit breaker vs retry vs bulkhead?

*System design*

- **Retry** with backoff: for brief glitches.
- **Circuit breaker**: after repeated failures, stop calling for a while so you don't pile onto a failing dependency.
- **Bulkhead**: cap concurrent calls to one dependency so it can't use up all your threads.

In .NET: Polly or Microsoft.Extensions.Http.Resilience. On one critical dependency, use all three together.

**[⬆ Back to Top](#table-of-contents)**

## 197. How would you push live price or order updates to the UI?

*System design*

> "SignalR over WebSockets. The server pushes updates instead of the client polling. With several API instances, SignalR needs a backplane, like Redis or Azure SignalR Service, so a message reaches the client whichever instance it's connected to."

**[⬆ Back to Top](#table-of-contents)**

## 198. How does your design scale?

*System design*

> "The Order API is stateless, so I add instances behind the gateway, with autoscaling on OpenShift or AKS. Kafka scales with partitions and consumers. Reads come from Redis and SQL read replicas, and writes stay on the primary."

**[⬆ Back to Top](#table-of-contents)**

## 199. Frontend: how do you position yourself if they go deep?

*Frontend*

> "My core strength is backend. On the frontend I've built Angular apps for years, mostly the pieces that talk to APIs: services, interceptors, guards and forms."

**[⬆ Back to Top](#table-of-contents)**

## 200. Angular: component vs service? Lifecycle hooks?

*Frontend*

- A component is a piece of UI. A service holds shared logic or data and is injected with DI, the same idea as .NET.
- `ngOnInit`: load data here, not in the constructor. `ngOnDestroy`: clean up subscriptions.

**[⬆ Back to Top](#table-of-contents)**

## 201. Angular: Observables, the async pipe and switchMap?

*Frontend*

- HttpClient returns an Observable; nothing happens until someone subscribes (like LINQ deferred execution).
- The async pipe subscribes and unsubscribes for you, which prevents memory leaks.
- switchMap cancels the previous request when a new one starts, like a search box as the user types.

**[⬆ Back to Top](#table-of-contents)**

## 202. Angular: HTTP interceptor and route guard?

*Frontend*

- **Interceptor**: attaches the JWT to every API call and handles 401 in one place.
- **Route guard**: blocks navigation unless the user is logged in or has the right role.

**[⬆ Back to Top](#table-of-contents)**

## 203. Angular: change detection, OnPush, and modern Angular?

*Frontend*

- Change detection checks for changes and updates the screen. OnPush only re-checks a component when its inputs change, so it's faster.
- Modern Angular: standalone components (no NgModules), signals for simpler reactive state, lazy-loaded routes.

**[⬆ Back to Top](#table-of-contents)**

## 204. React: props vs state, useState, useEffect, virtual DOM?

*Frontend*

- Props are passed in from the parent and read-only; state is owned by the component, and changing it re-renders.
- useState holds state; useEffect runs side effects like API calls after render.
- The virtual DOM compares new UI to old and updates only what changed.

**[⬆ Back to Top](#table-of-contents)**

## 205. Tell me about a disagreement with a teammate.

*Behavioural*

**S:** At Staples, our publishing table deleted rows as soon as messages were sent to the WMS and TMS.

**T:** I thought we were losing important information, but the team was comfortable with it because it worked.

**A:** I listened to their concern first, mainly table growth and extra work. Then I showed a concrete case: when a partner says "we never got shipment X", we couldn't prove whether or when we sent it. I proposed keeping rows with a status per destination, plus a cleanup job that purges sent rows after a set number of days.

**R:** Adopted: "Now we can answer partner questions in minutes instead of guessing." Or not yet: "We put it on the backlog. I committed to the team's decision and documented the risk. The lesson: bring a concrete example, not just an opinion."

**Follow-up:** What they check: you listen, argue with evidence, and commit to the team decision even when it doesn't go your way.

**[⬆ Back to Top](#table-of-contents)**

## 206. Tell me about a production incident or a hard problem you solved.

*Behavioural*

**S:** At insightsoftware, heavy reports like vesting and tax reports were slow for our largest clients, and clients were complaining.

**T:** As lead on the reporting team, I owned finding and fixing it.

**A:** Datadog APM showed almost all the time was inside the database call; the code was already async. I captured the slow queries with SQL Profiler and read the execution plans: table scans, SELECT * and key lookups. I replaced SELECT * with only the needed columns, added covering indexes, and cached reference data that rarely changes, shipping in small steps and checking each one in Datadog.

**R:** The heavy reports got significantly faster, roughly 40% on the worst ones, and the complaints stopped. Since then I check the execution plan for any new heavy query before it ships.

**Follow-up:** End on what you changed afterwards. That's the part they remember.

**[⬆ Back to Top](#table-of-contents)**

## 207. Working with another team or an external vendor whose system didn't do what you needed?

*Behavioural*

> "At Staples, our carrier platform is Centiro, a third-party vendor. Their response didn't include the content we needed in both English and French, which our Canadian customers require. Rather than hacking around it, I set up regular syncs with their team, every other day, and showed them concrete example payloads of exactly what we needed, so there was no room for misreading. Once we agreed the format, I built our side against it in parallel so we weren't blocked. They delivered the change, I switched our integration to the new payload, and it went live with bilingual responses. My takeaway: with vendors, agree the contract early, with real examples, and build against it in parallel."

**Follow-up:** Say 'I' more than 'we'. End with the result and the lesson.

**[⬆ Back to Top](#table-of-contents)**

## 208. Tell me about delivering under a tight deadline.

*Behavioural*

> "At Staples, integration requests often came with about two weeks' notice for work that needed four. On one [name a real integration], instead of just agreeing and hoping, I broke it down straight away into what was essential for go-live and what could follow, and shared that plan with stakeholders early. We delivered the core flow on time and shipped the rest in the next sprint. But the real fix was upstream: requests kept reaching us late, so I helped design a process where teams raise integration tickets ahead of time, with the data they need. Since then those last-minute crunches have become much rarer."

**Follow-up:** Avoid 'I worked day and night': it sounds like poor planning. The ticket process is the senior part: you fixed the root cause.

**[⬆ Back to Top](#table-of-contents)**

## 209. Tell me about a hard technical challenge you overcame.

*Behavioural*

> "At Accolite, on the insightsoftware platform, we migrated legacy .NET Framework APIs to .NET Core. The hardest part was dependencies: several NuGet packages and libraries had no .NET Core support. I went through them one by one and handled each in one of three ways: upgrade to a version that supported .NET Core, swap in an alternative library, or, where nothing existed, build that piece ourselves as an internal NuGet package so every service could reuse it. We migrated module by module, with tests confirming each behaved the same as before. We got fully onto .NET Core, with better performance and faster builds. The lesson: audit dependencies before starting a migration; that's where the real risk hides."

**Follow-up:** Matches the JD nice-to-have: reusable components and package deployment. Also works for 'learning under pressure'.

**[⬆ Back to Top](#table-of-contents)**

## 210. How do you use AI in your work?

*Behavioural*

> "GitHub Copilot and Claude help me with boilerplate and exploring options quickly, but I review and understand everything I ship. The design decisions and fundamentals are mine; AI speeds up the typing, not the thinking."

**Follow-up:** Tony raised AI himself in the screener: 'if you don't know the fundamentals it won't solve your problems for you'.

**[⬆ Back to Top](#table-of-contents)**

## 211. Other likely behavioural questions: quick starting points.

*Behavioural*

- **Ambiguous requirements:** ask what the consumer actually needs, write down the data mapping, confirm before building.
- **Learning something new quickly:** build a small working demo first (the Kafka demo, the sample API).
- **Disagreeing with a manager:** data, not opinion, then commit to the decision.
- **Feedback received:** something true, and what you changed afterwards.
- **Conflicting priorities:** make the trade-off visible to the lead or PO; let the business decide.
- **Improving a process:** the integration ticket process, code reviews, structured logging with correlation IDs.
- **Why hire you:** event-driven .NET integration, performance tuning, financial reporting; hands-on.
- **5 years:** growing into a senior or lead role on a platform like this: owning architecture, mentoring.

Formula: STAR in about 90 seconds. Most of the time on Action, then Result and what you learned.

**[⬆ Back to Top](#table-of-contents)**

## 212. How do you mentor other developers?

*Behavioural*

> "Mostly through code reviews: explaining why, not just what to change, and pairing on tricky pieces. When someone's stuck, I help them debug rather than fixing it for them, so they learn the approach."

**[⬆ Back to Top](#table-of-contents)**

## 213. Why RBC, and why this role?

*Behavioural*

> "It's a rebuild of a large trading platform, which is rare: modern .NET, Kafka, Redis and containers in a domain where correctness really matters. It lines up with what I've done, event-driven integration at Staples and financial reporting at insightsoftware, and I want to go deeper into capital markets."

**[⬆ Back to Top](#table-of-contents)**

## 214. You're okay with contract-to-hire?

*Behavioural*

> "Yes, completely. I'm looking for a long-term role, and I'm happy to prove myself during the contract and convert."

**Follow-up:** Answer without hesitation.

**[⬆ Back to Top](#table-of-contents)**

## 215. What questions do you have for us?

*Behavioural*

- What does the target architecture of the rebuild look like, and what stage is it at?
- How is the team split across the 4 openings?
- What does success look like in the first 3 months?
- What's the biggest technical challenge right now?

**[⬆ Back to Top](#table-of-contents)**

## 216. Walk me through your banking solution, level by level.

*CodeSignal*

Every method takes a timestamp first; the caller supplies the account id.

- **L1 CreateAccount / GetBalance:** Dictionary<string, Account>, false on a duplicate id, null for unknown.
- **L2 Deposit:** TryGetValue, reject amount <= 0, return the new balance.
- **L3 Transfer:** ALL checks first (same account, amount, both exist, enough balance), THEN move money and add to TotalSpent. Returns the source balance.
- **L4 TopSpenders:** LINQ: Where TotalSpent > 0, OrderByDescending, ThenBy id, Take(n), then string.Join(",", ...) of "id{total}", like "acct5{10},acct3{8}".
- **L5 Schedule / Cancel:** scheduling only records it; every method calls ProcessDue(timestamp) first, which executes due transfers through the same TryTransfer.

**Follow-up:** Why Dictionary of Account objects? O(1) lookups, and each level adds a field instead of another dictionary to keep in sync. Why return false on a duplicate instead of throwing? It's an expected case, and the spec says so.

**[⬆ Back to Top](#table-of-contents)**

## 217. Level 3: show the transfer and the traps.

*CodeSignal*

```csharp
private int? TryTransfer(string sourceId, string targetId, int amount)
{
    if (sourceId == targetId || amount <= 0)
        return null;
    if (!_accounts.TryGetValue(sourceId, out Account? source))
        return null;
    if (!_accounts.TryGetValue(targetId, out Account? target))
        return null;
    if (source.Balance < amount)
        return null;

    source.Balance -= amount;        // only after ALL checks pass
    target.Balance += amount;
    source.TotalSpent += amount;
    return source.Balance;
}
```

> "Validate everything before changing anything, so a failed transfer never leaves money half-moved."

**Follow-up:** Unsure whether the target had to exist? Say: the source check is essential; for the target I'd confirm the requirement, since crediting a non-existent account makes no sense in a bank. Is it thread-safe? No; CodeSignal is single-threaded. In a real bank: a database transaction with an atomic conditional update, or a lock. Why block same-account? It would count as spending while moving nothing. TryGetValue vs ContainsKey + []: one lookup instead of two.

**[⬆ Back to Top](#table-of-contents)**

## 218. Level 4: top spenders, and the traps.

*CodeSignal*

```csharp
IEnumerable<string> top = _accounts.Values
    .Where(a => a.TotalSpent > 0)
    .OrderByDescending(a => a.TotalSpent)
    .ThenBy(a => a.Id, StringComparer.Ordinal)
    .Take(n)
    .Select(a => a.Id + "{" + a.TotalSpent + "}");

return string.Join(",", top);     // "acct5{10},acct3{8},acct4{7}"
```

**Follow-up:** Why StringComparer.Ordinal? A plain character-by-character sort. Big-O? O(n log n) for the sort. Why a running TotalSpent? O(1) to update instead of re-scanning transfers.

**[⬆ Back to Top](#table-of-contents)**

## 219. How would you have implemented the scheduled transfer?

*CodeSignal*

> "Scheduling only records it. Every method calls ProcessDue(timestamp) first, which executes everything due, earliest first and then in scheduling order, through the same TryTransfer, so the balance is checked at execution time. If it's insufficient then, it's skipped for good."

```csharp
public override string? ScheduleTransfer(int timestamp, string sourceAccountId,
    string targetAccountId, int amount, int delay)
{
    ProcessDue(timestamp);
    if (sourceAccountId == targetAccountId || amount <= 0)
        return null;
    if (!_accounts.ContainsKey(sourceAccountId) || !_accounts.ContainsKey(targetAccountId))
        return null;

    _transferCount++;
    var transfer = new ScheduledTransfer
    {
        Id = "transfer" + _transferCount, Source = sourceAccountId, Target = targetAccountId,
        Amount = amount, ExecuteAt = timestamp + delay, Sequence = _transferCount
    };
    _scheduled.Add(transfer);
    return transfer.Id;
}

private void ProcessDue(int now)
{
    List<ScheduledTransfer> due = _scheduled
        .Where(t => t.ExecuteAt <= now)
        .OrderBy(t => t.ExecuteAt)
        .ThenBy(t => t.Sequence)
        .ToList();

    foreach (ScheduledTransfer transfer in due)
    {
        _scheduled.Remove(transfer);
        TryTransfer(transfer.Source, transfer.Target, transfer.Amount);
    }
}

public override bool CancelTransfer(int timestamp, string transferId)
{
    ProcessDue(timestamp);
    return _scheduled.RemoveAll(t => t.Id == transferId) > 0;
}
```

**Follow-up:** Due at 14, GetBalance at 14? The transfer runs FIRST, because ProcessDue runs before the operation. Cancel after execution? False, it's no longer pending. Invalid schedule doesn't use an id: increment only after validation. Why .ToList()? A copy, so removing inside the loop is safe. Why a List? Simple and correct; a PriorityQueue for thousands. Delay or exact time? Unsure which the real one used: only ExecuteAt changes (timestamp + delay vs the given time); everything else stays the same.

**[⬆ Back to Top](#table-of-contents)**

## 220. Why call ProcessDue in every method instead of a background service?

*CodeSignal*

In CodeSignal there is no real clock: time only exists as the timestamp parameter, and it only moves when a method is called. A background timer would use the real clock and give random test results.

```sql
CreateAccount(1, ...)       it is now time 1
ScheduleTransfer(5, ...)    time 5, due at 15
GetBalance(20, ...)         time 20: the transfer due at 15 must run FIRST
```

**In production:** a BackgroundService polling a ScheduledTransfers table (ExecuteAt, Status) with the real clock every few seconds.

- **Several pods:** claim rows atomically, UPDATE ... SET Status = 'Processing' WHERE Id = @id AND Status = 'Pending'; only the worker that gets 1 row updated executes it.
- **Idempotency:** a crash mid-way must not transfer twice on retry.

> "In the assessment, time only advanced through the timestamp parameter, so processing due transfers at the start of each call was the right design; it's deterministic. In production I'd use a background service polling a ScheduledTransfers table with the real clock, claiming rows atomically so two instances never execute the same transfer."

**Follow-up:** Raising this yourself shows production thinking, not just passing tests.

**[⬆ Back to Top](#table-of-contents)**

## 221. How would you improve your CodeSignal solution?

*CodeSignal*

> "The levels unlock one at a time, so I couldn't see what later requirements would need. At each level I kept it simple, and two dictionaries sharing the account id worked. With the full picture now, I'd model an Account object from the start, holding balance and total spent, because requirements always evolve and it keeps each new level to one field or one method. And one TryTransfer method would be the only place money moves."

```csharp
public class Account
{
    public string Id { get; set; } = "";
    public int Balance { get; set; }
    public int TotalSpent { get; set; }
}

private readonly Dictionary<string, Account> _accounts = new Dictionary<string, Account>();
```

**Follow-up:** Same idea as the country question: parallel collections that must stay in sync are fragile; one structure holding related data together is solid. It also honestly explains why Level 5 ran out of time.

**[⬆ Back to Top](#table-of-contents)**
