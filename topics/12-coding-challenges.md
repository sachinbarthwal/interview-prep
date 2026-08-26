# Coding & Algorithm Challenges

> Read the problem out loud, state your approach and its time/space complexity
> *before* you start typing, and only then write the code. Interviewers weight
> that narration as much as the working solution.

## Table of Contents

| No. | Question |
|-----|----------|
| 1 | [Design an LRU Cache with O(1) get/put](#1-design-an-lru-cache-with-o1-getput) |
| 2 | [Design an elevator system for two elevators](#2-design-an-elevator-system-for-two-elevators) |
| 3 | [Find the first repeating character in a string](#3-find-the-first-repeating-character-in-a-string) |
| 4 | [Find the missing element in an array](#4-find-the-missing-element-in-an-array) |
| 5 | [Find duplicate elements in an array](#5-find-duplicate-elements-in-an-array) |
| 6 | [Find elements in list1 not present in list2](#6-find-elements-in-list1-not-present-in-list2) |
| 7 | [Reverse the words in a sentence without a built-in reverse](#7-reverse-the-words-in-a-sentence-without-a-built-in-reverse) |
| 8 | [Sort a string by character frequency](#8-sort-a-string-by-character-frequency) |
| 9 | [Merge two sorted arrays](#9-merge-two-sorted-arrays) |
| 10 | [Calculate an order's total with discount and tax](#10-calculate-an-orders-total-with-discount-and-tax) |
| 11 | [Get the key with the max value from a Dictionary](#11-get-the-key-with-the-max-value-from-a-dictionary) |
| 12 | [Count all descendants of a hierarchical record set without recursion](#12-count-all-descendants-of-a-hierarchical-record-set-without-recursion) |
| 13 | [Check whether a number is prime](#13-check-whether-a-number-is-prime) |
| 14 | [Sum the digits of a number](#14-sum-the-digits-of-a-number) |
| 15 | [Time/space complexity — how to talk about Big-O in an interview](#15-timespace-complexity--how-to-talk-about-big-o-in-an-interview) |
| 16 | [How does a hash map reduce time complexity?](#16-how-does-a-hash-map-reduce-time-complexity) |
| 17 | [The "minimum cut" puzzle](#17-the-minimum-cut-puzzle) |
| 18 | [Reconciling data from two different sources](#18-reconciling-data-from-two-different-sources) |
| 19 | [Approach to planning a data migration](#19-approach-to-planning-a-data-migration) |

## 1. Design an LRU Cache with O(1) get/put

**Approach:** combine a `Dictionary` (O(1) key lookup) with a doubly linked list
(O(1) move-to-front / evict-from-back) — the dictionary maps a key straight to
its node in the list, so both operations avoid ever scanning the whole cache.
`LinkedList<T>` in .NET already gives O(1) node removal/insertion given a node
reference, which is exactly what's needed here.

```csharp
public class LRUCache
{
    private readonly int _capacity;
    private readonly Dictionary<int, LinkedListNode<(int Key, int Value)>> _map = new();
    private readonly LinkedList<(int Key, int Value)> _order = new(); // front = most recently used

    public LRUCache(int capacity) => _capacity = capacity;

    public int Get(int key)
    {
        if (!_map.TryGetValue(key, out var node)) return -1;
        _order.Remove(node);
        _order.AddFirst(node);
        return node.Value.Value;
    }

    public void Put(int key, int value)
    {
        if (_map.TryGetValue(key, out var existing))
        {
            _order.Remove(existing);
        }
        else if (_map.Count >= _capacity)
        {
            var lru = _order.Last!;
            _map.Remove(lru.Value.Key);
            _order.RemoveLast();
        }
        var newNode = new LinkedListNode<(int, int)>((key, value));
        _order.AddFirst(newNode);
        _map[key] = newNode;
    }
}
```

**Complexity:** O(1) for both `Get` and `Put`, O(capacity) space.

**[⬆ Back to Top](#table-of-contents)**

## 2. Design an elevator system for two elevators

**Approach:** model each elevator as an entity with a current floor, a direction,
and a **priority queue of requested stops** (min-heap when moving up, max-heap
when moving down, so the elevator naturally services stops in the order it
passes them rather than in the order they were requested). A dispatcher assigns
an incoming call to whichever elevator can service it with the least cost — the
simplest heuristic being "closest idle elevator, or the elevator already moving
toward that floor in the same direction," falling back to "least busy" if
neither elevator is a clean fit.

**Talk through, don't necessarily fully code:** the state machine per elevator
(idle / moving up / moving down), how a new request gets inserted into the
correct position in the queue based on current direction, and the dispatcher's
assignment heuristic. This question is testing system-design/data-structure
judgment more than a syntactically perfect implementation.

**[⬆ Back to Top](#table-of-contents)**

## 3. Find the first repeating character in a string

```csharp
public static char? FirstRepeatingChar(string s)
{
    var seen = new HashSet<char>();
    foreach (char c in s)
    {
        if (!seen.Add(c)) return c; // Add returns false if it was already present
    }
    return null;
}
```

**Complexity:** O(n) time, O(n) space — one pass with a hash set instead of a
nested loop (which would be O(n²)).

**[⬆ Back to Top](#table-of-contents)**

## 4. Find the missing element in an array

Given an array of `1..n` with exactly one number missing:

```csharp
public static int FindMissing(int[] arr, int n)
{
    int expectedSum = n * (n + 1) / 2;
    int actualSum = arr.Sum();
    return expectedSum - actualSum;
}
```

**Complexity:** O(n) time, O(1) space — the sum-formula trick avoids sorting or
a hash set entirely. (If duplicates can also occur, use a `HashSet` of `1..n`
and remove each seen value instead.)

**[⬆ Back to Top](#table-of-contents)**

## 5. Find duplicate elements in an array

```csharp
public static List<int> FindDuplicates(int[] arr)
{
    var seen = new HashSet<int>();
    var duplicates = new List<int>();
    foreach (int n in arr)
    {
        if (!seen.Add(n)) duplicates.Add(n);
    }
    return duplicates;
}
```

**Complexity:** O(n) time, O(n) space. (A sort-then-scan approach also works —
O(n log n) time, O(1) extra space if sorting in place — worth mentioning as the
trade-off if the interviewer asks for a lower-memory alternative.)

**[⬆ Back to Top](#table-of-contents)**

## 6. Find elements in list1 not present in list2

```csharp
var list2Set = new HashSet<int>(list2);
var onlyInList1 = list1.Where(x => !list2Set.Contains(x)).ToList();
// or simply: list1.Except(list2).ToList();
```

**Complexity:** O(n + m) using the hash set (or LINQ's `Except`, which does the
same thing internally) — much better than a nested-loop O(n·m) check.

**[⬆ Back to Top](#table-of-contents)**

## 7. Reverse the words in a sentence without a built-in reverse

```csharp
public static string ReverseWords(string sentence)
{
    if (string.IsNullOrWhiteSpace(sentence)) return sentence;
    var words = sentence.Split(' ');
    var result = new StringBuilder();
    for (int i = words.Length - 1; i >= 0; i--)
    {
        result.Append(words[i]);
        if (i > 0) result.Append(' ');
    }
    return result.ToString();
}
// "Hello world from OpenAI" -> "OpenAI from world Hello"
```

**[⬆ Back to Top](#table-of-contents)**

## 8. Sort a string by character frequency

```csharp
public static string SortByFrequency(string input)
{
    var freq = new Dictionary<char, int>();
    foreach (char c in input)
        freq[c] = freq.GetValueOrDefault(c) + 1;

    var sortedChars = freq.OrderByDescending(kv => kv.Value);
    return string.Concat(sortedChars.Select(kv => new string(kv.Key, kv.Value)));
}
// "aabbbccccddddd" -> "dddddccccbbbaa"
```

**Complexity:** O(n + k log k) where k is the number of distinct characters —
one pass to build frequencies, then sort just the distinct characters (not the
whole string).

**[⬆ Back to Top](#table-of-contents)**

## 9. Merge two sorted arrays

```csharp
public static int[] MergeSorted(int[] a, int[] b)
{
    int[] merged = new int[a.Length + b.Length];
    int i = 0, j = 0, k = 0;

    while (i < a.Length && j < b.Length)
        merged[k++] = a[i] <= b[j] ? a[i++] : b[j++];

    while (i < a.Length) merged[k++] = a[i++];
    while (j < b.Length) merged[k++] = b[j++];

    return merged;
}
```

**Complexity:** O(n + m) time, O(n + m) space — the classic merge step from
merge sort, reused directly since both inputs are already sorted.

**[⬆ Back to Top](#table-of-contents)**

## 10. Calculate an order's total with discount and tax

```csharp
public static decimal CalculateOrderTotal(List<Product> products, decimal discountPercent, decimal taxPercent)
{
    if (products == null || products.Count == 0) return 0m;

    decimal subtotal = products.Sum(p => p.Price * p.Quantity);
    decimal afterDiscount = subtotal - (subtotal * discountPercent / 100);
    decimal total = afterDiscount + (afterDiscount * taxPercent / 100);
    return total;
}

public class Product { public decimal Price { get; set; } public int Quantity { get; set; } }
```

Use `decimal`, not `float`/`double`, for money — floating point binary
representation introduces rounding errors that are unacceptable for currency.

**[⬆ Back to Top](#table-of-contents)**

## 11. Get the key with the max value from a Dictionary

```csharp
var maxPair = dictionary.OrderByDescending(kv => kv.Value).First();
// or, without sorting the whole thing (O(n) instead of O(n log n)):
var maxPair = dictionary.Aggregate((max, current) => current.Value > max.Value ? current : max);
```

The `Aggregate`/manual-loop version is worth mentioning as the more efficient
answer if the interviewer pushes on complexity — no need to fully sort when you
only want the single maximum.

**[⬆ Back to Top](#table-of-contents)**

## 12. Count all descendants of a hierarchical record set without recursion

Given a self-referencing table/list (`Id`, `ParentId`), count all descendants of
a node using an **iterative, queue-based breadth-first traversal** instead of
recursion (the constraint in the original question ruled out recursion *and* an
explicit stack, which points specifically at a queue-driven BFS):

```csharp
public static int CountDescendants(int rootId, List<(int Id, int? ParentId)> allNodes)
{
    var childrenLookup = allNodes
        .Where(n => n.ParentId.HasValue)
        .ToLookup(n => n.ParentId!.Value);

    var queue = new Queue<int>(childrenLookup[rootId].Select(n => n.Id));
    int count = 0;

    while (queue.Count > 0)
    {
        int current = queue.Dequeue();
        count++;
        foreach (var child in childrenLookup[current])
            queue.Enqueue(child.Id);
    }
    return count;
}
```

`ToLookup` groups children by `ParentId` once (O(n)), so each subsequent
lookup is O(1) instead of re-scanning the full list per node.

**[⬆ Back to Top](#table-of-contents)**

## 13. Check whether a number is prime

```csharp
public static bool IsPrime(int n)
{
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0) return false;
    }
    return true;
}
```

**Complexity:** O(√n) — you only need to check divisors up to the square root,
since any factor larger than √n would have a corresponding factor smaller than
it already checked.

**[⬆ Back to Top](#table-of-contents)**

## 14. Sum the digits of a number

```csharp
public static int SumDigits(int number)
{
    int sum = 0;
    number = Math.Abs(number);
    while (number > 0)
    {
        sum += number % 10;
        number /= 10;
    }
    return sum;
}
```

**[⬆ Back to Top](#table-of-contents)**

## 15. Time/space complexity — how to talk about Big-O in an interview

State it in one sentence right after you finish coding, without being prompted:
"this runs in O(n) time because it's a single pass, and O(n) space for the hash
set." If you optimized from a naive approach, say what you traded — e.g. "the
brute-force nested loop is O(n²); using a hash set drops it to O(n) time at the
cost of O(n) extra space." That trade-off framing is usually worth more to the
interviewer than reciting the final complexity alone.

**[⬆ Back to Top](#table-of-contents)**

## 16. How does a hash map reduce time complexity?

A linear scan checking "have I seen this value before" against a list is O(n)
*per check*, making an overall duplicate-detection loop O(n²). A hash map/set
computes a hash of the key and jumps near-directly to its bucket, making
"have I seen this" an O(1) average-case check — so the same duplicate-detection
problem drops to O(n) overall: one O(1) check per element instead of an O(n)
scan per element. The trade-off is O(n) extra memory for the hash structure
itself.

**[⬆ Back to Top](#table-of-contents)**

## 17. The "minimum cut" puzzle

A classic algorithmic-thinking puzzle (see
[GeeksforGeeks Puzzle #31](https://www.geeksforgeeks.org/puzzle-31-minimum-cut-puzzle/)
for the exact statement and answer) — these show up less to test a memorized
algorithm and more to see how you break an unfamiliar problem into smaller
pieces out loud. General approach for this style of puzzle: restate the problem
in your own words, work a tiny concrete example by hand before generalizing,
and state your reasoning as you go rather than going silent while you think.

**[⬆ Back to Top](#table-of-contents)**

## 18. Reconciling data from two different sources

When combining data pulled from, say, a REST API and SQL Server: pick a common
key both sources agree on, load both sides into a keyed structure (a
`Dictionary` keyed by that ID is usually the simplest correct approach), then
join in memory — being explicit about what happens on a mismatch (present in one
source but not the other), and about which source wins if a field conflicts
between them. For anything beyond a one-off script, prefer resolving this
mismatch at the design level (a canonical source of truth, or an ETL step that
reconciles and stores a merged view) rather than reconciling ad hoc on every
read.

**[⬆ Back to Top](#table-of-contents)**

## 19. Approach to planning a data migration

1. **Audit the source data** — volume, quality issues, edge cases (nulls,
   duplicates, orphaned foreign keys) — before writing any migration code.
2. **Design the target schema** and an explicit field-by-field mapping,
   including how to handle fields that don't exist on one side.
3. **Migrate in batches**, not one giant transaction, with the ability to resume
   from a checkpoint if it fails partway.
4. **Run it against a staging environment first**, and reconcile row counts/spot
   checks against the source before touching production.
5. **Plan a rollback path** and a cutover window, and decide up front whether the
   migration needs to support running twice safely (idempotency) in case it has
   to be re-run.
6. **Validate post-migration** with automated checks, not just "it looked right
   during a manual spot check."

**[⬆ Back to Top](#table-of-contents)**
