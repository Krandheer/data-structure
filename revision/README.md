# Revision kit

The kit was built from the ~220 problems in this repo. It's meant to get the patterns into long-term memory before the Hoomanely interview on 10 Nov 2026.

| File | What it's for | Time per day |
| --- | --- | --- |
| `quiz.py` | Recognition drill: read a problem, name the pattern. Spaced repetition. | 10 min |
| `PATTERNS.md` | Every pattern: hook, signals, **your own solved files**, trap | reading |
| `templates.py` | One verified template per pattern. Write them from memory, then run the file | 20–30 min |
| `PYTHON.md` | Python toolkit: heapq, bisect, `@cache`, and SortedList fallbacks | skim once, then as needed |

## Why this method works

Identifying the pattern is a **recognition** skill, and writing the code is a **recall** skill. Rereading solutions trains neither. These do:

1. **Retrieval, not rereading.** Run the quiz and write templates from a blank file. Struggling to recall is what makes it stick.
2. **Spacing.** `quiz.py` puts cards you got right further apart (1 → 3 → 7 → 14 days) and brings back missed cards the next session.
3. **Interleaving.** The quiz mixes patterns on purpose. In an interview, nobody tells you the chapter.
4. **Hooks.** Each pattern has one sentence in `PATTERNS.md`. Say the hook before you code.
5. **Your own problems.** Every card points to a file where you've already solved it. Your own past struggle is a stronger memory anchor than a new problem.
6. **Contrast pairs.** Most wrong guesses come from confusing two neighbouring patterns, so drill the difference:

| If you're torn between… | The deciding question |
| --- | --- |
| sliding window vs prefix sum + hashmap | Can values be negative? Then use the prefix sum. |
| monotonic stack vs monotonic deque | Do elements expire from the front because of a window? Then use the deque. |
| sort vs heap | Is the set fixed, or does it change while you work? A changing set needs a heap. |
| intervals sorted by start vs by end | Merging → start. Max non-overlapping → end. |
| BFS vs 0-1 BFS vs Dijkstra | All edge weights equal → BFS. Weights are only 0 or 1 → 0-1 BFS. Otherwise → Dijkstra. |
| DFS vs union-find | Is the graph fixed, or do edges arrive over time with queries in between? Edges arriving → union-find. |
| backtracking vs DP | List *all* solutions → backtracking. *Count* them or find the *best* → DP. |
| greedy vs DP | Can you prove "the locally best choice is safe" in one sentence? If not → DP. |
| binary search on index vs on answer | Is the input sorted, or is it "min/max value such that feasible"? The second is binary search on the answer. |

## The first 60 seconds of any interview problem

1. Restate the problem and confirm edge cases: empty input, duplicates, negatives, size of n.
2. **Constraints → target complexity** (the table at the top of `PATTERNS.md`).
3. "This looks like **X**, because **signal**." Say the hook.
4. Give the brute force in one line, then optimize with X.
5. Code, dry-run a small example, state time and space.

## Plan (Oct 29 – Nov 10)

This runs alongside the main prep in `~/projects/career-kb/hoomanely-r1.md`. Plan about 75 minutes of DSA a day.

**Every day:** `python revision/quiz.py` (10 min), then the block below:
- Write that day's template sections from memory in a scratch file.
- Compare with `templates.py` and run it.
- **Re-solve two of your own listed problems blind, with a 25-minute timer.**

| Date | Block (PATTERNS.md / templates.py §) | Fix-list item |
| --- | --- | --- |
| Oct 29 | Hashing, prefix sum + hashmap, two pointers, sliding window (§1–4) | — |
| Oct 30 | Monotonic stack and deque, binary search on the answer (§5–7) | `sliding_window_max.py`, `binary_search.py` |
| Oct 31 | Heap incl. two heaps and k-way merge, intervals, greedy (§8–10) | — |
| Nov 1 | Linked list, **LRU cache**, trees DFS and BFS (§11–13) | — |
| Nov 2 | Graph BFS (multi-source, 0-1), DFS, topological sort (§14–16) | — |
| Nov 3 | Union-find, Dijkstra, MST (§17–19) | `disjoint_set_graph.py`, `dijkstra_algo_graph.py` |
| Nov 4 | Backtracking, DP 1-D and grid (§20–21) | — |
| Nov 5 | DP knapsack, two strings, LIS (§21) | `dp/lis.py` |
| Nov 6 | DP interval, state machine, bitmask; trie, bits, Fenwick (§21–24) | — |
| Nov 7–9 | Mixed: `quiz.py -n 30`, two random mediums a day under a timer, one mock with Claude | — |
| Nov 10 | 10-minute quiz and reread the hooks. No new problems. | — |

Use `python revision/quiz.py --stats` to see your weakest families, and `-p <family>` to drill one (for example `-p heap`, `-p dp`).
