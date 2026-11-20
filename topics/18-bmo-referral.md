# BMO Referral: Deloitte full-stack lead (React, Lambda, ETF tools, OpenSpec)

> Temporary prep for the Friday interview. Team builds portfolio-management tools for BMO analysts who design and rebalance ETFs. Stack: React + AWS Lambda/ECS, TypeScript, Python, Node; bonus: OpenSpec. Role: hands-on lead who guides juniors. Say each answer out loud before revealing it.

## 1. Tell me about yourself (final version).

*Top answers*

> "I'm a full-stack developer with 10 years' experience: .NET, SQL and Azure, plus React, TypeScript, Node and Python. At Staples I'm on the **integration team**. Every system-to-system connection goes through us, and we build **event-driven microservices** that don't lose data. Before that, 3 years on a **financial reporting product** where every number had to be traceable. I use **AI coding agents** every day, and I enjoy helping teams use them well."

**[⬆ Back to Top](#table-of-contents)**

## 2. How would you help the juniors and support Mayukh?

*Top answers*

> "With AI, juniors write code fast, but not always right. I'd make sure it's the **right** code:
> - **spec first** with OpenSpec,
> - a **rules file** so the AI follows our patterns,
> - **small PRs with reviews**,
> - **tests in CI**,
> - and pairing, so they can explain what they wrote.
>
> Mayukh sets the direction; I make sure the team delivers it, and I bring him only the big decisions, **with options and a recommendation**."

**[⬆ Back to Top](#table-of-contents)**

## 3. Design it in one line (5 boxes).

*Top answers*

**React → API Gateway + Lambda → Step Functions → Database → Events out**

Steps: **validate → calculate weights → check rules → human approves → publish**

For a bank: **security, audit, no duplicates or lost messages.** Heavy jobs: **ECS**. Say **"the trade-off is…"**.

**[⬆ Back to Top](#table-of-contents)**

## 4. If you blank on a React/Node/Python detail.

*Top answers*

Say **"it's like X in .NET"**, then explain the idea. Examples:
- Node async/await = C# async/await; Promise.all = Task.WhenAll.
- Express middleware = ASP.NET Core middleware.
- npm + package.json = NuGet + csproj.
- TypeScript generics = C# generics; interfaces = C# interfaces/DTOs.
- pandas = LINQ / SQL GROUP BY over a table in memory.
- Lambda = Azure Functions; Step Functions = Durable Functions; SQS = Service Bus queue.

**[⬆ Back to Top](#table-of-contents)**

## 5. React in 60 seconds.

*5-min refresher*

- **Components** are functions that return UI (JSX).
- **Props** = inputs from the parent; **state** = the component's own data, and changing it redraws.
- **useState** holds data; **useEffect** runs after render (fetch, timers) with a dependency array and cleanup.
- **useMemo / useCallback** avoid redoing work; **useRef** keeps a value without redrawing.
- **Context** shares data without prop drilling; **React Query** for API data with caching.
- **Virtual DOM:** React diffs old vs new and updates only what changed.
- Lists need a unique **key** (not the index).

**[⬆ Back to Top](#table-of-contents)**

## 6. TypeScript in 60 seconds.

*5-min refresher*

- JavaScript **with types**: mistakes caught before the code runs.
- **interface / type** describe object shapes; **union** 'BUY' | 'SELL'.
- **Generics** like C#: Array<T>, Promise<T>.
- **any** turns checking off; **unknown** is the safe version.
- Utility types: Partial, Pick, Omit, Record.

**[⬆ Back to Top](#table-of-contents)**

## 7. Node in 60 seconds.

*5-min refresher*

- JavaScript on the **server**, single thread, **non-blocking I/O**.
- **Event loop:** finished async work is queued and run next; CPU-heavy work blocks it, so use worker threads.
- **async/await + Promises** like C#; **Promise.all** runs calls in parallel.
- **Express:** app.get('/funds', handler) plus **middleware** (auth, logging, errors).
- **npm + package.json** = NuGet + csproj; config via process.env.

**[⬆ Back to Top](#table-of-contents)**

## 8. Python in 60 seconds.

*5-min refresher*

- Simple syntax, **indentation** instead of braces.
- **list** [ ], **dict** { } (key → value), **tuple** ( ), **set**.
- **Comprehension:** [x * 2 for x in nums].
- try / except for errors; type hints def f(x: int) -> str.
- **pandas:** tables in code; merge, groupby, sum, like SQL.
- Lambda: def handler(event, context): with **boto3** as the AWS SDK.

**[⬆ Back to Top](#table-of-contents)**

## 9. Lambda in 60 seconds.

*5-min refresher*

- A function that runs **when an event happens**: HTTP (API Gateway), queue message (SQS), file upload (S3), schedule (EventBridge).
- Max **15 min**: **Step Functions** for multi-step flows, **ECS/Fargate** for long jobs.
- **Cold start:** first call is slow; create clients outside the handler, keep the package small, provisioned concurrency.
- **Idempotent** handlers + a **dead-letter queue** for failures; least-privilege **IAM role**; logs in **CloudWatch**.

**[⬆ Back to Top](#table-of-contents)**

## 10. What does this role really need? (inside info)

*Deloitte & interviewer*

**They need an experienced, hands-on lead**, not just another developer:
- **Guide juniors architecturally.** The juniors are "vibe coders" who lean on AI.
- Be technically capable across the stack (React, Lambda/ECS, TS, Python, Node).
- **Take responsibility off Mayukh** so he can focus on architecture and the client.

**Agenda:** intros → experience and skills → project overview and role → Q&A. A conversation, maybe a design question.

**Your positioning line:**
> "With AI, juniors can produce a lot of code quickly. My job is making sure it's the **right** code: spec first, clear patterns, code reviews, and tests in CI. That way you set the direction, and I make sure the team delivers it well."

**[⬆ Back to Top](#table-of-contents)**

## 11. How would you guide junior developers who rely heavily on AI?

*Leading the team*

> "AI makes juniors fast, but not always right. I'd put a few guardrails in place:
> 1. **Spec first:** with OpenSpec, they write the proposal and WHEN/THEN scenarios before the AI writes code, and I review the intent, which takes 10 minutes instead of reviewing 500 lines later.
> 2. **A rules file** (AGENTS.md / CLAUDE.md) in the repo with our patterns, so the AI follows the team's conventions, not random ones.
> 3. **Small PRs** with a review checklist: tests, error handling, security, idempotency, logging.
> 4. **CI gates:** type checks, lint, unit tests, so obvious mistakes never reach review.
> 5. **Pairing and "explain your code":** if they can't explain what the AI wrote, it doesn't merge. That's how they actually learn."

**[⬆ Back to Top](#table-of-contents)**

## 12. How would you take load off the architect?

*Leading the team*

> "I'd be the bridge between the architecture and the code. You set the direction and the big decisions; I turn that into **patterns, templates and stories** the team can build, **review the designs and PRs**, unblock people day to day, and only bring you the decisions that really need you, **with options and a recommendation** already worked out. Over time you spend less time in the weeds and more with the client."

**[⬆ Back to Top](#table-of-contents)**

## 13. Tell me about a time you mentored someone.

*Leading the team*

**STAR, use a real person (no names):**
- **Situation:** a newer developer joined the integration team / struggled with a pattern (e.g. outbox, async handling, a stored procedure chain).
- **Task:** get them productive without doing it for them.
- **Action:** walked them through one integration end to end, paired on the first one, gave them the next one to lead with me reviewing, explained the *why* (why idempotency, why the outbox).
- **Result:** they shipped the next integration mostly on their own and started reviewing others.

**Fill in the real details before Friday.**

**[⬆ Back to Top](#table-of-contents)**

## 14. Tell me about a time you pushed back on a design or decision.

*Leading the team*

**Shape (use a real example):**
> "There was a proposal to ___ (e.g. load a partial file / call a downstream system directly without a queue). I was concerned about ___ (lost data, partial financial data, coupling). I didn't just say no: I showed the risk with a concrete scenario and proposed ___ (all-or-nothing load / queue + outbox). We agreed on ___ and it ___."

**Key message:** disagree with **data and options**, then **commit** to the team's decision.

**[⬆ Back to Top](#table-of-contents)**

## 15. How do you run code reviews? What do you look for?

*Leading the team*

- **Does it do what the spec says?** (the scenarios)
- **Correctness and edge cases:** nulls, empty lists, duplicates, time zones and date ranges.
- **Failure handling:** retries, idempotency, timeouts, clear errors.
- **Security:** no secrets, input validation, least privilege.
- **Readability:** names, small functions, no dead code.
- **Tests** for the important paths.

> "I keep reviews kind and specific: suggest, explain why, and approve small PRs fast so the team isn't blocked."

**[⬆ Back to Top](#table-of-contents)**

## 16. How do you keep quality high when the team ships fast with AI?

*Leading the team*

> "Make the right way the easy way: **spec first**, a **repo rules file** for the AI, **templates** for common things (a Lambda handler, an API endpoint, a React data screen), **CI gates** (types, lint, tests), **small PRs**, and **monitoring** so we see problems in production quickly. Speed is fine as long as the guardrails are automatic."

**[⬆ Back to Top](#table-of-contents)**

## 17. The client changes requirements mid-sprint. What do you do?

*Leading the team*

> "First understand **why**: what changed for the business. Then show the **impact**: what moves, what's at risk, what it costs in time. Offer **options**: swap something out, split the work, or move it to next sprint. Let the product owner decide the trade-off, and **write it down** (in OpenSpec it's a new proposal), so everyone sees what changed and why."

**[⬆ Back to Top](#table-of-contents)**

## 18. How would you handle a junior whose AI-generated PR is wrong or messy?

*Leading the team*

> "I wouldn't just reject it. I'd sit with them for 15 minutes: ask them to walk me through it, find the issue together, and point to the pattern or spec they should follow. Then I'd add that lesson to the rules file or checklist, so the AI and the whole team avoid it next time. Fix the system, not just the PR."

**[⬆ Back to Top](#table-of-contents)**

## 19. What would you do in your first 30–60–90 days?

*Leading the team*

- **30 days:** learn the domain (how analysts rebalance today), the architecture and the codebase; ship a small change; meet the team and BMO stakeholders.
- **60 days:** own a feature end to end; set up or tighten review checklists, templates and CI gates; start pairing with juniors.
- **90 days:** be the go-to person for day-to-day technical decisions, so Mayukh only handles the big ones; propose 1–2 improvements (reliability, cost, dev speed).

**[⬆ Back to Top](#table-of-contents)**

## 20. How do you think about cost on AWS?

*Leading the team*

- **Lambda** is cheap for spiky, low-volume work; at steady high volume **containers** (ECS/Fargate) can be cheaper.
- Right-size Lambda memory (CPU scales with it); avoid chatty calls; use **S3 lifecycle** rules for old files.
- Tag resources per environment and team; set **budgets and alerts**.
> "**The trade-off** is usually cost vs ops effort: serverless costs more per unit at scale but saves a lot of team time."

**[⬆ Back to Top](#table-of-contents)**

## 21. Who is interviewing me and what do they care about?

*Deloitte & interviewer*

**Mayukh Mukherjee:** senior solution architect at Deloitte with 19 years in banking (Manulife, TD, IBM). MuleSoft certified (**integration**), AWS AI Practitioner (**agentic AI**). Role: **Full Stack Developer for a BMO client**: React, AWS Lambda & ECS, Python, TypeScript, Node; system design + DevOps a bonus.

**Expect big-picture questions:** design, trade-offs, integration, security, AI. Keep saying **"the trade-off is…"**.

**[⬆ Back to Top](#table-of-contents)**

## 22. Quick intro for the architect (30 sec).

*Deloitte & interviewer*

> "I'm a full-stack developer with 10 years' experience: .NET, SQL, Azure, plus React, TypeScript, Node and Python. At Staples I'm on the **integration team**. Every system-to-system connection goes through us, and we build **event-driven microservices**. Before that, 3 years on a **financial reporting product** where every number had to be traceable. And I use **AI coding agents** every day."

**[⬆ Back to Top](#table-of-contents)**

## 23. Design it: the 5 boxes and 3 bank must-haves.

*Deloitte & interviewer*

**React UI → API Gateway + Lambda → Step Functions → Database → Events out (EventBridge/SQS)**

Workflow: **validate → calculate weights → check rules → human approves → publish.** Long or heavy runs → **ECS Fargate**.

**Bank must-haves:**
- **Security:** least-privilege IAM, encryption (KMS), Secrets Manager, private VPC, data in Canada.
- **Audit:** every rebalance versioned, who approved, CloudTrail.
- **Reliability:** retries, idempotency, dead-letter queue, multi-AZ.

**MuleSoft-style layers he will like:** system APIs (holdings, prices) → process APIs (rebalance logic) → experience APIs (what React needs).

**[⬆ Back to Top](#table-of-contents)**

## 24. Tell me about your integration work (Staples).

*Stories (stack-neutral)*

> "I'm on the integration team. We build **event-driven microservices**: receive an event, transform it, dispatch it, each step as a **small stateless service** that scales on its own, with queues between the steps, **idempotent** handling, an **outbox pattern** and **dead-letter handling**. That's exactly the shape of a **Lambda + SQS** design; on AWS each step would be a Lambda. Our services are in .NET, but the design doesn't depend on the language. I could build the same thing in **Node or Python**."

**Say "on AWS this would be…", not "we used Lambda".**

**[⬆ Back to Top](#table-of-contents)**

## 25. Tell me about a hard problem you solved (Single Pool Inventory).

*Stories (stack-neutral)*

> "Different systems disagreed on stock: transport had 7, the warehouse had 6. We built **one central inventory service** that publishes changes as **events**, so every system reads the same number. For an ETF tool it's the same problem: **holdings and prices need one source of truth**, or the rebalance is wrong."

**[⬆ Back to Top](#table-of-contents)**

## 26. Tell me about your finance and front-end experience (Certent).

*Stories (stack-neutral)*

> "Three years on a **financial reporting product**: full stack, with a **TypeScript front end** talking to APIs over SQL. I worked on reports, calculations, and **tracing every number back to its source**. Moving to **React** is the same component and TypeScript thinking. And the finance lesson carries straight over: **accuracy and audit trails come first**."

**[⬆ Back to Top](#table-of-contents)**

## 27. Show me your Node and AI experience.

*Stories (stack-neutral)*

> "In my own time I built a **Node/Electron desktop app** that captures audio, transcribes it and calls **AI APIs** to answer in real time. I work **spec-first with AI coding agents** on it, keeping rules and plans in the repo, which is the OpenSpec idea."

**React / Python:** "I've built React front ends with hooks and TypeScript for ___, and used Python for ___." (fill from your real projects)

**[⬆ Back to Top](#table-of-contents)**

## 28. You are mostly .NET. Why should we hire you for React + Lambda?

*Stories (stack-neutral)*

> "My production back end has been mostly .NET, yes. But what I bring is **how to design distributed, event-driven systems that don't lose data**, and that's the same on Lambda with Node or Python. I've worked across TypeScript, Node, React and Python, and I'm productive in them quickly."

**[⬆ Back to Top](#table-of-contents)**

## 29. How do you prove Lambda depth?

*Stories (stack-neutral)*

> "What matters in production is: **idempotent** handlers because SQS can deliver twice; a **dead-letter queue** for failures; clients created **outside the handler** to cut cold starts; **Step Functions** for multi-step flows; **ECS** when a job runs over 15 minutes."

**If asked "production Lambda?":** "Most of my serverless and event-driven production work is on Azure with the same patterns: functions on events, queues, retries, DLQs. Moving to Lambda is changing service names, not learning a new way of thinking."

**[⬆ Back to Top](#table-of-contents)**

## 30. Three quick architect answers.

*Stories (stack-neutral)*

- **Lambda or ECS?** Lambda for short, event-driven work; ECS for long-running or heavy work.
- **AI for analysts?** AI suggests, the human approves, everything is logged (Bedrock + guardrails).
- **OpenSpec?** The team agrees the spec first, then the AI codes it. Every change is traceable, which is perfect for a bank.
- **Ask him:** "Is this a new build for BMO or a modernisation of an existing tool?"

**[⬆ Back to Top](#table-of-contents)**

## 31. Tell me about yourself.

*Intro & fit*

> "I'm a senior full-stack developer with about 10 years' experience. My core is **.NET, C#, SQL and Azure**, and on the front end and scripting side I've worked with **React, TypeScript, Node and Python**, at work and in my own projects.

> Right now at **Staples** I'm on the integration team building **event-driven microservices**: receive an event, transform it, dispatch it to the next system, each step its own small service with CI/CD and monitoring.

> Before that, ~3 years at **Accolite on insightsoftware's Certent product**: financial reporting and SEC disclosure, so I'm used to financial data where every number must be exact and traceable.

> I also use AI coding tools like Claude Code daily in my own projects. A portfolio tool built with React, serverless and spec-driven AI development is a really good fit for what I've done and where I want to go."

**[⬆ Back to Top](#table-of-contents)**

## 32. What is your experience with React, Node, Python and TypeScript?

*Intro & fit*

**Say it with confidence, short and concrete:**

> "**React and TypeScript:** I've built React front ends with function components and hooks, typed with TypeScript; I've also done a lot of Angular, so component design and typed front ends are second nature.

> **Node:** I've built Node projects and APIs; my current personal project is a Node/Electron desktop app that captures audio and calls AI APIs.

> **Python:** projects and scripting, including data handling and API calls.

> My deepest production experience is .NET and Azure, but the patterns are the same across all of them: APIs, async I/O, event-driven services, clean components. I pick up the specifics quickly."

**[⬆ Back to Top](#table-of-contents)**

## 33. Why do you want this role?

*Intro & fit*

> "Three reasons. **The domain:** analysts making portfolio decisions on financial data is close to my Certent work, where accuracy and audit trails were everything. **The architecture:** event-driven, small focused services is exactly what I build at Staples; Lambda is the AWS version of that. **The way of working:** spec-driven development with AI tools like OpenSpec is where engineering is heading, and I already work with AI assistants every day."

**[⬆ Back to Top](#table-of-contents)**

## 34. AWS vs Azure: map the services you know.

*Intro & fit*

| Azure (what you use) | AWS (what they use) |
|---|---|
| Azure Functions | **Lambda** |
| AKS | EKS / ECS / Fargate |
| Event Hub / Service Bus | **Kinesis / SQS / SNS / EventBridge** |
| Blob Storage | **S3** |
| Azure SQL | RDS / Aurora |
| Cosmos DB | **DynamoDB** |
| Logic Apps / Durable Functions | **Step Functions** |
| API Management | **API Gateway** |
| Key Vault | Secrets Manager / Parameter Store |
| App Insights / Monitor | **CloudWatch / X-Ray** |
| Entra ID / Managed Identity | **IAM roles** |
| ARM / Bicep | CloudFormation / CDK / SAM |

> "The concepts transfer one to one; it's mostly names."

**[⬆ Back to Top](#table-of-contents)**

## 35. What do you think our team builds day to day?

*What the team does*

**My best guess from what I heard about the team (say it as an understanding you want to confirm):**

> "From what I understand, BMO's ETF analysts design funds and rebalance them based on stock evaluations, and your team builds the tools they use for that. So probably:
> - a **React web app** where analysts see funds, holdings, scores and proposed changes;
> - **Lambda-based APIs and jobs** that pull data (prices, holdings, analyst scores), calculate target weights, check rules, and produce a proposed trade list;
> - **Python** for the number-crunching (pandas is great for portfolio math) and **Node/TypeScript** for APIs and the front end;
> - an **approval and audit trail**, because every change to a fund has to be explainable;
> - and you use **OpenSpec** so changes are specified and reviewed before AI tools write the code.
> Is that close?"

**Ending with "is that close?" turns it into a conversation, which is exactly what a 30-minute referral meeting should be.**

**[⬆ Back to Top](#table-of-contents)**

## 36. What is React and how does rendering work?

*React*

- A JavaScript **library for building UIs from components**: each component is a function that returns JSX.
- **One-way data flow:** data goes down as **props**, events come up via callbacks.
- When **state or props change**, React re-runs the component, builds a new **virtual DOM**, compares it with the previous one (**reconciliation / diffing**) and updates only what changed in the real DOM.
- **React 18+:** automatic batching of state updates, concurrent rendering (`useTransition` for non-urgent updates), `Suspense` for loading states. **React 19:** Actions, `use()`, Server Components, and the React Compiler (auto-memoisation).

**[⬆ Back to Top](#table-of-contents)**

## 37. Props vs state?

*React*

- **Props:** inputs passed from the parent; **read-only** inside the child.
- **State:** data the component owns and can change with `useState`; changing it re-renders.
- **Lifting state up:** if two siblings need the same data, move the state to their common parent and pass it down.
- Rule of thumb: keep state **as low as possible** and **derive** what you can instead of storing it twice.

```tsx
function FundRow({ fund, onSelect }: { fund: Fund; onSelect: (id: string) => void }) {
  return <tr onClick={() => onSelect(fund.id)}><td>{fund.name}</td></tr>;
}
```

**[⬆ Back to Top](#table-of-contents)**

## 38. Explain React hooks: useState, useEffect, useMemo, useCallback, useRef.

*React*

- **useState:** data that changes what's on screen; the setter triggers a re-render. Use the function form when the new value depends on the old: `setCount(c => c + 1)`.
- **useEffect:** side effects after render (fetching, subscriptions, timers). The **dependency array** controls when it re-runs; `[]` = once on mount; return a **cleanup** function.
- **useMemo:** cache an expensive calculation until inputs change.
- **useCallback:** cache a function so memoised children don't re-render.
- **useRef:** a mutable value that survives renders **without** re-rendering; also used to reach a DOM element.
- Others: **useContext** (read context), **useReducer** (complex state transitions).
- **Rules of hooks:** only call at the top level of a component or custom hook, never in loops or conditions.

**[⬆ Back to Top](#table-of-contents)**

## 39. How do you fetch data in React? Show loading and error handling.

*React*

```tsx
function Holdings({ fundId }: { fundId: string }) {
  const [rows, setRows] = useState<Holding[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const controller = new AbortController();
    setLoading(true);
    fetch(`/api/funds/${fundId}/holdings`, { signal: controller.signal })
      .then(r => { if (!r.ok) throw new Error(r.statusText); return r.json(); })
      .then(setRows)
      .catch(e => { if (e.name !== 'AbortError') setError(e.message); })
      .finally(() => setLoading(false));
    return () => controller.abort(); // cleanup if fundId changes or unmount
  }, [fundId]);

  if (loading) return <p>Loading…</p>;
  if (error) return <p>Error: {error}</p>;
  return <table>{rows.map(h => <tr key={h.ticker}><td>{h.ticker}</td><td>{h.weight}</td></tr>)}</table>;
}
```

> "In a real app I'd use **React Query (TanStack Query)**: caching, retries, refetching and loading states for free."

**[⬆ Back to Top](#table-of-contents)**

## 40. useEffect: common mistakes?

*React*

- **Missing dependencies** → stale values (stale closure). Include everything you read inside.
- **Setting state that's also a dependency** → infinite loop.
- **No cleanup** → memory leaks or setting state after unmount (timers, subscriptions, in-flight fetch → use AbortController).
- **Using an effect for derived data**: if you can calculate it during render, don't put it in state + effect.
- In **StrictMode (dev)** effects run twice on mount to surface missing cleanups; that's expected.

**[⬆ Back to Top](#table-of-contents)**

## 41. Why do lists need keys?

*React*

- Keys let React match items between renders, so it updates/moves the right element instead of re-creating everything.
- Use a **stable unique id** (e.g. ticker, fund id). **Avoid array index** when items can be reordered, inserted or deleted, since it causes wrong rows to keep the wrong state.

**[⬆ Back to Top](#table-of-contents)**

## 42. Controlled vs uncontrolled components (forms)?

*React*

- **Controlled:** the input's value lives in React state; `value` + `onChange`. Easy validation and formatting (e.g. weight must be 0–100).
- **Uncontrolled:** the DOM holds the value; read it with a ref when needed. Less code, fewer re-renders.
- Big forms: **React Hook Form** (+ **Zod** for schema validation).

```tsx
const [weight, setWeight] = useState('');
<input value={weight} onChange={e => setWeight(e.target.value)} />
```

**[⬆ Back to Top](#table-of-contents)**

## 43. How do you share state across components? Context vs Redux vs React Query.

*React*

- **Props / lifting state:** first choice for nearby components.
- **Context:** avoids **prop drilling** for app-wide things (current user, theme, selected fund). Every consumer re-renders when the value changes, so don't put fast-changing data in it.
- **Redux Toolkit / Zustand:** larger client-side state with many updates.
- **React Query:** **server state** (data from APIs) with caching and refetching. Most "global state" is actually server state.

> "For an analyst tool I'd keep fund and holdings data in React Query, the selected fund in the URL or context, and form state local."

**[⬆ Back to Top](#table-of-contents)**

## 44. How do you make a React app fast? (e.g. a big holdings table)

*React*

- **Measure first** with React DevTools Profiler.
- **React.memo** for components that get the same props; **useMemo / useCallback** to keep props stable.
- **Virtualise long lists/tables** (TanStack Virtual, react-window): render only visible rows; essential for 1000s of holdings.
- **Code splitting:** `React.lazy` + `Suspense` to load screens on demand.
- Avoid storing derived data in state; debounce search inputs; paginate on the server.
- React 19's compiler auto-memoises a lot of this.

**[⬆ Back to Top](#table-of-contents)**

## 45. What are custom hooks? Give an example.

*React*

- A function starting with `use` that bundles hooks so logic can be reused across components.

```tsx
function useFund(fundId: string) {
  const [fund, setFund] = useState<Fund | null>(null);
  useEffect(() => {
    fetch(`/api/funds/${fundId}`).then(r => r.json()).then(setFund);
  }, [fundId]);
  return fund;
}
// in any component:
const fund = useFund('ZSP');
```

**[⬆ Back to Top](#table-of-contents)**

## 46. What is an error boundary?

*React*

- A component that catches **render errors** in its children and shows a fallback UI instead of a blank screen.
- Written as a class (`componentDidCatch` / `getDerivedStateFromError`) or via the **react-error-boundary** package.
- It does **not** catch errors in event handlers or async code; handle those with try/catch.

**[⬆ Back to Top](#table-of-contents)**

## 47. How do you test React components?

*React*

- **Jest or Vitest + React Testing Library:** render the component and test it the way a user would (find by text/role, click, assert what's shown).
- Mock API calls with **MSW** (Mock Service Worker).
- **Playwright / Cypress** for end-to-end flows (e.g. analyst submits a rebalance).

```tsx
render(<FundRow fund={fund} onSelect={onSelect} />);
await userEvent.click(screen.getByText('ZSP'));
expect(onSelect).toHaveBeenCalledWith('ZSP');
```

**[⬆ Back to Top](#table-of-contents)**

## 48. React vs Angular: you have used both?

*React*

> "Yes. **Angular** is a full framework: modules, dependency injection, services, RxJS, two-way binding, opinionated structure. **React** is a UI library: components are just functions, one-way data flow, hooks for state, and you choose the router, state and form libraries. Angular is great for big teams that want one standard way; React is lighter and more flexible. The core skills, component design, typed models, API integration and testing, are the same in both."

**[⬆ Back to Top](#table-of-contents)**

## 49. TypeScript basics: interface vs type, generics, any vs unknown.

*TypeScript*

- **interface** for object shapes, extendable; **type** can also do unions and intersections: `type Side = 'BUY' | 'SELL'`.
- **Generics:** reusable typed code: `function first<T>(items: T[]): T | undefined`.
- **any** turns off checking; **unknown** forces you to check first, so it's safer for API responses.
- **strict mode** catches null/undefined bugs at compile time.
- **Narrowing:** `typeof`, `in`, discriminated unions (`switch (msg.type)`).

**[⬆ Back to Top](#table-of-contents)**

## 50. TypeScript utility types?

*TypeScript*

- **Partial<T>:** all props optional (good for update payloads).
- **Pick<T, K> / Omit<T, K>:** choose or drop fields.
- **Record<K, V>:** a typed dictionary: `Record<string, number>` for ticker → weight.
- **Readonly<T>:** prevent mutation.
- **ReturnType<typeof fn>**, **Awaited<T>**.

```ts
interface Holding { ticker: string; shares: number; price: number }
type HoldingUpdate = Partial<Omit<Holding, 'ticker'>>;
const targets: Record<string, number> = { AAPL: 0.05, MSFT: 0.04 };
```

**[⬆ Back to Top](#table-of-contents)**

## 51. What is Node.js and how does the event loop work?

*Node.js*

- JavaScript runtime on the server (V8 engine), **single-threaded with non-blocking I/O**.
- Slow work (network, file, DB) is handed to the system / libuv thread pool; when it finishes, its callback goes on a queue and the **event loop** runs it.
- Order: synchronous code → **microtasks** (resolved Promises, `process.nextTick`) → macrotasks (timers, I/O callbacks).
- Great for **I/O-heavy** APIs; **CPU-heavy** work blocks the loop, so move it to **worker threads** or a separate service.

> "Same idea as async/await in .NET: don't block a thread waiting for I/O."

**[⬆ Back to Top](#table-of-contents)**

## 52. Promises and async/await in Node: error handling and running in parallel?

*Node.js*

```ts
async function loadFund(id: string) {
  try {
    const [holdings, prices] = await Promise.all([getHoldings(id), getPrices(id)]); // parallel
    return { holdings, prices };
  } catch (err) {
    logger.error({ err, id }, 'loadFund failed');
    throw err;
  }
}
```
- **Promise.all:** parallel, fails fast if one fails. **Promise.allSettled:** wait for all, get each result/error.
- Sequential `await` in a loop is slow when calls are independent.
- Always handle rejections; an unhandled rejection can crash the process.

**[⬆ Back to Top](#table-of-contents)**

## 53. Build a simple REST API in Node (Express). What is middleware?

*Node.js*

```ts
import express from 'express';
const app = express();
app.use(express.json());                 // middleware: parse JSON body

app.get('/funds/:id', async (req, res, next) => {
  try {
    const fund = await repo.getFund(req.params.id);
    if (!fund) return res.status(404).json({ error: 'Not found' });
    res.json(fund);
  } catch (e) { next(e); }
});

app.use((err, req, res, next) => res.status(500).json({ error: 'Server error' })); // error middleware
app.listen(3000);
```
- **Middleware** = functions that run in order on each request (auth, logging, validation, errors), same idea as ASP.NET Core middleware.
- Alternatives: **Fastify**, **NestJS** (Angular-like structure with DI).

**[⬆ Back to Top](#table-of-contents)**

## 54. Node basics: npm, package.json, CommonJS vs ES modules, env config.

*Node.js*

- **package.json:** dependencies, scripts (`npm run build`), version. **package-lock.json** pins exact versions.
- **CommonJS:** `require` / `module.exports`; **ES modules:** `import` / `export` (modern default, `"type": "module"`).
- Config via **environment variables** (`process.env.DB_URL`); secrets from Secrets Manager, never in code.
- **Streams** for big files (read line by line instead of loading everything into memory).

**[⬆ Back to Top](#table-of-contents)**

## 55. Python basics: data structures and comprehensions.

*Python*

- **list** `[1, 2]` ordered, mutable; **tuple** `(1, 2)` immutable; **dict** `{'AAPL': 0.05}` key → value; **set** unique values.
- **Comprehensions:**
```python
weights = {h['ticker']: h['value'] / total for h in holdings}
big = [t for t, w in weights.items() if w > 0.05]
```
- Functions with **type hints**: `def drift(current: float, target: float) -> float:`
- **Exceptions:** `try / except ValueError as e / finally`.
- **Virtual environments** (`python -m venv`), `pip install`, `requirements.txt`.

**[⬆ Back to Top](#table-of-contents)**

## 56. Write a Python Lambda handler.

*Python*

```python
import json, boto3, os

s3 = boto3.client('s3')            # created once, reused on warm starts

def handler(event, context):
    body = json.loads(event.get('body') or '{}')
    fund_id = body.get('fundId')
    if not fund_id:
        return {'statusCode': 400, 'body': json.dumps({'error': 'fundId required'})}

    result = calculate_rebalance(fund_id)
    return {'statusCode': 200, 'body': json.dumps(result)}
```
- `event` = the trigger's payload (API Gateway request, SQS batch, S3 notification); `context` = request id, time remaining.
- **boto3** is the AWS SDK for Python.

**[⬆ Back to Top](#table-of-contents)**

## 57. Why Python for portfolio calculations? What is pandas?

*Python*

- **pandas:** tables (DataFrames) in memory: join holdings with prices, group by sector, compute weights in a few lines. **numpy** for fast math.

```python
import pandas as pd
df = holdings.merge(prices, on='ticker')
df['value'] = df['shares'] * df['price']
df['weight'] = df['value'] / df['value'].sum()
sector = df.groupby('sector')['weight'].sum()
```
- Python is the standard language for quant/analyst work, so analysts and engineers can share logic.
- Watch-outs: use **Decimal** or careful rounding for money; large Lambda packages (pandas) → use a **Lambda layer** or container image.

**[⬆ Back to Top](#table-of-contents)**

## 58. What is AWS Lambda and when would you use it?

*AWS Lambda*

**A function that runs when an event arrives.** No servers to manage, scales automatically, pay per run.

- **Triggers:** API Gateway (HTTP), **SQS**, **S3** upload, **EventBridge** (schedules/events), DynamoDB Streams.
- **Good for:** APIs, file processing, queue workers, scheduled jobs: short, stateless work.
- **Limits:** max **15 minutes**, memory up to 10 GB (CPU scales with memory), payload limits. Longer or multi-step → **Step Functions** or Fargate.

> "At Staples our receive → transform → dispatch services are exactly this shape. On AWS each step could be a Lambda reading from SQS."

**[⬆ Back to Top](#table-of-contents)**

## 59. Write a Lambda handler in TypeScript/Node behind API Gateway.

*AWS Lambda*

```ts
import type { APIGatewayProxyHandler } from 'aws-lambda';

const db = createDbClient(); // outside handler: reused across warm invocations

export const handler: APIGatewayProxyHandler = async (event) => {
  const fundId = event.pathParameters?.id;
  if (!fundId) return { statusCode: 400, body: JSON.stringify({ error: 'id required' }) };

  const fund = await db.getFund(fundId);
  return fund
    ? { statusCode: 200, body: JSON.stringify(fund) }
    : { statusCode: 404, body: JSON.stringify({ error: 'Not found' }) };
};
```

**[⬆ Back to Top](#table-of-contents)**

## 60. What are Lambda cold starts and how do you reduce them?

*AWS Lambda*

**Cold start** = the first call after idle: AWS creates the environment and loads your code, which adds latency.

- Keep the package small; bundle/tree-shake (esbuild).
- Create SDK and DB clients **outside the handler** so warm calls reuse them.
- **Provisioned concurrency** for latency-sensitive APIs; **SnapStart** for Java/Python/.NET.
- Node and Python start fast.

**[⬆ Back to Top](#table-of-contents)**

## 61. How do you make a Lambda reliable when processing SQS messages?

*AWS Lambda*

- **Idempotent:** SQS can deliver twice, so record processed message/business IDs and skip repeats.
- **Dead-letter queue (DLQ)** after N failures + an alert.
- **Partial batch response:** return only the failed message IDs so good ones aren't retried.
- **Visibility timeout** > function timeout.
- **Least-privilege IAM role** per function; logs/metrics in **CloudWatch**, tracing with **X-Ray**.

> "Same ideas as my outbox pattern at Staples: never lose a message, never process it twice."

**[⬆ Back to Top](#table-of-contents)**

## 62. What is Step Functions and when would you use it with Lambda?

*AWS Lambda*

- A managed **workflow / state machine**: chains Lambdas with retries, branches, parallel steps, and **waits** (even days, e.g. for human approval).
- Use it when a process has **multiple steps** or is longer than 15 min, instead of one Lambda calling another.
- Rebalance example: Validate scores → Calculate weights → Check constraints → **Wait for analyst approval** → Publish trades. Each step retries on its own and you see exactly where a run failed.
- Azure equivalent: **Durable Functions / Logic Apps**.

**[⬆ Back to Top](#table-of-contents)**

## 63. How do you deploy and configure Lambdas? (IaC, CI/CD, secrets)

*AWS Lambda*

- **Infrastructure as code:** AWS **CDK** (TypeScript), **SAM**, Serverless Framework or Terraform. Never click-ops in prod.
- **CI/CD:** build → test → deploy to dev/test/prod stages (GitHub Actions / CodePipeline), same as my Azure DevOps pipelines.
- **Config** in environment variables; **secrets** in Secrets Manager / Parameter Store, read at startup.
- **Versions and aliases** for safe rollouts (e.g. shift 10% traffic first).

**[⬆ Back to Top](#table-of-contents)**

## 64. Lambda vs containers: how do you choose?

*AWS Lambda*

- **Lambda:** spiky or event-driven load, short tasks, little ops. Downsides: 15-min limit, cold starts, harder local debugging.
- **Containers (ECS/Fargate/EKS):** long-running services, steady heavy traffic, full runtime control.

> "At Staples we run on AKS because the services are always on. For something like a rebalance that runs a few times a day, Lambda plus Step Functions is cheaper and simpler."

**[⬆ Back to Top](#table-of-contents)**

## 65. What is an ETF and what does rebalancing mean?

*ETF & portfolio*

- **ETF (exchange-traded fund):** a basket of stocks that trades on an exchange like a single stock.
- **Weights:** what % of the fund each stock is.
- **Rebalancing:** bringing holdings back to **target weights**, on a schedule (e.g. quarterly) or when **drift** passes a threshold, because prices move and weights change.
- **Weighting styles:** market-cap, equal-weight, or **factor/score-based** (theirs: weights from analysts' stock evaluations).
- **Constraints:** max % per stock, sector caps, liquidity, keep **turnover** and trading cost low.

**[⬆ Back to Top](#table-of-contents)**

## 66. Portfolio / ETF glossary.

*ETF & portfolio*

- **Ticker:** stock symbol (AAPL). **Holdings:** what the fund owns.
- **AUM:** assets under management (fund size).
- **NAV:** net asset value per unit = (assets − liabilities) / units.
- **Benchmark / index:** what the fund is compared against or tracks.
- **Tracking error:** how far the fund's return differs from its index.
- **Drift:** current weight − target weight.
- **Turnover:** how much of the fund is traded in a rebalance (more = more cost).
- **Creation / redemption:** how ETF units are created or removed by big dealers in exchange for baskets of stocks.
- **Active vs passive:** analysts picking/weighting (active) vs tracking an index (passive).

**[⬆ Back to Top](#table-of-contents)**

## 67. Walk me through a rebalance calculation with numbers.

*ETF & portfolio*

**Fund = $1,000,000. Targets: A 50%, B 30%, C 20%.**

After the market moves, current values: **A $600k (60%), B $250k (25%), C $150k (15%).**

| Stock | Target $ | Current $ | Trade |
|---|---|---|---|
| A | 500k | 600k | **Sell $100k** |
| B | 300k | 250k | **Buy $50k** |
| C | 200k | 150k | **Buy $50k** |

Sells = buys, so the fund stays fully invested. Trades in **shares** = dollar amount / price, rounded to whole shares.

**Drift threshold:** only trade if |drift| > e.g. 2%, to avoid tiny costly trades.

```ts
const trades = holdings.map(h => {
  const targetValue = totalValue * targets[h.ticker];
  const diff = targetValue - h.value;
  return { ticker: h.ticker, side: diff > 0 ? 'BUY' : 'SELL', amount: Math.abs(diff) };
}).filter(t => t.amount / totalValue > 0.02);
```

**[⬆ Back to Top](#table-of-contents)**

## 68. Design a tool for analysts to rebalance an ETF based on stock evaluations.

*ETF & portfolio*

**ASK → FLOW → FAIL → WATCH → SHIP.**

**ASK:** how many funds/stocks, how often, who approves, where prices and holdings come from, what rules apply.

**FLOW:**
1. Analysts enter or upload scores in the **React app** (file → **S3**).
2. **API Gateway + Lambda** validate and save (RDS/DynamoDB).
3. **Step Functions:** compute target weights (Python) → apply constraints → compare with holdings → **proposed trade list**.
4. Analyst/PM **reviews and approves** in the UI → publish to trading / downstream via SQS/EventBridge.

**FAIL:** bad or stale data stops the run, **all-or-nothing**; idempotent retries; DLQ + alerts.

**WATCH:** CloudWatch dashboards; **every rebalance versioned and auditable**: inputs, outputs, who approved, when.

**SHIP:** one fund first, run in parallel with the current process, reconcile, then expand.

> "Auditability is the part I'd insist on; at Certent every number had to trace back to its source."

**[⬆ Back to Top](#table-of-contents)**

## 69. How would you make sure portfolio calculations are correct?

*ETF & portfolio*

- **Decimal** types (or integer cents) for money, not floating point; consistent rounding rules.
- **Unit tests** with known examples: weights sum to 100%, caps respected, sells = buys.
- **Validate inputs:** missing or stale prices, unknown tickers, duplicate scores.
- **Reconcile** against the old process during rollout.
- Store inputs + outputs + code version of every run so any result can be reproduced.

**[⬆ Back to Top](#table-of-contents)**

## 70. What is OpenSpec?

*OpenSpec & AI*

**Open-source spec-driven development (SDD) framework for AI coding assistants**: works with Claude Code, Cursor, GitHub Copilot, Codex, Gemini CLI and 30+ tools. MIT licensed, by Fission AI.

**The problem it solves:** when requirements live only in chat with an AI, results are unpredictable, and nobody can review *what* was asked for. OpenSpec adds a light **spec layer in the repo** so humans and AI **"agree before you build"**.

**Philosophy:** fluid not rigid, iterative not waterfall, works on **brownfield** (existing) code, not just new projects.

> "What I like about OpenSpec is that it treats the spec like code: in the repo, reviewed in a PR, versioned. For a finance team that's huge, because you can always see *why* something changed."

**[⬆ Back to Top](#table-of-contents)**

## 71. Walk me through the OpenSpec workflow.

*OpenSpec & AI*

1. **Explore:** think through the idea with the AI, read the existing code and specs.
2. **Propose:** the AI drafts a change folder: `openspec/changes/<change-name>/`
   - **proposal.md:** why and what is changing
   - **specs/:** requirement deltas
   - **design.md:** technical approach
   - **tasks.md:** implementation checklist
3. **Review:** the team reviews the proposal like a PR and refines it **before any code**.
4. **Apply:** the AI implements, ticking off tasks.md.
5. **Verify:** check the implementation matches the spec.
6. **Archive:** the change moves to `openspec/changes/archive/<date>-<name>/` and its deltas merge into the main specs, so specs always describe the current system.

**Commands:** `openspec init` to set up; in the AI tool, slash commands like `/opsx:propose`, `/opsx:apply`, `/opsx:archive` (named `/openspec-propose` etc. in newer versions).

**[⬆ Back to Top](#table-of-contents)**

## 72. What does an OpenSpec spec look like?

*OpenSpec & AI*

Plain Markdown with requirements and **WHEN / THEN scenarios**:

```markdown
 ## ADDED Requirements

### Requirement: Drift threshold
The system SHALL only propose a trade when a holding's drift exceeds the fund's threshold.

#### Scenario: Small drift is ignored
- WHEN a holding's weight is 5.5% and its target is 5% with a 2% threshold
- THEN no trade is proposed for that holding

#### Scenario: Large drift is rebalanced
- WHEN a holding's weight is 8% and its target is 5% with a 2% threshold
- THEN a SELL trade bringing it back to 5% is proposed
```
- Delta sections: **ADDED / MODIFIED / REMOVED Requirements**.
- Scenarios double as **test cases**: each one maps to a unit test.

**[⬆ Back to Top](#table-of-contents)**

## 73. OpenSpec vs just prompting an AI, or other tools like Spec Kit and Kiro?

*OpenSpec & AI*

- **vs plain prompting:** the plan is a reviewable file in the repo, not lost chat history; the team reviews intent before code exists; specs stay as living documentation.
- **vs GitHub Spec Kit:** OpenSpec is lighter, with no rigid phase gates, and focuses on **changes to existing systems**.
- **vs Kiro (AWS's spec-driven IDE):** OpenSpec isn't tied to one IDE or model; it works with whatever AI tool each developer uses.

> "That's why I like it: spec-first is how I already work with AI. I keep the rules and the plan in the repo, the AI implements against them, and I review the result like any PR. OpenSpec makes that a team standard: proposal, spec deltas, tasks, then apply and archive, so the specs always describe the current system."

**[⬆ Back to Top](#table-of-contents)**

## 74. How do you use AI coding tools safely in a team?

*OpenSpec & AI*

- **Spec first** (OpenSpec): agree on the change before AI writes code.
- **Review AI code like any PR:** tests, edge cases, security, performance.
- Small changes; run tests, type checks and linters in CI before merging.
- Repo rules file (AGENTS.md / CLAUDE.md) so the AI follows team conventions.
- Never paste client or financial data into tools that aren't approved.

**[⬆ Back to Top](#table-of-contents)**

## 75. Tell me about a time you learned a new technology quickly.

*Behavioural*

**Staples:** joined the integration team and shipped a new integration microservice every 1–2 months across Event Hub, GCP Pub/Sub, AKS and Datadog. Or **Centric:** the Web Forms → Angular migration.

- **Situation:** new team / new stack.
- **Task:** deliver a working integration fast.
- **Action:** learned the existing pattern first, built one small piece end-to-end, asked questions early, reused the receive → transform → dispatch template.
- **Result:** shipped on time, and each new integration went faster.

**[⬆ Back to Top](#table-of-contents)**

## 76. Tell me about a time two systems or teams disagreed on data.

*Behavioural*

**Single Pool Inventory (Staples):** transport showed 7 of a blue SKU, warehouse showed 6. Two sources of truth.

- **Action:** built one central inventory service feeding every system, so everyone reads the same number.
- **Lesson for portfolio tools:** holdings and prices must come from **one trusted source**, or rebalancing decisions are wrong.

**[⬆ Back to Top](#table-of-contents)**

## 77. What questions do you have for us?

*Behavioural*

- "What does the team own: the analyst-facing React app, the rebalancing engine, or both?"
- "How is OpenSpec working for you? Has it changed how you review AI-written code?"
- "What's the most painful part of the analysts' current rebalancing process?"
- "What would success look like in my first 3 months?"

**[⬆ Back to Top](#table-of-contents)**

