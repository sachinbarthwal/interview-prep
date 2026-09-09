# Cloud & Azure

> Cloud questions are usually less about memorizing service names and more about
> "do you know which service to reach for, and why not the others" — that's the
> framing to answer with.

## Table of Contents

| No. | Question |
|-----|----------|
| 1 | [What Azure Storage types exist, and when do you use each?](#1-what-azure-storage-types-exist-and-when-do-you-use-each) |
| 2 | [What is Azure Cosmos DB, and when would you choose it?](#2-what-is-azure-cosmos-db-and-when-would-you-choose-it) |
| 3 | [What consistency levels does Azure offer?](#3-what-consistency-levels-does-azure-offer) |
| 4 | [What is Azure Key Vault, and how do you access secrets from it?](#4-what-is-azure-key-vault-and-how-do-you-access-secrets-from-it) |
| 5 | [Why use a Managed Identity instead of stored credentials?](#5-why-use-a-managed-identity-instead-of-stored-credentials) |
| 6 | [What is Azure Active Directory (AAD)?](#6-what-is-azure-active-directory-aad) |
| 7 | [Azure Service Bus vs Event Hubs](#7-azure-service-bus-vs-event-hubs) |
| 8 | [How does Azure Service Bus ensure message durability?](#8-how-does-azure-service-bus-ensure-message-durability) |
| 9 | [How do you onboard an API into Azure API Management (APIM)?](#9-how-do-you-onboard-an-api-into-azure-api-management-apim) |
| 10 | [How do you secure authentication between an HTTPS client and an HTTP-only backend?](#10-how-do-you-secure-authentication-between-an-https-client-and-an-http-only-backend) |
| 11 | [What are the key components of an Azure DevOps CI/CD pipeline?](#11-what-are-the-key-components-of-an-azure-devops-cicd-pipeline) |
| 12 | [What is Octopus Deploy?](#12-what-is-octopus-deploy) |
| 13 | [App Service vs Azure Functions — when do you choose each?](#13-app-service-vs-azure-functions--when-do-you-choose-each) |
| 14 | [What is Infrastructure as Code (IaC)?](#14-what-is-infrastructure-as-code-iac) |
| 15 | [How would you design a highly available, scalable Azure architecture?](#15-how-would-you-design-a-highly-available-scalable-azure-architecture) |
| 16 | [How do you use the Azure Storage SDK from a .NET app?](#16-how-do-you-use-the-azure-storage-sdk-from-a-net-app) |
| 17 | [Common enterprise use cases for Redis Cache](#17-common-enterprise-use-cases-for-redis-cache) |
| 18 | [Migrating from Service Fabric to Azure Container Apps](#18-migrating-from-service-fabric-to-azure-container-apps) |

## 1. What Azure Storage types exist, and when do you use each?

- **Blob Storage** — unstructured data (files, images, videos, backups); the
  default choice for "just store this file somewhere."
- **Table Storage** — a NoSQL key-value store for large volumes of structured,
  schema-less data with simple lookup patterns.
- **Queue Storage** — simple message queuing between application components (a
  lighter-weight alternative to Service Bus for basic scenarios).
- **File Storage** — fully managed file shares accessible via the standard SMB
  protocol, useful for lift-and-shift scenarios needing a shared network drive.

**[⬆ Back to Top](#table-of-contents)**

## 2. What is Azure Cosmos DB, and when would you choose it?

A globally distributed, multi-model NoSQL database (document, key-value, graph,
column-family APIs) with single-digit-millisecond latency guarantees and turnkey
global replication. Reach for it when you need very low, predictable latency at
global scale, elastic throughput scaling, and flexible schema — at a materially
higher cost than a relational database for equivalent workloads, so it's not the
default for everything.

**[⬆ Back to Top](#table-of-contents)**

## 3. What consistency levels does Azure offer?

From strongest (and slowest/most expensive) to weakest (fastest/cheapest):
**Strong** (always read the latest write), **Bounded Staleness** (reads lag
writes by a bounded time/version window), **Session** (a single client always sees
its own writes), **Consistent Prefix** (reads never see out-of-order writes, but
may be stale), **Eventual** (lowest latency, no ordering guarantee, will
eventually converge). Choosing one is a direct trade-off between correctness
guarantees and latency/throughput/cost.

**[⬆ Back to Top](#table-of-contents)**

## 4. What is Azure Key Vault, and how do you access secrets from it?

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

## 5. Why use a Managed Identity instead of stored credentials?

A Managed Identity gives an Azure resource (a Web App, a Function, a VM) an
identity in Azure AD that it can use to authenticate to other Azure services
(Key Vault, SQL, Storage) **without any credential ever being stored in code,
config, or a pipeline variable**. Azure rotates the underlying credential
automatically and it's scoped to that specific resource, which eliminates an
entire class of "leaked connection string" incidents.

**[⬆ Back to Top](#table-of-contents)**

## 6. What is Azure Active Directory (AAD)?

Microsoft's cloud-based identity and access management service — it authenticates
users and applications, issues tokens (OAuth2/OpenID Connect), and centrally
manages roles/permissions across Microsoft 365, Azure resources, and any
application registered against it (including custom line-of-business apps using
AAD as their identity provider for SSO).

**[⬆ Back to Top](#table-of-contents)**

## 7. Azure Service Bus vs Event Hubs

| | Service Bus | Event Hubs |
|---|---|---|
| Purpose | Enterprise messaging — queues and pub/sub topics | Big-data event/telemetry streaming |
| Throughput | Moderate | Very high (millions of events/sec) |
| Message retention | Typically short-term, consumed then removed | Can retain a stream for a configured window, replayable |
| Ordering | Can guarantee FIFO within a queue/session | Maintains order within a partition |
| Consumer model | Competing consumers (each message to one consumer) | Consumer groups (multiple independent readers over the same stream) |
| Typical use | Order processing, work queues, decoupling services | Telemetry ingestion, log/event streaming, IoT |

**[⬆ Back to Top](#table-of-contents)**

## 8. How does Azure Service Bus ensure message durability?

Messages are persisted to storage as soon as they're sent (not held only in
memory), so a broker failure doesn't lose them. Durability features include
message locking with a visibility timeout (a consumer must explicitly complete or
abandon a message, or it becomes available again), dead-lettering for messages
that repeatedly fail processing, and duplicate detection windows to guard against
redelivery causing double-processing.

**[⬆ Back to Top](#table-of-contents)**

## 9. How do you onboard an API into Azure API Management (APIM)?

Import the backend API (from an OpenAPI/Swagger definition, a WSDL, or manually),
which creates a managed **front door** in front of it. From there you configure
**policies** (rate limiting, IP filtering, request/response transformation,
caching), apply **products/subscriptions** to control who can call it and with
what key, and publish it through a **developer portal** for API consumers to
discover and self-service subscribe.

**[⬆ Back to Top](#table-of-contents)**

## 10. How do you secure authentication between an HTTPS client and an HTTP-only backend?

Ideally you don't leave a backend on plain HTTP at all — but where it's
unavoidable (an internal, network-isolated legacy service, for example), the
usual approach is to terminate TLS at a gateway/reverse proxy/App Service front
end that the public client talks to over HTTPS, then have that gateway talk to
the HTTP-only backend over a private, trusted network (a VNet or private
endpoint) that isn't internet-reachable — so the insecure hop never crosses an
untrusted network boundary.

**[⬆ Back to Top](#table-of-contents)**

## 11. What are the key components of an Azure DevOps CI/CD pipeline?

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

## 12. What is Octopus Deploy?

A dedicated release-management/deployment-automation tool that typically sits
*after* a CI system (Azure DevOps, TeamCity, Jenkins) — it takes the build
artifact and handles the deployment orchestration part: promoting a release
through environments, running deployment steps on target machines/services,
variable substitution per environment, and rollback. Teams often reach for it when
they want deployment logic decoupled from (and more powerful than) what their CI
tool's own release pipelines offer.

**[⬆ Back to Top](#table-of-contents)**

## 13. App Service vs Azure Functions — when do you choose each?

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

## 14. What is Infrastructure as Code (IaC)?

Defining and provisioning infrastructure (VMs, networks, databases, App Services)
through versioned, declarative configuration files — ARM templates, Bicep, or
Terraform — rather than clicking through a portal. Benefits: repeatable,
consistent environments (dev/staging/prod built from the same definition), full
change history in source control, and infrastructure changes go through the same
review/PR process as application code.

**[⬆ Back to Top](#table-of-contents)**

## 15. How would you design a highly available, scalable Azure architecture?

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

## 16. How do you use the Azure Storage SDK from a .NET app?

```csharp
var blobServiceClient = new BlobServiceClient(connectionString);
var containerClient = blobServiceClient.GetBlobContainerClient("uploads");

await containerClient.CreateIfNotExistsAsync();
var blobClient = containerClient.GetBlobClient("photo.jpg");
await blobClient.UploadAsync(fileStream, overwrite: true);
```

`BlobServiceClient` → `BlobContainerClient` → `BlobClient` is the standard
hierarchy for working with Blob Storage; equivalent client classes exist for
Table, Queue, and File Storage.

**[⬆ Back to Top](#table-of-contents)**

## 17. Common enterprise use cases for Redis Cache

Session storage for web farms (so any server instance can serve any user),
full-page or fragment caching to cut database load and latency, leaderboards and
real-time counters (via Redis's native sorted-set operations), distributed
locking for coordinating work across instances, rate limiting/throttling, and a
fast pub/sub layer for real-time notifications.

**[⬆ Back to Top](#table-of-contents)**

## 18. Migrating from Service Fabric to Azure Container Apps

Broadly: containerize each Service Fabric service (if not already containerized),
map Service Fabric's actor/reliable-services model onto Container Apps'
container + Dapr-based building blocks (Dapr provides comparable state
management, pub/sub, and service-invocation primitives), replace Service Fabric's
built-in cluster orchestration with Container Apps' KEDA-based scaling rules, and
migrate incrementally service-by-service behind a gateway rather than a single
big-bang cutover, so each migrated service can be validated independently before
the next one moves.

**[⬆ Back to Top](#table-of-contents)**
