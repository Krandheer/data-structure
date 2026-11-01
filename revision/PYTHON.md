# Python for DSA interviews

You're on Python 3.12. Everything here is in the standard library unless marked otherwise.

## The imports to type at the top of every solution

```python
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify, heappushpop, nlargest, nsmallest
from bisect import bisect_left, bisect_right, insort
from functools import cache
from itertools import accumulate, combinations, permutations, product, pairwise
import math
```

## collections

| Need | Write |
| --- | --- |
| frequency map | `freq = Counter(s)`; `freq.most_common(k)`; a missing key gives 0, no KeyError |
| multiset subset check | `Counter(a) <= Counter(b)` (3.10+); `c1 - c2` drops counts ≤ 0 |
| adjacency list | `g = defaultdict(list); g[u].append(v)` |
| group by key | `groups = defaultdict(list); groups[key].append(x)` |
| queue for BFS | `q = deque([start]); q.popleft()`. **Never `list.pop(0)`, it's O(n)** |
| deque for a window | `dq.append`, `dq.pop`, `dq.popleft`, `dq[0]`, `dq[-1]` |
| LRU | `OrderedDict`: `move_to_end(k)`, `popitem(last=False)` |

Trap: a `Counter` keeps a key at 0 after `-=`. If you rely on `len(freq)`, `del` the key when it reaches 0.

## heapq: only a min-heap

```python
heap = []
heappush(heap, (dist, node))      # tuples compare left to right
d, u = heappop(heap)
heap[0]                           # peek at the min
heapify(arr)                      # O(n), in place
heappush(heap, -x); -heap[0]      # max-heap: negate
heappushpop(heap, x)              # push then pop, faster than doing both
nlargest(k, nums, key=...)        # fine for one-off top-k
```

- **Tiebreak** when items aren't comparable: `(priority, counter, item)` or `(priority, i, item)`.
- **No decrease-key.** Push the new value and skip stale entries when you pop them (Dijkstra).
- **No delete.** Use lazy deletion: mark the item dead in a Counter and discard it when it reaches the top (`templates.py LazyMinHeap`).

## bisect: binary search on a sorted list

```python
i = bisect_left(a, x)    # first index with a[i] >= x   (count of < x)
j = bisect_right(a, x)   # first index with a[j] >  x   (count of <= x)
j - i                    # how many times x appears
bisect_right(a, x) - 1   # last index with a[i] <= x ("floor")
insort(a, x)             # insert keeping the list sorted: O(n), but fast memmove
bisect_left(a, x, key=lambda p: p[0])   # 3.10+, search by field; x is a key value
```

To remember the difference: **left** lands on the *first* x, **right** lands *just after the last* x.

## SortedList when the package isn't installed

LeetCode has `sortedcontainers` preinstalled. **HackerRank, CoderPad and a company's own editor might not**, and your local env doesn't either (`pip install sortedcontainers` if you want it). In an interview:

1. **Ask:** "Can I use `sortedcontainers`?" Many interviewers say yes.
2. **If not, pick a fallback by what you need:**

| You need | Use |
| --- | --- |
| min or max with removals | **heap + lazy deletion** |
| a running median | **two heaps** (`templates.py MedianFinder`), with lazy deletion if elements leave a window |
| a sorted container for n ≤ ~10⁵ | **`insort` + `bisect` on a plain list**. Insert is O(n), but it's a C memmove and fast in practice. Say the trade-off out loud. |
| "how many < x so far", rank, k-th smallest | **Fenwick tree over compressed values** (`templates.py §24`) |
| range min or max with updates | segment tree |
| "nearest greater key" (TreeMap floor/ceiling) | `bisect` on a sorted list; if you also delete, `insort` / `del a[i]` |

Saying "in production I'd use a balanced BST or `SortedList`; here's an O(log n) Fenwick version" shows you know the trade-off, and interviewers look for that at SDE2.

## Recursion and memoization

```python
import sys
sys.setrecursionlimit(10**6)     # Python's default is 1000, too low for 1e5-node DFS

@cache                           # = lru_cache(maxsize=None)
def dp(i, j): ...

dp.cache_clear()                 # between test cases, if dp is defined at module level
```

- Arguments must be hashable, so pass a `tuple`, not a list. A bitmask int is ideal.
- Define `dp` as a **nested function** so it captures the input and its cache is fresh for each call.
- For very deep recursion (n ≈ 10⁵), switch to bottom-up or an explicit stack.

## Sorting

```python
arr.sort(key=lambda x: (x[1], -x[0]))   # by second ascending, then first descending
sorted(words, key=len)
from functools import cmp_to_key         # custom comparison ("largest number")
nums.sort(key=cmp_to_key(lambda a, b: -1 if a + b > b + a else 1))
```

Sorting is stable, so you can sort by the secondary key first and then by the primary.

## Small idioms that save time

| Task | Idiom |
| --- | --- |
| infinity | `math.inf`, `-math.inf` |
| 2-D grid | `[[0] * cols for _ in range(rows)]`. **Never `[[0] * cols] * rows`**: every row is the same list |
| grid neighbours | `for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):` |
| in bounds | `0 <= r < rows and 0 <= c < cols` |
| prefix sums | `pre = [0, *accumulate(nums)]` |
| adjacent pairs | `for a, b in pairwise(nums):` (3.10+) |
| index and value | `for i, x in enumerate(nums):` |
| two lists together | `for a, b in zip(x, y):` |
| char to index | `ord(c) - ord('a')`; back with `chr(i + ord('a'))` |
| join a string | build a list, then `''.join(parts)`. Never `+=` in a loop |
| reverse | `s[::-1]`; `reversed(lst)` |
| bits | `x.bit_count()`, `x.bit_length()`, `x & -x`, `1 << k`, `mask >> i & 1` |
| maths | `math.gcd`, `math.lcm`, `math.comb(n, k)`, `math.isqrt(n)`, `pow(a, b, mod)`, `divmod(a, b)` |
| ceil division | `-(-a // b)` or `(a + b - 1) // b` |
| swap | `a, b = b, a` |
| copy the path in backtracking | `out.append(path[:])` |

## Mistakes that cost time in an interview

1. `[[0]*n]*m` aliasing, which gives you a shared row.
2. `list.pop(0)` in BFS. Use a `deque`.
3. A mutable default argument, `def f(x, memo={})`, keeps its value between test cases.
4. Comparing items inside a heap tuple raises `TypeError`. Add a tiebreaker.
5. Hitting the recursion limit on large inputs.
6. Negative division: `-7 // 2 == -4`, which floors and doesn't truncate. Use `int(a / b)` to truncate.
7. Strings are immutable. Convert to `list(s)` before editing in place.
