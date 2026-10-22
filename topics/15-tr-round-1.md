# Thomson Reuters Round 1: Senior Software Engineer I (Document AI platform)

> Hiring-manager round, 1 hour: technical questions on your experience with C#, .NET,
> OpenAPI, Kubernetes, GitHub, Docker and especially LLMs/AI. Say each answer out loud
> in under a minute before revealing it. Sections: Your stories, Kubernetes & Docker,
> APIs, AI & LLMs, Resilience, Quality, Behavioural, Your questions.

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
