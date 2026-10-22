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
