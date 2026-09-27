# RBC Final Round: Senior .NET, Direct Investing

> Final-round prep for a Senior .NET Developer role rebuilding a Direct Investing
> trading platform (.NET Core, Kafka, Redis, SQL Server, Docker/OpenShift). Say each
> answer out loud in under a minute before revealing it. Sections: Your stories, Screener follow-ups, Basics, Kafka, Redis, .NET core, EF Core & SQL, API & security, Testing, Docker & OpenShift, Git, Azure, System design, Frontend, Behavioural, CodeSignal.

## Table of Contents

| No. | Section | Question |
|-----|---------|----------|
| 1 | Your stories | [Tell me about yourself.](#1-tell-me-about-yourself) |
| 2 | Your stories | [Walk me through one integration flow at Staples, end to end.](#2-walk-me-through-one-integration-flow-at-staples-end-to-end) |
| 3 | Your stories | [What happens at Staples if publishing to Event Hubs fails?](#3-what-happens-at-staples-if-publishing-to-event-hubs-fails) |
| 4 | Your stories | [Why do you publish in 15-minute batches instead of immediately?](#4-why-do-you-publish-in-15-minute-batches-instead-of-immediately) |
| 5 | Your stories | [How do you keep stock consistent across multiple order management systems?](#5-how-do-you-keep-stock-consistent-across-multiple-order-management-systems) |
| 6 | Your stories | [If the inventory service is the source of truth, why publish stock updates at all?](#6-if-the-inventory-service-is-the-source-of-truth-why-publish-stock-updates-at-all) |
| 7 | Your stories | [What was the Bounteous / insightsoftware platform, and what was your role?](#7-what-was-the-bounteous--insightsoftware-platform-and-what-was-your-role) |
| 8 | Your stories | [How did you make the reports faster?](#8-how-did-you-make-the-reports-faster) |
| 9 | Your stories | [How did you find which queries were slow?](#9-how-did-you-find-which-queries-were-slow) |
| 10 | Your stories | [Why is SELECT * a problem?](#10-why-is-select--a-problem) |
| 11 | Your stories | [Tell me about a difficult legacy system you worked on.](#11-tell-me-about-a-difficult-legacy-system-you-worked-on) |
| 12 | Your stories | [What did you build with Kafka at Centric?](#12-what-did-you-build-with-kafka-at-centric) |
| 13 | Your stories | [Are you hands-on? What percentage of your day is coding?](#13-are-you-hands-on-what-percentage-of-your-day-is-coding) |
| 14 | Screener follow-ups | [Explain SOLID with a real example.](#14-explain-solid-with-a-real-example) |
| 15 | Screener follow-ups | [What are the benefits of dependency injection, beyond testing?](#15-what-are-the-benefits-of-dependency-injection-beyond-testing) |
| 16 | Screener follow-ups | [You wrote a class teammates need, in the same solution. How do you share it?](#16-you-wrote-a-class-teammates-need-in-the-same-solution-how-do-you-share-it) |
| 17 | Screener follow-ups | [Explain the Repository pattern. Isn't DbContext already one?](#17-explain-the-repository-pattern-isnt-dbcontext-already-one) |
| 18 | Screener follow-ups | [When would you use a Factory? Give an example.](#18-when-would-you-use-a-factory-give-an-example) |
| 19 | Screener follow-ups | [Find a number in a sorted array of 1 million ints, no built-ins.](#19-find-a-number-in-a-sorted-array-of-1-million-ints-no-built-ins) |
| 20 | Screener follow-ups | [Array of only 0s and 1s: move all 0s to the front in O(n).](#20-array-of-only-0s-and-1s-move-all-0s-to-the-front-in-on) |
| 21 | Screener follow-ups | [Country names and codes in two lists. Why a Dictionary?](#21-country-names-and-codes-in-two-lists-why-a-dictionary) |
| 22 | Screener follow-ups | [How does a Dictionary actually get O(1) lookups?](#22-how-does-a-dictionary-actually-get-o1-lookups) |
| 23 | Screener follow-ups | [Your country Dictionary lives in a Singleton and a nightly job reloads it while requests read. What goes wrong, and how do you fix it?](#23-your-country-dictionary-lives-in-a-singleton-and-a-nightly-job-reloads-it-while-requests-read-what-goes-wrong-and-how-do-you-fix-it) |
| 24 | Screener follow-ups | [If the lookup is a Singleton, how can Reload create a new Dictionary?](#24-if-the-lookup-is-a-singleton-how-can-reload-create-a-new-dictionary) |
| 25 | Basics | [IOptions vs IOptionsSnapshot vs IOptionsMonitor?](#25-ioptions-vs-ioptionssnapshot-vs-ioptionsmonitor) |
| 26 | Basics | [Abstract class vs interface?](#26-abstract-class-vs-interface) |
| 27 | Basics | [const vs readonly?](#27-const-vs-readonly) |
| 28 | Basics | [class vs struct?](#28-class-vs-struct) |
| 29 | Basics | [Why is string immutable, and when do you use StringBuilder?](#29-why-is-string-immutable-and-when-do-you-use-stringbuilder) |
| 30 | Basics | [ref vs out?](#30-ref-vs-out) |
| 31 | Basics | [What does using do with IDisposable?](#31-what-does-using-do-with-idisposable) |
| 32 | Basics | [== vs Equals()?](#32--vs-equals) |
| 33 | Basics | [Task vs Thread?](#33-task-vs-thread) |
| 34 | Basics | [virtual/override vs new?](#34-virtualoverride-vs-new) |
| 35 | Basics | [Filters vs middleware?](#35-filters-vs-middleware) |
| 36 | Basics | [What are the MVC filter types, in order?](#36-what-are-the-mvc-filter-types-in-order) |
| 37 | Basics | [How do model binding and validation work?](#37-how-do-model-binding-and-validation-work) |
| 38 | Basics | [[FromBody] vs [FromQuery] vs [FromRoute]?](#38-frombody-vs-fromquery-vs-fromroute) |
| 39 | Basics | [What is Kestrel?](#39-what-is-kestrel) |
| 40 | Basics | [What is CORS?](#40-what-is-cors) |
| 41 | Basics | [Minimal APIs vs controllers?](#41-minimal-apis-vs-controllers) |
| 42 | Basics | [Where does ASP.NET Core configuration come from, and in what order?](#42-where-does-aspnet-core-configuration-come-from-and-in-what-order) |
| 43 | Basics | [How do you log properly in .NET?](#43-how-do-you-log-properly-in-net) |
| 44 | Basics | [IActionResult vs ActionResult<T>?](#44-iactionresult-vs-actionresultt) |
| 45 | Basics | [What is a correlation ID?](#45-what-is-a-correlation-id) |
| 46 | Basics | [Write a minimal API endpoint.](#46-write-a-minimal-api-endpoint) |
| 47 | Basics | [How do you handle a question you haven't prepared?](#47-how-do-you-handle-a-question-you-havent-prepared) |
| 48 | Screener follow-ups | [Strategy pattern?](#48-strategy-pattern) |
| 49 | Screener follow-ups | [Decorator pattern?](#49-decorator-pattern) |
| 50 | Screener follow-ups | [Mediator / MediatR / CQRS?](#50-mediator--mediatr--cqrs) |
| 51 | Screener follow-ups | [Observer pattern?](#51-observer-pattern) |
| 52 | Screener follow-ups | [Singleton pattern?](#52-singleton-pattern) |
| 53 | Screener follow-ups | [Find the first non-repeating character in a string (e.g. "swiss" gives 'w'). No LINQ.](#53-find-the-first-non-repeating-character-in-a-string-eg-swiss-gives-w-no-linq) |
| 54 | Screener follow-ups | [An array holds 1 to 100 with one number missing, in any order. Find it. No built-ins.](#54-an-array-holds-1-to-100-with-one-number-missing-in-any-order-find-it-no-built-ins) |
| 55 | Screener follow-ups | [Two-sum: return the indexes of the two numbers that add up to a target.](#55-two-sum-return-the-indexes-of-the-two-numbers-that-add-up-to-a-target) |
| 56 | Screener follow-ups | [Reverse the words in a sentence ("I love coding" gives "coding love I"). No Split, no Reverse.](#56-reverse-the-words-in-a-sentence-i-love-coding-gives-coding-love-i-no-split-no-reverse) |
| 57 | Screener follow-ups | [Return all numbers that appear more than once ([4,3,2,7,8,2,3,1] gives [2,3]).](#57-return-all-numbers-that-appear-more-than-once-43278231-gives-23) |
| 58 | Basics | [What does string.Join do?](#58-what-does-stringjoin-do) |
| 59 | Basics | [What does GroupBy actually return? Visualise it.](#59-what-does-groupby-actually-return-visualise-it) |
| 60 | Kafka | [Why use Kafka instead of calling the other service's API?](#60-why-use-kafka-instead-of-calling-the-other-services-api) |
| 61 | Kafka | [Explain topics, partitions, offsets and consumer groups.](#61-explain-topics-partitions-offsets-and-consumer-groups) |
| 62 | Kafka | [How do you keep one account's Buy and Cancel in order?](#62-how-do-you-keep-one-accounts-buy-and-cancel-in-order) |
| 63 | Kafka | [A consumer processes a message but crashes before committing the offset.](#63-a-consumer-processes-a-message-but-crashes-before-committing-the-offset) |
| 64 | Kafka | [Why add a version number to events if Kafka keeps order?](#64-why-add-a-version-number-to-events-if-kafka-keeps-order) |
| 65 | Kafka | [Two consumers in the same group vs in different groups?](#65-two-consumers-in-the-same-group-vs-in-different-groups) |
| 66 | Kafka | [What's a dead-letter queue and when do you use it?](#66-whats-a-dead-letter-queue-and-when-do-you-use-it) |
| 67 | Kafka | [What's a rebalance?](#67-whats-a-rebalance) |
| 68 | Kafka | [Kafka vs a queue like MQ, RabbitMQ or Service Bus?](#68-kafka-vs-a-queue-like-mq-rabbitmq-or-service-bus) |
| 69 | Kafka | [Can more consumers than partitions make it faster?](#69-can-more-consumers-than-partitions-make-it-faster) |
| 70 | Kafka | [Is exactly-once delivery possible?](#70-is-exactly-once-delivery-possible) |
| 71 | Kafka | [Explain the transactional outbox pattern.](#71-explain-the-transactional-outbox-pattern) |
| 72 | Redis | [How do you implement caching with Redis?](#72-how-do-you-implement-caching-with-redis) |
| 73 | Redis | [How do you choose TTLs?](#73-how-do-you-choose-ttls) |
| 74 | Redis | [How do you invalidate the cache when data changes?](#74-how-do-you-invalidate-the-cache-when-data-changes) |
| 75 | Redis | [What's a cache stampede, and how do you prevent it?](#75-whats-a-cache-stampede-and-how-do-you-prevent-it) |
| 76 | Redis | [Redis goes down. What happens to your API?](#76-redis-goes-down-what-happens-to-your-api) |
| 77 | Redis | [In a trading platform, where would you use Redis, and what would you never trust a cache for?](#77-in-a-trading-platform-where-would-you-use-redis-and-what-would-you-never-trust-a-cache-for) |
| 78 | Redis | [Why shouldn't Redis be the source of truth for an account balance?](#78-why-shouldnt-redis-be-the-source-of-truth-for-an-account-balance) |
| 79 | Redis | [IMemoryCache vs Redis?](#79-imemorycache-vs-redis) |
| 80 | Redis | [What else is Redis used for besides caching?](#80-what-else-is-redis-used-for-besides-caching) |
| 81 | Redis | [What happens when Redis runs out of memory?](#81-what-happens-when-redis-runs-out-of-memory) |
| 82 | .NET core | [Transient vs Scoped vs Singleton?](#82-transient-vs-scoped-vs-singleton) |
| 83 | .NET core | [Why can't you inject a Scoped service into a Singleton?](#83-why-cant-you-inject-a-scoped-service-into-a-singleton) |
| 84 | .NET core | [How do you keep a Singleton thread-safe?](#84-how-do-you-keep-a-singleton-thread-safe) |
| 85 | .NET core | [What does async/await actually do? Does it create a thread?](#85-what-does-asyncawait-actually-do-does-it-create-a-thread) |
| 86 | .NET core | [Why is async void dangerous?](#86-why-is-async-void-dangerous) |
| 87 | .NET core | [What's wrong with .Result or .Wait()?](#87-whats-wrong-with-result-or-wait) |
| 88 | .NET core | [How do you run three independent calls in parallel?](#88-how-do-you-run-three-independent-calls-in-parallel) |
| 89 | .NET core | [Why use IHttpClientFactory?](#89-why-use-ihttpclientfactory) |
| 90 | .NET core | [IEnumerable vs IQueryable?](#90-ienumerable-vs-iqueryable) |
| 91 | .NET core | [What is middleware in ASP.NET Core?](#91-what-is-middleware-in-aspnet-core) |
| 92 | .NET core | [How do you handle exceptions globally in an API?](#92-how-do-you-handle-exceptions-globally-in-an-api) |
| 93 | .NET core | [How do you reduce memory allocations on large data?](#93-how-do-you-reduce-memory-allocations-on-large-data) |
| 94 | .NET core | [record vs class?](#94-record-vs-class) |
| 95 | EF Core & SQL | [What's the N+1 problem? How do you fix it?](#95-whats-the-n1-problem-how-do-you-fix-it) |
| 96 | EF Core & SQL | [What does AsNoTracking do, and when does it hurt?](#96-what-does-asnotracking-do-and-when-does-it-hurt) |
| 97 | EF Core & SQL | [Two users update the same balance at once. How do you stop a lost update?](#97-two-users-update-the-same-balance-at-once-how-do-you-stop-a-lost-update) |
| 98 | EF Core & SQL | [How do you deploy database changes safely?](#98-how-do-you-deploy-database-changes-safely) |
| 99 | EF Core & SQL | [Clustered vs nonclustered index? What's a key lookup?](#99-clustered-vs-nonclustered-index-whats-a-key-lookup) |
| 100 | EF Core & SQL | [Why would SQL Server ignore an index you created?](#100-why-would-sql-server-ignore-an-index-you-created) |
| 101 | EF Core & SQL | [What's parameter sniffing?](#101-whats-parameter-sniffing) |
| 102 | EF Core & SQL | [Two orders try to reserve the last unit at the same moment. How do you stop both succeeding?](#102-two-orders-try-to-reserve-the-last-unit-at-the-same-moment-how-do-you-stop-both-succeeding) |
| 103 | EF Core & SQL | [Does SQL Server lock rows by itself?](#103-does-sql-server-lock-rows-by-itself) |
| 104 | EF Core & SQL | [How do you prevent deadlocks in money transfers?](#104-how-do-you-prevent-deadlocks-in-money-transfers) |
| 105 | EF Core & SQL | [Add a NOT NULL column to a 50-million-row table without downtime.](#105-add-a-not-null-column-to-a-50-million-row-table-without-downtime) |
| 106 | EF Core & SQL | [Where should business logic live: stored procedures or C#?](#106-where-should-business-logic-live-stored-procedures-or-c) |
| 107 | EF Core & SQL | [Isolation levels, in one breath.](#107-isolation-levels-in-one-breath) |
| 108 | EF Core & SQL | [SQL: types of JOIN?](#108-sql-types-of-join) |
| 109 | EF Core & SQL | [SQL: WHERE vs HAVING?](#109-sql-where-vs-having) |
| 110 | EF Core & SQL | [SQL: DELETE vs TRUNCATE?](#110-sql-delete-vs-truncate) |
| 111 | EF Core & SQL | [SQL: UNION vs UNION ALL?](#111-sql-union-vs-union-all) |
| 112 | EF Core & SQL | [SQL: what's a CTE?](#112-sql-whats-a-cte) |
| 113 | EF Core & SQL | [SQL: ROW_NUMBER vs RANK vs DENSE_RANK?](#113-sql-rownumber-vs-rank-vs-denserank) |
| 114 | EF Core & SQL | [SQL: find the second-highest salary.](#114-sql-find-the-second-highest-salary) |
| 115 | EF Core & SQL | [SQL: delete duplicate rows but keep one.](#115-sql-delete-duplicate-rows-but-keep-one) |
| 116 | EF Core & SQL | [SQL: temp table vs table variable?](#116-sql-temp-table-vs-table-variable) |
| 117 | EF Core & SQL | [SQL: stored procedure vs function?](#117-sql-stored-procedure-vs-function) |
| 118 | EF Core & SQL | [SQL: what is ACID?](#118-sql-what-is-acid) |
| 119 | EF Core & SQL | [SQL: what is normalization?](#119-sql-what-is-normalization) |
| 120 | API & security | [What makes a RESTful API well designed?](#120-what-makes-a-restful-api-well-designed) |
| 121 | API & security | [POST vs PUT vs PATCH, and which are idempotent?](#121-post-vs-put-vs-patch-and-which-are-idempotent) |
| 122 | API & security | [Which status codes do you use, and when?](#122-which-status-codes-do-you-use-and-when) |
| 123 | API & security | [A client retries a timed-out order. How do you prevent a duplicate trade?](#123-a-client-retries-a-timed-out-order-how-do-you-prevent-a-duplicate-trade) |
| 124 | API & security | [How do you version an API?](#124-how-do-you-version-an-api) |
| 125 | API & security | [OAuth2 vs JWT?](#125-oauth2-vs-jwt) |
| 126 | API & security | [A partner system calls your API through APIM. Walk me through how it's secured.](#126-a-partner-system-calls-your-api-through-apim-walk-me-through-how-its-secured) |
| 127 | API & security | [How do users log in through the UI and call your API?](#127-how-do-users-log-in-through-the-ui-and-call-your-api) |
| 128 | API & security | [What does rotating secrets mean?](#128-what-does-rotating-secrets-mean) |
| 129 | API & security | [How do you implement authorization in .NET?](#129-how-do-you-implement-authorization-in-net) |
| 130 | API & security | [How does your API validate a JWT?](#130-how-does-your-api-validate-a-jwt) |
| 131 | API & security | [Name an OWASP risk you've mitigated.](#131-name-an-owasp-risk-youve-mitigated) |
| 132 | API & security | [How do you protect customer data and privacy?](#132-how-do-you-protect-customer-data-and-privacy) |
| 133 | API & security | [Where do secrets like connection strings go?](#133-where-do-secrets-like-connection-strings-go) |
| 134 | API & security | [What do you know about WCAG accessibility?](#134-what-do-you-know-about-wcag-accessibility) |
| 135 | Testing | [How do you test a service that consumes events and writes to a database?](#135-how-do-you-test-a-service-that-consumes-events-and-writes-to-a-database) |
| 136 | Testing | [Unit test vs integration test: where's the line?](#136-unit-test-vs-integration-test-wheres-the-line) |
| 137 | Testing | [How do you unit test a class that publishes to Kafka?](#137-how-do-you-unit-test-a-class-that-publishes-to-kafka) |
| 138 | Testing | [How do you test an API end to end?](#138-how-do-you-test-an-api-end-to-end) |
| 139 | Testing | [What makes a good unit test?](#139-what-makes-a-good-unit-test) |
| 140 | Testing | [Mock vs stub vs fake?](#140-mock-vs-stub-vs-fake) |
| 141 | Testing | [Do you practise TDD?](#141-do-you-practise-tdd) |
| 142 | Docker & OpenShift | [Image vs container vs Docker?](#142-image-vs-container-vs-docker) |
| 143 | Docker & OpenShift | [How do you write a Dockerfile for a .NET API?](#143-how-do-you-write-a-dockerfile-for-a-net-api) |
| 144 | Docker & OpenShift | [Explain the core Kubernetes objects.](#144-explain-the-core-kubernetes-objects) |
| 145 | Docker & OpenShift | [OpenShift vs Kubernetes?](#145-openshift-vs-kubernetes) |
| 146 | Docker & OpenShift | [Liveness vs readiness probe?](#146-liveness-vs-readiness-probe) |
| 147 | Docker & OpenShift | [Walk me through a CI/CD pipeline you've built.](#147-walk-me-through-a-cicd-pipeline-youve-built) |
| 148 | Docker & OpenShift | [How do you handle config per environment?](#148-how-do-you-handle-config-per-environment) |
| 149 | Git | [Git: merge vs rebase?](#149-git-merge-vs-rebase) |
| 150 | Git | [Git: what's your branching strategy?](#150-git-whats-your-branching-strategy) |
| 151 | Git | [Git: how do you resolve a merge conflict?](#151-git-how-do-you-resolve-a-merge-conflict) |
| 152 | Git | [What do you look for in a code review?](#152-what-do-you-look-for-in-a-code-review) |
| 153 | Git | [Git: revert vs reset?](#153-git-revert-vs-reset) |
| 154 | Azure | [Azure: App Service vs AKS vs Azure Functions?](#154-azure-app-service-vs-aks-vs-azure-functions) |
| 155 | Azure | [Azure: Event Hubs vs Service Bus vs Event Grid?](#155-azure-event-hubs-vs-service-bus-vs-event-grid) |
| 156 | Azure | [Azure: what is APIM for?](#156-azure-what-is-apim-for) |
| 157 | Azure | [Azure: Key Vault and Managed Identity?](#157-azure-key-vault-and-managed-identity) |
| 158 | Azure | [Azure: what does Application Insights give you?](#158-azure-what-does-application-insights-give-you) |
| 159 | Azure | [Azure: storage types?](#159-azure-storage-types) |
| 160 | Azure | [Azure: Table Storage vs Cosmos DB vs Azure SQL?](#160-azure-table-storage-vs-cosmos-db-vs-azure-sql) |
| 161 | Azure | [Azure: what is ACR?](#161-azure-what-is-acr) |
| 162 | Azure | [Azure: how does a request reach your AKS service?](#162-azure-how-does-a-request-reach-your-aks-service) |
| 163 | Azure | [Azure: what are deployment slots?](#163-azure-what-are-deployment-slots) |
| 164 | Azure | [Azure: how do you scale?](#164-azure-how-do-you-scale) |
| 165 | System design | [A client clicks 'Buy 100 shares'. Design what happens until the order reaches the market.](#165-a-client-clicks-buy-100-shares-design-what-happens-until-the-order-reaches-the-market) |
| 166 | System design | [Does the Direct Investing platform match buyers and sellers?](#166-does-the-direct-investing-platform-match-buyers-and-sellers) |
| 167 | System design | [Why return 202 Accepted instead of waiting for the market?](#167-why-return-202-accepted-instead-of-waiting-for-the-market) |
| 168 | System design | [Kafka is down when an order is placed. What happens?](#168-kafka-is-down-when-an-order-is-placed-what-happens) |
| 169 | System design | [How would a regulator reconstruct what happened to one order?](#169-how-would-a-regulator-reconstruct-what-happened-to-one-order) |
| 170 | System design | [How do you keep data consistent across microservices?](#170-how-do-you-keep-data-consistent-across-microservices) |
| 171 | System design | [Circuit breaker vs retry vs bulkhead?](#171-circuit-breaker-vs-retry-vs-bulkhead) |
| 172 | System design | [How would you push live price or order updates to the UI?](#172-how-would-you-push-live-price-or-order-updates-to-the-ui) |
| 173 | System design | [How does your design scale?](#173-how-does-your-design-scale) |
| 174 | Frontend | [Frontend: how do you position yourself if they go deep?](#174-frontend-how-do-you-position-yourself-if-they-go-deep) |
| 175 | Frontend | [Angular: component vs service? Lifecycle hooks?](#175-angular-component-vs-service-lifecycle-hooks) |
| 176 | Frontend | [Angular: Observables, the async pipe and switchMap?](#176-angular-observables-the-async-pipe-and-switchmap) |
| 177 | Frontend | [Angular: HTTP interceptor and route guard?](#177-angular-http-interceptor-and-route-guard) |
| 178 | Frontend | [Angular: change detection, OnPush, and modern Angular?](#178-angular-change-detection-onpush-and-modern-angular) |
| 179 | Frontend | [React: props vs state, useState, useEffect, virtual DOM?](#179-react-props-vs-state-usestate-useeffect-virtual-dom) |
| 180 | Behavioural | [Tell me about a disagreement with a teammate.](#180-tell-me-about-a-disagreement-with-a-teammate) |
| 181 | Behavioural | [Tell me about a production incident or a hard problem you solved.](#181-tell-me-about-a-production-incident-or-a-hard-problem-you-solved) |
| 182 | Behavioural | [How do you mentor other developers?](#182-how-do-you-mentor-other-developers) |
| 183 | Behavioural | [Why RBC, and why this role?](#183-why-rbc-and-why-this-role) |
| 184 | Behavioural | [You're okay with contract-to-hire?](#184-youre-okay-with-contract-to-hire) |
| 185 | Behavioural | [What questions do you have for us?](#185-what-questions-do-you-have-for-us) |
| 186 | CodeSignal | [Walk me through your banking solution, level by level.](#186-walk-me-through-your-banking-solution-level-by-level) |
| 187 | CodeSignal | [Level 3: show the transfer and the traps.](#187-level-3-show-the-transfer-and-the-traps) |
| 188 | CodeSignal | [Level 4: top spenders, and the traps.](#188-level-4-top-spenders-and-the-traps) |
| 189 | CodeSignal | [How would you have implemented the scheduled transfer?](#189-how-would-you-have-implemented-the-scheduled-transfer) |
| 190 | CodeSignal | [How would you improve your CodeSignal solution?](#190-how-would-you-improve-your-codesignal-solution) |

## 1. Tell me about yourself.

*Your stories*

**Formula:** Now, then before (1 to 2 highlights), then why this role. 60 to 90 seconds, then stop.

> "I'm a senior .NET developer with about ten years of experience, mostly C# and .NET Core backends with Angular or React front ends.

> Right now I'm at Staples, building .NET 8 microservices for inventory allocation and carrier integration. For example, I delivered the shipment flow end to end: we call a third-party carrier platform to pick the carrier, and publish events to the warehouse and transport systems through Google Pub/Sub and Azure Event Hubs. It runs on AKS with Azure DevOps pipelines.

> Before that I was lead developer at Accolite on a capital markets reporting SaaS for insightsoftware: equity-compensation reports like vesting and ESOP tax for corporate clients. A lot of my work there was performance: SQL tuning, execution plans, async and caching.

> What attracts me here is that this role combines exactly those things: event-driven .NET services, performance, and a financial domain, on a platform being rebuilt."

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

## 5. How do you keep stock consistent across multiple order management systems?

*Your stories*

> "The key is one source of truth. Our inventory service owns the stock numbers, the single pool of inventory, and the order management systems don't calculate stock themselves; they receive it.

> Every stock change is published as an event keyed by SKU, so changes for one product are processed in order. Each event carries a version number, so a late, older update is ignored instead of overwriting newer data. Consumers are idempotent, so a redelivered event doesn't change stock twice.

> Events can still fail, so a reconciliation pipeline periodically compares each system's stock with ours, fixes differences and alerts when drift crosses a threshold. Failing messages go to a dead-letter queue. So it's eventually consistent, with reconciliation as the safety net."

**Pattern:** one owner, then ordered and versioned events, then idempotent consumers, then reconciliation.

**Follow-up:** Why not one shared database for all systems? They're owned by different teams and vendors. A shared database couples them, so one team's schema change breaks everyone. Events keep them independent.

**[⬆ Back to Top](#table-of-contents)**

## 6. If the inventory service is the source of truth, why publish stock updates at all?

*Your stories*

> "The source of truth decides the numbers, but other systems still need to know them: the website shows availability on every page, and order systems check stock before accepting an order. They can't call us millions of times, so each keeps a read-only copy that our events keep current and reconciliation checks. Their copy never decides stock; ours wins."

Analogy: the bank is the source of truth, and your banking app shows a copy.

**[⬆ Back to Top](#table-of-contents)**

## 7. What was the Bounteous / insightsoftware platform, and what was your role?

*Your stories*

> "An equity-compensation reporting platform. Corporate clients used it to report on their employee stock plans: ESOP tax impact, vesting and unvesting schedules, grant reports. I was lead developer on the reporting team: building and changing reports end to end, API to database, and owning performance of the heavy ones."

**Follow-up:** Know a few domain words cold: grant, vesting schedule, cliff, exercise, unvested shares, fair market value.

**[⬆ Back to Top](#table-of-contents)**

## 8. How did you make the reports faster?

*Your stories*

1. **Diagnosis:** Datadog showed the API time was almost all inside the database call; the code path was already async.
1. **SELECT * → only needed columns.** Less I/O and network, and it lets indexes cover the query.
1. **Indexes** on the columns the reports filter and join on (client, grant date), checked in the execution plan.
1. **async/await end to end** so threads aren't blocked while waiting on SQL.
1. **Caching** data that rarely changes (plan definitions, reference data).

> "Heavy reports got significantly faster, roughly 40% on the worst ones."

**Follow-up:** Precision: async doesn't make one report faster. It improves throughput: the server handles many more concurrent report requests because threads aren't blocked.

**[⬆ Back to Top](#table-of-contents)**

## 9. How did you find which queries were slow?

*Your stories*

> "Datadog APM showed the time was spent in the database call, not in our code. Then I captured the slow queries with SQL Profiler and read their execution plans: table scans, key lookups, missing indexes."

**Follow-up:** Tooling: SQL Profiler is SQL Server only. On Oracle the equivalents are Explain Plan, AWR reports and SQL Trace/TKPROF.

**[⬆ Back to Top](#table-of-contents)**

## 10. Why is SELECT * a problem?

*Your stories*

- Reads and sends columns nobody uses: more I/O, network and memory.
- Prevents a covering index, so SQL does extra key lookups.
- Breaks or slows silently when someone adds a large column later.

**[⬆ Back to Top](#table-of-contents)**

## 11. Tell me about a difficult legacy system you worked on.

*Your stories*

> "Most business logic lived in stored procedures: thousands of lines of PL/SQL, procedures calling other procedures, with loops and cursors. The C# and Angular layers mostly just called them. It was hard to debug, hard to unit test and risky to change. It taught me why business logic belongs in the application layer, where it's testable, version-controlled and easy to scale, with SQL focused on data access."

**Follow-up:** Frame it as a lesson learned, not a complaint. If asked how you worked in it: trace the call chain, add logging, make small safe changes.

**[⬆ Back to Top](#table-of-contents)**

## 12. What did you build with Kafka at Centric?

*Your stories*

> "On an insurance platform, documents for different products were generated through Kafka. When a user requested a document, an event with the JSON payload was published to a topic per document type. I built consumer services that picked up the JSON, generated the PDF and stored it in Blob storage, where the UI read it from. The Kafka platform itself was set up by another team; my part was the consumers."

**Follow-up:** Likely follow-up: what if PDF generation fails halfway? Don't commit the offset until the PDF is stored. Retry, then dead-letter. Make it idempotent so a re-delivered message doesn't create a second document.

**[⬆ Back to Top](#table-of-contents)**

## 13. Are you hands-on? What percentage of your day is coding?

*Your stories*

> "Mostly hands-on. The majority of my day is design and coding; the rest is code reviews, sprint work with the team and mentoring. I like staying close to the code."

**[⬆ Back to Top](#table-of-contents)**

## 14. Explain SOLID with a real example.

*Screener follow-ups*

- **S**: one reason to change. `ShipmentService` runs the flow; `PubSubPublisher` only talks to Pub/Sub.
- **O**: extend without editing. A partner wants Kafka: add `KafkaPublisher`, nothing else changes.
- **L**: any implementation can replace another. A publisher that silently swallows errors would break the caller's retry logic.
- **I**: small interfaces. Publishing and consuming are separate interfaces.
- **D**: depend on `IEventPublisher`, never `new PubSubPublisher()`.

**[⬆ Back to Top](#table-of-contents)**

## 15. What are the benefits of dependency injection, beyond testing?

*Screener follow-ups*

- Loose coupling: callers depend on an interface, so implementations can be swapped.
- Dependencies are visible in the constructor instead of hidden.
- The container manages lifetimes (Transient, Scoped, Singleton) and disposal.
- Configuration lives in one place (Program.cs).
- And yes, unit tests can inject mocks.

**[⬆ Back to Top](#table-of-contents)**

## 16. You wrote a class teammates need, in the same solution. How do you share it?

*Screener follow-ups*

> "Within one solution, a project reference; NuGet is for sharing across solutions. For how teammates use it, I expose an interface and register the implementation in DI, so their code depends only on the contract, can be tested with mocks, and doesn't break when my implementation changes."

**Follow-up:** Why not a static class? Can't be mocked or swapped, hides dependencies, can't receive a DbContext or HttpClient. Static is fine for pure helpers like Math.Max.

**[⬆ Back to Top](#table-of-contents)**

## 17. Explain the Repository pattern. Isn't DbContext already one?

*Screener follow-ups*

> "A repository puts data access behind an interface, so services contain no EF or SQL, and I can mock it in tests. DbContext is already a unit of work and repository, so for simple CRUD I often use it directly. I add a repository when I want query logic in one place or EF out of the domain. I avoid a generic IRepository<T> that just wraps DbSet."

**Follow-up:** The repository doesn't call SaveChanges. The caller saves once per request so several changes commit together.

**[⬆ Back to Top](#table-of-contents)**

## 18. When would you use a Factory? Give an example.

*Screener follow-ups*

> "When which object to create depends on data at runtime. My example: a PublisherFactory. DI injects all IEventPublisher implementations, the factory stores them in a Dictionary by destination, and callers ask for 'WMS' or 'TMS'. Adding Kafka is one new class and one registration line."

**Follow-up:** Factory vs DI: DI when the type is known at startup, a factory when it depends on runtime data. They work together.

**[⬆ Back to Top](#table-of-contents)**

## 19. Find a number in a sorted array of 1 million ints, no built-ins.

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

## 20. Array of only 0s and 1s: move all 0s to the front in O(n).

*Screener follow-ups*

**With library:** `Array.Sort(bits);` works but is O(n log n). Faster built-in-ish: count the zeros, then fill. The two-pointer swap is O(n) in one pass.

**Without library:**

> "Two pointers, one at each end. A 0 on the left is in place, so move left forward. A 1 on the right is in place, so move right back. If both are wrong, swap them and move both. Each element is visited once: O(n) time, O(1) space, in place."

**Follow-up:** Mirror version (1s first): same algorithm with the value flipped, so pass the front value in as a parameter.

**[⬆ Back to Top](#table-of-contents)**

## 21. Country names and codes in two lists. Why a Dictionary?

*Screener follow-ups*

**With library:** `var lookup = names.Zip(codes).ToDictionary(p => p.First, p => p.Second);` Zip pairs the two lists item by item.

**Without library:** a for loop adding names[i] to codes[i].

> "Build a Dictionary once, O(n). After that every lookup is O(1). With two lists, every lookup scans the list, O(n) each time, and the two lists can drift out of sync."

**Follow-up:** Bonus: new Dictionary(StringComparer.OrdinalIgnoreCase) so 'canada' matches 'Canada'.

**[⬆ Back to Top](#table-of-contents)**

## 22. How does a Dictionary actually get O(1) lookups?

*Screener follow-ups*

- It calls `GetHashCode()` on the key and maps it to a bucket.
- It goes straight to that bucket and confirms the key with `Equals()`.
- Different keys landing in one bucket are a collision; they're chained, so a lookup checks a few entries.
- When it fills up, it resizes and rehashes into a bigger array.

**Follow-up:** Worst case is O(n) if many keys collide. Never change a key object's fields after inserting it, or its hash changes and you can't find it.

**[⬆ Back to Top](#table-of-contents)**

## 23. Your country Dictionary lives in a Singleton and a nightly job reloads it while requests read. What goes wrong, and how do you fix it?

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

## 24. If the lookup is a Singleton, how can Reload create a new Dictionary?

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

## 25. IOptions vs IOptionsSnapshot vs IOptionsMonitor?

*Basics*

- **IOptions**: reads config once at startup, never changes. Singleton.
- **IOptionsSnapshot**: re-reads per request. Scoped, so not usable in a Singleton.
- **IOptionsMonitor**: always current (`CurrentValue`) plus `OnChange`. Singleton-safe, for background services.

**[⬆ Back to Top](#table-of-contents)**

## 26. Abstract class vs interface?

*Basics*

> "An interface is a contract with no state. An abstract class can hold shared code and fields. A class can implement many interfaces but inherit only one class."

**[⬆ Back to Top](#table-of-contents)**

## 27. const vs readonly?

*Basics*

> "const is fixed at compile time and baked into calling code. readonly is set once, at declaration or in the constructor, so it can hold runtime values."

**[⬆ Back to Top](#table-of-contents)**

## 28. class vs struct?

*Basics*

> "A class is a reference type on the heap. A struct is a value type copied on assignment, good for small immutable values like a point or an amount."

**[⬆ Back to Top](#table-of-contents)**

## 29. Why is string immutable, and when do you use StringBuilder?

*Basics*

> "Every change creates a new string. Concatenating in a loop creates thousands of throwaway strings; StringBuilder edits one buffer."

**[⬆ Back to Top](#table-of-contents)**

## 30. ref vs out?

*Basics*

> "Both pass by reference. ref must be initialised before the call; out must be assigned inside the method, like TryGetValue."

**[⬆ Back to Top](#table-of-contents)**

## 31. What does using do with IDisposable?

*Basics*

> "It guarantees Dispose() runs even if an exception happens, releasing connections and file handles immediately instead of waiting for the GC."

**[⬆ Back to Top](#table-of-contents)**

## 32. == vs Equals()?

*Basics*

> "For classes, == checks whether it's the same object unless overridden; string overrides it to compare text. Equals can be overridden for value equality, and records do it automatically."

**[⬆ Back to Top](#table-of-contents)**

## 33. Task vs Thread?

*Basics*

> "A Thread is an OS thread, which is expensive. A Task is a unit of work scheduled on the thread pool, lighter and awaitable. Modern code almost always uses Tasks."

**[⬆ Back to Top](#table-of-contents)**

## 34. virtual/override vs new?

*Basics*

> "override replaces the base behaviour even when called through a base reference. new only hides it, so calling through the base type still runs the base version."

**[⬆ Back to Top](#table-of-contents)**

## 35. Filters vs middleware?

*Basics*

> "Middleware wraps every request in the pipeline, even ones that never reach MVC. Filters run inside MVC around controllers and actions, so they know which action is running. Filters suit validation or action-level logging."

**[⬆ Back to Top](#table-of-contents)**

## 36. What are the MVC filter types, in order?

*Basics*

Authorization, Resource, Action, Exception, Result. Action filters are the ones you write most, to validate input or log timing.

**[⬆ Back to Top](#table-of-contents)**

## 37. How do model binding and validation work?

*Basics*

> "Model binding maps route, query, body and header values onto action parameters. Data annotations like [Required] or [Range] validate them, and with [ApiController] an invalid model automatically returns 400 with the errors."

**[⬆ Back to Top](#table-of-contents)**

## 38. [FromBody] vs [FromQuery] vs [FromRoute]?

*Basics*

Where the value comes from: the JSON body, the query string (`?page=2`), or the URL path (`/orders/{id}`).

**[⬆ Back to Top](#table-of-contents)**

## 39. What is Kestrel?

*Basics*

> "The cross-platform web server built into ASP.NET Core. In containers it serves traffic directly, usually behind a load balancer or ingress."

**[⬆ Back to Top](#table-of-contents)**

## 40. What is CORS?

*Basics*

> "Browsers block a page from calling an API on another domain unless the API allows it. CORS configures which origins, methods and headers are allowed. It's a browser protection, so server-to-server calls aren't affected."

**[⬆ Back to Top](#table-of-contents)**

## 41. Minimal APIs vs controllers?

*Basics*

> "Minimal APIs map endpoints directly in Program.cs with less ceremony, good for small services. Controllers suit larger APIs with filters, conventions and more structure."

**[⬆ Back to Top](#table-of-contents)**

## 42. Where does ASP.NET Core configuration come from, and in what order?

*Basics*

appsettings.json, then appsettings.{Environment}.json, then user secrets (dev), then environment variables, then command-line args. Later sources override earlier ones, which is why env vars and ConfigMaps override JSON in Kubernetes.

**[⬆ Back to Top](#table-of-contents)**

## 43. How do you log properly in .NET?

*Basics*

> "Inject ILogger<T> and use structured logging, like LogInformation("Order {OrderId} placed", orderId), not string concatenation, so tools like Datadog can search by OrderId. Add a correlation id to trace one request across services."

**[⬆ Back to Top](#table-of-contents)**

## 44. IActionResult vs ActionResult<T>?

*Basics*

> "ActionResult<T> lets you return either the data or a status result like NotFound(), and tells Swagger the response type. It's the modern default for APIs."

**[⬆ Back to Top](#table-of-contents)**

## 45. What is a correlation ID?

*Basics*

> "A unique ID created when a request first enters the system, usually at the gateway. It's passed in a header to every service the request touches and included in every log line, so in Datadog I can search one ID and see the whole journey of that request across services."

**Follow-up:** Answer from what you do daily. Describing your real usage IS the best answer.

**[⬆ Back to Top](#table-of-contents)**

## 46. Write a minimal API endpoint.

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

## 47. How do you handle a question you haven't prepared?

*Basics*

1. **Start from the purpose:** "Filters exist so you can run code around an action without repeating it..."
1. **Connect to experience:** "We used an action filter to log request timing..."
1. **Reason out loud** about the uncertain part: "I believe X runs before Y, but I'd confirm in the docs."
1. **Be honest about the edge:** "I haven't gone deep on that, but based on how the pipeline works I'd expect..."

They grade how you think, not perfect recall.

**[⬆ Back to Top](#table-of-contents)**

## 48. Strategy pattern?

*Screener follow-ups*

> "Swap an algorithm at runtime behind one interface, like IShippingRateStrategy with an implementation per carrier. It removes big if/else chains."

**[⬆ Back to Top](#table-of-contents)**

## 49. Decorator pattern?

*Screener follow-ups*

> "Wrap an object to add behaviour without changing it, like a caching or logging wrapper around a repository with the same interface. Polly's retry around HttpClient is the same idea."

**[⬆ Back to Top](#table-of-contents)**

## 50. Mediator / MediatR / CQRS?

*Screener follow-ups*

> "Controllers send a command or query object and one handler processes it, keeping controllers thin. CQRS separates writes (commands) from reads (queries) so each can be optimised, like reads from a replica or cache."

**[⬆ Back to Top](#table-of-contents)**

## 51. Observer pattern?

*Screener follow-ups*

> "Subscribers are notified when something changes. C# events are the built-in form; Kafka consumers are the distributed version of the same idea."

**[⬆ Back to Top](#table-of-contents)**

## 52. Singleton pattern?

*Screener follow-ups*

> "One instance for the whole app. In modern .NET I register it with AddSingleton and let DI manage it, which keeps it testable. Hand-written, I'd use Lazy<T> for thread-safe initialisation."

**[⬆ Back to Top](#table-of-contents)**

## 53. Find the first non-repeating character in a string (e.g. "swiss" gives 'w'). No LINQ.

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

## 54. An array holds 1 to 100 with one number missing, in any order. Find it. No built-ins.

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

## 55. Two-sum: return the indexes of the two numbers that add up to a target.

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

## 56. Reverse the words in a sentence ("I love coding" gives "coding love I"). No Split, no Reverse.

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

## 57. Return all numbers that appear more than once ([4,3,2,7,8,2,3,1] gives [2,3]).

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

## 58. What does string.Join do?

*Basics*

Takes every element of a collection and puts the separator BETWEEN them (not at the ends).

```csharp
string.Join(" ", new[] { "coding", "love", "I" })   // "coding love I"
string.Join(", ", new[] { "a", "b", "c" })           // "a, b, c"
```

**[⬆ Back to Top](#table-of-contents)**

## 59. What does GroupBy actually return? Visualise it.

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

## 60. Why use Kafka instead of calling the other service's API?

*Kafka*

> "Decoupling. The producer writes once and doesn't need to know who's listening or whether they're up. If a consumer is down, messages wait in Kafka and it catches up later. New consumers like audit or analytics can be added without touching the producer."

**[⬆ Back to Top](#table-of-contents)**

## 61. Explain topics, partitions, offsets and consumer groups.

*Kafka*

- **Topic**: a named stream, like `orders`.
- **Partition**: a topic is split into ordered logs for parallelism. On disk each is a folder of log segments.
- **Offset**: a message's position within a partition.
- **Consumer group**: consumers sharing the work. Each partition goes to one consumer in the group.

Messages stay until retention removes them. Reading doesn't delete them.

**[⬆ Back to Top](#table-of-contents)**

## 62. How do you keep one account's Buy and Cancel in order?

*Kafka*

> "Kafka only guarantees order within a partition. I use AccountId as the message key, and the same key always goes to the same partition, so each account's events stay in order while different accounts are processed in parallel."

**Follow-up:** Without a key, Cancel could be processed before Buy.

**[⬆ Back to Top](#table-of-contents)**

## 63. A consumer processes a message but crashes before committing the offset.

*Kafka*

> "After restart it resumes from the last committed offset, so that message is delivered again. That's at-least-once delivery. The consumer must be idempotent: store processed message ids with a unique constraint and skip duplicates."

**Follow-up:** Commit after processing, not before. Committing first risks losing the message if you crash mid-processing.

**[⬆ Back to Top](#table-of-contents)**

## 64. Why add a version number to events if Kafka keeps order?

*Kafka*

> "Kafka only guarantees order within a partition. Retries, replays or a second producer can still deliver an older update late. With a version, the consumer ignores anything older than what it already has."

Example: v2 (stock 8) arrives, then v1 (stock 10) arrives late. The consumer already has v2, so it ignores v1. Without the version, stock jumps back to 10 and you oversell.

**Follow-up:** The version must be assigned by the owner of the data, such as a counter in the inventory database. Versions invented by different producers can't be compared.

**[⬆ Back to Top](#table-of-contents)**

## 65. Two consumers in the same group vs in different groups?

*Kafka*

> "Same group: they split the partitions, which is load balancing. Different groups: each gets every message, which is broadcast, like an order service and an audit service both reading all orders."

**[⬆ Back to Top](#table-of-contents)**

## 66. What's a dead-letter queue and when do you use it?

*Kafka*

> "When a message keeps failing because of bad data or a bug, I don't retry forever and block the partition. After N retries I move it to a dead-letter topic, alert, and keep processing. Someone fixes the cause and replays it."

**[⬆ Back to Top](#table-of-contents)**

## 67. What's a rebalance?

*Kafka*

> "When a consumer joins or leaves a group, Kafka reassigns partitions. Processing pauses briefly, and uncommitted messages may be reprocessed, which is another reason consumers must be idempotent."

**[⬆ Back to Top](#table-of-contents)**

## 68. Kafka vs a queue like MQ, RabbitMQ or Service Bus?

*Kafka*

> "In a queue a message is removed once consumed and goes to one receiver. Kafka is a log: messages stay for the retention period, many groups read independently, and you can replay from an older offset. Queues fit commands and task distribution; Kafka fits event streams and high throughput."

**[⬆ Back to Top](#table-of-contents)**

## 69. Can more consumers than partitions make it faster?

*Kafka*

> "No. Each partition is read by one consumer per group, so extra consumers sit idle. The partition count is the maximum parallelism, so size it for future load."

**[⬆ Back to Top](#table-of-contents)**

## 70. Is exactly-once delivery possible?

*Kafka*

> "Inside Kafka, yes, with an idempotent producer and transactions. End to end across a database and external systems it's rare, so in practice teams build at-least-once delivery plus idempotent consumers. The result is effectively-once processing."

**[⬆ Back to Top](#table-of-contents)**

## 71. Explain the transactional outbox pattern.

*Kafka*

> "Writing to the database and publishing to Kafka are two separate systems, so one can succeed while the other fails. With an outbox, I write the business row and an outbox row in the same database transaction. A background worker publishes pending outbox rows and marks them sent. Nothing is lost if Kafka is down or the service crashes; delivery is at-least-once, so consumers are idempotent."

**[⬆ Back to Top](#table-of-contents)**

## 72. How do you implement caching with Redis?

*Redis*

**Cache-aside**, the most common pattern:

1. Read: check Redis. On a hit, return it.
1. On a miss, read from SQL, store it in Redis with a TTL, return it.
1. On a write: update SQL, then **delete** the cache key.

In .NET: `IDistributedCache` or `StackExchange.Redis`. In .NET 9+, `HybridCache` adds an in-memory layer and stampede protection.

**[⬆ Back to Top](#table-of-contents)**

## 73. How do you choose TTLs?

*Redis*

> "By how stale the data is allowed to be. Data that changes often gets a short TTL, around 5 minutes. Reference data that rarely changes gets an hour or more. I add a little random jitter so thousands of keys don't expire at the same moment."

**Follow-up:** First question to ask in any caching discussion: how stale can this data be? That drives the whole design.

**[⬆ Back to Top](#table-of-contents)**

## 74. How do you invalidate the cache when data changes?

*Redis*

> "On write, I update the database, then delete the key. The next read fetches fresh data. I delete rather than update the cached value, because two concurrent writers could otherwise leave a stale value in the cache. The TTL is a safety net. When another service changes the data, it publishes an event and our consumer evicts the key."

**[⬆ Back to Top](#table-of-contents)**

## 75. What's a cache stampede, and how do you prevent it?

*Redis*

> "A popular key expires and hundreds of requests miss at once, so they all hit the database together. I let one request rebuild the value while the others wait for its result, using a lock or request coalescing. I also add TTL jitter and refresh hot keys before they expire. HybridCache in .NET does the coalescing for you."

**[⬆ Back to Top](#table-of-contents)**

## 76. Redis goes down. What happens to your API?

*Redis*

> "The cache must be optional. Redis calls get short timeouts, and a failure falls back to the database. A circuit breaker stops us waiting on Redis for every call while it's down. Because the database suddenly takes all the load, I protect it with rate limiting, and monitoring alerts the team."

**[⬆ Back to Top](#table-of-contents)**

## 77. In a trading platform, where would you use Redis, and what would you never trust a cache for?

*Redis*

**Rule: Redis for display, the source of truth for decisions.**

> "I'd use Redis for data that's read constantly where a tiny delay is fine: user profiles and preferences, reference data like instrument details, and live quotes for display, which the market data feed pushes into Redis on every tick so it's always current.

> What I'd never rely on a cache for is anything that moves money: buying power and balances when approving an order, positions when checking whether a client can sell, and order status transitions. Those come from the source of truth, and the execution price comes from the market at trade time, not a cached quote."

**Follow-up:** Common mistake: saying you'd never cache stock prices. Live quotes are a classic Redis use; the point is not to make trading decisions from them. Holdings can be cached for the portfolio screen, invalidated by fill events, but the sell check reads the database.

**[⬆ Back to Top](#table-of-contents)**

## 78. Why shouldn't Redis be the source of truth for an account balance?

*Redis*

> "A cache can be stale, evicted under memory pressure, or lose recent writes on failover. You can't approve a trade against a stale balance. SQL is the source of truth; Redis only speeds up reads where slightly old data is acceptable."

**[⬆ Back to Top](#table-of-contents)**

## 79. IMemoryCache vs Redis?

*Redis*

> "IMemoryCache lives inside one app instance: fastest, but each pod has its own copy and they can disagree. Redis is shared by all instances, so every pod sees the same data and the cache survives restarts. With several pods on Kubernetes, I use Redis, sometimes with a small in-memory layer in front."

**[⬆ Back to Top](#table-of-contents)**

## 80. What else is Redis used for besides caching?

*Redis*

- Sessions shared across instances
- Rate limiting with counters and expiry
- Distributed locks
- Sorted sets for leaderboards and rankings
- Pub/sub, for example as a SignalR backplane

**[⬆ Back to Top](#table-of-contents)**

## 81. What happens when Redis runs out of memory?

*Redis*

> "It evicts keys according to its maxmemory policy. allkeys-lru removes the least recently used keys; volatile-lru only removes keys that have a TTL. For a cache I'd use an LRU policy, always set TTLs, and monitor memory and hit rate."

**[⬆ Back to Top](#table-of-contents)**

## 82. Transient vs Scoped vs Singleton?

*.NET core*

- **Transient**: new instance every time. Lightweight stateless helpers.
- **Scoped**: one per HTTP request. DbContext, current user.
- **Singleton**: one for the app. Config, caches, Kafka producers.

**Follow-up:** Transient DbContext bug: two repositories get two DbContexts, so one SaveChanges doesn't include the other's changes.

**[⬆ Back to Top](#table-of-contents)**

## 83. Why can't you inject a Scoped service into a Singleton?

*.NET core*

> "The Singleton lives forever and keeps the Scoped DbContext it got from the first request. Every later request, on different threads, shares that one DbContext, which isn't thread-safe. It's a captive dependency. The fix is IServiceScopeFactory: create a scope when you need the DbContext."

**Follow-up:** Real example: a BackgroundService (always a Singleton) like an outbox worker creating a scope per batch.

**[⬆ Back to Top](#table-of-contents)**

## 84. How do you keep a Singleton thread-safe?

*.NET core*

> "Best is no mutable state. If it must hold state: ConcurrentDictionary for shared lookups, lock when several fields change together, Interlocked for counters. The danger is check-then-act: two threads both check 'not there' and both add."

**Follow-up:** count++ is read, add, write. Two threads both read 5 and both write 6, so an update is lost. That's a race condition.

**[⬆ Back to Top](#table-of-contents)**

## 85. What does async/await actually do? Does it create a thread?

*.NET core*

> "It doesn't create a thread. At an await on I/O, the thread goes back to the pool to serve other requests. When the I/O completes, a pool thread continues the method. That's how a server handles many more requests with the same threads."

**[⬆ Back to Top](#table-of-contents)**

## 86. Why is async void dangerous?

*.NET core*

> "It can't be awaited, so the caller doesn't know when it finishes, and an exception can crash the process because nothing can catch it. Always return Task. The only exception is event handlers."

**[⬆ Back to Top](#table-of-contents)**

## 87. What's wrong with .Result or .Wait()?

*.NET core*

> "It blocks a thread while waiting, which throws away the benefit of async and can cause thread-pool starvation. In older ASP.NET and UI apps it can deadlock. Go async all the way."

**[⬆ Back to Top](#table-of-contents)**

## 88. How do you run three independent calls in parallel?

*.NET core*

> "Start all three tasks, then await Task.WhenAll. Total time is the slowest call, not the sum."

**[⬆ Back to Top](#table-of-contents)**

## 89. Why use IHttpClientFactory?

*.NET core*

> "A new HttpClient per request exhausts sockets, because closed connections sit in TIME_WAIT. A single static client never picks up DNS changes. IHttpClientFactory pools and recycles handlers, so you avoid both problems."

**[⬆ Back to Top](#table-of-contents)**

## 90. IEnumerable vs IQueryable?

*.NET core*

> "IQueryable builds an expression that EF translates to SQL, so filtering happens in the database. IEnumerable works in memory on data already loaded. Calling ToList too early loads the whole table and filters in C#."

**Follow-up:** Deferred execution: building the query does nothing. It runs at ToList, First, Count or foreach.

**[⬆ Back to Top](#table-of-contents)**

## 91. What is middleware in ASP.NET Core?

*.NET core*

> "The request passes through an ordered pipeline of components: exception handling, authentication, authorization, logging. Each can act before and after the next one. Order matters: authentication before authorization. I've written custom middleware for correlation ids and global error handling."

**[⬆ Back to Top](#table-of-contents)**

## 92. How do you handle exceptions globally in an API?

*.NET core*

> "One place, not try/catch everywhere: exception-handling middleware, or IExceptionHandler in .NET 8. It logs the error with a correlation id and returns a consistent ProblemDetails response without leaking stack traces. Predictable conditions like 'not found' are handled explicitly, not with exceptions."

**[⬆ Back to Top](#table-of-contents)**

## 93. How do you reduce memory allocations on large data?

*.NET core*

- Stream data instead of loading everything into memory.
- `Span` / `ReadOnlySpan` to slice strings and arrays without copying.
- `StringBuilder` instead of string concatenation in loops.
- `ArrayPool` to reuse buffers.

Fewer allocations mean less GC work and fewer pauses.

**Follow-up:** GC basics: generations 0, 1, 2. Most objects die young in Gen 0. Objects over 85 KB go to the Large Object Heap, which is expensive to collect.

**[⬆ Back to Top](#table-of-contents)**

## 94. record vs class?

*.NET core*

> "A record has value equality (two records with the same data are equal) and is immutable by default, which makes it good for DTOs and events. A class has reference equality and is the choice for entities with behaviour and changing state."

**[⬆ Back to Top](#table-of-contents)**

## 95. What's the N+1 problem? How do you fix it?

*EF Core & SQL*

> "One query loads a list, then one extra query runs per item inside a loop: 100 orders become 101 database trips. Fix with Include, which loads the related data in the same query, or a Select projection when I only need a few fields."

**[⬆ Back to Top](#table-of-contents)**

## 96. What does AsNoTracking do, and when does it hurt?

*EF Core & SQL*

> "Normally EF keeps a copy of each loaded entity's original values and compares them on SaveChanges to generate updates. AsNoTracking skips that: faster and less memory, ideal for read-only queries. It hurts if you then change the entity and call SaveChanges, because nothing is saved."

**[⬆ Back to Top](#table-of-contents)**

## 97. Two users update the same balance at once. How do you stop a lost update?

*EF Core & SQL*

> "Optimistic concurrency. A rowversion column ([Timestamp] in EF). The update includes WHERE RowVersion = the value I read. If someone saved first, 0 rows are updated and EF throws DbUpdateConcurrencyException. I reload and retry, or tell the user."

**Follow-up:** Pessimistic alternative: lock the row when reading. Safer under heavy contention but blocks others.

**[⬆ Back to Top](#table-of-contents)**

## 98. How do you deploy database changes safely?

*EF Core & SQL*

> "EF Core migrations, reviewed in the PR like code. For production I generate an idempotent SQL script with dotnet ef migrations script --idempotent, and the pipeline or a DBA runs it. I don't let the app migrate itself on startup: several instances would race, and it would need admin permissions."

**[⬆ Back to Top](#table-of-contents)**

## 99. Clustered vs nonclustered index? What's a key lookup?

*EF Core & SQL*

> "The clustered index is the table itself, stored in key order, so there's one. A nonclustered index is a separate sorted copy of some columns with a pointer back to the row. If the query needs a column that isn't in the index, SQL jumps back to the table for every row: a key lookup. A covering index with INCLUDE removes it."

**[⬆ Back to Top](#table-of-contents)**

## 100. Why would SQL Server ignore an index you created?

*EF Core & SQL*

> "If the query matches many rows, thousands of key lookups cost more than one scan of the table, so the optimizer scans instead. There's no fixed percentage; it's a cost estimate and often a small fraction of rows. A covering index fixes it."

**Follow-up:** Every index slows inserts and updates and uses storage, so index the frequent, important queries, not everything.

**[⬆ Back to Top](#table-of-contents)**

## 101. What's parameter sniffing?

*EF Core & SQL*

> "SQL builds a plan using the first parameter value it sees and reuses it. If the first call returned 10 rows, the plan suits small results, and a later call returning a million rows reuses that bad plan. The sign is: fast in SSMS, slow in the app. Fixes: OPTION (RECOMPILE), OPTIMIZE FOR, or a covering index."

**[⬆ Back to Top](#table-of-contents)**

## 102. Two orders try to reserve the last unit at the same moment. How do you stop both succeeding?

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

## 103. Does SQL Server lock rows by itself?

*EF Core & SQL*

> "Yes, automatically. An UPDATE, INSERT or DELETE takes an exclusive lock on the rows it changes and holds it until the transaction commits. Anyone else changing those rows waits, and under the default Read Committed, readers wait too, so nobody sees a half-finished change. That's why a single conditional UPDATE is atomic."

**[⬆ Back to Top](#table-of-contents)**

## 104. How do you prevent deadlocks in money transfers?

*EF Core & SQL*

> "A deadlock is a circle: A holds account 1 and wants 2, B holds 2 and wants 1. I always lock in the same order, lower account id first, so a circle can't form; the second transfer just waits. I also keep transactions short. To diagnose, I read the deadlock graph from Extended Events."

**[⬆ Back to Top](#table-of-contents)**

## 105. Add a NOT NULL column to a 50-million-row table without downtime.

*EF Core & SQL*

1. Add it as nullable. Instant, metadata only.
1. Deploy code that always writes the new column.
1. Backfill old rows in batches of a few thousand so locks stay short.
1. Switch the column to NOT NULL.

**[⬆ Back to Top](#table-of-contents)**

## 106. Where should business logic live: stored procedures or C#?

*EF Core & SQL*

> "In the application layer. There it's unit-testable, version-controlled, debuggable, and scales by adding app instances instead of loading the database. Stored procedures still make sense for heavy set-based data work close to the data. I've seen the opposite: thousands of lines of nested PL/SQL that nobody could safely change."

**[⬆ Back to Top](#table-of-contents)**

## 107. Isolation levels, in one breath.

*EF Core & SQL*

> "The default is Read Committed: you only see committed data, but readers can wait on writers. Read Committed Snapshot lets readers see the last committed version without blocking. Serializable is safest but blocks most. For balances I prefer short transactions plus optimistic concurrency."

**[⬆ Back to Top](#table-of-contents)**

## 108. SQL: types of JOIN?

*EF Core & SQL*

> "INNER returns only matching rows. LEFT returns everything from the left with NULLs where there's no match. RIGHT is the mirror. FULL returns everything from both. CROSS gives every combination."

**[⬆ Back to Top](#table-of-contents)**

## 109. SQL: WHERE vs HAVING?

*EF Core & SQL*

> "WHERE filters rows before grouping. HAVING filters groups after GROUP BY, like HAVING COUNT(*) > 5."

**[⬆ Back to Top](#table-of-contents)**

## 110. SQL: DELETE vs TRUNCATE?

*EF Core & SQL*

> "DELETE removes rows one by one, can use WHERE, fires triggers and is fully logged. TRUNCATE removes all rows at once, is minimally logged, resets identity, and can't use WHERE."

**[⬆ Back to Top](#table-of-contents)**

## 111. SQL: UNION vs UNION ALL?

*EF Core & SQL*

> "UNION removes duplicates, which needs a sort, so it's slower. UNION ALL keeps everything and is faster; I use it unless I need duplicates removed."

**[⬆ Back to Top](#table-of-contents)**

## 112. SQL: what's a CTE?

*EF Core & SQL*

> "A named temporary result set defined with WITH, to make complex queries readable or to write recursive queries like walking an org hierarchy."

**[⬆ Back to Top](#table-of-contents)**

## 113. SQL: ROW_NUMBER vs RANK vs DENSE_RANK?

*EF Core & SQL*

For scores 100, 90, 90, 80:

- ROW_NUMBER: 1, 2, 3, 4
- RANK: 1, 2, 2, 4 (skips)
- DENSE_RANK: 1, 2, 2, 3 (no gap)

**[⬆ Back to Top](#table-of-contents)**

## 114. SQL: find the second-highest salary.

*EF Core & SQL*

```sql
SELECT Salary
FROM (SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS Rnk
      FROM Employees) AS Ranked
WHERE Rnk = 2;
```

DENSE_RANK handles ties: if two share the top salary, the next distinct one is still rank 2.

**[⬆ Back to Top](#table-of-contents)**

## 115. SQL: delete duplicate rows but keep one.

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

## 116. SQL: temp table vs table variable?

*EF Core & SQL*

> "A temp table (#Temp) lives in tempdb, can have indexes and statistics, so it's better for larger data. A table variable (@T) is lighter, but the optimizer assumes few rows, so it's for small sets."

**[⬆ Back to Top](#table-of-contents)**

## 117. SQL: stored procedure vs function?

*EF Core & SQL*

> "A procedure can modify data, return multiple result sets and manage transactions. A function returns a value or table, can be used inside a SELECT, and can't modify data."

**[⬆ Back to Top](#table-of-contents)**

## 118. SQL: what is ACID?

*EF Core & SQL*

> "Atomic: all or nothing. Consistent: constraints always hold. Isolated: concurrent transactions don't see each other's unfinished work. Durable: once committed, it survives a crash."

**[⬆ Back to Top](#table-of-contents)**

## 119. SQL: what is normalization?

*EF Core & SQL*

> "Organising tables so each fact is stored once and linked by keys. Up to 3NF is normal for transactional systems; reporting databases are often denormalized for fast reads."

**[⬆ Back to Top](#table-of-contents)**

## 120. What makes a RESTful API well designed?

*API & security*

- Resources as nouns, correct verbs: `GET /accounts/42/orders`.
- Correct status codes and consistent errors (ProblemDetails).
- Versioning, so existing clients never break.
- Pagination and filtering for lists.
- Idempotency for retries, validation, and authentication on every endpoint.

**[⬆ Back to Top](#table-of-contents)**

## 121. POST vs PUT vs PATCH, and which are idempotent?

*API & security*

> "POST creates and isn't idempotent: two calls create two things. PUT replaces the whole resource and is idempotent. PATCH changes part of it. GET, PUT and DELETE are idempotent. For POSTs that must be safe to retry, like placing an order, I use an Idempotency-Key header."

**[⬆ Back to Top](#table-of-contents)**

## 122. Which status codes do you use, and when?

*API & security*

- **200** OK · **201** Created · **202** Accepted (processing later) · **204** No Content
- **400** bad input · **401** not authenticated · **403** authenticated but not allowed · **404** not found
- **409** conflict (concurrency, duplicate) · **422** valid format, fails business rules · **429** rate limited
- **500** server error · **503** dependency down

**Follow-up:** 401 vs 403 is a classic: 401 = who are you? 403 = I know who you are, and you can't do this.

**[⬆ Back to Top](#table-of-contents)**

## 123. A client retries a timed-out order. How do you prevent a duplicate trade?

*API & security*

> "The client sends an Idempotency-Key, unique per order attempt. I store it with the order under a unique constraint. On a retry with the same key, I return the original result instead of placing a second order."

**[⬆ Back to Top](#table-of-contents)**

## 124. How do you version an API?

*API & security*

> "Usually in the URL, like /v1/orders, because it's explicit and easy to route in APIM. Existing versions never get breaking changes; breaking changes go in a new version, and the old one is deprecated with notice to consumers."

**[⬆ Back to Top](#table-of-contents)**

## 125. OAuth2 vs JWT?

*API & security*

> "OAuth2 is the authorization framework: how a client gets a token from an identity provider like Microsoft Entra ID. A JWT is a token format: a signed JSON token carrying claims like user id, roles and expiry. OAuth2 commonly issues JWTs as access tokens."

**[⬆ Back to Top](#table-of-contents)**

## 126. A partner system calls your API through APIM. Walk me through how it's secured.

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

## 127. How do users log in through the UI and call your API?

*API & security*

**Authorization code flow with PKCE**, through Entra ID.

1. The UI redirects the user to **Microsoft's login page**. Our app never sees the password; MFA and lockout are handled by Entra.
1. Entra redirects back with a **one-time authorization code**.
1. The app exchanges the code for three tokens: an **ID token** (who the user is, for the UI), an **access token** (sent to the API), and a **refresh token** (gets new access tokens without logging in again).
1. Every API call carries the access token; the API validates it and checks roles.

Refresh token stored server-side and encrypted. If the access token is in a cookie, the cookie is **HttpOnly, Secure, SameSite**. The ID token is never sent to the API.

**Follow-up:** PKCE: the app sends a hashed random secret with the login, then proves it has the original when exchanging the code, so a stolen code is useless. Why not localStorage? Any script can read it, so one XSS bug leaks the token.

**[⬆ Back to Top](#table-of-contents)**

## 128. What does rotating secrets mean?

*API & security*

A client secret is like a password and expires in Entra. Rotating means replacing it on a schedule, before it expires or leaks:

1. Create a new secret (an app can hold two at once).
1. Put it in Key Vault and switch the client to it.
1. Delete the old one.

> "Two valid secrets during the switch means no downtime. Better still: certificates or managed identity, so there's no secret to leak."

**[⬆ Back to Top](#table-of-contents)**

## 129. How do you implement authorization in .NET?

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

## 130. How does your API validate a JWT?

*API & security*

- `AddAuthentication().AddJwtBearer()` checks the signature with the identity provider's public keys.
- It validates issuer, audience and expiry.
- `[Authorize]` policies check roles or scopes.
- APIM can also validate the JWT at the gateway before the request reaches the service.

**[⬆ Back to Top](#table-of-contents)**

## 131. Name an OWASP risk you've mitigated.

*API & security*

> "Broken access control is the big one for banking. Checking that someone is logged in isn't enough; for GET /accounts/123 I verify account 123 belongs to the caller, otherwise anyone can change the id and read other people's data. Also SQL injection, prevented with parameterized queries and EF, and secrets kept out of code in Key Vault."

**[⬆ Back to Top](#table-of-contents)**

## 132. How do you protect customer data and privacy?

*API & security*

- Collect and return only what's needed.
- Never log account numbers, SINs, tokens or passwords; mask them.
- TLS in transit, encryption at rest (TDE).
- Least-privilege access, and secrets in Key Vault with managed identity.

**[⬆ Back to Top](#table-of-contents)**

## 133. Where do secrets like connection strings go?

*API & security*

> "Never in appsettings or Git. Azure Key Vault or OpenShift/Kubernetes secrets, and ideally managed identity so there's no password to store at all."

**[⬆ Back to Top](#table-of-contents)**

## 134. What do you know about WCAG accessibility?

*API & security*

> "It's the standard for making apps usable by everyone: keyboard navigation, alt text, enough color contrast, proper labels and ARIA for screen readers. On the front end I check with tools like Lighthouse or axe. On the API side, it means returning clear, structured error messages the UI can present accessibly."

**[⬆ Back to Top](#table-of-contents)**

## 135. How do you test a service that consumes events and writes to a database?

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

## 136. Unit test vs integration test: where's the line?

*Testing*

> "A unit test checks one class's logic with its dependencies mocked: fast, no database, no network. An integration test checks that real pieces work together: API, database, Kafka. Business rules get unit tests; queries, serialization and wiring get integration tests."

**[⬆ Back to Top](#table-of-contents)**

## 137. How do you unit test a class that publishes to Kafka?

*Testing*

> "The class depends on an IEventPublisher interface, not the Kafka client. In the test I inject a Moq mock, run the method, and verify PublishAsync was called once with the expected event. No Kafka needed."

```csharp
var publisher = new Mock<IEventPublisher>();
var service = new ShipmentService(publisher.Object);

await service.CreateAsync(shipment);

publisher.Verify(p => p.PublishAsync(It.IsAny<ShipmentEvent>()), Times.Once);
```

**[⬆ Back to Top](#table-of-contents)**

## 138. How do you test an API end to end?

*Testing*

> "WebApplicationFactory starts the real API in memory, and the test calls it with HttpClient. For real dependencies, Testcontainers starts SQL Server, Redis or Kafka in Docker for the test run, so it's close to production and runs in CI."

**[⬆ Back to Top](#table-of-contents)**

## 139. What makes a good unit test?

*Testing*

- Arrange, Act, Assert.
- Tests one behaviour; the name says what it checks.
- Fast and deterministic: no real clock, network or random values.
- Covers edge cases, not just the happy path.

**[⬆ Back to Top](#table-of-contents)**

## 140. Mock vs stub vs fake?

*Testing*

> "A stub returns canned answers. A mock also lets you verify how it was called. A fake is a simple working implementation, like an in-memory repository."

**[⬆ Back to Top](#table-of-contents)**

## 141. Do you practise TDD?

*Testing*

> "For business rules, yes: write a failing test, make it pass, refactor. It's most useful where the logic has many edge cases. For plumbing code I usually write the tests right after."

**[⬆ Back to Top](#table-of-contents)**

## 142. Image vs container vs Docker?

*Docker & OpenShift*

> "An image is the immutable package: compiled app, runtime and OS files. A container is a running instance of an image. Docker builds images and runs containers on one machine. Kubernetes or OpenShift runs them at scale across many."

**[⬆ Back to Top](#table-of-contents)**

## 143. How do you write a Dockerfile for a .NET API?

*Docker & OpenShift*

> "Multi-stage. The first stage uses the .NET SDK image to restore, build and publish. The final stage copies only the published output into the smaller ASP.NET runtime image. The production image has no SDK or source code, is much smaller, and runs as a non-root user."

**[⬆ Back to Top](#table-of-contents)**

## 144. Explain the core Kubernetes objects.

*Docker & OpenShift*

- **Pod**: one or more containers running together.
- **Deployment**: keeps N replicas running and does rolling updates.
- **Service**: a stable address in front of changing pods.
- **Ingress** (Route in OpenShift): external traffic in.
- **ConfigMap / Secret**: configuration and secrets.
- **HPA**: scales pods on CPU or other metrics.

**[⬆ Back to Top](#table-of-contents)**

## 145. OpenShift vs Kubernetes?

*Docker & OpenShift*

> "OpenShift is Red Hat's enterprise Kubernetes, so pods, deployments and services all carry over. It adds stricter security by default (containers can't run as root, via Security Context Constraints), Routes for external traffic, Projects as namespaces with extra controls, a built-in image registry and builds, and the oc CLI alongside kubectl."

**[⬆ Back to Top](#table-of-contents)**

## 146. Liveness vs readiness probe?

*Docker & OpenShift*

> "Readiness: is this pod ready for traffic? If not, it's taken out of the load balancer, for example while it warms up or loses the database. Liveness: is it still alive? If not, Kubernetes restarts it. In .NET I expose them with health checks via MapHealthChecks."

**[⬆ Back to Top](#table-of-contents)**

## 147. Walk me through a CI/CD pipeline you've built.

*Docker & OpenShift*

1. On a PR: build, unit tests, code and dependency scans.
1. On merge: build the Docker image, tag it and push to the registry.
1. Deploy to dev automatically, then higher environments with approvals.
1. Rolling deployment with health checks, and rollback to the previous image if checks fail.

The same image moves through every environment; only configuration changes.

**[⬆ Back to Top](#table-of-contents)**

## 148. How do you handle config per environment?

*Docker & OpenShift*

> "One image for all environments. Settings come from appsettings.{Environment}.json overridden by environment variables or ConfigMaps, and secrets come from Key Vault or Kubernetes secrets. Nothing environment-specific is baked into the image."

**[⬆ Back to Top](#table-of-contents)**

## 149. Git: merge vs rebase?

*Git*

> "Merge combines branches with a merge commit and keeps full history. Rebase replays my commits on top of the latest main for a clean, straight history. I rebase my own feature branch, but never a shared branch, because it rewrites history others depend on."

**[⬆ Back to Top](#table-of-contents)**

## 150. Git: what's your branching strategy?

*Git*

> "Trunk-based with short-lived feature branches: branch from main, PR, review, CI must pass, merge, and the pipeline deploys. Long-lived branches cause painful merges."

**[⬆ Back to Top](#table-of-contents)**

## 151. Git: how do you resolve a merge conflict?

*Git*

> "Pull the latest main, understand both changes, talk to the other developer if it's not obvious, combine them, run the tests, then commit. Never blindly pick mine."

**[⬆ Back to Top](#table-of-contents)**

## 152. What do you look for in a code review?

*Git*

> "Correctness and edge cases first, then security like validation and authorization, then readability, tests and performance issues like N+1. I explain why in comments so it's a learning moment."

**[⬆ Back to Top](#table-of-contents)**

## 153. Git: revert vs reset?

*Git*

> "Revert creates a new commit that undoes an earlier one, safe on shared branches. Reset moves the branch pointer back and rewrites history, only for local unpushed work."

**[⬆ Back to Top](#table-of-contents)**

## 154. Azure: App Service vs AKS vs Azure Functions?

*Azure*

> "App Service is the simplest way to host a web app or API: deploy code, Azure manages servers. AKS is managed Kubernetes for many containerised microservices, with fine control over scaling and networking. Functions are event-driven and serverless: pay per execution, good for small background jobs."

**[⬆ Back to Top](#table-of-contents)**

## 155. Azure: Event Hubs vs Service Bus vs Event Grid?

*Azure*

- **Event Hubs**: high-throughput event streaming with partitions and replay. Azure's Kafka; supports the Kafka protocol.
- **Service Bus**: reliable enterprise messaging: queues, topics, sessions for ordering, dead-lettering, transactions. For commands like "process this order".
- **Event Grid**: lightweight event notification, like "a blob was uploaded", pushed to subscribers.

Your example: "At Staples we use Event Hubs for high-throughput integration events to the TMS."

**[⬆ Back to Top](#table-of-contents)**

## 156. Azure: what is APIM for?

*Azure*

> "A gateway in front of our APIs: JWT validation, rate limiting and quotas, versioning, request transformation, and a developer portal for partners. One secure front door for all APIs."

**[⬆ Back to Top](#table-of-contents)**

## 157. Azure: Key Vault and Managed Identity?

*Azure*

> "Key Vault stores secrets, keys and certificates. Managed Identity gives the app its own Azure identity, so it reads Key Vault without any stored password. That removes the problem of where to keep the secret that unlocks the secrets."

**[⬆ Back to Top](#table-of-contents)**

## 158. Azure: what does Application Insights give you?

*Azure*

> "Azure's APM: request rates, failures, dependency calls with timings, exceptions and distributed traces across services. It's how you find that time is going into a slow SQL call, the same way we use Datadog at Staples."

**[⬆ Back to Top](#table-of-contents)**

## 159. Azure: storage types?

*Azure*

- **Blob**: files like PDFs.
- **Table Storage**: cheap NoSQL key-value (used at Staples).
- **Queue Storage**: simple queuing.
- **Files**: SMB file shares.

**[⬆ Back to Top](#table-of-contents)**

## 160. Azure: Table Storage vs Cosmos DB vs Azure SQL?

*Azure*

> "Azure SQL is relational with joins, transactions and strong consistency, what you want for money. Cosmos DB is globally distributed NoSQL with low latency and flexible schemas. Table Storage is the cheapest key-value option for simple lookups at scale."

**[⬆ Back to Top](#table-of-contents)**

## 161. Azure: what is ACR?

*Azure*

> "Azure Container Registry: the private Docker image registry. The pipeline pushes images there and AKS pulls from it."

**[⬆ Back to Top](#table-of-contents)**

## 162. Azure: how does a request reach your AKS service?

*Azure*

DNS, then Azure Front Door or Application Gateway (WAF, TLS), then APIM, then the AKS ingress controller, then the Kubernetes Service, then the pods.

**[⬆ Back to Top](#table-of-contents)**

## 163. Azure: what are deployment slots?

*Azure*

> "An App Service feature: deploy to a staging slot, warm it up, then swap with production for near-zero downtime, and swap back if something breaks."

**[⬆ Back to Top](#table-of-contents)**

## 164. Azure: how do you scale?

*Azure*

> "Scale up means a bigger machine; scale out means more instances. App Service autoscales on rules like CPU; AKS uses the Horizontal Pod Autoscaler for pods and the cluster autoscaler for nodes."

**[⬆ Back to Top](#table-of-contents)**

## 165. A client clicks 'Buy 100 shares'. Design what happens until the order reaches the market.

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

## 166. Does the Direct Investing platform match buyers and sellers?

*System design*

> "No. Direct Investing is a broker, not an exchange. Matching happens on the market (TSX, NYSE and so on). The broker's system validates the order, reserves the client's cash, routes the order to the market, and processes the execution report that comes back. The other side of the trade is another market participant, not one of our clients."

**Follow-up:** This is why execution is asynchronous: a limit order can fill hours later, or never, so it can't happen inside one API call.

**[⬆ Back to Top](#table-of-contents)**

## 167. Why return 202 Accepted instead of waiting for the market?

*System design*

> "Reaching the market and getting filled can take a while and depends on systems we don't control. Holding the client's connection open wastes server resources and risks timeouts, which cause retries. So I accept the order, return 202 with the order id, and push status updates as it moves: sent, filled, rejected."

**[⬆ Back to Top](#table-of-contents)**

## 168. Kafka is down when an order is placed. What happens?

*System design*

> "The order and its outbox row are already saved in one transaction, so the client still gets 202. The worker keeps retrying and publishes once Kafka is back. Nothing is lost, and order intake doesn't depend on Kafka being up."

**[⬆ Back to Top](#table-of-contents)**

## 169. How would a regulator reconstruct what happened to one order?

*System design*

> "Every state change (received, validated, sent, filled, cancelled) is written as an immutable, append-only event with timestamp, user and source. A correlation id follows the order across every service and log. Replaying one order's events shows exactly what happened and when."

**[⬆ Back to Top](#table-of-contents)**

## 170. How do you keep data consistent across microservices?

*System design*

> "Each service owns its database, so there are no distributed transactions. Services communicate with events via an outbox, and multi-step processes use a saga with compensating actions: reserve cash, place the order, and if the market rejects it, release the cash. It's eventually consistent, and every step is idempotent."

**[⬆ Back to Top](#table-of-contents)**

## 171. Circuit breaker vs retry vs bulkhead?

*System design*

- **Retry** with backoff: for brief glitches.
- **Circuit breaker**: after repeated failures, stop calling for a while so you don't pile onto a failing dependency.
- **Bulkhead**: cap concurrent calls to one dependency so it can't use up all your threads.

In .NET: Polly or Microsoft.Extensions.Http.Resilience. On one critical dependency, use all three together.

**[⬆ Back to Top](#table-of-contents)**

## 172. How would you push live price or order updates to the UI?

*System design*

> "SignalR over WebSockets. The server pushes updates instead of the client polling. With several API instances, SignalR needs a backplane, like Redis or Azure SignalR Service, so a message reaches the client whichever instance it's connected to."

**[⬆ Back to Top](#table-of-contents)**

## 173. How does your design scale?

*System design*

> "The Order API is stateless, so I add instances behind the gateway, with autoscaling on OpenShift or AKS. Kafka scales with partitions and consumers. Reads come from Redis and SQL read replicas, and writes stay on the primary."

**[⬆ Back to Top](#table-of-contents)**

## 174. Frontend: how do you position yourself if they go deep?

*Frontend*

> "My core strength is backend. On the frontend I've built Angular apps for years, mostly the pieces that talk to APIs: services, interceptors, guards and forms."

**[⬆ Back to Top](#table-of-contents)**

## 175. Angular: component vs service? Lifecycle hooks?

*Frontend*

- A component is a piece of UI. A service holds shared logic or data and is injected with DI, the same idea as .NET.
- `ngOnInit`: load data here, not in the constructor. `ngOnDestroy`: clean up subscriptions.

**[⬆ Back to Top](#table-of-contents)**

## 176. Angular: Observables, the async pipe and switchMap?

*Frontend*

- HttpClient returns an Observable; nothing happens until someone subscribes (like LINQ deferred execution).
- The async pipe subscribes and unsubscribes for you, which prevents memory leaks.
- switchMap cancels the previous request when a new one starts, like a search box as the user types.

**[⬆ Back to Top](#table-of-contents)**

## 177. Angular: HTTP interceptor and route guard?

*Frontend*

- **Interceptor**: attaches the JWT to every API call and handles 401 in one place.
- **Route guard**: blocks navigation unless the user is logged in or has the right role.

**[⬆ Back to Top](#table-of-contents)**

## 178. Angular: change detection, OnPush, and modern Angular?

*Frontend*

- Change detection checks for changes and updates the screen. OnPush only re-checks a component when its inputs change, so it's faster.
- Modern Angular: standalone components (no NgModules), signals for simpler reactive state, lazy-loaded routes.

**[⬆ Back to Top](#table-of-contents)**

## 179. React: props vs state, useState, useEffect, virtual DOM?

*Frontend*

- Props are passed in from the parent and read-only; state is owned by the component, and changing it re-renders.
- useState holds state; useEffect runs side effects like API calls after render.
- The virtual DOM compares new UI to old and updates only what changed.

**[⬆ Back to Top](#table-of-contents)**

## 180. Tell me about a disagreement with a teammate.

*Behavioural*

**S:** At Staples, our publishing table deleted rows as soon as messages were sent to the WMS and TMS.

**T:** I thought we were losing important information, but the team was comfortable with it because it worked.

**A:** I listened to their concern first, mainly table growth and extra work. Then I showed a concrete case: when a partner says "we never got shipment X", we couldn't prove whether or when we sent it. I proposed keeping rows with a status per destination, plus a cleanup job that purges sent rows after a set number of days.

**R:** Adopted: "Now we can answer partner questions in minutes instead of guessing." Or not yet: "We put it on the backlog. I committed to the team's decision and documented the risk. The lesson: bring a concrete example, not just an opinion."

**Follow-up:** What they check: you listen, argue with evidence, and commit to the team decision even when it doesn't go your way.

**[⬆ Back to Top](#table-of-contents)**

## 181. Tell me about a production incident or a hard problem you solved.

*Behavioural*

**S:** At insightsoftware, heavy reports like vesting and tax reports were slow for our largest clients, and clients were complaining.

**T:** As lead on the reporting team, I owned finding and fixing it.

**A:** Datadog APM showed almost all the time was inside the database call; the code was already async. I captured the slow queries with SQL Profiler and read the execution plans: table scans, SELECT * and key lookups. I replaced SELECT * with only the needed columns, added covering indexes, and cached reference data that rarely changes, shipping in small steps and checking each one in Datadog.

**R:** The heavy reports got significantly faster, roughly 40% on the worst ones, and the complaints stopped. Since then I check the execution plan for any new heavy query before it ships.

**Follow-up:** End on what you changed afterwards. That's the part they remember.

**[⬆ Back to Top](#table-of-contents)**

## 182. How do you mentor other developers?

*Behavioural*

> "Mostly through code reviews: explaining why, not just what to change, and pairing on tricky pieces. When someone's stuck, I help them debug rather than fixing it for them, so they learn the approach."

**[⬆ Back to Top](#table-of-contents)**

## 183. Why RBC, and why this role?

*Behavioural*

> "It's a rebuild of a large trading platform, which is rare: modern .NET, Kafka, Redis and containers in a domain where correctness really matters. It lines up with what I've done, event-driven integration at Staples and financial reporting at insightsoftware, and I want to go deeper into capital markets."

**[⬆ Back to Top](#table-of-contents)**

## 184. You're okay with contract-to-hire?

*Behavioural*

> "Yes, completely. I'm looking for a long-term role, and I'm happy to prove myself during the contract and convert."

**Follow-up:** Answer without hesitation.

**[⬆ Back to Top](#table-of-contents)**

## 185. What questions do you have for us?

*Behavioural*

- What does the target architecture of the rebuild look like, and what stage is it at?
- How is the team split across the 4 openings?
- What does success look like in the first 3 months?
- What's the biggest technical challenge right now?

**[⬆ Back to Top](#table-of-contents)**

## 186. Walk me through your banking solution, level by level.

*CodeSignal*

Every method takes a timestamp first; the caller supplies the account id.

- **L1 CreateAccount / GetBalance:** Dictionary<string, Account>, false on a duplicate id, null for unknown.
- **L2 Deposit:** TryGetValue, reject amount <= 0, return the new balance.
- **L3 Transfer:** ALL checks first (same account, amount, both exist, enough balance), THEN move money and add to TotalSpent. Returns the source balance.
- **L4 TopSpenders:** LINQ: Where TotalSpent > 0, OrderByDescending, ThenBy id, Take(n), then string.Join(",", ...) of "id{total}", like "acct5{10},acct3{8}".
- **L5 Schedule / Cancel:** scheduling only records it; every method calls ProcessDue(timestamp) first, which executes due transfers through the same TryTransfer.

**Follow-up:** Why Dictionary of Account objects? O(1) lookups, and each level adds a field instead of another dictionary to keep in sync. Why return false on a duplicate instead of throwing? It's an expected case, and the spec says so.

**[⬆ Back to Top](#table-of-contents)**

## 187. Level 3: show the transfer and the traps.

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

**Follow-up:** Is it thread-safe? No; CodeSignal is single-threaded. In a real bank: a database transaction with an atomic conditional update, or a lock. Why block same-account? It would count as spending while moving nothing. TryGetValue vs ContainsKey + []: one lookup instead of two.

**[⬆ Back to Top](#table-of-contents)**

## 188. Level 4: top spenders, and the traps.

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

**Follow-up:** Why StringComparer.Ordinal? A plain character-by-character sort, the same on every machine. Big-O? O(n log n) for the sort; fine here, a sorted structure if called constantly on huge data. Why a running TotalSpent? O(1) to update instead of re-scanning every transfer.

**[⬆ Back to Top](#table-of-contents)**

## 189. How would you have implemented the scheduled transfer?

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

**Follow-up:** Due at 14, GetBalance at 14? The transfer runs FIRST, because ProcessDue runs before the operation. Cancel after execution? False, it's no longer pending. Invalid schedule doesn't use an id: increment only after validation. Why .ToList()? A copy, so removing inside the loop is safe. Why a List? Simple and correct; a PriorityQueue for thousands.

**[⬆ Back to Top](#table-of-contents)**

## 190. How would you improve your CodeSignal solution?

*CodeSignal*

> "In the assessment I kept adding separate dictionaries for each new requirement: balances, then spending, then scheduled transfers. By Level 4 every change was slow and error-prone. Now I'd model an Account class from the start, holding balance and total spent, in one Dictionary keyed by account id. Each new level adds a field or method instead of another dictionary to keep in sync, and one TryTransfer method is the only place money moves."

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
