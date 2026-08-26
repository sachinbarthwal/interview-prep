# Angular & Frontend

> Angular questions tend to test whether you understand the *reactive* model
> underneath the framework (RxJS, change detection) rather than just component
> syntax — that's usually where the depth question lands.

## Table of Contents

| No. | Question |
|-----|----------|
| 1 | [What is an Angular module, and how do components share data across modules?](#1-what-is-an-angular-module-and-how-do-components-share-data-across-modules) |
| 2 | [`var` vs `let` vs `const`](#2-var-vs-let-vs-const) |
| 3 | [How do you write a custom directive and a custom pipe?](#3-how-do-you-write-a-custom-directive-and-a-custom-pipe) |
| 4 | [Angular lifecycle hooks, and `ngOnInit` vs the constructor](#4-angular-lifecycle-hooks-and-ngoninit-vs-the-constructor) |
| 5 | [How do you share data between components?](#5-how-do-you-share-data-between-components) |
| 6 | [`Subject` vs `BehaviorSubject` vs `ReplaySubject` vs `AsyncSubject`](#6-subject-vs-behaviorsubject-vs-replaysubject-vs-asyncsubject) |
| 7 | [What are Route Guards, and how do functional guards/interceptors work?](#7-what-are-route-guards-and-how-do-functional-guardsinterceptors-work) |
| 8 | [Content projection and `ng-template`](#8-content-projection-and-ng-template) |
| 9 | [What is an HTTP Interceptor?](#9-what-is-an-http-interceptor) |
| 10 | [How does Dependency Injection work in Angular?](#10-how-does-dependency-injection-work-in-angular) |
| 11 | [Observable vs Promise](#11-observable-vs-promise) |
| 12 | [Common RxJS operators](#12-common-rxjs-operators) |
| 13 | [How does routing work, and what is lazy loading?](#13-how-does-routing-work-and-what-is-lazy-loading) |
| 14 | [Where should an auth token be stored client-side?](#14-where-should-an-auth-token-be-stored-client-side) |
| 15 | [How do you approach state management in a large Angular app?](#15-how-do-you-approach-state-management-in-a-large-angular-app) |
| 16 | [Explain Angular's change detection, including `OnPush`](#16-explain-angulars-change-detection-including-onpush) |
| 17 | [AngularJS vs Angular (2+)](#17-angularjs-vs-angular-2) |
| 18 | [Advantages of TypeScript in Angular development](#18-advantages-of-typescript-in-angular-development) |
| 19 | [How would you optimize an Angular app with slow rendering?](#19-how-would-you-optimize-an-angular-app-with-slow-rendering) |
| 20 | [Dictionaries, JSON conversion, merging objects/arrays in JS/TS](#20-dictionaries-json-conversion-merging-objectsarrays-in-jsts) |
| 21 | [Building dynamic components and reusable libraries](#21-building-dynamic-components-and-reusable-libraries) |
| 22 | [What is a source map?](#22-what-is-a-source-map) |
| 23 | [Newer Angular features: Signals, Standalone, SSR/Hydration, DestroyRef](#23-newer-angular-features-signals-standalone-ssrhydration-destroyref) |
| 24 | [Build a reusable product-card component](#24-build-a-reusable-product-card-component) |
| 25 | [Angular unit testing with Jasmine](#25-angular-unit-testing-with-jasmine) |
| 26 | [JavaScript fundamentals: type inference, dates, closures, callbacks](#26-javascript-fundamentals-type-inference-dates-closures-callbacks) |
| 27 | [Implement a palindrome check without loops](#27-implement-a-palindrome-check-without-loops) |
| 28 | [CSS Flexbox and Bootstrap grid basics](#28-css-flexbox-and-bootstrap-grid-basics) |
| 29 | [At a high level, how does a browser render a web page?](#29-at-a-high-level-how-does-a-browser-render-a-web-page) |

## 1. What is an Angular module, and how do components share data across modules?

An `NgModule` groups related components, directives, pipes, and services into a
cohesive block, declaring what belongs to it and what it imports from elsewhere.
Since Angular 14+, **standalone components** let you skip `NgModule` almost
entirely for new code (see item 23), but the underlying compilation-unit concept
is the same either way. To share data **across** module boundaries, you don't pass
it through the module system directly — you use a shared, tree-provided **service**
(injected into whichever components need it) as the common source of truth, often
backed by an RxJS `Subject`/`BehaviorSubject` so consumers can react to changes.

**[⬆ Back to Top](#table-of-contents)**

## 2. `var` vs `let` vs `const`

`var` is function-scoped (or global) and hoisted, which allows confusing bugs like
being accessible before its declaration line and leaking out of `{}` blocks.
`let` is block-scoped and not usable before declaration (temporal dead zone).
`const` is block-scoped like `let`, but the binding can't be reassigned — though
for objects/arrays, the *contents* can still be mutated; only the reference is
locked.

**[⬆ Back to Top](#table-of-contents)**

## 3. How do you write a custom directive and a custom pipe?

A **directive** attaches behavior to a DOM element:

```typescript
@Directive({ selector: '[appHighlight]' })
export class HighlightDirective {
  constructor(private el: ElementRef) {
    el.nativeElement.style.backgroundColor = 'yellow';
  }
}
```

A **pipe** transforms a value for display in a template:

```typescript
@Pipe({ name: 'truncate' })
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit = 20): string {
    return value.length > limit ? value.slice(0, limit) + '…' : value;
  }
}
// usage: {{ longText | truncate:30 }}
```

**[⬆ Back to Top](#table-of-contents)**

## 4. Angular lifecycle hooks, and `ngOnInit` vs the constructor

Order: `constructor` → `ngOnChanges` → `ngOnInit` → `ngDoCheck` →
`ngAfterContentInit` → `ngAfterContentChecked` → `ngAfterViewInit` →
`ngAfterViewChecked` → ... → `ngOnDestroy`.

The **constructor** is plain TypeScript/DI wiring — Angular hasn't set up
`@Input()` bindings yet, so reading them there is unreliable. **`ngOnInit`** runs
once, right after Angular has set the initial `@Input()` values, which is why
component initialization logic (an initial API call, setting up derived state)
belongs there, not in the constructor.

**[⬆ Back to Top](#table-of-contents)**

## 5. How do you share data between components?

- **Parent → child:** `@Input()`.
- **Child → parent:** `@Output()` + `EventEmitter`.
- **Unrelated/distant components:** a shared, injectable service (often backed by
  a `BehaviorSubject` so late subscribers immediately get the current value).
- **Route-to-route:** route parameters, or a resolver.

**[⬆ Back to Top](#table-of-contents)**

## 6. `Subject` vs `BehaviorSubject` vs `ReplaySubject` vs `AsyncSubject`

| | Needs an initial value? | What a new subscriber gets |
|---|---|---|
| `Subject` | No | Nothing — only values emitted *after* subscribing |
| `BehaviorSubject` | Yes | Immediately replays the **current/last** value |
| `ReplaySubject` | No | Replays the last *N* (configurable buffer) values |
| `AsyncSubject` | No | Only the **final** value, and only after `complete()` fires |

`BehaviorSubject` is the one you reach for most often for shared component state,
since a late subscriber always sees the current value instead of missing past
emissions.

**[⬆ Back to Top](#table-of-contents)**

## 7. What are Route Guards, and how do functional guards/interceptors work?

Route Guards control whether navigation to/from a route is allowed —
`CanActivate` (can you enter this route), `CanDeactivate` (can you leave, e.g. an
unsaved-changes prompt), `CanActivateChild`, `Resolve` (pre-fetch data before the
route activates). Modern Angular (14+) supports **functional guards** — plain
functions instead of injectable classes:

```typescript
export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  return auth.isLoggedIn() ? true : inject(Router).createUrlTree(['/login']);
};
```

**Functional interceptors** work the same way for HTTP — a plain function
registered via `provideHttpClient(withInterceptors([authInterceptor]))` instead of
an injectable class implementing `HttpInterceptor`.

**[⬆ Back to Top](#table-of-contents)**

## 8. Content projection and `ng-template`

**Content projection** (`<ng-content>`) lets a parent pass markup *into* a child
component's template, similar to `children` in React or a `<slot>` in web
components:

```html
<!-- card.component.html -->
<div class="card"><ng-content></ng-content></div>

<!-- usage -->
<app-card><p>Anything goes here</p></app-card>
```

**`ng-template`** defines a chunk of template that isn't rendered by default — it's
rendered on demand (by `*ngIf`/`*ngFor` under the hood, or explicitly via
`ngTemplateOutlet` or a `TemplateRef`), useful for conditional layouts or reusable
template fragments passed as inputs.

**[⬆ Back to Top](#table-of-contents)**

## 9. What is an HTTP Interceptor?

A hook that runs on every outgoing `HttpClient` request (and/or incoming
response), used for cross-cutting concerns — attaching an auth header, logging,
transforming errors globally, or showing/hiding a loading spinner:

```typescript
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = inject(AuthService).token;
  const cloned = req.clone({ setHeaders: { Authorization: `Bearer ${token}` } });
  return next(cloned);
};
```

**[⬆ Back to Top](#table-of-contents)**

## 10. How does Dependency Injection work in Angular?

Angular's DI is hierarchical — providers can be registered at the root level
(`providedIn: 'root'`, effectively a singleton for the whole app), at a specific
module, or at a specific component (creating a new instance scoped to that
component and its children). When a component asks for a dependency via its
constructor, Angular walks up the injector tree looking for a matching provider,
starting from the component's own injector.

**[⬆ Back to Top](#table-of-contents)**

## 11. Observable vs Promise

| | Observable (RxJS) | Promise |
|---|---|---|
| Values over time | Can emit **many** values | Resolves **once** |
| Laziness | Lazy — nothing happens until you `.subscribe()` | Eager — starts executing immediately on creation |
| Cancellation | Cancellable (`unsubscribe()`) | Not cancellable |
| Operators | Rich operator set (`map`, `filter`, `debounceTime`, `switchMap`, ...) | Only `.then()`/`.catch()` chaining |

Angular's `HttpClient` returns Observables specifically so requests can be
cancelled (e.g. a stale autocomplete request) and composed with operators like
`switchMap`.

**[⬆ Back to Top](#table-of-contents)**

## 12. Common RxJS operators

- **`map`** — transform each emitted value.
- **`filter`** — only let values matching a predicate through.
- **`debounceTime`** — wait for a pause in emissions before emitting (classic
  search-box use case).
- **`switchMap`** — map to a new inner observable, **cancelling** the previous
  inner subscription — the standard choice for "cancel the last HTTP call if a new
  one starts" (like typeahead search).
- **`mergeMap`** — map to a new inner observable, running all of them
  concurrently without cancelling.
- **`concatMap`** — map to a new inner observable, running them strictly in
  sequence.
- **`combineLatest`** — combine the latest values from multiple observables
  whenever any of them emits.
- **`catchError`** — handle/recover from an error in the stream.
- **`takeUntil`** — a common pattern for auto-unsubscribing on component destroy.

**[⬆ Back to Top](#table-of-contents)**

## 13. How does routing work, and what is lazy loading?

The `Router` matches the current URL against a route configuration
(path → component) and swaps the component rendered in a `<router-outlet>`.
**Lazy loading** defers loading a feature module's (or a standalone component's)
JavaScript bundle until the user actually navigates to a route that needs it —
`loadChildren`/`loadComponent` with a dynamic `import()` — which keeps the initial
bundle small and speeds up first load.

**[⬆ Back to Top](#table-of-contents)**

## 14. Where should an auth token be stored client-side?

- **In-memory (a service field)** — safest against XSS since JavaScript on
  another origin can't read it and it's not persisted, but it disappears on a
  full page refresh, so it's usually paired with a refresh-token flow that
  re-establishes it silently.
- **`localStorage`** — persists across refreshes/tabs, but is readable by any
  script on the page, so it's vulnerable if the app has an XSS hole.
- **HttpOnly cookie** — not readable by JavaScript at all (best XSS protection),
  sent automatically by the browser, but needs CSRF protection since the browser
  attaches it to *every* request to that domain automatically.

**How to phrase it:** "There's no universally 'correct' answer — it's a trade-off
between XSS and CSRF exposure. I lean toward an HttpOnly, SameSite cookie for the
refresh token and keep the short-lived access token in memory, which minimizes
both attack surfaces."

**[⬆ Back to Top](#table-of-contents)**

## 15. How do you approach state management in a large Angular app?

- **Plain services + RxJS** — a service holding a `BehaviorSubject`, exposing it
  as a read-only `Observable`. Sufficient for most apps; simplest to reason about.
- **NgRx** — a Redux-style store (actions, reducers, effects, selectors).
  Predictable, testable, great DevTools story, but real ceremony/boilerplate —
  worth it once state and cross-component interactions get genuinely complex.
- **NgXS** — similar goals to NgRx with a less boilerplate-heavy, more
  Angular-idiomatic (decorator-based) API.
- **Signals** (Angular 16+) — fine-grained reactive primitives built into the
  framework itself, increasingly used as a lighter-weight alternative to a full
  external state library for component/local state.

**How to phrase it:** "I start with services + RxJS by default, and only reach
for NgRx once state is shared across many unrelated features and the
predictability/DevTools story starts paying for the added boilerplate."

**[⬆ Back to Top](#table-of-contents)**

## 16. Explain Angular's change detection, including `OnPush`

Angular's default change detection walks the **entire component tree** on every
async event (a click, an HTTP response, a timer) via Zone.js, comparing bound
values to their previous values and updating the DOM where they differ. With the
`OnPush` change detection strategy, a component only gets re-checked when: an
`@Input()` reference changes, an event originates from inside the component
itself, an `async` pipe emits, or you manually call `markForCheck()`. This
dramatically cuts the number of components checked per cycle, but it requires
treating inputs as **immutable** — mutating an object in place won't trigger a
re-check under `OnPush`, since the reference itself didn't change.

**[⬆ Back to Top](#table-of-contents)**

## 17. AngularJS vs Angular (2+)

| | AngularJS (1.x) | Angular (2+) |
|---|---|---|
| Architecture | MVC | Component-based |
| Language | JavaScript | TypeScript |
| Mobile support | Limited | Built with mobile performance in mind |
| Change detection | Dirty-checking (digest cycle) | Zone.js-based / Signals |
| Two-way binding | Default (`ng-model`) | Opt-in (`[(ngModel)]`) |

They're effectively different frameworks that share a name and lineage, not
versions of the same codebase.

**[⬆ Back to Top](#table-of-contents)**

## 18. Advantages of TypeScript in Angular development

Static typing catches a large class of bugs at compile time instead of runtime;
better IDE tooling (autocomplete, safe refactoring, go-to-definition); interfaces
and generics make large codebases easier to navigate and enforce contracts across
team boundaries; and it compiles down to plain JavaScript, so there's no runtime
cost.

**[⬆ Back to Top](#table-of-contents)**

## 19. How would you optimize an Angular app with slow rendering?

- Switch relevant components to **`OnPush`** change detection.
- **Lazy-load** feature modules/routes instead of one giant bundle.
- **`trackBy`** on `*ngFor` loops so Angular doesn't tear down and rebuild every
  DOM node on each update.
- Avoid calling functions directly in templates (`{{ getValue() }}`) — they
  re-run on every change-detection cycle; use a pipe (pure by default) or a
  precomputed property instead.
- **Virtual scrolling** (`cdk-virtual-scroll-viewport`) for long lists.
- Profile with Chrome DevTools' Performance tab / Angular DevTools to find the
  actual bottleneck before guessing.

**[⬆ Back to Top](#table-of-contents)**

## 20. Dictionaries, JSON conversion, merging objects/arrays in JS/TS

```typescript
// dictionary-like structure
const superhero = new Map<string, number>();
superhero.set('homelander', 28);
const heroPower = superhero.get('homelander');

// JSON string <-> object
const obj = JSON.parse(jsonString);
const str = JSON.stringify(obj);

// merge objects
const merged = { ...objA, ...objB };        // spread
const merged2 = Object.assign({}, objA, objB);

// combine arrays
const combined = [...arr1, ...arr2];
const combined2 = arr1.concat(arr2);
```

**[⬆ Back to Top](#table-of-contents)**

## 21. Building dynamic components and reusable libraries

**Dynamic components** are created at runtime rather than declared in a template
— via `ViewContainerRef.createComponent(SomeComponent)` — useful for things like a
generic modal/dialog host that can render any component passed to it. A
**reusable library** is built with the Angular CLI (`ng generate library`),
producing a separate publishable package with its own `public-api.ts` barrel
export, which can then be consumed by multiple apps (or published to npm/an
internal registry) instead of copy-pasting shared components.

**[⬆ Back to Top](#table-of-contents)**

## 22. What is a source map?

A file (`.map`) that maps positions in minified/bundled production JavaScript back
to the original TypeScript source — lines, columns, file names — so a stack trace
or breakpoint in production code can be inspected against the *actual* source you
wrote, instead of an unreadable, minified one-liner.

**[⬆ Back to Top](#table-of-contents)**

## 23. Newer Angular features: Signals, Standalone, SSR/Hydration, DestroyRef

- **Signals** — a fine-grained reactive primitive (`signal()`, `computed()`,
  `effect()`) that tracks exactly which parts of the UI depend on a value, so
  updates can skip Zone.js-driven full-tree change detection entirely.
- **Standalone components** — components/directives/pipes that declare their own
  imports directly, without needing an enclosing `NgModule` — the new default for
  Angular apps.
- **Server-Side Rendering (SSR) and Hydration** — SSR renders the initial HTML on
  the server for faster first paint and SEO; hydration then attaches Angular's
  event listeners/state to that existing DOM on the client **without re-rendering
  it from scratch**, which is what makes modern Angular SSR fast instead of just
  "render twice".
- **`DestroyRef`** — an injectable that lets any injectable code (not just
  components) register an `onDestroy` cleanup callback, useful for cleanup logic
  that lives outside a component class.
- **Required inputs** (`@Input({ required: true })`) — a compile-time guarantee
  that a binding must be supplied.
- **Directive Composition API** (`hostDirectives`) — apply another directive's
  behavior to a component/directive by composition instead of inheritance.
- **Binding route params to inputs** (`withComponentInputBinding()`) — route
  parameters are bound directly to matching `@Input()`s, no manual
  `ActivatedRoute` subscription needed for simple cases.

**[⬆ Back to Top](#table-of-contents)**

## 24. Build a reusable product-card component

```typescript
@Component({
  selector: 'app-product-card',
  standalone: true,
  template: `
    <div class="product-card">
      <h3>{{ product.name }}</h3>
      <img [src]="product.imageUrl" [alt]="product.name">
      <p>{{ product.price | currency }}</p>
    </div>
  `
})
export class ProductCardComponent {
  @Input({ required: true }) product!: { name: string; price: number; imageUrl: string };
}
```

**[⬆ Back to Top](#table-of-contents)**

## 25. Angular unit testing with Jasmine

Angular's CLI wires up **Jasmine** (assertions/spec structure) with **Karma**
(test runner) by default, plus `TestBed` to configure a testing module:

```typescript
describe('ProductCardComponent', () => {
  let fixture: ComponentFixture<ProductCardComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({ imports: [ProductCardComponent] });
    fixture = TestBed.createComponent(ProductCardComponent);
  });

  it('should display the product name', () => {
    fixture.componentInstance.product = { name: 'Widget', price: 10, imageUrl: '' };
    fixture.detectChanges();
    const el: HTMLElement = fixture.nativeElement;
    expect(el.querySelector('h3')?.textContent).toContain('Widget');
  });
});
```

Use `jasmine.createSpyObj` to mock injected services rather than pulling in real
HTTP calls/dependencies during a unit test.

**[⬆ Back to Top](#table-of-contents)**

## 26. JavaScript fundamentals: type inference, dates, closures, callbacks

- **Type inference** — TypeScript infers a variable's type from its initializer
  when no explicit type is given (`let x = 5` is inferred as `number`), still
  giving compile-time checking without writing the type out.
- **Dates** — `Date` in JavaScript has famously awkward ergonomics: months are
  **zero-indexed** (`0` = January), mutation methods (`setDate`, etc.) mutate in
  place rather than returning a new date, and time zone handling is easy to get
  wrong — most real apps reach for a library (`date-fns`, `Luxon`) rather than raw
  `Date`.
- **Closures/variable scope** — a function defined inside another function
  retains access to the outer function's variables even after the outer function
  has returned, which is both how private state is faked in plain JS and a common
  source of subtle bugs in loops (`var i` inside a `setTimeout` closure captures
  the same shared `i`, whereas `let i` gives each iteration its own binding).
- **Callbacks** — a function passed as an argument to be invoked later, typically
  when an asynchronous operation completes; Promises and `async`/`await` were
  introduced largely to avoid deeply nested "callback hell".

**[⬆ Back to Top](#table-of-contents)**

## 27. Implement a palindrome check without loops

```typescript
function isPalindrome(str: string): boolean {
  if (str.length <= 1) return true;
  if (str[0] !== str[str.length - 1]) return false;
  return isPalindrome(str.slice(1, -1)); // recursion instead of a loop
}
```

**[⬆ Back to Top](#table-of-contents)**

## 28. CSS Flexbox and Bootstrap grid basics

Flexbox lays out children of a `display: flex` container along a main axis:
`justify-content` controls alignment along that axis (`flex-start`, `center`,
`space-between`), `align-items` controls the cross axis, and `flex: 1` lets an
item grow to fill available space. Bootstrap's grid divides a row into **12
columns**; a class like `col-md-4` means "4 of 12 columns wide starting at the
`md` breakpoint and up", and columns automatically wrap to a new row once a row's
column widths exceed 12.

**[⬆ Back to Top](#table-of-contents)**

## 29. At a high level, how does a browser render a web page?

Parse HTML into the **DOM**, parse CSS into the **CSSOM**, combine them into a
**render tree** (only visible nodes), compute **layout** (geometry/position of
every element), then **paint** pixels to layers, and finally **composite** those
layers onto the screen. JavaScript execution can block this pipeline (which is
why blocking scripts are placed at the end of `<body>` or loaded with
`async`/`defer`), and any DOM/style change that affects layout triggers some or
all of layout → paint → composite to re-run.

**[⬆ Back to Top](#table-of-contents)**
