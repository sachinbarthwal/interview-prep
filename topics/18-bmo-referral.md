# BMO Referral: React, Lambda, ETF portfolio tools, OpenSpec

> 30-minute referral meeting. Team builds portfolio-management tools: analysts design ETFs and rebalance them based on stock evaluations. Stack: React + AWS Lambda, TypeScript, Python, Node; bonus: OpenSpec. Say each answer out loud before revealing it.

## 1. Tell me about yourself.

*Intro & fit*

> "I'm a senior full-stack developer with about 10 years' experience. My core is **.NET, C#, SQL and Azure**, and on the front end and scripting side I've worked with **React, TypeScript, Node and Python**, at work and in my own projects.

> Right now at **Staples** I'm on the integration team building **event-driven microservices**: receive an event, transform it, dispatch it to the next system, each step its own small service with CI/CD and monitoring.

> Before that, ~3 years at **Accolite on insightsoftware's Certent product**: financial reporting and SEC disclosure, so I'm used to financial data where every number must be exact and traceable.

> I also use AI coding tools like Claude Code daily in my own projects. A portfolio tool built with React, serverless and spec-driven AI development is a really good fit for what I've done and where I want to go."

**[⬆ Back to Top](#table-of-contents)**

## 2. What is your experience with React, Node, Python and TypeScript?

*Intro & fit*

**Say it with confidence, short and concrete:**

> "**React and TypeScript:** I've built React front ends with function components and hooks, typed with TypeScript; I've also done a lot of Angular, so component design and typed front ends are second nature.

> **Node:** I've built Node projects and APIs; my current personal project is a Node/Electron desktop app that captures audio and calls AI APIs.

> **Python:** projects and scripting, including data handling and API calls.

> My deepest production experience is .NET and Azure, but the patterns are the same across all of them: APIs, async I/O, event-driven services, clean components. I pick up the specifics quickly."

**[⬆ Back to Top](#table-of-contents)**

## 3. Why do you want this role?

*Intro & fit*

> "Three reasons. **The domain:** analysts making portfolio decisions on financial data is close to my Certent work, where accuracy and audit trails were everything. **The architecture:** event-driven, small focused services is exactly what I build at Staples; Lambda is the AWS version of that. **The way of working:** spec-driven development with AI tools like OpenSpec is where engineering is heading, and I already work with AI assistants every day."

**[⬆ Back to Top](#table-of-contents)**

## 4. AWS vs Azure: map the services you know.

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

## 5. What do you think our team builds day to day?

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

## 6. What is React and how does rendering work?

*React*

- A JavaScript **library for building UIs from components**: each component is a function that returns JSX.
- **One-way data flow:** data goes down as **props**, events come up via callbacks.
- When **state or props change**, React re-runs the component, builds a new **virtual DOM**, compares it with the previous one (**reconciliation / diffing**) and updates only what changed in the real DOM.
- **React 18+:** automatic batching of state updates, concurrent rendering (`useTransition` for non-urgent updates), `Suspense` for loading states. **React 19:** Actions, `use()`, Server Components, and the React Compiler (auto-memoisation).

**[⬆ Back to Top](#table-of-contents)**

## 7. Props vs state?

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

## 8. Explain React hooks: useState, useEffect, useMemo, useCallback, useRef.

*React*

- **useState:** data that changes what's on screen; the setter triggers a re-render. Use the function form when the new value depends on the old: `setCount(c => c + 1)`.
- **useEffect:** side effects after render (fetching, subscriptions, timers). The **dependency array** controls when it re-runs; `[]` = once on mount; return a **cleanup** function.
- **useMemo:** cache an expensive calculation until inputs change.
- **useCallback:** cache a function so memoised children don't re-render.
- **useRef:** a mutable value that survives renders **without** re-rendering; also used to reach a DOM element.
- Others: **useContext** (read context), **useReducer** (complex state transitions).
- **Rules of hooks:** only call at the top level of a component or custom hook, never in loops or conditions.

**[⬆ Back to Top](#table-of-contents)**

## 9. How do you fetch data in React? Show loading and error handling.

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

## 10. useEffect: common mistakes?

*React*

- **Missing dependencies** → stale values (stale closure). Include everything you read inside.
- **Setting state that's also a dependency** → infinite loop.
- **No cleanup** → memory leaks or setting state after unmount (timers, subscriptions, in-flight fetch → use AbortController).
- **Using an effect for derived data**: if you can calculate it during render, don't put it in state + effect.
- In **StrictMode (dev)** effects run twice on mount to surface missing cleanups; that's expected.

**[⬆ Back to Top](#table-of-contents)**

## 11. Why do lists need keys?

*React*

- Keys let React match items between renders, so it updates/moves the right element instead of re-creating everything.
- Use a **stable unique id** (e.g. ticker, fund id). **Avoid array index** when items can be reordered, inserted or deleted, since it causes wrong rows to keep the wrong state.

**[⬆ Back to Top](#table-of-contents)**

## 12. Controlled vs uncontrolled components (forms)?

*React*

- **Controlled:** the input's value lives in React state; `value` + `onChange`. Easy validation and formatting (e.g. weight must be 0–100).
- **Uncontrolled:** the DOM holds the value; read it with a ref when needed. Less code, fewer re-renders.
- Big forms: **React Hook Form** (+ **Zod** for schema validation).

```tsx
const [weight, setWeight] = useState('');
<input value={weight} onChange={e => setWeight(e.target.value)} />
```

**[⬆ Back to Top](#table-of-contents)**

## 13. How do you share state across components? Context vs Redux vs React Query.

*React*

- **Props / lifting state:** first choice for nearby components.
- **Context:** avoids **prop drilling** for app-wide things (current user, theme, selected fund). Every consumer re-renders when the value changes, so don't put fast-changing data in it.
- **Redux Toolkit / Zustand:** larger client-side state with many updates.
- **React Query:** **server state** (data from APIs) with caching and refetching. Most "global state" is actually server state.

> "For an analyst tool I'd keep fund and holdings data in React Query, the selected fund in the URL or context, and form state local."

**[⬆ Back to Top](#table-of-contents)**

## 14. How do you make a React app fast? (e.g. a big holdings table)

*React*

- **Measure first** with React DevTools Profiler.
- **React.memo** for components that get the same props; **useMemo / useCallback** to keep props stable.
- **Virtualise long lists/tables** (TanStack Virtual, react-window): render only visible rows; essential for 1000s of holdings.
- **Code splitting:** `React.lazy` + `Suspense` to load screens on demand.
- Avoid storing derived data in state; debounce search inputs; paginate on the server.
- React 19's compiler auto-memoises a lot of this.

**[⬆ Back to Top](#table-of-contents)**

## 15. What are custom hooks? Give an example.

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

## 16. What is an error boundary?

*React*

- A component that catches **render errors** in its children and shows a fallback UI instead of a blank screen.
- Written as a class (`componentDidCatch` / `getDerivedStateFromError`) or via the **react-error-boundary** package.
- It does **not** catch errors in event handlers or async code; handle those with try/catch.

**[⬆ Back to Top](#table-of-contents)**

## 17. How do you test React components?

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

## 18. React vs Angular: you have used both?

*React*

> "Yes. **Angular** is a full framework: modules, dependency injection, services, RxJS, two-way binding, opinionated structure. **React** is a UI library: components are just functions, one-way data flow, hooks for state, and you choose the router, state and form libraries. Angular is great for big teams that want one standard way; React is lighter and more flexible. The core skills, component design, typed models, API integration and testing, are the same in both."

**[⬆ Back to Top](#table-of-contents)**

## 19. TypeScript basics: interface vs type, generics, any vs unknown.

*TypeScript*

- **interface** for object shapes, extendable; **type** can also do unions and intersections: `type Side = 'BUY' | 'SELL'`.
- **Generics:** reusable typed code: `function first<T>(items: T[]): T | undefined`.
- **any** turns off checking; **unknown** forces you to check first, so it's safer for API responses.
- **strict mode** catches null/undefined bugs at compile time.
- **Narrowing:** `typeof`, `in`, discriminated unions (`switch (msg.type)`).

**[⬆ Back to Top](#table-of-contents)**

## 20. TypeScript utility types?

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

## 21. What is Node.js and how does the event loop work?

*Node.js*

- JavaScript runtime on the server (V8 engine), **single-threaded with non-blocking I/O**.
- Slow work (network, file, DB) is handed to the system / libuv thread pool; when it finishes, its callback goes on a queue and the **event loop** runs it.
- Order: synchronous code → **microtasks** (resolved Promises, `process.nextTick`) → macrotasks (timers, I/O callbacks).
- Great for **I/O-heavy** APIs; **CPU-heavy** work blocks the loop, so move it to **worker threads** or a separate service.

> "Same idea as async/await in .NET: don't block a thread waiting for I/O."

**[⬆ Back to Top](#table-of-contents)**

## 22. Promises and async/await in Node: error handling and running in parallel?

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

## 23. Build a simple REST API in Node (Express). What is middleware?

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

## 24. Node basics: npm, package.json, CommonJS vs ES modules, env config.

*Node.js*

- **package.json:** dependencies, scripts (`npm run build`), version. **package-lock.json** pins exact versions.
- **CommonJS:** `require` / `module.exports`; **ES modules:** `import` / `export` (modern default, `"type": "module"`).
- Config via **environment variables** (`process.env.DB_URL`); secrets from Secrets Manager, never in code.
- **Streams** for big files (read line by line instead of loading everything into memory).

**[⬆ Back to Top](#table-of-contents)**

## 25. Python basics: data structures and comprehensions.

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

## 26. Write a Python Lambda handler.

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

## 27. Why Python for portfolio calculations? What is pandas?

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

## 28. What is AWS Lambda and when would you use it?

*AWS Lambda*

**A function that runs when an event arrives.** No servers to manage, scales automatically, pay per run.

- **Triggers:** API Gateway (HTTP), **SQS**, **S3** upload, **EventBridge** (schedules/events), DynamoDB Streams.
- **Good for:** APIs, file processing, queue workers, scheduled jobs: short, stateless work.
- **Limits:** max **15 minutes**, memory up to 10 GB (CPU scales with memory), payload limits. Longer or multi-step → **Step Functions** or Fargate.

> "At Staples our receive → transform → dispatch services are exactly this shape. On AWS each step could be a Lambda reading from SQS."

**[⬆ Back to Top](#table-of-contents)**

## 29. Write a Lambda handler in TypeScript/Node behind API Gateway.

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

## 30. What are Lambda cold starts and how do you reduce them?

*AWS Lambda*

**Cold start** = the first call after idle: AWS creates the environment and loads your code, which adds latency.

- Keep the package small; bundle/tree-shake (esbuild).
- Create SDK and DB clients **outside the handler** so warm calls reuse them.
- **Provisioned concurrency** for latency-sensitive APIs; **SnapStart** for Java/Python/.NET.
- Node and Python start fast.

**[⬆ Back to Top](#table-of-contents)**

## 31. How do you make a Lambda reliable when processing SQS messages?

*AWS Lambda*

- **Idempotent:** SQS can deliver twice, so record processed message/business IDs and skip repeats.
- **Dead-letter queue (DLQ)** after N failures + an alert.
- **Partial batch response:** return only the failed message IDs so good ones aren't retried.
- **Visibility timeout** > function timeout.
- **Least-privilege IAM role** per function; logs/metrics in **CloudWatch**, tracing with **X-Ray**.

> "Same ideas as my outbox pattern at Staples: never lose a message, never process it twice."

**[⬆ Back to Top](#table-of-contents)**

## 32. What is Step Functions and when would you use it with Lambda?

*AWS Lambda*

- A managed **workflow / state machine**: chains Lambdas with retries, branches, parallel steps, and **waits** (even days, e.g. for human approval).
- Use it when a process has **multiple steps** or is longer than 15 min, instead of one Lambda calling another.
- Rebalance example: Validate scores → Calculate weights → Check constraints → **Wait for analyst approval** → Publish trades. Each step retries on its own and you see exactly where a run failed.
- Azure equivalent: **Durable Functions / Logic Apps**.

**[⬆ Back to Top](#table-of-contents)**

## 33. How do you deploy and configure Lambdas? (IaC, CI/CD, secrets)

*AWS Lambda*

- **Infrastructure as code:** AWS **CDK** (TypeScript), **SAM**, Serverless Framework or Terraform. Never click-ops in prod.
- **CI/CD:** build → test → deploy to dev/test/prod stages (GitHub Actions / CodePipeline), same as my Azure DevOps pipelines.
- **Config** in environment variables; **secrets** in Secrets Manager / Parameter Store, read at startup.
- **Versions and aliases** for safe rollouts (e.g. shift 10% traffic first).

**[⬆ Back to Top](#table-of-contents)**

## 34. Lambda vs containers: how do you choose?

*AWS Lambda*

- **Lambda:** spiky or event-driven load, short tasks, little ops. Downsides: 15-min limit, cold starts, harder local debugging.
- **Containers (ECS/Fargate/EKS):** long-running services, steady heavy traffic, full runtime control.

> "At Staples we run on AKS because the services are always on. For something like a rebalance that runs a few times a day, Lambda plus Step Functions is cheaper and simpler."

**[⬆ Back to Top](#table-of-contents)**

## 35. What is an ETF and what does rebalancing mean?

*ETF & portfolio*

- **ETF (exchange-traded fund):** a basket of stocks that trades on an exchange like a single stock.
- **Weights:** what % of the fund each stock is.
- **Rebalancing:** bringing holdings back to **target weights**, on a schedule (e.g. quarterly) or when **drift** passes a threshold, because prices move and weights change.
- **Weighting styles:** market-cap, equal-weight, or **factor/score-based** (theirs: weights from analysts' stock evaluations).
- **Constraints:** max % per stock, sector caps, liquidity, keep **turnover** and trading cost low.

**[⬆ Back to Top](#table-of-contents)**

## 36. Portfolio / ETF glossary.

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

## 37. Walk me through a rebalance calculation with numbers.

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

## 38. Design a tool for analysts to rebalance an ETF based on stock evaluations.

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

## 39. How would you make sure portfolio calculations are correct?

*ETF & portfolio*

- **Decimal** types (or integer cents) for money, not floating point; consistent rounding rules.
- **Unit tests** with known examples: weights sum to 100%, caps respected, sells = buys.
- **Validate inputs:** missing or stale prices, unknown tickers, duplicate scores.
- **Reconcile** against the old process during rollout.
- Store inputs + outputs + code version of every run so any result can be reproduced.

**[⬆ Back to Top](#table-of-contents)**

## 40. What is OpenSpec?

*OpenSpec & AI*

**Open-source spec-driven development (SDD) framework for AI coding assistants**: works with Claude Code, Cursor, GitHub Copilot, Codex, Gemini CLI and 30+ tools. MIT licensed, by Fission AI.

**The problem it solves:** when requirements live only in chat with an AI, results are unpredictable, and nobody can review *what* was asked for. OpenSpec adds a light **spec layer in the repo** so humans and AI **"agree before you build"**.

**Philosophy:** fluid not rigid, iterative not waterfall, works on **brownfield** (existing) code, not just new projects.

> "What I like about OpenSpec is that it treats the spec like code: in the repo, reviewed in a PR, versioned. For a finance team that's huge, because you can always see *why* something changed."

**[⬆ Back to Top](#table-of-contents)**

## 41. Walk me through the OpenSpec workflow.

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

## 42. What does an OpenSpec spec look like?

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

## 43. OpenSpec vs just prompting an AI, or other tools like Spec Kit and Kiro?

*OpenSpec & AI*

- **vs plain prompting:** the plan is a reviewable file in the repo, not lost chat history; the team reviews intent before code exists; specs stay as living documentation.
- **vs GitHub Spec Kit:** OpenSpec is lighter, with no rigid phase gates, and focuses on **changes to existing systems**.
- **vs Kiro (AWS's spec-driven IDE):** OpenSpec isn't tied to one IDE or model; it works with whatever AI tool each developer uses.

> "That's why I like it: spec-first is how I already work with AI. I keep the rules and the plan in the repo, the AI implements against them, and I review the result like any PR. OpenSpec makes that a team standard: proposal, spec deltas, tasks, then apply and archive, so the specs always describe the current system."

**[⬆ Back to Top](#table-of-contents)**

## 44. How do you use AI coding tools safely in a team?

*OpenSpec & AI*

- **Spec first** (OpenSpec): agree on the change before AI writes code.
- **Review AI code like any PR:** tests, edge cases, security, performance.
- Small changes; run tests, type checks and linters in CI before merging.
- Repo rules file (AGENTS.md / CLAUDE.md) so the AI follows team conventions.
- Never paste client or financial data into tools that aren't approved.

**[⬆ Back to Top](#table-of-contents)**

## 45. Tell me about a time you learned a new technology quickly.

*Behavioural*

**Staples:** joined the integration team and shipped a new integration microservice every 1–2 months across Event Hub, GCP Pub/Sub, AKS and Datadog. Or **Centric:** the Web Forms → Angular migration.

- **Situation:** new team / new stack.
- **Task:** deliver a working integration fast.
- **Action:** learned the existing pattern first, built one small piece end-to-end, asked questions early, reused the receive → transform → dispatch template.
- **Result:** shipped on time, and each new integration went faster.

**[⬆ Back to Top](#table-of-contents)**

## 46. Tell me about a time two systems or teams disagreed on data.

*Behavioural*

**Single Pool Inventory (Staples):** transport showed 7 of a blue SKU, warehouse showed 6. Two sources of truth.

- **Action:** built one central inventory service feeding every system, so everyone reads the same number.
- **Lesson for portfolio tools:** holdings and prices must come from **one trusted source**, or rebalancing decisions are wrong.

**[⬆ Back to Top](#table-of-contents)**

## 47. What questions do you have for us?

*Behavioural*

- "What does the team own: the analyst-facing React app, the rebalancing engine, or both?"
- "How is OpenSpec working for you? Has it changed how you review AI-written code?"
- "What's the most painful part of the analysts' current rebalancing process?"
- "What would success look like in my first 3 months?"

**[⬆ Back to Top](#table-of-contents)**

