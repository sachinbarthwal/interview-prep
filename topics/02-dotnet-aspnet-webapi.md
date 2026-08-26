# .NET Core, ASP.NET MVC & Web API

> This is the "can you actually build the thing" topic. Interviewers use it to check
> whether you understand the request pipeline well enough to debug it, not just wire
> up a `[HttpGet]` and call it done.

## Table of Contents

| No. | Question |
|-----|----------|
| 1 | [Walk through the ASP.NET MVC request life cycle](#1-walk-through-the-aspnet-mvc-request-life-cycle) |
| 2 | [What are filters in ASP.NET MVC, and what types exist?](#2-what-are-filters-in-aspnet-mvc-and-what-types-exist) |
| 3 | [Explain routing, including custom routes](#3-explain-routing-including-custom-routes) |
| 4 | [`ViewBag` vs `ViewData` vs `TempData`](#4-viewbag-vs-viewdata-vs-tempdata) |
| 5 | [3-tier vs n-tier architecture](#5-3-tier-vs-n-tier-architecture) |
| 6 | [What is middleware, and how do you write a custom one?](#6-what-is-middleware-and-how-do-you-write-a-custom-one) |
| 7 | [Middleware vs action filter — when do you use which?](#7-middleware-vs-action-filter--when-do-you-use-which) |
| 8 | [`AddSingleton` vs `AddScoped` vs `AddTransient`](#8-addsingleton-vs-addscoped-vs-addtransient) |
| 9 | [What is Dependency Injection, and how is it implemented in .NET Core?](#9-what-is-dependency-injection-and-how-is-it-implemented-in-net-core) |
| 10 | [Code review: Singleton depending on Scoped — what's wrong?](#10-code-review-singleton-depending-on-scoped--whats-wrong) |
| 11 | [What is a message handler / delegating handler in Web API?](#11-what-is-a-message-handler--delegating-handler-in-web-api) |
| 12 | [What is `HttpClientFactory`, and why use it?](#12-what-is-httpclientfactory-and-why-use-it) |
| 13 | [GET vs POST, PUT vs PATCH](#13-get-vs-post-put-vs-patch) |
| 14 | [What makes an HTTP method idempotent?](#14-what-makes-an-http-method-idempotent) |
| 15 | [What triggers a CORS preflight request?](#15-what-triggers-a-cors-preflight-request) |
| 16 | [How do you design a RESTful API?](#16-how-do-you-design-a-restful-api) |
| 17 | [Web Service vs Web API (SOAP vs REST)](#17-web-service-vs-web-api-soap-vs-rest) |
| 18 | [What is WCF, and what are its ABC components?](#18-what-is-wcf-and-what-are-its-abc-components) |
| 19 | [WCF vs Web API](#19-wcf-vs-web-api) |
| 20 | [How does token-based authentication work end to end?](#20-how-does-token-based-authentication-work-end-to-end) |
| 21 | [OAuth vs JWT](#21-oauth-vs-jwt) |
| 22 | [OAuth 1.0 vs OAuth 2.0](#22-oauth-10-vs-oauth-20) |
| 23 | [How do you implement OAuth2 in a .NET application?](#23-how-do-you-implement-oauth2-in-a-net-application) |
| 24 | [What is Single Sign-On (SSO) and Multi-Factor Authentication (MFA)?](#24-what-is-single-sign-on-sso-and-multi-factor-authentication-mfa) |
| 25 | [How would you design multi-tenancy into an application?](#25-how-would-you-design-multi-tenancy-into-an-application) |
| 26 | [What is an Anti-Forgery Token?](#26-what-is-an-anti-forgery-token) |
| 27 | [How does `[Authorize]` work, and how do you build custom authorization?](#27-how-does-authorize-work-and-how-do-you-build-custom-authorization) |
| 28 | [What is Model Binding, and what are Data Annotations?](#28-what-is-model-binding-and-what-are-data-annotations) |
| 29 | [How do you implement global exception handling in ASP.NET Core?](#29-how-do-you-implement-global-exception-handling-in-aspnet-core) |
| 30 | [How does routing resolve internally in ASP.NET Core?](#30-how-does-routing-resolve-internally-in-aspnet-core) |
| 31 | [How do you implement distributed caching in .NET Core?](#31-how-do-you-implement-distributed-caching-in-net-core) |
| 32 | [`Session.Abandon()` vs `Session.Clear()`](#32-sessionabandon-vs-sessionclear) |
| 33 | [Design a secure, scalable Web API — what do you actually check?](#33-design-a-secure-scalable-web-api--what-do-you-actually-check) |
| 34 | [Design a REST endpoint to create an account — controller/service/repository](#34-design-a-rest-endpoint-to-create-an-account--controllerservicerepository) |
| 35 | [What does `[FromBody]` do?](#35-what-does-frombody-do) |
| 36 | [What's new in .NET 6?](#36-whats-new-in-net-6) |
| 37 | [Benefits of `async`/`await` in C#](#37-benefits-of-asyncawait-in-c) |

## 1. Walk through the ASP.NET MVC request life cycle

A request comes in → the **routing engine** matches a URL pattern to a controller
and action → the **controller factory** instantiates the controller → **action
filters** run (`OnActionExecuting`) → the **action method** executes, returning an
`ActionResult` → **result filters** run → the **view engine** renders the view (if
it's a `ViewResult`) → the response is sent. Model binding happens just before the
action executes, populating action parameters from route data, query string, form
data, or the request body.

**[⬆ Back to Top](#table-of-contents)**

## 2. What are filters in ASP.NET MVC, and what types exist?

Filters let you inject cross-cutting logic around action execution without
polluting the action itself:

| Filter type | Runs | Typical use |
|---|---|---|
| Authorization filter | Before anything else | Auth/permission checks |
| Action filter | Before/after the action method | Logging, model validation, modifying arguments/results |
| Exception filter | When an unhandled exception propagates out | Centralized error handling |
| Result filter | Before/after the result executes | Modifying response headers, output caching |

They can be applied via attribute (`[Authorize]`, `[ValidateAntiForgeryToken]`), or
registered globally so every controller picks them up.

**[⬆ Back to Top](#table-of-contents)**

## 3. Explain routing, including custom routes

Routing maps an incoming URL to a controller/action. Convention-based routing is
registered centrally:

```csharp
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");
```

**Attribute routing** puts the pattern directly on the action, which is more
explicit and is the norm in Web API:

```csharp
[Route("api/orders/{id:int}")]
[HttpGet]
public IActionResult GetOrder(int id) { ... }
```

Custom routes let you version APIs (`api/v2/orders`), support SEO-friendly URLs, or
handle URL structures a plain convention can't express.

**[⬆ Back to Top](#table-of-contents)**

## 4. `ViewBag` vs `ViewData` vs `TempData`

| | Type | Lifetime | Notes |
|---|---|---|---|
| `ViewData` | `Dictionary<string, object>` | Current request only | Needs casting to read values |
| `ViewBag` | `dynamic` wrapper over `ViewData` | Current request only | Same store as `ViewData`, nicer syntax, no casting |
| `TempData` | `Dictionary<string, object>`, backed by session/cookie | Survives **one** redirect | Used to pass data across a `RedirectToAction` (e.g. a "saved successfully" message) |

**[⬆ Back to Top](#table-of-contents)**

## 5. 3-tier vs n-tier architecture

**3-tier** is the classic split: Presentation (UI) → Business Logic → Data Access,
each physically or logically separated so a change in one doesn't ripple through
the others. **N-tier** generalizes this to however many layers a system actually
needs — e.g. adding a separate API gateway tier, a caching tier, or splitting
business logic into multiple service tiers. The point of both is the same:
isolate concerns so each layer can change, scale, or be tested independently.

**[⬆ Back to Top](#table-of-contents)**

## 6. What is middleware, and how do you write a custom one?

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

## 7. Middleware vs action filter — when do you use which?

**Middleware** operates on the raw HTTP request/response and runs for *every*
request regardless of which controller/action (or even whether one exists) —
good for cross-cutting infrastructure concerns like authentication, logging,
CORS, exception handling, response compression. **Action filters** run inside
the MVC pipeline, after routing has already resolved a controller/action, and have
access to MVC-specific context (model state, action arguments, the
`ActionDescriptor`) — good for concerns tied to *that specific action*, like
model validation or auditing a particular endpoint.

**[⬆ Back to Top](#table-of-contents)**

## 8. `AddSingleton` vs `AddScoped` vs `AddTransient`

| Lifetime | Instance created | Typical use |
|---|---|---|
| `AddTransient` | A new instance every time it's requested | Lightweight, stateless services |
| `AddScoped` | One instance per HTTP request (or per scope) | `DbContext`, per-request unit-of-work services |
| `AddSingleton` | One instance for the lifetime of the app | Stateless services, in-memory caches, configuration objects |

**[⬆ Back to Top](#table-of-contents)**

## 9. What is Dependency Injection, and how is it implemented in .NET Core?

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

## 10. Code review: Singleton depending on Scoped — what's wrong?

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

## 11. What is a message handler / delegating handler in Web API?

A `DelegatingHandler` sits in the Web API pipeline *before* routing/controllers,
intercepting every outgoing/incoming HTTP message — useful for cross-cutting
concerns like adding auth headers, logging every request/response, or short-
circuiting on a failed check, similar in spirit to ASP.NET Core middleware but
scoped specifically to `HttpClient`/Web API's message pipeline.

**[⬆ Back to Top](#table-of-contents)**

## 12. What is `HttpClientFactory`, and why use it?

Creating a new `HttpClient` per request and disposing it looks correct but leaks
sockets under load (`HttpClient` doesn't release the underlying TCP connection
immediately on `Dispose()`, so heavy churn can exhaust available sockets — the
well-known "socket exhaustion" problem). Reusing a single static `HttpClient`
avoids that, but then DNS changes never get picked up. `IHttpClientFactory` solves
both: it pools and reuses underlying handlers while still letting you get a fresh
logical `HttpClient` per use, and it integrates with DI, named/typed clients, and
Polly-based retry policies.

**[⬆ Back to Top](#table-of-contents)**

## 13. GET vs POST, PUT vs PATCH

- **GET** retrieves a resource; no body, safe (no side effects), cacheable.
- **POST** creates a resource or triggers a non-idempotent action; has a body, not
  safe, not idempotent (posting twice usually creates two things).
- **PUT** replaces a resource entirely at a known URI; idempotent — sending the
  same PUT twice leaves the resource in the same state.
- **PATCH** applies a partial update to a resource; not guaranteed idempotent in
  general, though many implementations make it so.

**[⬆ Back to Top](#table-of-contents)**

## 14. What makes an HTTP method idempotent?

An idempotent method produces the same result on the server no matter how many
times you repeat the identical request. `GET`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`
are idempotent by spec; `POST` and (typically) `PATCH` are not. This matters
practically for retry logic — it's safe to blindly retry an idempotent request
after a timeout, but retrying a `POST` risks double-creating a resource unless
you've added your own idempotency key.

**[⬆ Back to Top](#table-of-contents)**

## 15. What triggers a CORS preflight request?

The browser sends an automatic `OPTIONS` preflight request before the "real" one
whenever a cross-origin request isn't a "simple request" — e.g. it uses a method
other than GET/HEAD/POST, sets custom headers (like `Authorization`), or sets a
`Content-Type` other than form-encoded/plain-text. The server must respond to the
`OPTIONS` request with the right `Access-Control-Allow-*` headers, or the browser
blocks the actual request before it's ever sent.

**[⬆ Back to Top](#table-of-contents)**

## 16. How do you design a RESTful API?

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

## 17. Web Service vs Web API (SOAP vs REST)

A classic "Web Service" usually means **SOAP** — a strict, XML-based protocol with
a formal contract (WSDL), built-in standards for security/transactions (WS-*), and
support for transports beyond HTTP. **Web API** here means a **REST**-style HTTP
API — lightweight, typically JSON, no formal contract required, and it only uses
HTTP as the transport (which is also its main limitation vs. SOAP). REST won out
for most modern APIs because it's simpler, more cacheable, and easier to consume
from anything that speaks HTTP.

**[⬆ Back to Top](#table-of-contents)**

## 18. What is WCF, and what are its ABC components?

WCF (Windows Communication Foundation) is Microsoft's older unified framework for
building service-oriented applications that can talk over many protocols (HTTP,
TCP, MSMQ, named pipes). Every WCF service is defined by three things — the
**ABC**:
- **A**ddress — where the service lives (a URI).
- **B**inding — how to talk to it (protocol, encoding, security — e.g.
  `basicHttpBinding`, `netTcpBinding`).
- **C**ontract — what it does (the `[ServiceContract]`/`[OperationContract]`
  interface).

**[⬆ Back to Top](#table-of-contents)**

## 19. WCF vs Web API

WCF is heavier, XML/config-driven, and supports multiple protocols and bindings
out of the box (including strict SOAP contracts) — a good fit when you need
transactions, reliable messaging, or non-HTTP transports. Web API is lighter,
REST/HTTP-only, JSON-first, and much simpler to stand up and consume — the default
choice for anything public-facing or consumed by web/mobile clients today. Most
new development uses Web API (or gRPC for internal service-to-service calls)
rather than WCF.

**[⬆ Back to Top](#table-of-contents)**

## 20. How does token-based authentication work end to end?

1. Client sends credentials to a login endpoint.
2. Server validates them and issues a signed token (typically a JWT) containing
   claims (user id, roles, expiry).
3. Client stores the token and sends it on every subsequent request, usually as
   `Authorization: Bearer <token>`.
4. Server validates the token's signature and expiry on each request — no session
   state needs to be kept server-side, which is what makes this approach scale
   horizontally so well.

**[⬆ Back to Top](#table-of-contents)**

## 21. OAuth vs JWT

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

## 22. OAuth 1.0 vs OAuth 2.0

OAuth 1.0 required cryptographically signing every request (HMAC-based request
signing) and had no separation between short-lived access tokens and long-lived
refresh tokens. OAuth 2.0 dropped mandatory request signing in favor of relying on
TLS, introduced distinct **grant types** for different client scenarios
(authorization code, client credentials, etc.), and separated access tokens from
refresh tokens — simpler to implement, but it depends entirely on HTTPS for
transport security since requests are no longer signed themselves. The two are not
backward compatible.

**[⬆ Back to Top](#table-of-contents)**

## 23. How do you implement OAuth2 in a .NET application?

Register the authentication scheme in `Program.cs`/`Startup.cs`, pointing at the
provider's endpoints:

```csharp
builder.Services.AddAuthentication(options =>
{
    options.DefaultAuthenticateScheme = "OAuth";
    options.DefaultChallengeScheme = "OAuth";
})
.AddOAuth("OAuth", options =>
{
    options.ClientId = "<clientId>";
    options.ClientSecret = "<clientSecret>";
    options.CallbackPath = "/signin-oauth";
    options.AuthorizationEndpoint = "<authEndpoint>";
    options.TokenEndpoint = "<tokenEndpoint>";
});

app.UseAuthentication();
app.UseAuthorization();
```

Then protect endpoints with `[Authorize]`, or kick off the flow explicitly via
`Challenge(properties, "OAuth")`.

**[⬆ Back to Top](#table-of-contents)**

## 24. What is Single Sign-On (SSO) and Multi-Factor Authentication (MFA)?

**SSO** lets a user authenticate once with a central identity provider and gain
access to multiple independent applications without logging in again to each one
(typically via SAML or OpenID Connect). **MFA** requires a second factor beyond a
password — something you have (an OTP app, a hardware key) or something you are
(biometrics) — to significantly raise the bar against credential theft alone.

**[⬆ Back to Top](#table-of-contents)**

## 25. How would you design multi-tenancy into an application?

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

## 26. What is an Anti-Forgery Token?

A per-request, per-user token embedded in forms (`[ValidateAntiForgeryToken]` in
MVC, automatic in Razor Pages) to prevent **Cross-Site Request Forgery** — an
attacker's page can't forge a valid token for your session, so a malicious
auto-submitting form on another site can't perform actions as the logged-in user.

**[⬆ Back to Top](#table-of-contents)**

## 27. How does `[Authorize]` work, and how do you build custom authorization?

`[Authorize]` short-circuits the pipeline with a `401`/`403` unless the current
principal satisfies the requirement — by default just "is authenticated", but you
can narrow it with roles (`[Authorize(Roles = "Admin")]`) or named policies backed
by custom `IAuthorizationRequirement`/`AuthorizationHandler` implementations for
more complex rules (e.g. "user must own this resource"). A "public" endpoint is
simply one marked `[AllowAnonymous]`, which overrides a controller-level
`[Authorize]` for that specific action.

**[⬆ Back to Top](#table-of-contents)**

## 28. What is Model Binding, and what are Data Annotations?

**Model binding** is the framework automatically populating action-method
parameters (or a bound model object) from route values, query string, form data,
or a JSON request body — so you write `public IActionResult Create(OrderDto dto)`
instead of manually reading `Request.Form["..."]`. **Data Annotations** are
attributes on model properties (`[Required]`, `[StringLength(100)]`, `[Range]`,
`[EmailAddress]`) that drive automatic validation during model binding — a failed
validation populates `ModelState`, which you check with `ModelState.IsValid`.

**[⬆ Back to Top](#table-of-contents)**

## 29. How do you implement global exception handling in ASP.NET Core?

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

## 30. How does routing resolve internally in ASP.NET Core?

Endpoint routing builds a route table from all registered endpoints (attribute
routes, conventional routes, Razor Pages, minimal APIs) during startup. On each
request, `UseRouting()` matches the incoming path against that table (most
specific match wins) and selects an endpoint, storing it on `HttpContext`;
`UseEndpoints()` (or the equivalent minimal-API registration) later actually
executes that selected endpoint. Splitting matching from execution is what lets
middleware between the two (like authorization) make decisions based on which
endpoint was matched, before it actually runs.

**[⬆ Back to Top](#table-of-contents)**

## 31. How do you implement distributed caching in .NET Core?

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

## 32. `Session.Abandon()` vs `Session.Clear()`

`Session.Clear()` removes all items from the current session but keeps the same
session ID and cookie alive. `Session.Abandon()` destroys the session entirely —
the next request gets an entirely new session ID. Use `Abandon()` for something
like logout, where you want a genuinely fresh session, not just an empty one.

**[⬆ Back to Top](#table-of-contents)**

## 33. Design a secure, scalable Web API — what do you actually check?

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

## 34. Design a REST endpoint to create an account — controller/service/repository

```csharp
public record CreateAccountRequest(string Name, string EmailId, List<string> PhoneNumbers);

[ApiController]
[Route("api/[controller]")]
public class AccountController : ControllerBase
{
    private readonly IAccountService _accountService;
    public AccountController(IAccountService accountService) => _accountService = accountService;

    [HttpPost]
    public async Task<ActionResult<Account>> Create([FromBody] CreateAccountRequest request)
    {
        var account = await _accountService.CreateAsync(request);
        return CreatedAtAction(nameof(GetById), new { accountNumber = account.AccountNumber }, account);
    }

    [HttpGet("{accountNumber}")]
    public async Task<ActionResult<Account>> GetById(string accountNumber)
    {
        var account = await _accountService.GetAsync(accountNumber);
        return account is null ? NotFound() : Ok(account);
    }
}
```

**Layering:** the **controller** only handles HTTP concerns (binding, status
codes) and delegates to a **service** that owns business rules/validation; the
service calls a **repository** that owns data access, so the persistence
technology (EF Core, Dapper, a different database entirely) can change without
touching the controller or business logic.

**[⬆ Back to Top](#table-of-contents)**

## 35. What does `[FromBody]` do?

It tells model binding to deserialize the action parameter from the **request
body** (typically JSON) rather than from route values or the query string. Only
one parameter per action can use `[FromBody]`, since the body can only be read
once.

**[⬆ Back to Top](#table-of-contents)**

## 36. What's new in .NET 6?

A unified platform for desktop/mobile/web on one BCL, Hot Reload for C#/XAML,
minimal APIs for lightweight endpoints without full MVC ceremony, `DateOnly`/
`TimeOnly` types, file-scoped namespaces, global `using` directives, and
performance improvements in the JIT.

**[⬆ Back to Top](#table-of-contents)**

## 37. Benefits of `async`/`await` in C#

Frees up threads during I/O-bound waits (DB calls, HTTP calls, file I/O) instead
of blocking them, which is what lets a web server handle far more concurrent
requests with the same thread pool. It also keeps asynchronous code readable —
sequential-looking code instead of nested callbacks — while still giving you
structured exception handling (a regular `try/catch` around an `await`) and easy
composition of multiple async operations (`Task.WhenAll`, `Task.WhenAny`).

**[⬆ Back to Top](#table-of-contents)**
