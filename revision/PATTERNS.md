# Pattern map

This covers every pattern in this repo: about 220 problems across the root files, `dp/`, `graph/`, `leetcode_daily.py` and `leetcode_daily2.py`. Each pattern has:

- **Hook**: one sentence to remember. If you remember only the hook, you can rebuild the rest.
- **Signals**: words or constraints in the problem that should make you think of it.
- **Yours**: problems you already solved. Reopen them; they're more memorable than new ones.
- **Trap**: the mistake that costs time in an interview.
- **Code**: the matching section number in `templates.py`.

Problems in the daily files are listed as `file:line function`.

---

## Step 0. How to identify the pattern in 60 seconds

Ask these in order. The first "yes" is usually the answer.

**1. What do the constraints allow?**

| n is about | Allowed complexity | Usually means |
| --- | --- | --- |
| ≤ 12 | O(n!) | permutations, backtracking |
| ≤ 20 | O(2ⁿ · n) | subsets, bitmask DP |
| ≤ 500 | O(n³) | interval DP, Floyd–Warshall |
| ≤ 5,000 | O(n²) | 2-D DP, all pairs |
| ≤ 10⁵–10⁶ | O(n log n) or O(n) | sort, heap, binary search, two pointers, window, prefix sums, monotonic stack |
| ≤ 10⁹ (a value, not a length) | O(log V) | binary search on the answer, math |

**2. What is the question asking for?**

| The problem says… | Think |
| --- | --- |
| "contiguous subarray / substring", longest or shortest with a condition | Sliding window (positives) or prefix sum + hashmap (negatives) |
| "subarray sum equals k", "count subarrays with sum…" | Prefix sum + hashmap |
| "many range updates, then read" | Difference array |
| "next greater / smaller", "previous smaller", "how many days until" | Monotonic stack |
| "max / min of every window" | Monotonic deque |
| "sorted array", "find position", "first / last index" | Binary search |
| "minimize the maximum", "maximize the minimum", "minimum speed / capacity / time such that" | Binary search on the answer |
| "k largest / smallest / most frequent", "k-th" | Heap of size k |
| "repeatedly take the best one", "schedule", "rooms", "merge k sorted" | Heap |
| intervals, meetings, events, "overlap" | Sort by start (merging) or by end (picking max non-overlapping), plus a heap for rooms |
| "pair / triplet with sum" on sorted data, "in place" | Two pointers |
| "shortest path / min steps", unweighted grid or graph | BFS |
| weights 0 or 1 | 0-1 BFS |
| non-negative weights | Dijkstra |
| "connected", "islands", "regions", "can reach" | DFS / BFS / union-find |
| "dependencies", "order", "prerequisites" | Topological sort |
| "edges added one by one", "are x and y connected" | Union-find |
| "all combinations / permutations / subsets", "generate all" | Backtracking |
| "number of ways", "min / max cost", choices that overlap | DP |
| "prefix", "dictionary of words", "max XOR" | Trie |
| "range sum / min / max with updates" | Fenwick or segment tree |
| "each element appears twice except", XOR, AND, OR | Bits |

**3. If you're still stuck:** write the brute force, find the repeated work, and ask what data structure removes it. That usually points to a pattern: a hashmap, heap, stack or memo.

---

## A. Arrays and strings

### 1. Hashing and counting — `templates.py §1`
- **Hook:** "Have I seen what I need?" Store what you've seen, and look up the *complement*.
- **Signals:** pairs, duplicates, anagrams, frequency, "count pairs with…", O(n) required.
- **Key trick:** turn the condition into a key. `j - i == nums[j] - nums[i]` becomes "same `nums[i] - i`" (countBadPairs). An anagram becomes "same sorted tuple". `a*b == c*d` becomes "count products".
- **Yours:** `anagram.py`, `group_of_anagrams.py`, `check_duplicate.py`, `leetcodes.py:5 longestConsecutive`, `leetcode_daily.py:1014 countBadPairs`, `:987 tupleSameProduct`, `:500 wordSubsets`, `:527 canConstruct`, `:590 findThePrefixCommonArray`, `:693 firstCompleteIndex`, `:1543 FindSumPairs`, `:1566 countKDifference`, `:2117 countTrapezoids`, `leetcode_daily2.py:375 findDuplicates` (index marking), `:183 minMirrorPairDistance`.
- **Trap:** a list isn't hashable. Use `tuple(...)` as the key.

### 2. Prefix sum and difference array — `§2`
- **Hook:** "a range is the difference of two prefixes." `sum(l..r) = pre[r+1] - pre[l]`. For *range updates*, mark the start and the end+1, then take a running sum.
- **Signals:** many range queries; "subarray sum equals k" (with negatives); left vs right split; many range updates followed by one read.
- **Yours:** `leetcode_daily.py:67 is_array_special`, `:342 maxScore`, `:363 vowelStrings`, `:389 ways_to_split_array`, `:456 shiftingLetters` (difference array), `:475 minOperations`, `:722 gridGame`, `:1201 minZeroArray` (difference array + binary search), `product_of_array_except_self.py`, `get_max_length.py`, `leetcode_daily2.py:358 distance`, `:554 maxValue` (prefix max / suffix min).
- **Gap:** you haven't drilled the **prefix sum + hashmap** version (`{0: 1}` seed). It's very common. See `§2 subarray_sum_equals_k`.
- **Trap:** forgetting to seed `{0: 1}` misses subarrays that start at index 0.

### 3. Two pointers — `§3`
- **Hook:** "sorted, or monotone? Then move the pointer that can only improve things."
- **Signals:** sorted input, pair or triplet sum, in-place, partitioning, merging two sorted arrays, palindromes.
- **Yours:** `container_with_most_water.py`, `find_triplet.py`, `trap_water.py`, `movezeros_leet.py`, `remove_duplicates*.py`, `sort_colors_s5.py` (Dutch flag), `merge_sorted_arrays_s9.py`, `reverse_vowels_of_string.py`, `dp/is_subsequence.py`, `leetcode_daily.py:1417 num_subsequences`, `:1595 countFairPairs`, `:1741 matchPlayersAndTrainers`, `:1758 isLongPressedName`, `:1804 maximizeGreatness`, `:1818 maxProfitAssignment`, `leetcode_daily2.py:306 maxDistance1`.
- **Trap:** in 3-sum, skip duplicates *after* recording an answer, not before.

### 4. Sliding window — `§4`
- **Hook:** "grow right always, shrink left while invalid, record when valid."
- **Signals:** contiguous; longest or shortest; "at most k"; all values non-negative.
- **Key tricks:**
  - Fixed size k: add `i`, remove `i - k`.
  - **Exactly k = atMost(k) − atMost(k−1).**
  - Counting subarrays: add `r - l + 1` at each `r`.
- **Yours:** `longest_substring_without_repchar.py`, `minimum_size_subarry_sum.py`, `find_max_avg.py`, `power_of_ksize_subarray.py`, `leetcode_2461.py`, `defuse_bomb_leetcode.py`, `leetcodes.py:28, :45 characterReplacement, :63 check_inclusion`, `leetcode_daily.py:1185 numberOfSubstrings`, `:1290 longestNiceSubarray` (OR mask), `:1662 maxFreeTime`, `:2044 longestSubarray`, `leetcode_daily2.py:114 minimumDifference`, `:857 maximumLengthSubstring`.
- **Trap:** negative numbers break the "shrink makes it smaller" rule. Switch to prefix sum + hashmap, or a monotonic deque.

### 5. Monotonic stack — `§5`
- **Hook:** "the stack holds the elements still waiting for their answer." When a new element answers them, pop.
- **Signals:** next or previous greater or smaller; histogram; "span"; "how far to the left can I extend"; removing characters to get the smallest string.
- **Yours:** `daily_temperature_leetcode.py`, `monotonic_increasing_stack.py`, `largest_rectangle_area.py`, `mock_q.py:58 find_next_greater`, `leetcode_daily.py:220 final_prices`, `:278 leftmost_building_queries`, `leetcode_daily2.py:52 maximalRectangle` (histogram per row), plain stacks: `valid_parenthesis.py`, `leetcode_daily.py:1030 clearDigits`, `:1045 removeOccurrences`, `:1910 maximumGain`.
- **Trap:** store *indices*, not values. You almost always need the distance.

### 6. Monotonic deque — `§6`
- **Hook:** "a stack that also expires from the front."
- **Signals:** max or min of each window; "max − min ≤ k" in a window; shortest subarray with sum ≥ k when there are negatives.
- **Yours:** `shortest_subarray_with_sumk.py`, `leetcode_daily.py:127 continuous_subarrays`.
- **Fix:** `sliding_window_max.py` is O(n·k) because it calls `max(nums[i:j])`. Rewrite it from `§6` without looking.

### 7. Binary search — `§7`
- **Hook:** "find the boundary where `ok()` flips from False to True." One template, `first_true`, covers every case.
- **Signals:** sorted input; rotated array; "first or last position"; **binary search on the answer**: "minimize the max", "minimum capacity / speed / days", "maximum candies per child". If you can check a guess in O(n), you can binary search for it.
- **Yours:** `binary_search*.py`, `first_and_last_position.py`, `rotated_sorted_array.py`, `binary_search_2d_matrix_s13.py`, `leetcode_daily.py:1221 maximumCandies`, `:1238 minCapability`, `:1262 repairCars`, `:1840 successfulPairs`, `leetcode_daily2.py:316 search` (rotated with duplicates), `:412 kthRemainingInteger`, `:678 minimumEffort`.
- **Fix:** `binary_search.py recursive_binary_search` slices the list, which makes it O(n). Pass `lo` and `hi` instead.
- **Trap:** before writing the loop, decide whether you want the *first true* or the *last true*, then check it on a 2-element array.

### 8. Kadane and running best
- **Hook:** "extend the current run, or start fresh here."
- **Yours:** `kadanes'_algo_s4.py`, `max_subarray.py`, `maximum_product_subarray.py` (track both min and max), `max_sum_circular_subarray.py` (total − min subarray), `best_sight_seeing_pair.py`, `best_time_to_buy_sell_stock.py`.

---

## B. Heaps, intervals, greedy

### 9. Heap — `§8`
- **Hook:** "I keep needing the current best, and the set keeps changing."
- **Signals:**
  - top k, k-th largest
  - "repeatedly pick the max or min and modify it"
  - merging k sorted lists or streams
  - a running median (two heaps)
  - scheduling with "next free"
- **Yours:** `kth_largest_elemnent.py`, `minheap.py`, `top_k_frequent_elements.py`, `reorganise_string.py`, `nth_ugli_number.py`, `leetcode_daily.py:98 pick_gifts`, `:109 find_score`, `:147 max_average_ratio` (heap by marginal gain), `:173 get_final_state`, `:190 repeat_limited_string`, `:1052 minOperations_1`, `:1411 max_subsequence`, `:669 trapRainWater` (heap expanding from the boundary).
- **Gap:** you haven't done **two heaps (median)** or **k-way merge** yet. Both are in `§8`. K-way merge also fits Hoomanely's streams of sensor readings.
- **Trap:** Python only has a min-heap, so push `-x` to get a max-heap. Add a tiebreaker to tuples, `(priority, i, item)`, so Python never has to compare the items themselves.

### 10. Intervals and sweep line — `§9`
- **Hook:** "sort first." Sort **by start** to merge. Sort **by end** to keep the most non-overlapping intervals. Use a **heap of end times** to count rooms.
- **Signals:** intervals, meetings, events, booking, "overlap", "free time".
- **Yours:** `merge_intervals_s8.py`, `mock_q.py:42 number_of_arrows`, `leetcode_daily.py:42 max_two_events`, `:1618 maxEvents`, `:1641 maxValue` (DP + bisect), `:1662 maxFreeTime`, `:1683 mostBooked` (two heaps).
- **Trap:** decide whether `[1,2]` and `[2,3]` overlap. That decides `<` vs `<=`. Say it out loud.

### 11. Greedy
- **Hook:** "sort, then make the locally best choice. Justify it with 'swapping two choices never helps'."
- **Yours:** `can_jump.py`, `min_jump.py` (BFS by levels), `can_place_flowers.py`, `increasing_triplet_subsequence.py`, `leetcode_daily.py:235 max_chunks_to_sorted`, `:547 canBeValid` (two passes), `:796 lexicographicallySmallestArray`, `:1306 partitionArray`, `leetcode_daily2.py:74 maximizeSquareHoleArea`, `:726 splitNum`, `:749 maxIceCream`.
- **Trap:** greedy without a proof. If you can't justify it in one sentence, test it on a tricky case or switch to DP.

---

## C. Linked lists, trees, design

### 12. Linked list — `§11`
- **Hook:** "a dummy head node; fast and slow pointers; reverse with prev / cur / next."
- **Yours:** `linked_list.py`, `doubly_linked_list.py`, `circular_linked_list.py`, `ll_palindrome.py` (middle + reverse), `rotate_list.py`, `stack_using_linked_list.py`.
- **Gap:** cycle detection with Floyd, and **LRU cache** (it comes up a lot at SDE2). Both are in `§11`.

### 13. Tree DFS — `§12`
- **Hook:** "what does each child need to *return* to its parent?" Update a global best inside, return a single value up.
- **Signals:** height, diameter, max path sum, LCA, "subtree with…", validating a BST, "split the tree into components".
- **Yours:** `binary_tree_traversal.py`, `diameter_binary_tree.py`, `binary_tree_max_path_sum.py`, `maximum_depth_of_binary_tree_leetcode.py`, `lowest_common_ancestor.py`, `child_sum_property.py`, `subtree_size.py`, `construct_bt_from_pre_ino_traversal.py`, `bst*.py`, `delete_node_bst.py`, `bst_serialise_and_deserialize.py`, `leetcode_daily.py:248 max_k_divisible_components`, `leetcode_daily2.py:16 subtreeWithAllDeepest`.
- **Trap:** a path *through* a node (left + right) is different from a path *returned up* (1 + max). That's the diameter and max-path-sum idea.

### 14. Tree BFS — `§13`
- **Hook:** `for _ in range(len(q))` processes exactly one level.
- **Yours:** `vertical_tree_traversal.py`, level order in `binary_tree_traversal.py`.

---

## D. Graphs

### 15. BFS: shortest path in unweighted graphs and grids — `§14`
- **Hook:** "a level is one step. For multiple sources, push them all at distance 0."
- **Signals:** min steps or moves; a grid; spreading (rot, fire); a puzzle state (BFS over states as strings); weights of 0 or 1 → **0-1 BFS with a deque**.
- **Yours:** `graph/bfs.py`, `bfs_on_grid.py`, `rotten_oranges_graph.py`, `graph/chess_knight_graph.py`, `sliding_puzzle.py`, `jungle_run.py`, `minimum_obstacle_removal_grid.py` (0-1 BFS), `graph/shortest_path_after_road_addition.py`, `leetcode_daily.py:738 highestPeak` (multi-source), `:643 minCost2` (0-1 BFS), `:891 magnificentSets`, `leetcode_daily2.py:579 minJumps`, `:701 canReach`, `minimum_diameter_after_merge.py` and `graph/diameter_of_graph.py` (two BFS passes for the tree diameter).
- **Trap:** mark a cell visited **when you push it**, not when you pop it. Otherwise the same cell gets queued many times.

### 16. DFS: components, flood fill, cycles — `§15`
- **Hook:** "three colors for a directed cycle: white, gray (on the current path), black (done)."
- **Yours:** `graph/dfs.py`, `dfs_on_grid.py`, `counting_rooms_graph.py`, `island_perimeter.py`, `surrounded_regions_2dmat.py` (start from the border), `grid_travel_graph.py`, `graph/cycle_detection_graph.py`, `graph/cycle_detection_directed_graph.py`, `graph/bipartite_graph.py`, `graph/in_out_time_graph.py`, `leetcode_daily.py:778 eventualSafeNodes`, `:814 maximumInvitations`.
- **Trap:** Python's recursion limit is 1000. On a 10⁵-node graph, use an iterative stack or `sys.setrecursionlimit(10**6)`.

### 17. Topological sort — `§16`
- **Hook:** "repeatedly take the nodes with no incoming edges. If some are left over, there's a cycle."
- **Signals:** prerequisites, build order, "is a before b", scheduling a DAG.
- **Yours:** `graph/topological_sort_graph.py`, `leetcode_daily.py:865 checkIfPrerequisite` (your note says Kahn would be faster; it would).

### 18. Union-find — `§17`
- **Hook:** "every node points toward a leader. Two nodes are connected if they have the same leader."
- **Signals:** dynamic connectivity, edges arriving over time, "number of components", "redundant edge", Kruskal.
- **Yours:** `graph/disjoint_set_graph.py`, `leetcode_daily2.py:804 pathExistenceQueries`.
- **Fix:** your `find` has **no path compression**, so one find can take O(n). Use the `§17` class with path halving and union by size.

### 19. Weighted shortest paths and MST — `§18–19`
- **Hook:** Dijkstra is BFS with a heap, and it **skips stale entries**. Bellman–Ford relaxes every edge n−1 times and handles negative weights. Floyd–Warshall tries every middle node k, for small n.
- **Yours:** `graph/dijkstra_algo_graph.py`, `graph/single_source_shortest_path_graph.py`, `graph/floyd_warshall_algo_graph.py`, `minimum_time_to_visit_cell.py`, `mst_graph.py`, `prim's_algo_graph.py`, `leetcode_daily.py:615 minCost`.
- **Fix:** your Dijkstra has no `if d > dist[u]: continue`. It's still correct, but it does extra work. Interviewers look for that line.

### 20. Advanced graph topics (low priority for this interview)
- Bridges and articulation points (`finding_bridge_graph.py`, `articulation_point_graph.py`), Tarjan and SCC (`tarjons_algo_graph.py`, `strongly_connected_component.py`), Euler path (`valid_arrangements_pair.py`). Know what each one is for and skip re-coding them.

---

## E. Recursion, backtracking, DP

### 21. Backtracking — `§20`
- **Hook:** "choose, explore, un-choose." Append, recurse, pop. Save a **copy** of the path.
- **Signals:** "all" combinations, permutations, subsets or partitions; n ≤ 15–20; sudoku or N-queens.
- **Key trick:** to skip duplicates, sort first, then `if i > start and a[i] == a[i-1]: continue`.
- **Yours:** `permutations.py`, `powerset.py`, `subsequences.py`, `generate_parenthesis.py`, `letter_com_phone_num.py`, `sudoku_solver.py`, `leetcode_daily.py:9 find_minimumTime`, `:1067 punishmentNumber`, `:1113 numTilePossibilities`, `:1121 smallestNumber`, `:1149 getHappyString`, `:1167 findDifferentBinaryString`, `leetcode_daily2.py:230 combinationSum`, `:253 combinationSum2`.

### 22. Dynamic programming — `§21`
**Hook for all DP:** "write the recursion with choices, find the parameters that change (that's the state), then add `@cache`." Only go bottom-up if they ask, or if memory or the recursion limit matters.

Six families. Name the family first, and the state follows from it:

| Family | State | Your files |
| --- | --- | --- |
| **1-D linear** (take or skip, ways to reach) | `i` | `dp/fib.py`, `climb_stairs_leetcode.py`, `dp/house_robber*.py`, `dp/min_cost_climbing_stairs.py`, `decode_ways.py`, `delete_earn.py`, `word_break.py`, `dp/min_cost_tickets.py` |
| **Grid** | `(r, c)` | `dp/gridtravel.py`, `dp/min_path_sum*.py`, `unique_path_with_obstacles.py`, `dp/min_falling_path_*.py`, `dp/count_squares.py`, `leetcode_contest.py`, `leetcode_daily2.py:531 maxPathScore` (adds `k`) |
| **Knapsack / subset sum** (go down over capacity for 0/1, up for unbounded) | `(i, remaining)` | `dp/knapsack_0_1.py`, `dp/minimum_coin.py`, `dp/rod_cutting.py`, `dp/partition_in_2_sequence_of_equal_sum.py`, `dp/dice_target_value.py`, `leetcode_daily.py:304 find_target_sum_ways` |
| **Two strings** | `(i, j)` | `dp/longest_common_subsequence.py`, `dp/edit_distance.py`, `dp/shortest_common_supersequence.py`, `longest_palindromic_subsequence.py` (LCS with the reverse), `minimum_insertion_palindrome.py`, `leetcode_daily2.py:33 minimumDeleteSum` |
| **LIS** | `i` (+ prev) | `dp/lis.py`, `largest_divisible_subset.py`, `minimum_no_of_deletion_to_get_sorted_line.py` |
| **Interval / partition** (try every split k) | `(i, j)` | `dp/matrix_chain_multiplication.py`, `dp/minimum_cost_to_cut_rod.py`, `dp/palindrome_partitioning.py`, `boolean_expression_true.py`, `unique_binary_search_trees.py` |
| *Variant:* **state machine** | `(i, holding, k)` | `dp/best_time_to_buy_sell_stock2.py`, `dp/best_time_to_buy_stocks3.py`, `stocks4.py` |
| *Variant:* **bitmask / multi-dimensional** | `(i, mask)` | `leetcode_daily.py:1713 earliestAndLatest`, `leetcode_daily2.py:127 minimumDistance` (two fingers) |

- **Gap:** `dp/lis.py` only has the O(n²) version. Learn the O(n log n) version with `bisect` (`§21 lis_length`). It takes five lines.
- **Python habit:** you pass `dp` dicts around by hand (`leetcode_daily.py:324`). Use `@cache` on a nested function instead. It's less code to write under pressure.

---

## F. Specialized

| Pattern | Hook | Yours | Code |
| --- | --- | --- | --- |
| **Trie** | a dict of dicts with an end marker; for max XOR, walk the opposite bit | `trie.py`, `max_xor_trie.py` | §22 |
| **Bits** | `x & (x-1)` drops the lowest set bit; XOR cancels pairs; track the last position of each bit | `bit_manipulation_leet.py`, `is_power_2.py`, `get_xor.py`, `divide_two_int.py`, `leetcode_daily.py:604 doesValidArrayExist`, `:1981 smallestSubarrays`, `:1290`, `leetcode_daily2.py:102 minBitwiseArray` | §23 |
| **Fenwick / segment tree** | range query + point update in O(log n) | `build_segment_tree.py`, `leetcode_daily.py:2002–2032 numOfUnplacedFruits` | §24 |
| **Math** | sieve, gcd, `pow(a, b, mod)` | `get_prime.py`, `factor.py`, `greatest_common_divisor_of_string.py`, `nth_ugli_number.py`, `leetcode_daily.py:1384 kMirror`, `:2136 sumFourDivisors` | §25 |
| **Matrix simulation** | layers, and swapping row and column indices | `rotate_matrix_by_90_degree_in_place.py`, `set_matrix_zero.py`, `transpose_matrix.py`, `complex_number_spiraling.py`, `leetcode_daily2.py:642 rotateGrid` | — |
| **Array tricks** | next permutation: find the pivot from the right, swap, reverse the suffix | `next_permutations_s3.py`, `rotate_array.py` | — |

Sorting algorithms (`bubble_sort.py`, `merge_sort.py`, `quicksort.py`, …): know merge sort and the quicksort partition step by heart. Merge sort also counts inversions.

Not DSA, so skip for this interview: `async_experiment.py`, `contextManager.py`, `decorator.py`, `multhreading_mulprocessing.py`, `namedtuple.py`, the file-moving scripts.

---

## Fix list, from reading your code

1. `graph/dijkstra_algo_graph.py`: add the stale-entry skip.
2. `graph/disjoint_set_graph.py`: add path compression.
3. `sliding_window_max.py`: O(n·k), so rewrite it with a deque.
4. `binary_search.py`: the recursive version slices the list, so pass indices instead.
5. `dp/lis.py`: add the O(n log n) version.

Each fix doubles as a "write it from memory" drill.
