# Thomson Reuters Round 1: Senior Software Engineer I (Document AI platform)

> Hiring-manager round, 1 hour: technical questions on your experience with C#, .NET,
> OpenAPI, Kubernetes, GitHub, Docker and especially LLMs/AI. Say each answer out loud
> in under a minute before revealing it. Sections: Your stories, Kubernetes & Docker,
> APIs, AI & LLMs, Resilience, Quality, Behavioural, Your questions, then core practice: C# & .NET,
> ASP.NET Core & APIs, Azure, Microservices, Design & patterns, Async & concurrency, Testing,
> DevOps & Agile, Scenarios.

## 1. Tell me about yourself.

*Your stories*

**About 60 seconds.** Bold words are hooks that lead to prepared answers.

> "I'm a senior .NET engineer with about 10 years of experience, mostly backend on Azure.

> Right now at Staples I'm on the middleware team. I build **.NET 8 microservices on AKS** that connect our order systems with third-party platforms: the carrier platform, the warehouse system and the TMS. They're event-driven, publishing to **Azure Event Hubs and Google Pub/Sub**, with an **outbox pattern** so we don't lose messages when a pod crashes. I own them end to end: tests, Azure DevOps pipelines and monitoring.

> Before that, at Accolite, I led full-stack work on a compliance SaaS used by **100+ corporate clients**: **OpenAPI**-documented APIs, SQL performance tuning, and a .NET Framework to .NET Core migration. Day to day I use AI heavily, mainly **Claude Code** and Copilot.

> And early in my career at Helm360, a Thomson Reuters Elite partner, I worked inside **Elite 3E** for law firms, which is where I learned the legal world.

> So this role brings together what I've been doing: high-volume Azure services, AI, and legal documents."

**[⬆ Back to Top](#table-of-contents)**

## 2. Walk me through a system you work on.

*Your stories*

> "The Single Pool of Inventory: one source of truth for product data across all downstream systems.

> 1. Stibo, our master data system, publishes an event to **Azure Event Hubs** whenever a SKU changes.
> 2. Our .NET consumers save the change to SQL, **outbox-style**, so nothing is lost if a pod crashes.
> 3. Every 15 minutes a background service **transforms** the pending changes for each downstream system and publishes them to another Event Hub.
> 4. Some consumers are modern; one needs a **legacy fixed-width file** (characters 1-10 one field, 11-20 the next). I built that file generation.

> Consumers are fully decoupled: if one is down, its events wait in Event Hubs and it catches up later. I own the consumer and transformation services end to end. What I'd improve: move from 15-minute batches to near-real-time publishing, since the outbox already gives us safety."

**Follow-up:** Why 15-minute batches? Downstream systems preferred batched updates and it reduced load; with idempotent consumers we could go near-real-time.

**[⬆ Back to Top](#table-of-contents)**

## 3. The same SKU changes twice in a few seconds. How do you keep order and avoid duplicates?

*Your stories*

> "**Duplicates:** every change carries an ID, and we and our consumers are idempotent, so a repeat is detected and skipped.

> **Ordering:** Event Hubs has partitions just like Kafka. We publish with the **SKU ID as the partition key**, so all updates for one SKU land in the same partition, in order, while different SKUs spread across partitions for throughput. Consumers read a partition sequentially and **checkpoint** their position. As a safety net, each update carries a **version number from MDM**: an older version than what we have is ignored."

**Follow-up:** Kafka to Event Hubs mapping: topic = event hub, partition = partition, message key = partition key, offset commit = checkpoint (stored in Blob), consumer group = consumer group. A trace ID is a random GUID for tracing, not for ordering.

**[⬆ Back to Top](#table-of-contents)**

## 4. Tell me about a production issue with a vendor API.

*Your stories*

> "A shipment request to the carrier platform succeeded, but the response failed with a 500. On retry the vendor said 'duplicate' without the shipment details, so the customer saw a failure. Hours later they created it again as a new request, and the vendor ended up with two shipments.

> The duplicate wasn't the real bug. The real bug was **telling the customer a successful request had failed**. So we fixed it at the source: on a 500 or a 'duplicate', **look up the actual shipment** by our order reference and return it as a success; use the **order reference as the business key**, not a short-lived trace ID; and a **reconciliation job** finds orphaned shipments and cancels them."

**Follow-up:** True idempotency = same key returns the same response, not an error. Lesson: never assume a third party is idempotent; track your own state (Pending / Created / Unknown).

**[⬆ Back to Top](#table-of-contents)**

## 5. Tell me about your experience with Kubernetes and Docker.

*Kubernetes & Docker*

> "All our microservices run on **AKS**. Each service has a **Dockerfile**: a multi-stage build where the SDK image publishes and only the output goes into the smaller ASP.NET runtime image.

> I write the **Kubernetes YAML manifests**: a Deployment with multiple replicas, CPU/memory requests and limits, and **liveness and readiness probes**; a Service for a stable internal address; requests come in through APIM. Config from ConfigMaps, secrets from **Key Vault**.

> **Azure Pipelines** runs the tests, builds the image, tags it with the build number, pushes it to **Azure Container Registry**, and deploys dev, then staging, then prod with approval. Rolling updates mean no downtime, and rollback is redeploying the previous tag."

**[⬆ Back to Top](#table-of-contents)**

## 6. Liveness vs readiness probes?

*Kubernetes & Docker*

> "Liveness asks 'is it stuck?': failing it **restarts** the pod. Readiness asks 'can it take traffic?': failing it **removes the pod from the Service** without killing it. Keep liveness simple, so a database blip doesn't restart every pod."

**[⬆ Back to Top](#table-of-contents)**

## 7. Requests vs limits, and rolling updates?

*Kubernetes & Docker*

> "Requests are what the scheduler reserves; limits are the maximum. Over the memory limit the pod is **OOMKilled**; over CPU it's **throttled**.

> A rolling update brings up new pods, sends them traffic once they pass readiness, then terminates old ones. maxSurge and maxUnavailable control the pace. Rollback: redeploy the previous image tag, or kubectl rollout undo in an emergency."

**[⬆ Back to Top](#table-of-contents)**

## 8. A pod keeps crashing after a deploy. What do you do?

*Kubernetes & Docker*

> "kubectl get pods for the status, kubectl describe pod for events (failed probe, OOMKilled, image pull error), kubectl logs --previous for why the last instance crashed. Usually it's bad config, a missing secret or a startup exception. If prod is affected, I roll back first, then debug."

**[⬆ Back to Top](#table-of-contents)**

## 9. How do secrets and traffic reach your pods? How do you scale?

*Kubernetes & Docker*

> "Secrets: the **Key Vault CSI driver** with **workload identity**, mounted at runtime, so nothing sits in YAML or the repo. Traffic: APIM calls an **ingress controller**, which routes to the Service, which load-balances across ready pods. Scaling: replicas plus the **HPA** on CPU. For Event Hub consumers, scaling is capped by **partition count**, one active consumer per partition, so KEDA on backlog fits better."

**[⬆ Back to Top](#table-of-contents)**

## 10. Have you designed APIs with OpenAPI? How do you version them?

*APIs*

> "At Accolite I built and owned **10+ versioned REST APIs** documented with **OpenAPI via Swashbuckle**. The spec was our contract: the Angular front end and client integrations built against it, and we generated clients from it.

> Additive changes (new optional fields, new endpoints) stay in the same version. Breaking changes (renamed or removed fields, type changes) go into a **new version, /v2**, and the old one stays live with a deprecation period.

> At Staples it was **contract-first** with the carrier vendor: we agreed example payloads, including bilingual EN/FR fields, and built in parallel."

**Follow-up:** Code-first is faster for internal APIs; contract-first is better when other teams or vendors depend on you. Status codes: 200/201, 202 for async jobs, 400, 404, 409 conflict, 429 rate limit, with ProblemDetails for consistent errors. Catch accidental breaking changes by reviewing the spec diff in the PR or a breaking-change check in CI.

**[⬆ Back to Top](#table-of-contents)**

## 11. What's your AI / LLM experience?

*AI & LLMs*

> "Three levels. **Daily:** Claude Code and GitHub Copilot for building and testing, with a project instructions file holding our conventions; I review every diff, because I own what ships. **Built:** an internal **RAG assistant** over our API specs and runbooks with **Azure OpenAI and Azure AI Search**. **Experimented:** running models locally with **Ollama**, which taught me why model serving is a real engineering problem. Very relevant for a team running its own model."

**Follow-up:** Why Claude? Strong on large codebases and multi-file changes, and its agentic loop (read code, run tests, iterate) fits real work; Copilot is great for inline completion. Quality with AI code: small changes, review every diff, tests must pass, human PR review before merge.

**[⬆ Back to Top](#table-of-contents)**

## 12. Tell me about the RAG assistant you built.

*AI & LLMs*

> "Devs and support kept asking the same questions about API specs and runbooks. I built a RAG assistant: **chunk** the docs by headings (~500 tokens with overlap, plus metadata for source and section), **embed** them, store in **Azure AI Search**. At question time: **hybrid search**, take the **top 5 chunks**, prompt the model to **answer only from that context and cite the source**. .NET backend on Azure."

**Follow-up:** Small internal initiative: me on the backend and ingestion, with one other developer. Evaluated with a test set of ~25 real questions with known answers, re-run after every change.

**[⬆ Back to Top](#table-of-contents)**

## 13. Why chunk by headings? Why hybrid search?

*AI & LLMs*

> "Fixed-size chunks cut sentences and tables in half; headings keep one topic per chunk, so retrieval is more precise. Overlap keeps meaning across boundaries. Hybrid because vectors find meaning but miss exact terms like error codes and API names; keyword search catches those."

**[⬆ Back to Top](#table-of-contents)**

## 14. What went wrong with the RAG assistant, and how would it scale?

*AI & LLMs*

> "Tables got split, so we kept them whole. Answers went stale after doc changes, so we re-indexed a doc when its content hash changed. The model made things up, so we refuse when the retrieval score is low: 'I don't know' beats a wrong answer.

> At large scale, ingestion becomes a queue-based pipeline (OCR, chunk, embed, index) with workers scaling on backlog, citations down to page and paragraph, and throttling for the LLM's 429 limits."

**[⬆ Back to Top](#table-of-contents)**

## 15. Have you hosted a model yourself?

*AI & LLMs*

> "I ran **Ollama** with small models on my own laptop, wired into VS Code through Cline. A simple 'hi' took about two minutes: no GPU, and coding agents send huge system prompts, so processing the input dominated. Takeaway: self-host when **data can't leave** or at **steady high volume on GPUs**; for dev tools a managed API won, so I moved to Claude. Speed-ups: GPU, smaller prompts, prefix caching, a serving engine like vLLM."

**[⬆ Back to Top](#table-of-contents)**

## 16. Tokens, context window, temperature, structured output, rate limits?

*AI & LLMs*

> "Text is split into **tokens** (~¾ of a word); the **context window** caps input plus output; you pay per token and latency grows with them. **Temperature** controls randomness: low for extraction and classification. For **structured output**, ask for a JSON schema, validate it in code, retry or flag on failure. For **rate limits**, LLM APIs return 429 on token-per-minute quotas: retry honouring Retry-After, cap concurrency with SemaphoreSlim, and queue big workloads so workers process at a controlled rate."

**[⬆ Back to Top](#table-of-contents)**

## 17. How do you call an external API reliably? (Polly)

*Resilience*

> "HttpClientFactory with the .NET resilience handler (Polly underneath): **retry** with exponential backoff and jitter on transient errors (5xx, 408, 429, honouring Retry-After), a **per-attempt timeout**, and a **circuit breaker** so we stop hammering a failing dependency. For create calls I only retry with an idempotency key; otherwise retries can create duplicates."

```csharp
builder.Services.AddHttpClient<CarrierClient>(c => c.BaseAddress = new Uri("https://api.carrier.com"))
    .AddResilienceHandler("carrier", p =>
    {
        p.AddRetry(new HttpRetryStrategyOptions {
            MaxRetryAttempts = 3, Delay = TimeSpan.FromMilliseconds(500),
            BackoffType = DelayBackoffType.Exponential, UseJitter = true });
        p.AddCircuitBreaker(new HttpCircuitBreakerStrategyOptions {
            FailureRatio = 0.5, SamplingDuration = TimeSpan.FromSeconds(30),
            MinimumThroughput = 10, BreakDuration = TimeSpan.FromSeconds(15) });
        p.AddTimeout(TimeSpan.FromSeconds(5));
    });
```

**Follow-up:** Jitter spreads retries so 100 pods don't retry at the same instant. No retry on 400/404: a bad request fails again.

**[⬆ Back to Top](#table-of-contents)**

## 18. Circuit breaker states? And what does your API return while it's open?

*Resilience*

> "Closed: calls go through, failures are counted. Open: calls **fail immediately** with a BrokenCircuitException. Half-open after the break: a trial call goes through; success closes it, failure opens it again.

> While it's open it depends on the call. For a create like a shipment, save it as **Pending** and return **202 Accepted**; a background worker sends it once the circuit closes (the outbox again). For reads, serve a **cached** result. If the caller needs a real-time answer, a fast **503 with Retry-After** beats a slow timeout."

**[⬆ Back to Top](#table-of-contents)**

## 19. What's the point of async/await if we wait anyway?

*Resilience*

> "Await waits, but it doesn't **block the thread**. While a DB or HTTP call is in flight, the thread goes back to the pool and serves other requests, so the API scales under load. That's why it's async all the way up: one .Result or .Wait() blocks the thread and brings back thread-pool starvation. For independent calls, start them all and await Task.WhenAll, so total time is the slowest call, not the sum."

**Follow-up:** An async method runs synchronously until its first await on an unfinished task. The async keyword only enables await; it doesn't create a thread.

**[⬆ Back to Top](#table-of-contents)**

## 20. How do you make sure a change doesn't break production?

*Quality*

> "Every change goes through a **PR with code review** and unit tests. The **CI/CD pipeline** runs unit and integration tests and deploys to dev, then staging, where **QA runs end-to-end tests**. For production we raise a **CAB request with a rollback plan**. After deploy we watch errors and latency in App Insights, and if something breaks we roll back to the previous version right away."

**[⬆ Back to Top](#table-of-contents)**

## 21. How do you ensure quality, and how do you measure it?

*Quality*

> "Layers. Before merge: unit tests (150+ per service), integration tests, PR review, SonarQube quality gates. In the pipeline: build the image **once** and promote the same artifact through environments. After deploy: dashboards and alerts on errors and latency, with **correlation IDs** to trace one request across services. After an incident: a blameless review that ends with a test or an alert, so the same bug can't come back.

> To measure it: **DORA metrics**, deployment frequency, lead time for changes, change failure rate, time to restore. I'd love to hear how your team tracks them."

**Follow-up:** Reviewing a PR: correctness first, then edge cases, error handling, tests, naming. Small PRs so review is real.

**[⬆ Back to Top](#table-of-contents)**

## 22. Tell me about a performance problem you solved.

*Behavioural*

> "Heavy compliance reports got slow for clients. **App Insights** showed which requests were slow; **SQL execution plans** showed why: SELECT *, missing indexes, synchronous calls. We selected only needed columns, added indexes, went async end to end and added caching. The heavy reports got roughly **40% faster**."

**[⬆ Back to Top](#table-of-contents)**

## 23. How do you mentor juniors?

*Behavioural*

> "Through **PR reviews** where I explain the why, not just 'change this'; **pairing on their first tickets** in a new service; and **API design reviews**. One junior was struggling with async code: instead of fixing it for them, we paired on one endpoint, then they did the next alone. Within a few weeks they were reviewing others' async code."

**[⬆ Back to Top](#table-of-contents)**

## 24. Tell me about a technical disagreement.

*Behavioural*

> "A teammate wanted to publish events straight from the API after saving to the database. I pushed for the **outbox pattern**: if the pod crashes between the save and the publish, the event is lost. Instead of arguing in the abstract, I **showed the failure case** with a quick demo, crashing between the two steps. We went with the outbox. Disagree with data, not opinions."

**[⬆ Back to Top](#table-of-contents)**

## 25. Tell me about a failure.

*Behavioural*

> "Early in the carrier integration I **trusted the vendor's duplicate handling** and didn't track request state on our side. That's how we ended up with duplicate shipments. Lesson: never assume a third party is idempotent; track your own state and reconcile. Now I ask about idempotency in the first vendor meeting."

**[⬆ Back to Top](#table-of-contents)**

## 26. Why Thomson Reuters? Why leave your current role?

*Behavioural*

> "CoCounsel is one of the most serious legal AI products out there, and the **document platform behind it**, processing huge volumes of documents for AI, is the engineering problem I want to work on. I know the legal world from **Elite 3E**, and this role combines my high-volume, event-driven Azure work with AI and documents. I'm happy where I am; this is about moving **toward** AI and legal tech."

**[⬆ Back to Top](#table-of-contents)**

## 27. What is Elite 3E, and why do law firms customise it?

*Behavioural*

> "3E is Thomson Reuters' financial and practice management system for large law firms: timekeepers log hours on timecards, against client and matter, with rates; then proforma (draft bill), partner review, bill, collections. Firms customise it because billing differs: rate structures, fixed-fee and capped deals, client billing guidelines, LEDES e-billing with UTBMS codes, approval workflows and integrations. I did 3E IDE customisations, APIs, stored procedures, a billing tool, and a time-capture integration into timecards."

**[⬆ Back to Top](#table-of-contents)**

## 28. What questions do you have for me?

*Your questions*

> 1. "What's the biggest technical challenge for the team right now: scale, accuracy, or something else?"
> 2. "How does the team measure delivery and quality? Do you track DORA-style metrics?"
> 3. "What would success look like for me in the first 6 months?"
> 4. "How is the team using the Thomson model and AI tools in day-to-day development?"

**[⬆ Back to Top](#table-of-contents)**

## 29. What document-processing work have you done?

*Your stories*

> "At Centric, in US insurance, I worked on **Kafka-driven document generation**: a policy event arrives as JSON, we render the **PDF**, store it in **Blob Storage** and notify downstream. It's **idempotent on policy ID + version**, so a replayed event doesn't create a second document. Consumers scale with partitions at renewal peaks, and failures retry, then go to a **dead-letter topic**.

> At Accolite I worked on high-volume **compliance reports** for 100+ clients, and at Staples I generate **legacy fixed-width files** from events. So: documents in, documents out, at volume, reliably."

**Follow-up:** PDF created but the notification failed? The retry sees the PDF already exists, skips regenerating, and only re-sends the notification.

**[⬆ Back to Top](#table-of-contents)**

## 30. How would you process 10,000 documents with an LLM?

*AI & LLMs*

> "Never in one synchronous request. The client gets **202 Accepted** with a job ID. Each document becomes a **message on a queue** (Service Bus). **Workers on AKS**, scaled by **KEDA** on queue length, process them: extract text (OCR if scanned), chunk, call the LLM.

> The LLM is the bottleneck, so I **throttle to the quota**: cap concurrency with SemaphoreSlim, retry 429s honouring Retry-After. Each result is saved per document, **idempotent on document ID**, so retries don't duplicate. Failures go to a **dead-letter queue** for replay. The client polls the job status and sees progress, like 7,412 of 10,000."

**Follow-up:** Cost control: cache by document content hash, use a smaller model for easy steps, send only the relevant chunks instead of whole documents.

**[⬆ Back to Top](#table-of-contents)**

## 31. Walk me through a document pipeline: upload to searchable.

*AI & LLMs*

> "1. **Upload** straight to Blob Storage with a short-lived **SAS URL**, so big files don't go through the API. 2. A Blob event puts a message on a **queue**. 3. A worker runs **OCR** if needed and **layout detection**: headings, tables, pages. 4. **Classify** the document type. 5. **Chunk** by structure with metadata (document, page, section). 6. **Embed** and index in **Azure AI Search**. 7. Update the status so the user sees 'ready'.

> Each step is idempotent and retryable, and a poison document goes to dead-letter instead of blocking the queue."

**[⬆ Back to Top](#table-of-contents)**

## 32. What do you know about CoCounsel and the Thomson model?

*Behavioural*

> "CoCounsel is TR's AI assistant for legal and tax professionals, now used by over a million people. It's agentic: it plans multi-step work, and there's Deep Research. TR also has its own model, **Thomson**, first used in **Tabular Analysis**: asking many questions across thousands of documents and getting answers **with citations**. That's why the document platform matters so much: if extraction and chunking are wrong, the AI's answers and citations are wrong."

**[⬆ Back to Top](#table-of-contents)**

## 33. Which Azure services have you used, and for what?

*Kubernetes & Docker*

> "**AKS** for our microservices; **APIM** as the gateway; **Event Hubs** for events; **Azure SQL / SQL Server** and **Table Storage** for data; **Blob Storage** for documents; **Key Vault** with managed identity for secrets; **Container Registry** for images; **App Insights** for monitoring; **Azure DevOps** for CI/CD. On the AI side, **Azure OpenAI and Azure AI Search**. And **Google Pub/Sub** on GCP for one of our consumers."

**Follow-up:** Event Hubs vs Service Bus: Event Hubs for high-volume streams that many consumers read and can replay. Service Bus for commands and work items: one consumer per message, dead-lettering, sessions for ordering.

**[⬆ Back to Top](#table-of-contents)**

## 34. Why event-driven? When would you NOT use it?

*Kubernetes & Docker*

> "Event-driven **decouples** systems: the producer doesn't wait for consumers, a slow or down consumer doesn't break the producer, and you can add consumers without changing the producer. The price is **eventual consistency**, harder debugging (correlation IDs help), and handling duplicates and ordering.

> I wouldn't use it when the caller **needs the answer now**, like our carrier call: the customer needs the carrier in the response, so that one is synchronous."

**[⬆ Back to Top](#table-of-contents)**

## 35. Tell me about the .NET Framework to .NET Core migration.

*Your stories*

> "At Accolite we migrated **module by module**, not as a big bang. For each module: check the NuGet dependencies, then upgrade them, find alternatives, or wrap the unsupported ones in an internal package. Port the code, run the **existing tests plus new ones** around risky areas, deploy, then move to the next module. Benefits: better performance, cross-platform containers, modern DI and configuration, long-term support."

**Follow-up:** Hardest part: unsupported dependencies and old configuration (web.config to appsettings). Kept risk low with tests and small releases.

**[⬆ Back to Top](#table-of-contents)**

## 36. Have you worked with Angular? Front end or back end?

*Your stories*

> "Backend is my strength, but I'm comfortable full stack. At Centric I worked on the **ASP.NET to Angular migration** with PrimeNG, and at Accolite I built Angular features for the compliance platform: components, services calling our APIs, RxJS for async data, forms with validation."

**[⬆ Back to Top](#table-of-contents)**

## 37. Any experience with Rust, Python, AWS or GCP?

*Your stories*

> "**GCP:** yes, Google Pub/Sub for the warehouse integration. **AWS:** lighter, but the concepts map directly: S3 is Blob, SQS is a storage queue or Service Bus, EKS is AKS, Lambda is Functions. **Python:** scripting and AI tooling. **Rust:** I've started learning it. It fits performance-heavy document processing, and I'd be keen to go deeper here."

**[⬆ Back to Top](#table-of-contents)**

## 38. What does MLOps mean to you as a software engineer?

*AI & LLMs*

> "Treating models like any other production dependency: **versioning** models and prompts, **evaluating** before rollout (a test set with known answers), **monitoring** quality, latency and cost in production, handling **quotas and rate limits**, and being able to **roll back** to the previous model or prompt version. My Ollama experiment taught me the serving side: hardware, latency and throughput really matter."

**[⬆ Back to Top](#table-of-contents)**

## 39. How do you handle multi-region and data residency?

*Kubernetes & Docker*

> "Data residency means a UK customer's documents stay in UK regions. So we deploy the **same stack per region**: storage, database, queues, processing. Route users to their region (Front Door or by tenant), and **never replicate their data across regions**. For availability within a region, use zone redundancy, and pair regions inside the same geography for failover. Shared things like code and container images can be global."

**[⬆ Back to Top](#table-of-contents)**

## 40. How do you work in Agile? Estimates and deadlines?

*Behavioural*

> "Two-week sprints with planning, daily stand-ups, review and retro. I break features into small, shippable tickets so progress is visible. On a tight deadline I split the work into **essentials first** and agreed with the business what could come in a second release. I also helped set up an **upfront integration-ticket process**, so other teams' requests came with payloads and requirements before we started, which cut back-and-forth a lot."

**[⬆ Back to Top](#table-of-contents)**

## 41. How do you handle vague or changing requirements?

*Behavioural*

> "I turn conversations into something concrete fast: a **mapping document or example payload**, so people react to a draft instead of an idea. With the carrier integration we built in parallel with the vendor from **example payloads**, including bilingual EN/FR fields, and confirmed edge cases early. When requirements change, I make the impact visible (what moves, what's at risk) and let the product owner decide."

**[⬆ Back to Top](#table-of-contents)**

## 42. What is SOLID? Give a real example.

*Quality*

> "**S:** one reason to change, e.g. separate the carrier client from the mapping logic. **O:** add a new downstream format by adding a new class, not editing the old ones. **L:** any implementation of an interface must behave as callers expect. **I:** small focused interfaces. **D:** depend on interfaces and inject implementations, which is what makes our services testable with mocks.

> In our inventory flow each downstream system has its own **formatter behind one interface** (JSON for one, fixed-width for another), so a new consumer is a new class plus a DI registration."

**[⬆ Back to Top](#table-of-contents)**

## 43. DRY, and composition vs inheritance?

*Quality*

> "**DRY:** one source of truth for each piece of logic, e.g. one shared mapping helper instead of copying the same SKU mapping into three services. But don't over-DRY: two things that look similar today but change for different reasons should stay separate.

> **Composition over inheritance:** build behaviour by combining small objects (inject a retry policy and a formatter) rather than deep base-class hierarchies, which are rigid and fragile. Inheritance only for a true 'is-a' relationship."

**[⬆ Back to Top](#table-of-contents)**

## 44. Which collection keeps items sorted as you insert?

*Quality*

> "**SortedDictionary<TKey,TValue>**: a tree, O(log n) insert and lookup. **SortedList**: arrays, less memory and fast lookups, but O(n) inserts. **SortedSet<T>** for unique sorted values. **PriorityQueue** when you only need the smallest item next. A normal Dictionary has **no order guarantee**."

**[⬆ Back to Top](#table-of-contents)**

## 45. How do you handle race conditions in .NET?

*Resilience*

> "A race condition is two threads updating shared state at once, like count++ on a shared field losing updates. Fixes: **lock** for a small critical section, **Interlocked.Increment** for counters, **ConcurrentDictionary** for shared maps, **SemaphoreSlim** for async code (you can't await inside a lock). Best of all is **avoiding shared state**. Across services, use the database: optimistic concurrency with a row version, or a unique constraint."

**[⬆ Back to Top](#table-of-contents)**

## 46. Explain Kubernetes architecture at a high level.

*Kubernetes & Docker*

> "The **control plane** (managed by Azure in AKS) has the **API server**, which everything talks to; **etcd**, which stores the cluster state; the **scheduler**, which picks a node for each pod; and **controllers**, which keep the actual state matching the desired state. Each **worker node** runs the **kubelet**, which starts and watches pods, **kube-proxy** for networking, and the container runtime. You declare the desired state in YAML, and Kubernetes keeps making it true."

**[⬆ Back to Top](#table-of-contents)**

## 47. How do you secure your APIs and services?

*APIs*

> "Users authenticate with **OAuth2 / OpenID Connect** (Entra ID). The API validates the **JWT** (signature, issuer, audience, expiry), then checks **scopes or roles**. Service to service uses **managed identity**, so there are no secrets in config. APIM in front adds rate limiting. Secrets live in Key Vault, everything is HTTPS, inputs are validated, and SQL is parameterised."

**[⬆ Back to Top](#table-of-contents)**

## 48. Abstract class vs interface — what's the difference and when do you use each?

*C# & .NET*

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

## 49. Value type vs reference type

*C# & .NET*

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

## 50. How do you handle exceptions in C#?

*C# & .NET*

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

## 51. What are generics, and why use them?

*C# & .NET*

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

## 52. What are record types?

*C# & .NET*

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

## 53. How does the Garbage Collector work?

*C# & .NET*

The GC tracks object reachability from a set of roots (static fields, thread stacks,
CPU registers) and reclaims anything unreachable. It's generational — Gen 0
(short-lived objects, collected most often/cheaply), Gen 1 (a buffer), Gen 2
(long-lived objects, collected least often, most expensively), plus a separate Large
Object Heap for allocations over ~85KB. This is why churning lots of small,
short-lived objects is usually fine (Gen 0 collections are fast) while large
allocations or objects that survive into Gen 2 are the ones that hurt.

**[⬆ Back to Top](#table-of-contents)**

## 54. `Dispose()` vs `Finalize()`

*C# & .NET*

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

## 55. Hashtable vs Dictionary, and how do they work internally?

*C# & .NET*

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

## 56. `IEnumerable` vs `IQueryable`

*C# & .NET*

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

## 57. .NET Framework vs .NET Core

*C# & .NET*

The **.NET Framework** is the original, Windows-only runtime and base class library.
**.NET Core** (now unified as modern **.NET 5+**) is cross-platform (Windows,
macOS, Linux), open-source, more modular, and generally faster — built for cloud and
containerized workloads. New development targets modern .NET; the Framework is
effectively legacy-maintenance-only at this point.

**[⬆ Back to Top](#table-of-contents)**

## 58. IEnumerable vs List — deferred execution vs eager loading

*C# & .NET*

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

## 59. What is middleware, and how do you write a custom one?

*ASP.NET Core & APIs*

Middleware are components chained together in the ASP.NET Core **request
pipeline** — each one can inspect/modify the request, decide to short-circuit, or
call the next component and then inspect/modify the response on the way back out.

```csharp
public class RequestTimingMiddleware
{
    private readonly RequestDelegate _next;
    public RequestTimingMiddleware(RequestDelegate next) => _next = next;

    public async Task InvokeAsync(HttpContext context)
    {
        var sw = Stopwatch.StartNew();
        await _next(context); // call the rest of the pipeline
        Console.WriteLine($"{context.Request.Path} took {sw.ElapsedMilliseconds}ms");
    }
}

// Startup/Program.cs:
app.UseMiddleware<RequestTimingMiddleware>();
```

Order matters — middleware registered earlier wraps everything registered after it
(think nested `try/finally` blocks).

**[⬆ Back to Top](#table-of-contents)**

## 60. Middleware vs action filter — when do you use which?

*ASP.NET Core & APIs*

**Middleware** operates on the raw HTTP request/response and runs for *every*
request regardless of which controller/action (or even whether one exists) —
good for cross-cutting infrastructure concerns like authentication, logging,
CORS, exception handling, response compression. **Action filters** run inside
the MVC pipeline, after routing has already resolved a controller/action, and have
access to MVC-specific context (model state, action arguments, the
`ActionDescriptor`) — good for concerns tied to *that specific action*, like
model validation or auditing a particular endpoint.

**[⬆ Back to Top](#table-of-contents)**

## 61. `AddSingleton` vs `AddScoped` vs `AddTransient`

*ASP.NET Core & APIs*

| Lifetime | Instance created | Typical use |
|---|---|---|
| `AddTransient` | A new instance every time it's requested | Lightweight, stateless services |
| `AddScoped` | One instance per HTTP request (or per scope) | `DbContext`, per-request unit-of-work services |
| `AddSingleton` | One instance for the lifetime of the app | Stateless services, in-memory caches, configuration objects |

```csharp
builder.Services.AddTransient<IEmailValidator, EmailValidator>(); // new one every injection
builder.Services.AddScoped<IOrderContext, OrderContext>();        // one per HTTP request
builder.Services.AddSingleton<IAppCache, AppCache>();              // one for the app's whole life
```

**[⬆ Back to Top](#table-of-contents)**

## 62. What is Dependency Injection, and how is it implemented in .NET Core?

*ASP.NET Core & APIs*

DI is a pattern for **Inversion of Control** — a class receives its dependencies
from the outside instead of constructing them itself, which decouples it from
concrete implementations and makes it trivially testable (swap in a mock).

```csharp
public interface IMyService { void DoWork(); }
public class MyService : IMyService { public void DoWork() { /* ... */ } }

// Program.cs
builder.Services.AddTransient<IMyService, MyService>();

// consumer — the container resolves IMyService automatically
public class MyController : Controller
{
    private readonly IMyService _myService;
    public MyController(IMyService myService) => _myService = myService;
}
```

.NET Core ships a built-in DI container (`IServiceCollection`/`IServiceProvider`);
third-party containers like Autofac or Simple Injector plug in when you need more
advanced features (e.g. property injection, assembly scanning, child containers).

**[⬆ Back to Top](#table-of-contents)**

## 63. Code review: Singleton depending on Scoped — what's wrong?

*ASP.NET Core & APIs*

```csharp
public class B {}
public class A { public A(B b) {} }

builder.Services.AddSingleton<A>();
builder.Services.AddScoped<B>();
```

This is a **captive dependency** bug. `A` is built exactly once, for the whole
app's lifetime, at which point it captures a single instance of `B`. But `B` is
`Scoped` — meant to be created fresh per request (or disposed at the end of a
scope). The result: every request that goes through `A` gets the *same* `B`
instance forever, frozen at whatever state it had when `A` was first constructed —
and if `B` holds a `DbContext` or anything disposable, you can end up calling
methods on an already-disposed object.

**The fix:** either make `B` a singleton too (if it's safe to share), make `A`
scoped/transient instead, or — if `A` genuinely needs to live for the app's
lifetime but needs a fresh `B` per operation — inject `IServiceScopeFactory` (or
`IServiceProvider`) into `A` and create a new scope each time you need `B`, rather
than injecting `B` directly into the constructor.

**[⬆ Back to Top](#table-of-contents)**

## 64. What is `HttpClientFactory`, and why use it?

*ASP.NET Core & APIs*

Creating a new `HttpClient` per request and disposing it looks correct but leaks
sockets under load (`HttpClient` doesn't release the underlying TCP connection
immediately on `Dispose()`, so heavy churn can exhaust available sockets — the
well-known "socket exhaustion" problem). Reusing a single static `HttpClient`
avoids that, but then DNS changes never get picked up. `IHttpClientFactory` solves
both: it pools and reuses underlying handlers while still letting you get a fresh
logical `HttpClient` per use, and it integrates with DI, named/typed clients, and
Polly-based retry policies.

**[⬆ Back to Top](#table-of-contents)**

## 65. GET vs POST, PUT vs PATCH

*ASP.NET Core & APIs*

- **GET** retrieves a resource; no body, safe (no side effects), cacheable.
- **POST** creates a resource or triggers a non-idempotent action; has a body, not
  safe, not idempotent (posting twice usually creates two things).
- **PUT** replaces a resource entirely at a known URI; idempotent — sending the
  same PUT twice leaves the resource in the same state.
- **PATCH** applies a partial update to a resource; not guaranteed idempotent in
  general, though many implementations make it so.

**[⬆ Back to Top](#table-of-contents)**

## 66. What makes an HTTP method idempotent?

*ASP.NET Core & APIs*

An idempotent method produces the same result on the server no matter how many
times you repeat the identical request. `GET`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`
are idempotent by spec; `POST` and (typically) `PATCH` are not. This matters
practically for retry logic — it's safe to blindly retry an idempotent request
after a timeout, but retrying a `POST` risks double-creating a resource unless
you've added your own idempotency key.

**[⬆ Back to Top](#table-of-contents)**

## 67. How do you design a RESTful API?

*ASP.NET Core & APIs*

- Model URIs around **resources** (nouns), not actions: `/orders/42`, not
  `/getOrder?id=42`.
- Use HTTP verbs to express the operation (GET/POST/PUT/PATCH/DELETE) and
  status codes to express the outcome (`200`, `201 Created` with a `Location`
  header, `204 No Content`, `400`, `401`/`403`, `404`, `409 Conflict`, `500`).
- Version the API (`/api/v2/...` or a header) from day one.
- Support pagination, filtering, and sorting via query parameters for collection
  endpoints.
- Keep responses consistent — a predictable envelope/error shape across every
  endpoint.
- Secure it (auth, input validation, rate limiting, HTTPS-only) and document it
  (OpenAPI/Swagger).

**[⬆ Back to Top](#table-of-contents)**

## 68. How does token-based authentication work end to end?

*ASP.NET Core & APIs*

1. Client sends credentials to a login endpoint.
2. Server validates them and issues a signed token (typically a JWT) containing
   claims (user id, roles, expiry).
3. Client stores the token and sends it on every subsequent request, usually as
   `Authorization: Bearer <token>`.
4. Server validates the token's signature and expiry on each request — no session
   state needs to be kept server-side, which is what makes this approach scale
   horizontally so well.

**[⬆ Back to Top](#table-of-contents)**

## 69. OAuth vs JWT

*ASP.NET Core & APIs*

They solve different problems and are often confused: **OAuth 2.0** is an
**authorization framework/protocol** — it defines how a client gets permission
(and a token) to access a resource on a user's behalf, typically involving a
redirect-based consent flow with an authorization server. **JWT** is just a
**token format** — a compact, signed, self-contained way to represent claims. OAuth
doesn't require JWTs (opaque tokens work too), and JWTs are used plenty outside of
OAuth flows (e.g. a simple app issuing its own signed session tokens). In practice
they're often combined: OAuth handles the authorization dance, and the access
token it hands back happens to be a JWT.

**[⬆ Back to Top](#table-of-contents)**

## 70. How would you design multi-tenancy into an application?

*ASP.NET Core & APIs*

Three common models, in increasing order of isolation (and cost):

1. **Shared database, shared schema** — every tenant's rows live in the same
   tables, distinguished by a `TenantId` column present everywhere. Cheapest to
   run and easiest to patch, but requires discipline (every query must filter by
   tenant, usually enforced via a global query filter in EF Core).
2. **Shared database, separate schema** — each tenant gets its own schema in one
   database. Better isolation, still one database to operate.
3. **Separate database per tenant** — strongest isolation and easiest per-tenant
   backup/compliance story, but the most operational overhead (migrations have to
   run against every tenant database).

**[⬆ Back to Top](#table-of-contents)**

## 71. How do you implement global exception handling in ASP.NET Core?

*ASP.NET Core & APIs*

Register exception-handling middleware near the top of the pipeline:

```csharp
app.UseExceptionHandler(errApp => errApp.Run(async context =>
{
    context.Response.StatusCode = 500;
    var feature = context.Features.Get<IExceptionHandlerFeature>();
    await context.Response.WriteAsJsonAsync(new { error = "Something went wrong." });
}));
```

Alternatively, implement `IExceptionFilter` for MVC-scoped handling, or a custom
`ProblemDetails` factory to return RFC 7807-style error payloads consistently
across every endpoint.

**[⬆ Back to Top](#table-of-contents)**

## 72. How do you implement distributed caching in .NET Core?

*ASP.NET Core & APIs*

Register an `IDistributedCache` implementation (Redis, SQL Server, or NCache) so
multiple app instances share one cache instead of each keeping its own in-memory
copy:

```csharp
builder.Services.AddStackExchangeRedisCache(options =>
    options.Configuration = "redis-server:6379");

// usage
await cache.SetStringAsync("key", value, new DistributedCacheEntryOptions
{
    AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(10)
});
var cached = await cache.GetStringAsync("key");
```

Use this over `IMemoryCache` whenever the app runs on more than one instance,
since an in-memory cache would be inconsistent across instances.

**[⬆ Back to Top](#table-of-contents)**

## 73. Design a secure, scalable Web API — what do you actually check?

*ASP.NET Core & APIs*

- **AuthN/AuthZ:** token-based auth (JWT/OAuth2), least-privilege authorization
  policies, not relying on obscurity.
- **Input validation:** validate and sanitize everything at the boundary; never
  trust client-supplied IDs or roles.
- **Transport security:** HTTPS everywhere, HSTS, no sensitive data in URLs.
- **Rate limiting/throttling** to blunt abuse and brute-force attempts.
- **Consistent error handling** that doesn't leak stack traces or internals.
- **Scalability:** stateless auth (no server-side session), horizontal scale-out
  behind a load balancer, distributed cache instead of in-process cache.
- **Observability:** structured logging, correlation IDs, health checks.

**[⬆ Back to Top](#table-of-contents)**

## 74. Benefits of `async`/`await` in C#

*ASP.NET Core & APIs*

Frees up threads during I/O-bound waits (DB calls, HTTP calls, file I/O) instead
of blocking them, which is what lets a web server handle far more concurrent
requests with the same thread pool. It also keeps asynchronous code readable —
sequential-looking code instead of nested callbacks — while still giving you
structured exception handling (a regular `try/catch` around an `await`) and easy
composition of multiple async operations (`Task.WhenAll`, `Task.WhenAny`).

**[⬆ Back to Top](#table-of-contents)**

## 75. IOptions vs IOptionsSnapshot vs IOptionsMonitor — configuration lifetimes

*ASP.NET Core & APIs*

All three give you strongly-typed access to a section of `appsettings.json`, but
they differ in **when** they read the configuration:

| | Lifetime | Re-reads config? |
|---|---|---|
| `IOptions<T>` | Singleton | No — loaded once at startup, never changes for the app's lifetime |
| `IOptionsSnapshot<T>` | Scoped | Yes — re-reads once per request/scope, so a config file change shows up on the next request |
| `IOptionsMonitor<T>` | Singleton | Yes — re-reads live, and can notify you via `OnChange` the instant the file changes, even inside a singleton |

```csharp
builder.Services.Configure<MySettings>(builder.Configuration.GetSection("MySettings"));

public class MyService
{
    public MyService(IOptions<MySettings> options)
    {
        var value = options.Value.SomeSetting; // fixed for the app's entire lifetime
    }
}

public class MyScopedService
{
    public MyScopedService(IOptionsSnapshot<MySettings> options)
    {
        var value = options.Value.SomeSetting; // fresh on every HTTP request
    }
}

public class MyMonitoringService
{
    public MyMonitoringService(IOptionsMonitor<MySettings> options)
    {
        options.OnChange(updated => Console.WriteLine($"Config changed: {updated.SomeSetting}"));
    }
}
```

**How to phrase it:** "`IOptions` is a singleton snapshot taken once at startup —
fine for settings that never change while the app runs. `IOptionsSnapshot` is
scoped, so it's for settings you want to pick up per request without restarting
the app. `IOptionsMonitor` is for the same live-reload need but from inside a
singleton, plus it gives you a change notification callback."

**[⬆ Back to Top](#table-of-contents)**

## 76. What is Azure Key Vault, and how do you access secrets from it?

*Azure*

A managed service for storing secrets, connection strings, API keys, and
certificates outside of application code/config files, with fine-grained access
policies and audit logging. Typical access pattern from a .NET app:

```csharp
var client = new SecretClient(
    new Uri("https://myvault.vault.azure.net/"),
    new DefaultAzureCredential()); // uses Managed Identity when running in Azure

KeyVaultSecret secret = await client.GetSecretAsync("MyConnectionString");
```

`DefaultAzureCredential` is what lets the same code authenticate via Managed
Identity in Azure and via developer credentials locally, without hardcoding
anything.

**[⬆ Back to Top](#table-of-contents)**

## 77. Why use a Managed Identity instead of stored credentials?

*Azure*

A Managed Identity gives an Azure resource (a Web App, a Function, a VM) an
identity in Azure AD that it can use to authenticate to other Azure services
(Key Vault, SQL, Storage) **without any credential ever being stored in code,
config, or a pipeline variable**. Azure rotates the underlying credential
automatically and it's scoped to that specific resource, which eliminates an
entire class of "leaked connection string" incidents.

**[⬆ Back to Top](#table-of-contents)**

## 78. Azure Service Bus vs Event Hubs

*Azure*

| | Service Bus | Event Hubs |
|---|---|---|
| Purpose | Enterprise messaging — queues and pub/sub topics | Big-data event/telemetry streaming |
| Throughput | Moderate | Very high (millions of events/sec) |
| Message retention | Typically short-term, consumed then removed | Can retain a stream for a configured window, replayable |
| Ordering | Can guarantee FIFO within a queue/session | Maintains order within a partition |
| Consumer model | Competing consumers (each message to one consumer) | Consumer groups (multiple independent readers over the same stream) |
| Typical use | Order processing, work queues, decoupling services | Telemetry ingestion, log/event streaming, IoT |

**[⬆ Back to Top](#table-of-contents)**

## 79. How does Azure Service Bus ensure message durability?

*Azure*

Messages are persisted to storage as soon as they're sent (not held only in
memory), so a broker failure doesn't lose them. Durability features include
message locking with a visibility timeout (a consumer must explicitly complete or
abandon a message, or it becomes available again), dead-lettering for messages
that repeatedly fail processing, and duplicate detection windows to guard against
redelivery causing double-processing.

**[⬆ Back to Top](#table-of-contents)**

## 80. How do you onboard an API into Azure API Management (APIM)?

*Azure*

Import the backend API (from an OpenAPI/Swagger definition, a WSDL, or manually),
which creates a managed **front door** in front of it. From there you configure
**policies** (rate limiting, IP filtering, request/response transformation,
caching), apply **products/subscriptions** to control who can call it and with
what key, and publish it through a **developer portal** for API consumers to
discover and self-service subscribe.

**[⬆ Back to Top](#table-of-contents)**

## 81. What are the key components of an Azure DevOps CI/CD pipeline?

*Azure*

- **Repos** — source control (or an external Git provider).
- **Build (CI) pipelines** — compile, run tests, produce artifacts on every
  push/PR.
- **Artifacts** — the versioned output of a build (a package, a zip, a container
  image) that release pipelines consume.
- **Release (CD) pipelines** — take an artifact and deploy it through
  environments (Dev → QA → Staging → Prod), often with approval gates between
  stages.
- **Triggers** — events (a push, a schedule, a successful upstream build) that
  kick off a pipeline automatically.

**[⬆ Back to Top](#table-of-contents)**

## 82. App Service vs Azure Functions — when do you choose each?

*Azure*

**App Service** is a fully managed PaaS for hosting a continuously running web
app/API — predictable load, always-on, full control over the runtime environment.
**Azure Functions** is serverless/event-driven — code runs in response to a
trigger (an HTTP call, a queue message, a timer), scales automatically (including
to zero when idle), and you're billed per execution rather than for an always-on
instance. Choose Functions for sporadic, event-driven workloads or when you want
to avoid managing an always-on server; choose App Service for a full web
application or when you need more control over the hosting environment
(warm-up behavior, longer-running requests, specific runtime configuration).

**[⬆ Back to Top](#table-of-contents)**

## 83. What is Infrastructure as Code (IaC)?

*Azure*

Defining and provisioning infrastructure (VMs, networks, databases, App Services)
through versioned, declarative configuration files — ARM templates, Bicep, or
Terraform — rather than clicking through a portal. Benefits: repeatable,
consistent environments (dev/staging/prod built from the same definition), full
change history in source control, and infrastructure changes go through the same
review/PR process as application code.

**[⬆ Back to Top](#table-of-contents)**

## 84. How would you design a highly available, scalable Azure architecture?

*Azure*

- **Compute:** Azure App Service (or AKS) with auto-scaling rules, running
  multiple instances behind a load balancer.
- **Data tier:** Azure SQL Database with geo-replication/failover groups for
  disaster recovery.
- **Global routing:** Azure Traffic Manager or Front Door to route traffic across
  regions and fail over automatically.
- **Storage:** Blob Storage or Cosmos DB, chosen for the access pattern, with
  geo-redundant replication.
- **Caching/CDN:** Azure CDN for static content at the edge; Redis Cache to take
  load off the database for hot reads.
- **Resilience patterns:** retries with backoff, circuit breakers, health checks
  feeding into the load balancer so unhealthy instances get pulled out of
  rotation automatically.

**[⬆ Back to Top](#table-of-contents)**

## 85. How do you ensure data consistency across microservices?

*Microservices*

Because each microservice typically owns its own database, you can't rely on a
single ACID transaction spanning several of them. Approaches, roughly in order of
how often they come up:

- **Saga pattern** — a sequence of local transactions across services, each
  publishing an event that triggers the next step; if a step fails, previously
  completed steps run **compensating transactions** to undo their effect (e.g.
  "release inventory" if payment fails after inventory was already reserved).
- **Eventual consistency** — accept that data across services converges over
  time rather than instantly, communicated via events.
- **CQRS** — separate the write model from the read model, so reads can be served
  from a denormalized, eventually-consistent projection built from the events the
  write side emits.
- **Idempotent operations** — design consumers so processing the same event twice
  (which *will* happen in a distributed system) doesn't double-apply an effect.

**[⬆ Back to Top](#table-of-contents)**

## 86. What strategies do you use for inter-service communication?

*Microservices*

| Style | Good for |
|---|---|
| Synchronous REST | Simple request/response, external-facing APIs |
| gRPC | Low-latency, high-throughput internal service-to-service calls, strongly-typed contracts |
| Message queues (RabbitMQ, Azure Service Bus) | Decoupled, asynchronous work, reliable delivery, buffering load spikes |
| Event streaming (Kafka) | High-volume event pipelines, multiple independent consumers, replayable history |
| GraphQL | Flexible querying, especially aggregating data from several services for a client |
| Service mesh (Istio, Linkerd) | Cross-cutting networking concerns (retries, mTLS, observability) applied uniformly without changing service code |

**General rule to state out loud:** prefer asynchronous messaging between
services for anything that doesn't need an immediate response — it's what
actually gives you the resilience and independent scalability microservices are
supposed to provide; synchronous chains of calls just recreate a distributed
monolith with worse latency.

**[⬆ Back to Top](#table-of-contents)**

## 87. How do you handle failures between two microservices?

*Microservices*

- **Retries with exponential backoff** for transient failures.
- **Circuit breaker** (e.g. Polly in .NET) — stop calling a downstream service
  that's clearly failing, fail fast for a cooldown period, and periodically probe
  whether it's recovered, instead of piling up timeouts and cascading the failure
  upstream.
- **Timeouts** on every outbound call — never wait indefinitely.
- **Fallbacks/graceful degradation** — return cached or default data instead of a
  hard failure where the business can tolerate it.
- **Dead-letter queues** for messages that repeatedly fail processing, so they
  don't block the queue or get silently dropped.

**[⬆ Back to Top](#table-of-contents)**

## 88. How do you secure microservice-to-microservice communication?

*Microservices*

**TLS everywhere** (including internal traffic, not just the public edge) —
often via **mutual TLS (mTLS)** so both sides authenticate each other, commonly
enforced transparently by a service mesh rather than each service implementing it
itself. Combine with network-level isolation (private VNets/subnets, no direct
internet exposure for internal services) and short-lived, scoped service
credentials rather than long-lived shared secrets.

**[⬆ Back to Top](#table-of-contents)**

## 89. How do you debug a microservice in a containerized environment?

*Microservices*

- **Structured logging** with a **correlation ID** propagated across every
  service a request touches, aggregated into a central log store (e.g. ELK,
  Azure Log Analytics) so you can trace one request across service boundaries.
- **Distributed tracing** (OpenTelemetry, Jaeger, Application Insights) to see
  the full call graph and where time/errors actually occurred.
- **`kubectl logs`/`kubectl exec`** (or the equivalent for your orchestrator) to
  inspect a running container directly, and remote-debugger attach for local
  reproduction when a log trail alone isn't enough.
- Reproducing the issue locally with the same container image via Docker Compose
  where possible, rather than debugging only against the live cluster.

**[⬆ Back to Top](#table-of-contents)**

## 90. How would you refactor a monolith into microservices?

*Microservices*

1. **Identify seams** along business capability boundaries (bounded contexts, in
   Domain-Driven Design terms) — not arbitrary technical layers.
2. **Strangle, don't rewrite** — extract one capability at a time behind a
   facade/gateway, routing traffic for that capability to the new service while
   everything else still goes to the monolith (the "Strangler Fig" pattern).
3. Give the extracted service its **own data store** as soon as practical —
   sharing a database with the monolith defeats most of the point and just
   recreates coupling through the schema.
4. Handle **cross-cutting concerns** (auth, logging) consistently across old and
   new via a shared gateway/library rather than duplicating ad hoc.
5. Migrate incrementally, validating each extracted service in production before
   moving to the next, rather than a single big-bang cutover.

**[⬆ Back to Top](#table-of-contents)**

## 91. How do you monitor application health and performance?

*Microservices*

- **Health check endpoints** (`/health`) that a load balancer or orchestrator
  polls to decide whether to route traffic to an instance.
- **Metrics** (request rate, error rate, latency percentiles, resource
  utilization) shipped to a monitoring platform (Application Insights, Datadog,
  Prometheus/Grafana) with alerting thresholds.
- **Structured logs** with correlation IDs, centrally aggregated.
- **Distributed tracing** to see where latency actually accumulates across a
  multi-service call chain.
- **Dashboards** built around the metrics that actually predict user-facing
  problems (latency and error rate), not just infrastructure vanity metrics like
  raw CPU.

**[⬆ Back to Top](#table-of-contents)**

## 92. Explain the SOLID principles, with a violation and a fix for each

*Design & patterns*

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

## 93. What design patterns have you actually used?

*Design & patterns*

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

## 94. `Thread` vs `Task`

*Async & concurrency*

A **`Thread`** is a raw OS-level thread — you manage its lifecycle directly, and
it's relatively expensive to create. A **`Task`** is a higher-level abstraction
representing a unit of work that runs on the **thread pool** by default — the
runtime manages scheduling, reuses pooled threads instead of creating new OS
threads per task, and `Task` composes cleanly with `async`/`await`,
continuations (`ContinueWith`), and cancellation. In modern C#, you almost always
want `Task`, not a raw `Thread` — reach for `Thread` only when you specifically
need a dedicated, long-lived, foreground/background-controlled thread outside the
pool.

```csharp
Thread t = new Thread(() => Console.WriteLine("Raw OS thread"));
t.Start(); // you manage this thread's lifecycle yourself

Task task = Task.Run(() => Console.WriteLine("Runs on a pooled thread"));
await task; // the runtime schedules and reuses threads for you
```

**[⬆ Back to Top](#table-of-contents)**

## 95. What is a `ConcurrentDictionary`?

*Async & concurrency*

A thread-safe dictionary implementation designed for high-concurrency scenarios —
multiple threads can read and write it simultaneously without external locking,
using fine-grained internal locking (or lock-free techniques) rather than a
single global lock. Use it instead of wrapping a plain `Dictionary` in your own
`lock` whenever multiple threads genuinely need concurrent read/write access; for
single-threaded or externally-synchronized access, a plain `Dictionary` is faster.

```csharp
var counts = new ConcurrentDictionary<string, int>();

// safe to call from many threads at once, no manual lock needed
Parallel.For(0, 1000, i =>
{
    counts.AddOrUpdate("hits", 1, (key, oldValue) => oldValue + 1);
});

Console.WriteLine(counts["hits"]); // reliably 1000 — a plain Dictionary here would corrupt or throw
```

**[⬆ Back to Top](#table-of-contents)**

## 96. How do you cancel a running Task?

*Async & concurrency*

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

## 97. What should you consider when writing async code?

*Async & concurrency*

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

## 98. What's the actual benefit of `async`/`await` over raw `Task`?

*Async & concurrency*

You *can* compose raw `Task` objects with `.ContinueWith()` chains, but it gets
unreadable fast, and exception handling across a chain of continuations is
awkward. `async`/`await` lets you write asynchronous code that **reads like
sequential code** — normal `try`/`catch`, normal control flow (`if`, loops)
around `await` points — while the compiler does the equivalent state-machine
transformation under the hood. The benefit is entirely about *readability and
correctness of the calling code*, not a different runtime execution model.

**[⬆ Back to Top](#table-of-contents)**

## 99. What is mocking, and when should you use it?

*Testing*

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

## 100. What makes a unit test a good one?

*Testing*

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

## 101. How do you handle external dependencies in a unit test?

*Testing*

Depend on **interfaces**, not concrete implementations, so a real database/HTTP
client/file system can be swapped for a mock or fake in the test. For code that's
hard to restructure this way (legacy code with concrete dependencies baked in),
wrap the external dependency behind a thin interface first (an "adapter"), which
is often the very first refactor needed before legacy code becomes testable at
all.

```csharp
// 1. Wrap the external call behind an interface
public interface IExternalApiService { Task<string> GetDataAsync(); }

public class MyService
{
    private readonly IExternalApiService _api;
    public MyService(IExternalApiService api) => _api = api; // injected, not `new`-ed up inside

    public async Task<string> GetGreetingAsync() => "Hello, " + await _api.GetDataAsync();
}

// 2. Unit test with Moq — no real HTTP call ever happens
var mockApi = new Mock<IExternalApiService>();
mockApi.Setup(x => x.GetDataAsync()).ReturnsAsync("Sam");

var service = new MyService(mockApi.Object);
var result = await service.GetGreetingAsync();

Assert.Equal("Hello, Sam", result);
mockApi.Verify(x => x.GetDataAsync(), Times.Once); // confirms it was actually called
```

**[⬆ Back to Top](#table-of-contents)**

## 102. Integration tests vs unit tests

*Testing*

**Unit tests** isolate a single unit with all its dependencies faked/mocked —
fast, pinpoint failures, but don't prove the pieces actually work *together*.
**Integration tests** exercise real collaborators (a real database, typically via
a test container or a dedicated test database; a real HTTP call to a downstream
service, or at least a more realistic stand-in) to verify the wiring between
components is actually correct. A healthy test suite has many fast unit tests and
a smaller number of integration tests covering the critical seams — not one
extreme or the other.

**[⬆ Back to Top](#table-of-contents)**

## 103. How do you unit test code that uses Dependency Injection?

*Testing*

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

## 104. What are the key components of a CI/CD pipeline?

*DevOps & Agile*

- **Continuous Integration:** every push/PR triggers an automated build and test
  run, catching integration problems immediately rather than at release time.
- **Continuous Delivery/Deployment:** a validated build automatically flows
  through environments (Dev → QA → Staging → Prod), with approval gates where
  needed for delivery, or fully automated for deployment.
- **Artifact management:** the exact build that passed CI is the *same* artifact
  promoted through every environment — never rebuilt per environment, which
  eliminates "it worked in staging but not prod because it was a different
  build" class of bugs.
- **Automated tests** integrated into the pipeline as a gate, not an afterthought.
- **Rollback strategy** for when a deployment goes wrong in production.

**[⬆ Back to Top](#table-of-contents)**

## 105. How do you resolve a merge conflict in Git?

*DevOps & Agile*

```bash
git status                     # see which files conflict
# open each conflicting file, look for <<<<<<<, =======, >>>>>>> markers
# manually edit to keep the correct combined result, remove the markers
git add <resolved-file>
git commit                     # completes the merge
```

For a conflict during a `rebase` instead of a `merge`, the flow is the same
(edit, `git add`), but you continue with `git rebase --continue` instead of
`git commit`. **Talk through your actual judgment process too:** understanding
*why* both sides changed the same lines (checking `git log` / `git blame` on the
conflicting hunk) before blindly picking one side, and running the test suite
after resolving — a conflict resolving cleanly doesn't guarantee it's
*semantically* correct.

**[⬆ Back to Top](#table-of-contents)**

## 106. Describe your experience with Agile/Scrum

*DevOps & Agile*

Structure this around the actual ceremonies and your role in them: daily
stand-ups (status/blockers, kept short), sprint planning (estimating and
committing to a sprint's scope), sprint reviews/demos (showing working software
to stakeholders), and retrospectives (what to keep/stop/start doing next sprint).
Mention concrete tools (Jira, Azure Boards) and something specific you
personally contributed to process improvement — a generic "we did stand-ups"
answer is forgettable; "I pushed for splitting a recurring blocker into its own
tracked spike after three retros flagged it" is not.

**[⬆ Back to Top](#table-of-contents)**

## 107. Concurrent update: User A's stale save overwrites User B's edit

*Scenarios*

**What's actually happening:** there's no concurrency control — the system reads
a row, and blindly writes it back based on what was read, regardless of whether
another write happened in between ("last write wins" by accident, not by
design).

**How to answer:**
1. Diagnose it as a classic **lost update** problem.
2. Fix it with **optimistic concurrency control** — add a version/timestamp
   column; on save, the `UPDATE` includes `WHERE Version = @originalVersion`,
   and if zero rows are affected, that tells you someone else changed it first
   (see the EF Core example in the [Entity Framework file](03-entity-framework-data-access.md#6-how-do-you-handle-concurrency-conflicts-in-ef-core)).
3. Decide the UX for the conflict: reject User B's save and ask them to
   re-review the current data (safest default), attempt a field-level merge if
   the changes don't overlap, or — for scenarios where losing the latest change
   is genuinely unacceptable — use **pessimistic locking** instead (lock the row
   for the duration of the edit), accepting the throughput cost that comes with
   it.

**[⬆ Back to Top](#table-of-contents)**

## 108. 1,000+ clients want conflicting business logic changes

*Scenarios*

This is a **configuration/extensibility** design question, not a "just add an
if statement" question.

- **Feature flags/toggles** scoped per client/tenant, so the new behavior only
  activates for clients who opted in.
- **Strategy pattern** — extract the varying logic behind a common interface,
  with a per-client (or per-plan) implementation resolved at runtime, instead of
  branching on client ID inline throughout the codebase.
- **Per-tenant configuration** stored as data, not code, wherever the difference
  is genuinely just parameters (thresholds, rates) rather than fundamentally
  different logic.
- Explicitly avoid the trap of a single codebase riddled with
  `if (clientId == "Acme") { ... }` scattered across files — that's what makes a
  system unmaintainable at scale.

**[⬆ Back to Top](#table-of-contents)**

## 109. An API that used to be fast is now over a minute slow

*Scenarios*

Work this like a real investigation, out loud:

1. **Establish what actually changed** — data volume growth is the single most
   common cause (a query that was fine against 10K rows can fall over at 50M
   without a supporting index).
2. **Profile, don't guess** — get the actual execution plan/APM trace for a slow
   request; check whether the time is in the database, in application code, or
   in a downstream call.
3. **Common suspects for "this used to be fast":** a missing or now-ineffective
   index as data grew, stale statistics causing a bad query plan, an N+1 query
   introduced by a later code change, a downstream dependency that's slowed down,
   or a cache that used to exist and quietly stopped working.
4. **Fix and verify** — apply the targeted fix (index, query rewrite, caching,
   pagination) and confirm with the same profiling tool, not just "it feels
   faster."

**[⬆ Back to Top](#table-of-contents)**

## 110. How do you troubleshoot performance issues in a distributed system?

*Scenarios*

1. **Establish where the time is actually going** first — distributed tracing
   (a correlation ID through every hop) is the single highest-leverage tool
   here; don't start optimizing a service that isn't actually the bottleneck.
2. Check for the usual distributed-systems suspects: a downstream service with
   degraded latency, a lock/contention point shared across instances, a
   thundering-herd retry storm, or a connection-pool exhaustion issue.
3. **Reproduce it under load** if possible (a load test against a
   staging/pre-prod environment) rather than guessing from production metrics
   alone.
4. Fix the actual bottleneck, then re-measure with the same tracing/metrics to
   confirm the fix, not just "the ticket is closed."

**[⬆ Back to Top](#table-of-contents)**

## 111. How do you ensure code quality across a team?

*Scenarios*

Code reviews with real substance (not rubber-stamp approvals), automated checks
enforced in CI (linting, formatting, test coverage gates) so review time is spent
on design/logic rather than style nits, a shared and written-down set of
conventions so reviews aren't relitigating personal preference every time, and
pairing/mentoring junior engineers on trickier changes rather than only
reviewing after the fact. Mention a concrete practice you've personally driven,
not just a list of generic best practices.

**[⬆ Back to Top](#table-of-contents)**

## 112. How do you handle disagreements over technical decisions?

*Scenarios*

Lead with **data over opinion** — a benchmark, a prototype, a concrete trade-off
comparison beats "I think X is better." State the other person's position back
to them accurately before countering it, to make sure the disagreement is real
and not a miscommunication. If it's a genuine judgment call with no clearly
correct answer, default to whoever owns the long-term maintenance of that code,
or escalate to a lightweight decision (a time-boxed spike, or a tech lead's
call) rather than letting it stall the team. And be honest that you've been on
the losing side of one of these before, and it worked out fine — that's a more
credible answer than claiming you're always right.

**[⬆ Back to Top](#table-of-contents)**

## 113. What's the most challenging part of working with microservices?

*Scenarios*

A credible, specific answer usually lands on one of: **debugging across service
boundaries** (a single user-facing failure can originate several hops away, and
without good distributed tracing it's genuinely hard to find), **data
consistency** without a shared database/transaction, or **operational
complexity** (more deployments, more moving pieces, more places for
configuration drift). Pick one, give a concrete example of it biting you, and
say what practice you adopted in response (e.g. correlation IDs everywhere,
after a specific incident that was painful to trace without them).

**[⬆ Back to Top](#table-of-contents)**

## 114. Describe a time you had to meet a tight deadline

*Scenarios*

STAR again, but the interesting part interviewers are listening for is **what
you cut or triaged**, not that you worked longer hours. A strong answer names a
specific trade-off you made deliberately (deferred a nice-to-have, shipped
behind a flag, cut test coverage on a low-risk path *and said so explicitly to
the team*) rather than implying you simply did everything, faster.

**[⬆ Back to Top](#table-of-contents)**

## 115. How do you respond to constructive criticism in code review?

*Scenarios*

The strongest answer treats review feedback as a normal, low-stakes part of the
process — evaluate the feedback on its merits, ask a clarifying question if the
concern isn't clear rather than assuming you know what they meant, and change
your approach when they're right without treating it as a loss. If you disagree,
explain your reasoning rather than either capitulating silently or digging in —
and if you've ever been wrong and updated your approach based on review
feedback, that's a genuinely good, concrete example to have ready.

**[⬆ Back to Top](#table-of-contents)**

## 116. An interviewer keeps probing deeper past your comfort zone

*Scenarios*

This happens in genuinely tough technical rounds — an interviewer asks you to
explain a concept, then keeps pushing ("what happens at a memory level," "how
does this compare to that other approach") past where your knowledge is solid.

**How to handle it:**
- It's completely fine, and more credible than bluffing, to say plainly: "I
  haven't gone that deep into it — my understanding stops around here, and in
  practice I'd look that specific detail up rather than rely on memory."
- Show your reasoning process on the parts you *do* know, rather than going
  silent — interviewers are often evaluating how you think under pressure at
  least as much as raw recall.
- If a term comes up that you can name but not fully explain, say so rather
  than guessing confidently and being wrong — a wrong confident answer reads
  worse than an honest "I'd need to check."
- Afterward, treat it as free diagnostic information: whatever they kept
  drilling into is exactly what to go deepen before the next interview.

**[⬆ Back to Top](#table-of-contents)**
