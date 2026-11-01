"""
Pattern-recognition drill with spaced repetition (Leitner boxes).

    python revision/quiz.py            # 15 due cards
    python revision/quiz.py -n 25      # more cards
    python revision/quiz.py -p heap    # only cards whose pattern contains "heap"
    python revision/quiz.py --stats    # progress per pattern

For each card: read the problem, SAY the pattern and the signal that gave it
away, press Enter, then grade yourself. Wrong -> box 1 (see it again next
session). Right -> next box (seen again after 1, 3, 7, 14 days).
Do not code during the drill. Recognition is the skill being trained.
"""

import argparse
import json
import random
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

STATE_FILE = Path(__file__).with_name(".quiz_state.json")
BOX_DAYS = {1: 0, 2: 1, 3: 3, 4: 7, 5: 14}

# (problem statement, pattern, why: the signal -> the idea, where you solved it)
CARDS = [
    ("Count contiguous subarrays whose sum equals k. Values can be negative.",
     "prefix sum + hashmap", "'subarray sum = k' + negatives: sliding window breaks; count earlier prefixes equal to total-k, seed {0:1}", "new"),
    ("Length of the longest substring with no repeated characters.",
     "sliding window", "contiguous + longest + validity check: grow right, shrink left on repeat", "leetcodes.py:28"),
    ("Longest substring you can make all one letter by replacing at most k characters.",
     "sliding window", "window is valid while len - maxfreq <= k", "leetcodes.py:45"),
    ("Does s2 contain some permutation of s1 as a substring?",
     "sliding window (fixed size)", "fixed length = len(s1), compare letter counts as the window slides", "leetcodes.py:63"),
    ("For each day, how many days until a warmer temperature?",
     "monotonic stack", "'next greater' — stack holds days still waiting for an answer", "daily_temperature_leetcode.py"),
    ("Largest rectangle that fits under a histogram.",
     "monotonic stack", "each bar extends until the previous/next smaller bar", "largest_rectangle_area.py"),
    ("Largest rectangle of 1s in a binary matrix.",
     "monotonic stack", "build a histogram per row, run largest-rectangle on each", "leetcode_daily2.py:52"),
    ("Maximum of every window of size k.",
     "monotonic deque", "window max: decreasing deque of indices, expire from the front", "sliding_window_max.py"),
    ("Shortest subarray with sum at least k. Values can be negative.",
     "monotonic deque", "negatives kill the window; prefix sums + increasing deque of prefix indices", "shortest_subarray_with_sumk.py"),
    ("Count subarrays in which max - min <= 2.",
     "sliding window + monotonic deque", "window validity needs window max and min: two deques", "leetcode_daily.py:127"),
    ("Split candy piles (you may split, not merge) so k children each get an equal pile. Maximize the pile size.",
     "binary search on answer", "'maximize the size such that feasible' and feasibility is a simple count", "leetcode_daily.py:1221"),
    ("Mechanic with rank r repairs n cars in r*n*n minutes. All work in parallel. Minimum time to repair all cars.",
     "binary search on answer", "guess time T, count cars each can do in T: monotone feasibility", "leetcode_daily.py:1262"),
    ("Rob at least k non-adjacent houses. Minimize the maximum amount taken from any single house.",
     "binary search on answer", "'minimize the maximum' -> guess cap, greedy check", "leetcode_daily.py:1238"),
    ("For each spell, count potions with spell * potion >= success.",
     "sort + binary search", "sort potions once; each query is a bisect", "leetcode_daily.py:1840"),
    ("Search a target in a rotated sorted array that may contain duplicates.",
     "binary search", "one half is always sorted; duplicates force shrinking both ends", "leetcode_daily2.py:316"),
    ("Each second take the largest pile and replace it with floor(sqrt(pile)). Sum after k seconds.",
     "heap", "'repeatedly take the max and modify it' = max-heap", "leetcode_daily.py:98"),
    ("Add extra brilliant students to classes to maximize the average pass ratio.",
     "heap (greedy by marginal gain)", "always give the next student to the class with the biggest gain", "leetcode_daily.py:147"),
    ("n rooms; each meeting takes the lowest-numbered free room, else waits for the earliest free one. Which room hosts the most meetings?",
     "two heaps + intervals", "one heap of free room ids, one heap of (end time, room) busy", "leetcode_daily.py:1683"),
    ("Each event can be attended on any one day in [start, end]. Maximize the events attended.",
     "greedy + heap", "sweep days; among open events attend the one ending soonest (min-heap of ends)", "leetcode_daily.py:1618"),
    ("Choose at most two non-overlapping events to maximize total value.",
     "sort + binary search", "sort by start, bisect for the next compatible event, suffix max", "leetcode_daily.py:42"),
    ("Choose at most k non-overlapping events to maximize total value.",
     "dp + binary search", "take/skip per event; bisect to jump to the next compatible event", "leetcode_daily.py:1641"),
    ("Minimum arrows to burst all balloons given as horizontal intervals.",
     "greedy intervals (sort by end)", "max non-overlapping set = sort by end and take greedily", "mock_q.py:42"),
    ("Merge all overlapping intervals.",
     "intervals (sort by start)", "sort by start; extend the last one or start a new one", "merge_intervals_s8.py"),
    ("How much rain water is trapped by a 1-D elevation map?",
     "two pointers", "water at i = min(maxLeft, maxRight) - h; move the smaller side", "trap_water.py"),
    ("How much rain water is trapped by a 2-D height map?",
     "heap (BFS from boundary)", "water level is set by the lowest wall: min-heap from the border inward", "leetcode_daily.py:669"),
    ("Count pairs i<j with lower <= nums[i] + nums[j] <= upper.",
     "sort + two pointers", "order doesn't matter for pairs -> sort; count(<=upper) - count(<lower)", "leetcode_daily.py:1595"),
    ("Count pairs i<j where j - i != nums[j] - nums[i].",
     "hashing (transformed key)", "rewrite as nums[i]-i == nums[j]-j; count good pairs, subtract from total", "leetcode_daily.py:1014"),
    ("Count tuples (a,b,c,d) of distinct elements with a*b == c*d.",
     "hashing", "count every pair's product; each product with c pairs gives 8*C(c,2)", "leetcode_daily.py:987"),
    ("Apply many 'shift letters in range [l, r] forward or backward' operations, then output the string.",
     "difference array", "many range updates then one read", "leetcode_daily.py:456"),
    ("Answer queries: is subarray [l, r] such that every adjacent pair has different parity?",
     "prefix sum", "prefix-count the 'bad' adjacent pairs; query is a difference", "leetcode_daily.py:67"),
    ("2xN grid. Robot 1 goes right/down collecting points and zeroes its path; robot 2 then does the same. Robot 1 minimizes robot 2's score.",
     "prefix sum", "robot 1 turns down at one column; robot 2 gets max(top suffix, bottom prefix)", "leetcode_daily.py:722"),
    ("Given water cells, assign heights so adjacent cells differ by at most 1 and the highest peak is maximized.",
     "multi-source BFS", "distance from the nearest water cell; all water cells start at 0", "leetcode_daily.py:738"),
    ("Grid of arrows. Changing a cell's arrow costs 1. Minimum cost to reach the bottom-right.",
     "0-1 BFS", "following the arrow costs 0, other moves cost 1", "leetcode_daily.py:643"),
    ("Minimum obstacles to remove to walk from top-left to bottom-right.",
     "0-1 BFS", "entering an empty cell costs 0, an obstacle costs 1", "minimum_obstacle_removal_grid.py"),
    ("Minutes until every fresh orange rots, if rot spreads to neighbours each minute.",
     "multi-source BFS", "all rotten oranges start together; each level is one minute", "rotten_oranges_graph.py"),
    ("Minimum moves to solve a 2x3 sliding puzzle.",
     "BFS over states", "min moves + small state space: board as a string is a node", "sliding_puzzle.py"),
    ("Find all nodes from which every path leads to a terminal node.",
     "DFS cycle detection (3 colours)", "unsafe = can reach a cycle; gray node seen again means a cycle", "leetcode_daily.py:778"),
    ("Courses with prerequisites: can you finish them all, and in what order?",
     "topological sort", "dependencies + order + cycle check = Kahn's algorithm", "graph/topological_sort_graph.py"),
    ("Answer many queries 'is course u a prerequisite of course v?'",
     "topological sort + reachability", "propagate ancestor sets in topo order (or Floyd for small n)", "leetcode_daily.py:865"),
    ("Split graph nodes into the most groups so every edge joins adjacent groups.",
     "BFS + bipartite check", "per component: bipartite, else -1; answer = max BFS depth from any start", "leetcode_daily.py:891"),
    ("Edges are added one at a time. Report the first edge that creates a cycle.",
     "union-find", "edges arriving over time + 'already connected?'", "graph/disjoint_set_graph.py"),
    ("Minimum total cost to connect all points.",
     "MST (Kruskal / Prim)", "connect everything at min total edge cost", "mst_graph.py"),
    ("Shortest travel time from a city to all others, non-negative road times.",
     "Dijkstra", "weighted + non-negative + single source", "graph/dijkstra_algo_graph.py"),
    ("Shortest distance between every pair of cities, n <= 100.",
     "Floyd-Warshall", "all pairs + small n allows O(n^3)", "graph/floyd_warshall_algo_graph.py"),
    ("Find every connection whose removal disconnects the network.",
     "bridges (Tarjan low-link)", "critical edges: low[child] > disc[node]", "finding_bridge_graph.py"),
    ("Generate all valid strings of n pairs of parentheses.",
     "backtracking", "'generate all' with a validity rule: open < n, close < open", "generate_parenthesis.py"),
    ("All unique combinations summing to target; each candidate used at most once; input has duplicates.",
     "backtracking (skip duplicates)", "sort, then skip equal values at the same depth", "leetcode_daily2.py:253"),
    ("Smallest number using digits 1-9 once each that matches an I/D pattern.",
     "backtracking / stack greedy", "small n: try digits in order; or reverse runs of D", "leetcode_daily.py:1121"),
    ("How many distinct non-empty sequences can be made from the letters on these tiles?",
     "backtracking (counts)", "branch on each letter with a remaining count to avoid duplicates", "leetcode_daily.py:1113"),
    ("Fill a 9x9 sudoku.",
     "backtracking", "try digits, check row/col/box sets, undo on failure", "sudoku_solver.py"),
    ("Maximum money robbing houses arranged in a circle, no two adjacent.",
     "1-D DP", "circle -> run linear robber twice: without first, without last", "dp/house_robber2.py"),
    ("Number of ways to decode a digit string where 1-26 map to letters.",
     "1-D DP", "ways(i) = ways(i+1) [one digit] + ways(i+2) [valid two digits]", "decode_ways.py"),
    ("Can the string be split into words from a dictionary?",
     "1-D DP", "dp[i] = some dictionary word ends at i and dp[start] is True", "word_break.py"),
    ("Fewest coins to make an amount, unlimited coins of each type.",
     "unbounded knapsack DP", "min over coins of dp[a - c] + 1", "dp/minimum_coin.py"),
    ("Put + or - before each number; count the ways to reach target.",
     "subset sum DP", "count subsets with sum (total + target) / 2", "leetcode_daily.py:304"),
    ("Can the array be split into two subsets with equal sums?",
     "0/1 knapsack DP", "subset sum to total/2; iterate capacity downward", "dp/partition_in_2_sequence_of_equal_sum.py"),
    ("Minimum insert/delete/replace operations to turn word1 into word2.",
     "two-string DP", "state (i, j): match -> diagonal, else 1 + min of three", "dp/edit_distance.py"),
    ("Minimum ASCII sum of deleted characters to make two strings equal.",
     "two-string DP (LCS variant)", "LCS where the score is the ASCII sum kept", "leetcode_daily2.py:33"),
    ("Minimum insertions to make a string a palindrome.",
     "two-string DP", "n - LPS, and LPS = LCS(s, reversed s)", "minimum_insertion_palindrome.py"),
    ("Largest subset in which every pair divides one way or the other.",
     "LIS-style DP", "sort; dp[i] = 1 + max dp[j] where nums[i] % nums[j] == 0", "largest_divisible_subset.py"),
    ("Length of the longest strictly increasing subsequence, n = 1e5.",
     "LIS with binary search", "n too big for n^2: tails array + bisect_left", "dp/lis.py (add n log n)"),
    ("Minimum cuts to split a string into palindromes.",
     "partition DP", "dp[i] = min over j of dp[j] + 1 where s[j..i] is a palindrome", "dp/palindrome_partitioning.py"),
    ("Minimum total cost to cut a stick at given positions; each cut costs the current piece length.",
     "interval DP", "state (i, j) over sorted cut points; try every first cut", "dp/minimum_cost_to_cut_rod.py"),
    ("Count the ways to parenthesize a boolean expression so it evaluates to True.",
     "interval DP", "split at each operator; combine (true, false) counts of both sides", "boolean_expression_true.py"),
    ("Maximum profit with at most k stock transactions.",
     "state machine DP", "state (day, transactions left, holding?)", "stocks4.py"),
    ("Maximum subarray sum where the array is circular.",
     "Kadane", "max(normal Kadane, total - min subarray), careful when all negative", "max_sum_circular_subarray.py"),
    ("Type a word with two fingers on a keyboard grid; minimize total finger travel.",
     "DP (multi-dimensional state)", "state (index, finger1 position, finger2 position)", "leetcode_daily2.py:127"),
    ("In a knockout tournament, find the earliest and latest rounds two given players can meet.",
     "memo DP / bitmask", "small n; state = who is left; memoize", "leetcode_daily.py:1713"),
    ("Maximum XOR of any two numbers in an array.",
     "trie (bitwise)", "insert bits high to low; greedily walk the opposite bit", "max_xor_trie.py"),
    ("For each index i, the smallest subarray starting at i whose OR is the maximum possible.",
     "bit manipulation", "track the nearest position of each bit to the right", "leetcode_daily.py:1981"),
    ("Longest subarray in which every pair of elements has bitwise AND 0.",
     "sliding window + bitmask", "window OR mask must not share bits with the new number", "leetcode_daily.py:1290"),
    ("derived[i] = original[i] XOR original[i+1] (circular). Does a valid original exist?",
     "bit manipulation (XOR)", "every original element appears twice, so XOR of derived must be 0", "leetcode_daily.py:604"),
    ("Each fruit goes to the leftmost basket with capacity >= fruit (one fruit per basket). Count unplaced fruits, n = 1e5.",
     "segment tree", "'leftmost with value >= x' + updates: max segment tree, descend left first", "leetcode_daily.py:2032"),
    ("Split a tree into the maximum number of components whose value sums are divisible by k.",
     "tree DFS (post-order)", "child returns its remainder; when 0, cut it off as a component", "leetcode_daily.py:248"),
    ("Smallest subtree containing all the deepest nodes.",
     "tree DFS (post-order)", "return (depth, node); equal depths on both sides -> this node", "leetcode_daily2.py:16"),
    ("Maximum path sum between any two nodes of a binary tree.",
     "tree DFS (post-order)", "return the best downward path; update global with left + node + right", "binary_tree_max_path_sum.py"),
    ("Permutation of 0..n-1: maximum chunks so sorting each chunk sorts the whole array.",
     "greedy (prefix max)", "a chunk can end at i when the max so far == i", "leetcode_daily.py:235"),
    ("Build the lexicographically largest string from given letters with no letter repeated more than k times in a row.",
     "greedy + heap", "take the largest letter; when limit is hit insert one next-largest", "leetcode_daily.py:190"),
    ("Rearrange a string so no two adjacent characters are equal.",
     "greedy + heap", "always place the most frequent letter that isn't the previous one", "reorganise_string.py"),
    ("Design a cache with O(1) get and put that evicts the least recently used key.",
     "design: hashmap + linked list", "O(1) lookup + O(1) reorder = dict + doubly linked list (OrderedDict)", "new"),
    ("Store set(key, value, timestamp); get(key, t) returns the value with the largest timestamp <= t.",
     "hashmap + binary search", "per-key sorted timestamps; bisect_right - 1", "new"),
    ("A stream of numbers arrives; return the median at any time.",
     "two heaps", "max-heap of the lower half, min-heap of the upper half", "new"),
    ("Merge k sorted streams of sensor readings into one sorted stream.",
     "heap (k-way merge)", "heap holds the current head of each stream", "new"),
    ("For each element, count how many smaller elements are to its right.",
     "Fenwick tree / merge sort", "scan right to left, count values seen so far below x", "new"),
    ("Detect whether a linked list has a cycle and find where it starts.",
     "fast and slow pointers", "they meet inside the cycle; reset one to head, step both by 1", "new"),
    ("Length of the longest run of consecutive integers in an unsorted array, in O(n).",
     "hashing (set)", "only start counting at x where x-1 is not in the set", "leetcodes.py:5"),
    ("Product of all elements except self, without division.",
     "prefix / suffix products", "answer[i] = product of left part * product of right part", "product_of_array_except_self.py"),
    ("Rearrange numbers into the next lexicographically greater permutation, in place.",
     "array trick", "pivot = first i from right with a[i] < a[i+1]; swap with next larger; reverse suffix", "next_permutations_s3.py"),
    ("Sort an array of 0s, 1s and 2s in one pass.",
     "two pointers (Dutch flag)", "low / mid / high pointers", "sort_colors_s5.py"),
    ("Find all duplicates in an array where 1 <= a[i] <= n, using O(1) extra space.",
     "index marking (cyclic sort)", "values are valid indices: negate a[value-1] to mark seen", "leetcode_daily2.py:375"),
    ("Minimum jumps to reach the last index, each value is the max jump length.",
     "greedy (BFS by levels)", "track the farthest reach of the current level", "min_jump.py"),
    ("Find the k-th largest element in an unsorted array.",
     "heap of size k", "min-heap keeps the k largest; root is the answer (or quickselect)", "kth_largest_elemnent.py"),
]


def load_state():
    try:
        return json.loads(STATE_FILE.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=1))


def is_due(entry, today):
    if entry is None:
        return True
    last = date.fromisoformat(entry["last"])
    return last + timedelta(days=BOX_DAYS[entry["box"]]) <= today


# First match wins, so order matters ("tree DFS" is a tree problem, not a graph one).
FAMILIES = [
    ("design", ["design", "hashmap +"]),
    ("trees", ["tree dfs", "trie"]),
    ("dp", ["dp", "knapsack", "lis", "kadane"]),
    ("sliding window", ["sliding window"]),
    ("monotonic stack / deque", ["monotonic"]),
    ("heap", ["heap"]),
    ("binary search", ["binary search"]),
    ("prefix sum", ["prefix", "difference"]),
    ("intervals / greedy", ["interval", "greedy"]),
    ("two pointers", ["two pointers", "fast and slow", "array trick", "index marking"]),
    ("hashing", ["hash"]),
    ("graph bfs", ["bfs"]),
    ("graph dfs / topo / union-find / paths", ["dfs", "topolog", "union", "mst", "dijkstra", "floyd", "bridges"]),
    ("backtracking", ["backtracking"]),
    ("bits / segment tree / fenwick", ["bit", "segment", "fenwick"]),
]


def family(pattern):
    lowered = pattern.lower()
    for name, keys in FAMILIES:
        if any(k in lowered for k in keys):
            return name
    return "other"


def show_stats(state):
    by_family = defaultdict(list)
    for prompt, pattern, _, _ in CARDS:
        entry = state.get(prompt)
        by_family[family(pattern)].append(entry["box"] if entry else 0)
    print(f"{'family':40} cards  avg box (0 = unseen, 5 = mastered)")
    for name, boxes in sorted(by_family.items(), key=lambda kv: sum(kv[1]) / len(kv[1])):
        print(f"{name:40} {len(boxes):5}  {sum(boxes) / len(boxes):.1f}")
    seen = sum(1 for p, *_ in CARDS if p in state)
    mastered = sum(1 for p, *_ in CARDS if state.get(p, {}).get("box", 0) >= 4)
    print(f"\n{seen}/{len(CARDS)} seen, {mastered} in box 4+")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-n", type=int, default=15, help="cards this session")
    parser.add_argument("-p", "--pattern", help="only cards whose pattern or family contains this text")
    parser.add_argument("--stats", action="store_true")
    args = parser.parse_args()

    state = load_state()
    if args.stats:
        show_stats(state)
        return

    today = date.today()
    pool = [
        c for c in CARDS
        if not args.pattern or args.pattern.lower() in f"{c[1]} {family(c[1])}".lower()
    ]
    due = [c for c in pool if is_due(state.get(c[0]), today)]
    random.shuffle(due)
    due.sort(key=lambda c: state.get(c[0], {"box": 0})["box"])  # weakest first
    session = due[: args.n]
    if not session:
        print("Nothing due. Come back tomorrow, or use -p to drill one pattern.")
        return

    right = graded = 0
    for i, (prompt, pattern, why, src) in enumerate(session, 1):
        print(f"\n[{i}/{len(session)}] {prompt}")
        input("   pattern + the signal that gave it away? (Enter to reveal) ")
        print(f"   -> {pattern}\n   why: {why}\n   yours: {src}")
        answer = input("   got it? [y/n/q] ").strip().lower()
        if answer == "q":
            break
        graded += 1
        entry = state.get(prompt, {"box": 1})
        if answer == "y":
            entry["box"] = min(entry["box"] + 1, 5)
            right += 1
        else:
            entry["box"] = 1
        entry["last"] = today.isoformat()
        state[prompt] = entry
        save_state(state)

    print(f"\n{right}/{graded} right. Missed cards come back next session.")


if __name__ == "__main__":
    main()
