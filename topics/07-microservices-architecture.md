# Microservices & System Architecture

> This is the "senior" filter topic — junior candidates know what a microservice
> is, senior candidates know what actually breaks when you have twelve of them
> talking to each other in production.

## Table of Contents

| No. | Question |
|-----|----------|
| 1 | [What are the core principles of Clean Architecture?](#1-what-are-the-core-principles-of-clean-architecture) |
| 2 | [How do you ensure data consistency across microservices?](#2-how-do-you-ensure-data-consistency-across-microservices) |
| 3 | [What strategies do you use for inter-service communication?](#3-what-strategies-do-you-use-for-inter-service-communication) |
| 4 | [How do you handle auth across a microservices architecture?](#4-how-do-you-handle-auth-across-a-microservices-architecture) |
| 5 | [How do you evenly distribute load across multiple instances of a service?](#5-how-do-you-evenly-distribute-load-across-multiple-instances-of-a-service) |
| 6 | [How do you handle failures between two microservices?](#6-how-do-you-handle-failures-between-two-microservices) |
| 7 | [How do you secure microservice-to-microservice communication?](#7-how-do-you-secure-microservice-to-microservice-communication) |
| 8 | [How do you debug a microservice in a containerized environment?](#8-how-do-you-debug-a-microservice-in-a-containerized-environment) |
| 9 | [How would you refactor a monolith into microservices?](#9-how-would-you-refactor-a-monolith-into-microservices) |
| 10 | [Design a real-time, multi-source analytics system](#10-design-a-real-time-multi-source-analytics-system) |
| 11 | [Kafka producer/consumer basics](#11-kafka-producerconsumer-basics) |
| 12 | [What is RabbitMQ used for?](#12-what-is-rabbitmq-used-for) |
| 13 | [How do you monitor application health and performance?](#13-how-do-you-monitor-application-health-and-performance) |

## 1. What are the core principles of Clean Architecture?

Dependencies point **inward**, toward the domain — outer layers (UI, database,
frameworks) depend on inner layers (business rules), never the other way around.
Concretely, that usually means:

- **Entities/Domain** at the center — pure business rules, no framework
  dependencies.
- **Use Cases/Application** layer around that — orchestrates domain logic.
- **Interface Adapters** (controllers, presenters, repositories' interfaces).
- **Frameworks & Drivers** on the outside — the database, the web framework, the
  UI — all swappable without touching business logic.

The payoff: you can unit test business rules with zero database/web framework in
the loop, and swapping infrastructure (a different database, a different web
framework) doesn't ripple into the domain.

**[⬆ Back to Top](#table-of-contents)**

## 2. How do you ensure data consistency across microservices?

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

## 3. What strategies do you use for inter-service communication?

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

## 4. How do you handle auth across a microservices architecture?

- An **API Gateway** as the single entry point that authenticates the caller once
  and forwards a validated identity/token downstream, so individual services
  don't each reimplement login.
- **JWTs** carrying claims (user id, roles, tenant) that any downstream service
  can verify independently (signature + expiry) without a round trip to an auth
  server for every call.
- **OAuth2/OpenID Connect** for standardized token issuance, especially for
  third-party/external client access.
- **RBAC** (Role-Based Access Control) for fine-grained per-endpoint permission
  checks.
- **Mutual TLS** for service-to-service calls, so services also authenticate
  *each other*, not just the end user.

**[⬆ Back to Top](#table-of-contents)**

## 5. How do you evenly distribute load across multiple instances of a service?

A **load balancer** in front of the instances, using a strategy like round-robin,
least-connections, or weighted routing based on instance health/capacity.
Combine that with **health checks** so the balancer stops sending traffic to an
unhealthy instance, and **auto-scaling** rules that add/remove instances based on
CPU/queue-depth/request-rate metrics so the fleet size actually matches demand.

**[⬆ Back to Top](#table-of-contents)**

## 6. How do you handle failures between two microservices?

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

## 7. How do you secure microservice-to-microservice communication?

**TLS everywhere** (including internal traffic, not just the public edge) —
often via **mutual TLS (mTLS)** so both sides authenticate each other, commonly
enforced transparently by a service mesh rather than each service implementing it
itself. Combine with network-level isolation (private VNets/subnets, no direct
internet exposure for internal services) and short-lived, scoped service
credentials rather than long-lived shared secrets.

**[⬆ Back to Top](#table-of-contents)**

## 8. How do you debug a microservice in a containerized environment?

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

## 9. How would you refactor a monolith into microservices?

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

## 10. Design a real-time, multi-source analytics system

- **Ingestion:** an event-streaming platform (Kafka/Event Hubs) as the front
  door, absorbing bursts from multiple source systems without back-pressuring
  them.
- **Processing:** a stream-processing layer (Kafka Streams, Flink, or Azure
  Stream Analytics) to filter/aggregate/enrich events in near real time.
- **Storage:** a fast analytical store for the processed results (a time-series
  DB, or a columnar store) separate from the raw event log.
- **Serving:** a read-optimized API/dashboard layer querying the analytical
  store, decoupled from the ingestion/processing pipeline so a slow dashboard
  query never backs up ingestion.
- **Resilience:** replayability (Kafka retains the log) so a downstream
  processing bug can be fixed and the stream reprocessed, rather than data being
  lost forever.

**[⬆ Back to Top](#table-of-contents)**

## 11. Kafka producer/consumer basics

```csharp
// Producer
var config = new ProducerConfig { BootstrapServers = "localhost:9092" };
using var producer = new ProducerBuilder<Null, string>(config).Build();
await producer.ProduceAsync("my-topic", new Message<Null, string> { Value = "hello" });

// Consumer
var consumerConfig = new ConsumerConfig
{
    BootstrapServers = "localhost:9092",
    GroupId = "my-group",
    AutoOffsetReset = AutoOffsetReset.Earliest
};
using var consumer = new ConsumerBuilder<Ignore, string>(consumerConfig).Build();
consumer.Subscribe("my-topic");
while (true)
{
    var result = consumer.Consume();
    Console.WriteLine($"Received: {result.Message.Value}");
}
```

Key concepts to be ready to explain: **topics** are split into **partitions** for
parallelism; a **consumer group** lets multiple consumer instances share the work
of a topic (each partition goes to exactly one consumer within the group);
messages are retained for a configurable window regardless of whether they've
been consumed, which is what makes replay possible.

**[⬆ Back to Top](#table-of-contents)**

## 12. What is RabbitMQ used for?

A message broker implementing the AMQP protocol, typically used for
**task/work queues** and flexible routing (direct, topic, fanout exchanges)
between producers and consumers. Compared to Kafka: RabbitMQ is optimized for
traditional message-queuing patterns (a message is typically consumed once and
removed) at moderate throughput with rich routing logic, whereas Kafka is built
for very high-throughput, replayable event streams. Pick RabbitMQ for classic
task distribution/work queues; pick Kafka for event streaming and when multiple
independent consumers need to read the same stream.

**[⬆ Back to Top](#table-of-contents)**

## 13. How do you monitor application health and performance?

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
