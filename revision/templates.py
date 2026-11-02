"""
One template per pattern, numbered to match PATTERNS.md.

How to use: pick a section, cover it, write it from memory in a scratch file,
then compare. Run `python revision/templates.py` — every assert must pass.
"""

import math
from bisect import bisect_left, bisect_right, insort
from collections import Counter, defaultdict, deque
from functools import cache
from heapq import heapify, heappop, heappush
from typing import List, Optional


# ---------------------------------------------------------------- 1. Hashing
def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Problem: LeetCode 1. Given an array nums and a target, return the
             indices of the two numbers that add up to target. Exactly one
             answer exists.
    Example: nums = [2, 7, 11, 15], target = 9 -> [0, 1]
    Idea: For each x, the partner we need is target - x. Check if we've
          already seen it.
    """
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Problem: LeetCode 49. Group the words that are anagrams of each other.
    Example: ["eat", "tea", "tan", "ate", "nat"] -> [["eat", "tea", "ate"],
             ["tan", "nat"]]
    Idea: Anagrams share the same sorted letters, so use that as the dict
          key.
    """
    groups = defaultdict(list)
    for w in words:
        groups[tuple(sorted(w))].append(w)  # key = canonical form
    return list(groups.values())


# ------------------------------------------------------------- 2. Prefix sum
def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    Problem (LeetCode 560): Given an integer array nums and an integer k,
    return how many contiguous subarrays have a sum equal to k.
    Numbers can be negative, so a sliding window does not work.

    Example: nums = [1, 2, 3], k = 3 -> 2   (subarrays [1, 2] and [3])

    Idea:
      prefix(j) = nums[0] + ... + nums[j]   (the running total)
      The subarray from i+1 to j sums to k  <=>  prefix(j) - prefix(i) == k
                                             <=>  prefix(i) == prefix(j) - k
      So at each position, with the running total so far, ask:
        "How many EARLIER running totals were equal to (total - k)?"
      Each one marks a start point where a subarray ending here sums to k.
      A Counter of the running totals seen so far answers that in O(1).
      Seed it with {0: 1}: the empty prefix, so subarrays that start at
      index 0 are counted too.

    Trace for nums = [1, 2, 3], k = 3:
      x   total   need = total - k   seen before the lookup   ans
      1     1          -2            {0: 1}                     0
      2     3           0            {0: 1, 1: 1}               1  <- [1, 2]
      3     6           3            {0: 1, 1: 1, 3: 1}         2  <- [3]


    seen[total - k] can we seen as at current index how many ways i can chop off
    front part so that whatever is left is adds up to k
    """
    seen = Counter({0: 1})  # prefix sum -> how many times seen
    total = ans = 0
    for x in nums:
        total += x
        ans += seen[total - k]  # earlier prefix p with total - p == k
        seen[total] += 1
    return ans


def range_add(n: int, updates: List[List[int]]) -> List[int]:
    """
    Problem: LeetCode 370 (Range Addition). Start with n zeros. Each update
             [l, r, delta] adds delta to every index from l to r inclusive.
             Return the final array.
    Example: n = 5, updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]] -> [-2, 0,
             3, 5, 3]
    Idea: Difference array: each update (l, r, delta) is inclusive.
    """
    diff = [0] * (n + 1)
    for l, r, d in updates:
        diff[l] += d
        diff[r + 1] -= d
    out, run = [], 0
    for i in range(n):
        run += diff[i]
        out.append(run)
    return out


# ----------------------------------------------------------- 3. Two pointers
def max_area(height: List[int]) -> int:
    """
    Problem: LeetCode 11 (Container With Most Water). height[i] is a
             vertical line at x = i. Pick two lines that, with the x-axis,
             hold the most water. Return that amount.
    Example: [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49 (lines at index 1 and 8:
             width 7, height 7)
    Idea: Start wide. Moving the taller line can never help, so always move
          the shorter one.
    """
    l, r, best = 0, len(height) - 1, 0
    while l < r:
        best = max(best, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:  # move the side that limits the answer
            l += 1
        else:
            r -= 1
    return best


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Problem: LeetCode 15. Return all unique triplets [a, b, c] from nums
             with a + b + c == 0.
    Example: [-1, 0, 1, 2, -1, -4] -> [[-1, -1, 2], [-1, 0, 1]]
    Idea: Sort, fix the first number, then run two-sum with two pointers on
          the rest.
    """
    nums.sort()
    out = []
    for i in range(len(nums) - 2):
        if i and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                out.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return out


# --------------------------------------------------------- 4. Sliding window
def longest_at_most_k_distinct(s: str, k: int) -> int:
    """
    Problem: LeetCode 340. Length of the longest substring that has at most
             k distinct characters.
    Example: s = "eceba", k = 2 -> 3 ("ece")
    """
    freq = Counter()
    l = best = 0
    for r, ch in enumerate(s):
        freq[ch] += 1  # 1. grow
        while len(freq) > k:  # 2. shrink while invalid
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l += 1
        best = max(best, r - l + 1)  # 3. window is valid: record
    return best


def subarrays_exactly_k_distinct(nums: List[int], k: int) -> int:
    """
    Problem: LeetCode 992. Count the subarrays that contain exactly k
             distinct integers.
    Example: nums = [1, 2, 1, 2, 3], k = 2 -> 7
    Idea: exactly(k) = atMost(k) - atMost(k - 1).
    """

    def at_most(k):
        freq = Counter()
        l = total = 0
        for r, x in enumerate(nums):
            freq[x] += 1
            while len(freq) > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            total += r - l + 1  # every subarray ending at r
        return total

    return at_most(k) - at_most(k - 1)


# -------------------------------------------------------- 5. Monotonic stack
def next_greater(nums: List[int]) -> List[int]:
    """
    Problem: For each element, find the first element to its right that is
             greater. Use -1 if there is none. (LeetCode 496/739 family.)
    Example: [2, 1, 2, 4, 3] -> [4, 2, 4, -1, -1]
    """
    ans = [-1] * len(nums)
    stack = []  # indices whose answer is unknown; values decreasing
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            ans[stack.pop()] = x
        stack.append(i)
    return ans


def largest_rectangle(heights: List[int]) -> int:
    """
    Problem: LeetCode 84. heights[i] is a bar of width 1. Return the area of
             the largest rectangle inside the histogram.
    Example: [2, 1, 5, 6, 2, 3] -> 10 (bars 5 and 6, width 2, height 5)
    Idea: When a bar is popped, the bar that pops it is its first smaller
          bar on the right and the new stack top is its first smaller bar on
          the left. That gives its widest rectangle.
    """
    stack, best = [], 0
    for i, h in enumerate(heights + [0]):  # sentinel 0 flushes the stack
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            best = max(best, height * (i - left - 1))
        stack.append(i)
    return best


# -------------------------------------------------------- 6. Monotonic deque
def window_max(nums: List[int], k: int) -> List[int]:
    """
    Problem: LeetCode 239. Return the maximum of every contiguous window of
             size k.
    Example: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3 -> [3, 3, 5, 5, 6, 7]
    Idea: A smaller element to the left of a bigger one can never be a
          window max again, so drop it.
    """
    dq, out = deque(), []  # indices; values decreasing front -> back
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:  # front fell out of the window
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out


# ---------------------------------------------------------- 7. Binary search
def first_true(lo: int, hi: int, ok) -> int:
    """
    Problem: Not a problem: the one binary-search loop to reuse everywhere.
    Idea: Smallest x in [lo, hi] with ok(x) True. ok must look like F F F T
          T T. Returns hi + 1 if ok is never True.
    """
    while lo <= hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


def ship_within_days(weights: List[int], days: int) -> int:
    """
    Problem: LeetCode 1011. Packages with these weights must ship in order
             within `days` days. Each day the ship is loaded in order up to
             its capacity. Return the minimum capacity that works.
    Example: weights = [1..10], days = 5 -> 15
    Idea: Binary search on the answer: 'minimum capacity such that ...'.
    """

    def ok(cap):
        need, cur = 1, 0
        for w in weights:
            if cur + w > cap:
                need += 1
                cur = 0
            cur += w
        return need <= days

    return first_true(max(weights), sum(weights), ok)


def search_rotated(nums: List[int], target: int) -> int:
    """
    Problem: LeetCode 33. A sorted array of distinct numbers was rotated at
             an unknown pivot. Return the index of target, or -1, in O(log
             n).
    Example: nums = [4, 5, 6, 7, 0, 1, 2], target = 0 -> 4
    Idea: At every mid, one half is sorted. Check whether target lies in
          that half.
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# ------------------------------------------------------------------ 8. Heap
def kth_largest(nums: List[int], k: int) -> int:
    """
    Problem: LeetCode 215. Return the k-th largest element in an unsorted
             array.
    Example: nums = [3, 2, 1, 5, 6, 4], k = 2 -> 5
    Idea: Keep a min-heap of the k largest so far; its root is the k-th
          largest.
    """
    heap = []  # min-heap of the k largest seen so far
    for x in nums:
        heappush(heap, x)
        if len(heap) > k:
            heappop(heap)
    return heap[0]


def merge_k_sorted(lists: List[List[int]]) -> List[int]:
    """
    Problem: LeetCode 23 (with lists instead of linked lists). Merge k
             sorted lists into one sorted list.
    Example: [[1, 4, 5], [1, 3, 4], [2, 6]] -> [1, 1, 2, 3, 4, 4, 5, 6]
    Idea: The heap holds the current smallest unused item of each list.
    """
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapify(heap)
    out = []
    while heap:
        val, i, j = heappop(heap)  # i breaks ties so tuples always compare
        out.append(val)
        if j + 1 < len(lists[i]):
            heappush(heap, (lists[i][j + 1], i, j + 1))
    return out


class MedianFinder:
    """
    Problem: LeetCode 295. Numbers arrive one at a time. Support add(x) and
             median() at any moment.
    Example: add 5 -> 5, add 15 -> 10, add 1 -> 5, add 3 -> 4
    Idea: Two heaps: lo is a max-heap (negated), hi is a min-heap.
    """

    def __init__(self):
        self.lo, self.hi = [], []

    def add(self, x: int) -> None:
        heappush(self.lo, -x)
        heappush(self.hi, -heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heappush(self.lo, -heappop(self.hi))

    def median(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2


# --------------------------------------------------- 9. Intervals and sweep
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Problem: LeetCode 56. Merge all overlapping intervals.
    Example: [[1, 3], [2, 6], [8, 10], [15, 18]] -> [[1, 6], [8, 10], [15,
             18]]
    """
    out = []
    for s, e in sorted(intervals):
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Problem: LeetCode 253. Given meeting times [start, end], return the
             minimum number of rooms needed. A room freed at time t can host
             a meeting starting at t.
    Example: [[0, 30], [5, 10], [15, 20]] -> 2
    """
    ends = []  # min-heap of end times of rooms in use
    for s, e in sorted(intervals):
        if ends and ends[0] <= s:
            heappop(ends)  # reuse the room that frees up first
        heappush(ends, e)
    return len(ends)


def max_overlap_sweep(intervals: List[List[int]]) -> int:
    """
    Problem: Given intervals [start, end) (end not included), return the
             largest number of intervals that overlap at any single point.
    Example: [[1, 4], [4, 5], [2, 3]] -> 2
    Idea: Turn each interval into +1 at start and -1 at end, sort, and keep
          a running count.
    """
    events = []
    for s, e in intervals:
        events.append((s, 1))
        events.append((e, -1))  # (e, -1) sorts before (e, 1): end before start
    best = cur = 0
    for _, delta in sorted(events):
        cur += delta
        best = max(best, cur)
    return best


# ---------------------------------------------------------------- 10. Greedy
def min_arrows(points: List[List[int]]) -> int:
    """
    Problem: LeetCode 452. Balloons are intervals [x_start, x_end]. An arrow
             shot at x bursts every balloon with x_start <= x <= x_end.
             Return the minimum number of arrows.
    Example: [[10, 16], [2, 8], [1, 6], [7, 12]] -> 2 (arrows at 6 and 12)
    Idea: Sort by END, take as many as possible (interval scheduling).
    """
    arrows, end = 0, -math.inf
    for s, e in sorted(points, key=lambda p: p[1]):
        if s > end:
            arrows += 1
            end = e
    return arrows


# ----------------------------------------------------------- 11. Linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Problem: LeetCode 206. Reverse a singly linked list.
    Example: 1 -> 2 -> 3 becomes 3 -> 2 -> 1
    """
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


def middle_node(head: ListNode) -> ListNode:
    """
    Problem: LeetCode 876. Return the middle node of a linked list (the
             second middle if the length is even).
    Example: 1 -> 2 -> 3 -> 4 -> 5 -> node 3
    Idea: Fast moves 2 steps, slow moves 1. When fast reaches the end, slow
          is in the middle.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Problem: LeetCode 141. Does the linked list contain a cycle?
    Idea: If there is a loop, the fast pointer laps the slow one and they
          meet.
    """
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False


class LRUCache:
    """
    Problem: LeetCode 146. A cache with a fixed capacity. get(key) returns
             the value or -1. put(key, value) inserts or updates, and evicts
             the least recently used key when over capacity. Both must be
             O(1).
    Example: capacity 2: put(1,1), put(2,2), get(1) -> 1, put(3,3) evicts 2,
             get(2) -> -1
    Idea: Design classic. OrderedDict = hashmap + doubly linked list in one.
          Be ready to also build it by hand with a dict and ListNode-style
          nodes.
    """

    def __init__(self, capacity: int):
        from collections import OrderedDict

        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.data.move_to_end(key)  # mark as most recently used
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        self.data.move_to_end(key)
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)  # evict least recently used


class TimeMap:
    """
    Problem: LeetCode 981. set(key, value, timestamp) stores a value.
             get(key, t) returns the value stored with the largest timestamp
             <= t, or "".
    Example: set("bowl", "full", 1), set("bowl", "half", 4): get("bowl", 3)
             -> "full", get("bowl", 5) -> "half"
    Idea: Time-based key-value store: hashmap of time-sorted lists + bisect.
    """

    def __init__(self):
        self.times = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, t: int) -> None:
        self.times[key].append(t)  # timestamps arrive increasing
        self.values[key].append(value)

    def get(self, key: str, t: int) -> str:
        i = bisect_right(self.times[key], t) - 1  # last time <= t
        return self.values[key][i] if i >= 0 else ""


# ------------------------------------------------------------ 12-13. Trees
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter(root: Optional[TreeNode]) -> int:
    """
    Problem: LeetCode 543. Return the length (in edges) of the longest path
             between any two nodes of a binary tree.
    Example: tree [3, 5, 1, 6, 2, null, null, null, null, 7, 4] -> 4 (7 -> 2
             -> 5 -> 3 -> 1)
    Idea: Every path has one highest node where it bends (left arm + right
          arm). Each node does two jobs:
            1. RECORD: the best path that bends here = left arm + right arm.
               Only this node sees both arms, so record it now.
            2. REPORT: tell the parent its longest single arm, because a
               parent can only extend a straight line, not a fork.
    """
    best = 0

    def height(node):
        nonlocal best
        if not node:
            return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)  # path THROUGH node
        return 1 + max(l, r)  # path going UP from node

    height(root)
    return best


def lca(root, p, q):
    """
    Problem: LeetCode 236. Return the lowest common ancestor of nodes p and
             q in a binary tree (both are in the tree).
    Idea: If p and q are found in different subtrees, this node is the
          answer. Otherwise pass up whichever side found something.
    """
    if not root or root is p or root is q:
        return root
    left, right = lca(root.left, p, q), lca(root.right, p, q)
    return root if left and right else left or right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Problem: LeetCode 102. Return the node values level by level, left to
             right.
    Example: [3, 5, 1, 6, 2, ...] -> [[3], [5, 1], [6, 2], [7, 4]]
    """
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):  # exactly one level per outer loop
            node = q.popleft()
            level.append(node.val)
            for child in (node.left, node.right):
                if child:
                    q.append(child)
        out.append(level)
    return out


# ---------------------------------------------------------- 14. Graph BFS
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def oranges_rotting(grid: List[List[int]]) -> int:
    """
    Problem: LeetCode 994. Grid cells: 0 empty, 1 fresh orange, 2 rotten
             orange. Each minute, fresh oranges next to rotten ones rot.
             Return the minutes until none are fresh, or -1 if that never
             happens.
    Example: [[2, 1, 1], [1, 1, 0], [0, 1, 1]] -> 4
    Idea: Multi-source BFS: put every source in the queue at distance 0.
    """
    rows, cols = len(grid), len(grid[0])
    q = deque((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 2)
    fresh = sum(row.count(1) for row in grid)
    minutes = 0
    while q and fresh:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # mark when PUSHED, not when popped
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1
    return -1 if fresh else minutes


def min_obstacles_0_1_bfs(grid: List[List[int]]) -> int:
    """
    Problem: LeetCode 2290. Grid cells: 0 empty, 1 obstacle. Move
             up/down/left/right. Return the minimum number of obstacles to
             remove to get from top-left to bottom-right.
    Example: [[0, 1, 1], [1, 1, 0], [1, 1, 0]] -> 2
    Idea: Edge weights 0 or 1: deque, weight-0 to the front, weight-1 to the
          back.
    """
    rows, cols = len(grid), len(grid[0])
    dist = [[math.inf] * cols for _ in range(rows)]
    dist[0][0] = 0
    dq = deque([(0, 0)])
    while dq:
        r, c = dq.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                nd = dist[r][c] + grid[nr][nc]
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    if grid[nr][nc]:
                        dq.append((nr, nc))
                    else:
                        dq.appendleft((nr, nc))
    return dist[-1][-1]


# ---------------------------------------------------------- 15. Graph DFS
def has_cycle_directed(n: int, edges: List[List[int]]) -> bool:
    """
    Problem: Core of LeetCode 207. Given n nodes and directed edges [u, v],
             does the graph contain a cycle?
    Example: 3 nodes, edges 0->1, 1->2, 2->0 -> True
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    color = [0] * n  # 0 unvisited, 1 on current path, 2 done

    def dfs(u):
        color[u] = 1
        for v in graph[u]:
            if color[v] == 1 or (color[v] == 0 and dfs(v)):
                return True  # back edge to the current path
        color[u] = 2
        return False

    return any(color[u] == 0 and dfs(u) for u in range(n))


def num_islands(grid: List[List[str]]) -> int:
    """
    Problem: LeetCode 200. Grid of '1' (land) and '0' (water). Count the
             islands (groups of land connected up/down/left/right).
    Idea: Each time you find unvisited land, count it and sink its whole
          island.
    """
    rows, cols = len(grid), len(grid[0])

    def sink(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        for dr, dc in DIRS:
            sink(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                sink(r, c)
    return count


# ---------------------------------------------------- 16. Topological sort
def topo_sort(n: int, edges: List[List[int]]) -> List[int]:
    """
    Problem: LeetCode 210 (here [u, v] means u must come before v). Return
             an order of the n nodes that respects every edge, or [] if a
             cycle makes it impossible.
    Example: 4 nodes, edges [[0, 1], [0, 2], [1, 3], [2, 3]] -> [0, 1, 2, 3]
    Idea: Kahn's algorithm. Returns [] if there is a cycle.
    """
    graph = defaultdict(list)
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    q = deque(u for u in range(n) if indegree[u] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    return order if len(order) == n else []


# ------------------------------------------------------------ 17. Union-find
class DSU:
    """
    Problem: Union-find structure. union(a, b) joins two groups and returns
             False if they were already joined (that edge would close a
             cycle, as in LeetCode 684). components = number of groups.
    """

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path halving
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        a, b = self.find(a), self.find(b)
        if a == b:
            return False  # already connected: this edge closes a cycle
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a  # attach smaller under bigger
        self.size[a] += self.size[b]
        self.components -= 1
        return True


# ------------------------------------------- 18-19. Weighted graphs and MST
def dijkstra(n: int, edges: List[List[int]], src: int) -> List[float]:
    """
    Problem: LeetCode 743 style. n nodes, directed edges [u, v, w] with w >=
             0. Return the shortest distance from src to every node (inf if
             unreachable).
    Example: edges [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1]], src 0 ->
             [0, 3, 1, 4]
    """
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    dist = [math.inf] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = heappop(heap)
        if d > dist[u]:
            continue  # stale entry: a shorter path was already found
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(heap, (dist[v], v))
    return dist


def kruskal(n: int, edges: List[List[int]]) -> int:
    """
    Problem: LeetCode 1584 style. n nodes and undirected edges [u, v, w].
             Return the total weight of the minimum spanning tree.
    Example: edges [[0, 1, 1], [1, 2, 2], [0, 2, 3], [2, 3, 4]] -> 7
    Idea: Take edges cheapest first; skip any edge whose ends are already
          connected.
    """
    dsu, total = DSU(n), 0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if dsu.union(u, v):
            total += w
    return total


# ---------------------------------------------------------- 20. Backtracking
def subsets(nums: List[int]) -> List[List[int]]:
    """
    Problem: LeetCode 78. Return all subsets of a list of distinct numbers.
    Example: [1, 2, 3] -> 8 subsets
    """
    out, path = [], []

    def bt(i):
        if i == len(nums):
            out.append(path[:])  # copy! path keeps changing
            return
        path.append(nums[i])  # take
        bt(i + 1)
        path.pop()  # undo
        bt(i + 1)  # skip

    bt(0)
    return out


def permutations(nums: List[int]) -> List[List[int]]:
    """
    Problem: LeetCode 46. Return all orderings of a list of distinct
             numbers.
    Example: [1, 2, 3] -> 6 permutations
    """
    out, path, used = [], [], [False] * len(nums)

    def bt():
        if len(path) == len(nums):
            out.append(path[:])
            return
        for i, x in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(x)
            bt()
            path.pop()
            used[i] = False

    bt()
    return out


def combination_sum2(cands: List[int], target: int) -> List[List[int]]:
    """
    Problem: LeetCode 40. Return all unique combinations of candidates that
             sum to target. Each candidate may be used once; the input can
             contain duplicates.
    Example: [10, 1, 2, 7, 6, 1, 5], target 8 -> [[1, 1, 6], [1, 2, 5], [1,
             7], [2, 6]]
    Idea: Each number used once, no duplicate combinations.
    """
    cands.sort()
    out, path = [], []

    def bt(start, remain):
        if remain == 0:
            out.append(path[:])
            return
        for i in range(start, len(cands)):
            if i > start and cands[i] == cands[i - 1]:
                continue  # same value at the same depth = duplicate branch
            if cands[i] > remain:
                break  # sorted, so every later one is too big as well
            path.append(cands[i])
            bt(i + 1, remain - cands[i])
            path.pop()

    bt(0, target)
    return out


# ------------------------------------------------------------------- 21. DP
def rob(nums: List[int]) -> int:
    """
    Problem: LeetCode 198. Houses in a row hold nums[i] money. You can't rob
             two adjacent houses. Return the maximum you can rob.
    Example: [2, 7, 9, 3, 1] -> 12 (2 + 9 + 1)
    Idea: 1-D: dp[i] = max(dp[i-1], dp[i-2] + nums[i]), rolled into two
          vars.
    """
    prev2 = prev1 = 0
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1


def coin_change(coins: List[int], amount: int) -> int:
    """
    Problem: LeetCode 322. Return the fewest coins needed to make amount
             (unlimited coins of each type), or -1 if impossible.
    Example: coins = [1, 2, 5], amount = 11 -> 3 (5 + 5 + 1)
    Idea: Unbounded knapsack: inner loop goes UP so a coin can be reused.
    """
    dp = [0] + [math.inf] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != math.inf else -1


def can_partition(nums: List[int]) -> bool:
    """
    Problem: LeetCode 416. Can the array be split into two subsets with
             equal sums?
    Example: [1, 5, 11, 5] -> True ([1, 5, 5] and [11])
    Idea: 0/1 knapsack (subset sum): iterate capacity DOWN so each item used
          once.
    """
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [True] + [False] * target
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]


def lcs(a: str, b: str) -> int:
    """
    Problem: LeetCode 1143. Length of the longest common subsequence of two
             strings (characters in order, not necessarily adjacent).
    Example: a = "abcde", b = "ace" -> 3
    Idea: Two sequences: state (i, j). Top-down with @cache.
    """

    @cache
    def solve(i, j):
        if i == len(a) or j == len(b):
            return 0
        if a[i] == b[j]:
            return 1 + solve(i + 1, j + 1)
        return max(solve(i + 1, j), solve(i, j + 1))

    return solve(0, 0)


def edit_distance(a: str, b: str) -> int:
    """
    Problem: LeetCode 72. Minimum number of single-character inserts,
             deletes or replaces to turn a into b.
    Example: a = "horse", b = "ros" -> 3
    Idea: Same state, bottom-up. dp[i][j] = cost to turn a[:i] into b[:j].
    """
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]


def lis_length(nums: List[int]) -> int:
    """
    Problem: LeetCode 300. Length of the longest strictly increasing
             subsequence.
    Example: [10, 9, 2, 5, 3, 7, 101, 18] -> 4 ([2, 3, 7, 18])
    Idea: O(n log n): tails[k] = smallest tail of any increasing run of
          length k+1.
    """
    tails = []
    for x in nums:
        i = bisect_left(tails, x)  # bisect_right for non-decreasing
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def matrix_chain(dims: List[int]) -> int:
    """
    Problem: Matrix chain multiplication. Matrix i has size dims[i] x
             dims[i+1]. Return the minimum number of scalar multiplications
             to multiply them all.
    Example: dims = [10, 30, 5, 60] -> 4500 ((A x B) x C)
    Idea: Interval DP: try every split point k between i and j.
    """

    @cache
    def solve(i, j):
        if j - i < 2:
            return 0
        return min(
            solve(i, k) + solve(k, j) + dims[i] * dims[k] * dims[j]
            for k in range(i + 1, j)
        )

    return solve(0, len(dims) - 1)


def max_profit_with_fee(prices: List[int], fee: int) -> int:
    """
    Problem: LeetCode 714. Buy and sell a stock any number of times (hold at
             most one share). Each sale costs fee. Return the maximum
             profit.
    Example: prices = [1, 3, 2, 8, 4, 9], fee = 2 -> 8
    Idea: State machine DP: best cash if not holding / if holding a share.
    """
    cash, hold = 0, -math.inf
    for p in prices:
        cash, hold = max(cash, hold + p - fee), max(hold, cash - p)
    return cash


def min_assignment_cost(cost: List[List[int]]) -> int:
    """
    Problem: Assignment problem. n workers and n jobs; cost[w][j] is the
             cost of worker w doing job j. Each worker gets exactly one job.
             Return the minimum total cost.
    Example: [[9, 2, 7], [6, 4, 3], [5, 8, 1]] -> 9 (2 + 6 + 1)
    Idea: Bitmask DP (n <= ~15): mask = set of jobs already taken.
    """
    n = len(cost)

    @cache
    def solve(worker, mask):
        if worker == n:
            return 0
        return min(
            cost[worker][job] + solve(worker + 1, mask | 1 << job)
            for job in range(n)
            if not mask & 1 << job
        )

    return solve(0, 0)


# ------------------------------------------------------------------ 22. Trie
class Trie:
    """
    Problem: LeetCode 208. Implement insert(word), search(word) (whole word)
             and starts_with(prefix).
    Example: insert "apple": search "apple" -> True, search "app" -> False,
             starts_with "app" -> True
    """

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True  # end-of-word marker

    def _walk(self, s: str):
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and "$" in node

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None


# -------------------------------------------------------------- 23. Bits
def single_number(nums: List[int]) -> int:
    """
    Problem: LeetCode 136. Every number appears twice except one. Find it in
             O(n) time and O(1) space.
    Example: [4, 1, 2, 1, 2] -> 4
    """
    ans = 0
    for x in nums:
        ans ^= x  # pairs cancel: a ^ a = 0
    return ans


def bit_tricks(x: int):
    """
    Problem: Not a problem: the bit tricks worth knowing by heart.
    """
    return {
        "is_power_of_two": x > 0 and x & (x - 1) == 0,
        "lowest_set_bit": x & -x,
        "drop_lowest_set_bit": x & (x - 1),
        "popcount": x.bit_count(),  # Python 3.10+; older: bin(x).count("1")
    }


# ------------------------------------------- 24. Fenwick tree (range sums)
class Fenwick:
    """
    Problem: Fenwick tree (binary indexed tree): add to one position and get
             a prefix sum, both in O(log n).
    Idea: Point update + prefix sum in O(log n). Indices are 0-based
          outside.
    """

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def prefix(self, i: int) -> int:
        """Sum of [0, i]."""
        i += 1
        total = 0
        while i:
            total += self.tree[i]
            i -= i & -i
        return total


def count_smaller_after_self(nums: List[int]) -> List[int]:
    """
    Problem: LeetCode 315. For each element, count how many smaller elements
             are to its right.
    Example: [5, 2, 6, 1] -> [2, 1, 1, 0]
    Idea: Coordinate-compress, then a Fenwick tree counts values seen so
          far.
    """
    rank = {v: i for i, v in enumerate(sorted(set(nums)))}
    fw = Fenwick(len(rank))
    out = []
    for x in reversed(nums):
        out.append(fw.prefix(rank[x] - 1) if rank[x] else 0)
        fw.add(rank[x], 1)
    return out[::-1]


# ------------------------------------------------------------- 25. Math
def primes_up_to(n: int) -> List[int]:
    """
    Problem: Sieve of Eratosthenes (LeetCode 204 family). Return all primes
             <= n.
    Example: 20 -> [2, 3, 5, 7, 11, 13, 17, 19]
    """
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i :: i] = [False] * len(range(i * i, n + 1, i))
    return [i for i, p in enumerate(sieve) if p]


# ------------------------------------------- SortedList without the package
class SortedListLite:
    """
    Problem: Not a problem: a stand-in for sortedcontainers.SortedList.
    Idea: Good enough for n up to ~1e5 in an interview: insort is O(n) but a
          fast memmove. Say the trade-off out loud; offer a Fenwick tree if
          pushed.
    """

    def __init__(self):
        self.a = []

    def add(self, x) -> None:
        insort(self.a, x)

    def remove(self, x) -> None:
        del self.a[bisect_left(self.a, x)]

    def count_less(self, x) -> int:
        return bisect_left(self.a, x)

    def __getitem__(self, i):
        return self.a[i]

    def __len__(self):
        return len(self.a)


class LazyMinHeap:
    """
    Problem: Not a problem: a heap that supports removing any value.
    Idea: Min-heap that supports remove(x): mark it, discard it when it
          surfaces.
    """

    def __init__(self):
        self.heap, self.dead = [], Counter()

    def push(self, x) -> None:
        heappush(self.heap, x)

    def remove(self, x) -> None:
        self.dead[x] += 1

    def top(self):
        while self.heap and self.dead[self.heap[0]]:
            self.dead[heappop(self.heap)] -= 1
        return self.heap[0]


# ================================================================== tests
def _build_list(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def _to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert sorted(map(sorted, group_anagrams(["eat", "tea", "tan", "ate", "nat"]))) == [
        ["ate", "eat", "tea"],
        ["nat", "tan"],
    ]
    assert subarray_sum_equals_k([1, 2, 3], 3) == 2
    assert subarray_sum_equals_k([1, 2, 3, -3, 3], 3) == 5
    assert range_add(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]) == [-2, 0, 3, 5, 3]
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert longest_at_most_k_distinct("eceba", 2) == 3
    assert subarrays_exactly_k_distinct([1, 2, 1, 2, 3], 2) == 7
    assert next_greater([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    assert largest_rectangle([2, 1, 5, 6, 2, 3]) == 10
    assert window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6], []]) == [
        1,
        1,
        2,
        3,
        4,
        4,
        5,
        6,
    ]
    mf = MedianFinder()
    for val, want in [(5, 5), (15, 10), (1, 5), (3, 4)]:
        mf.add(val)
        assert mf.median() == want
    assert merge_intervals([[1, 3], [8, 10], [2, 6], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert max_overlap_sweep([[1, 4], [4, 5], [2, 3]]) == 2
    assert min_arrows([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert _to_list(reverse_list(_build_list([1, 2, 3]))) == [3, 2, 1]
    assert middle_node(_build_list([1, 2, 3, 4, 5])).val == 3
    looped = _build_list([1, 2, 3])
    looped.next.next.next = looped.next
    assert has_cycle(looped) and not has_cycle(_build_list([1, 2]))
    cache_ = LRUCache(2)
    cache_.put(1, 1)
    cache_.put(2, 2)
    assert cache_.get(1) == 1
    cache_.put(3, 3)  # evicts 2
    assert cache_.get(2) == -1 and cache_.get(3) == 3
    tm = TimeMap()
    tm.set("bowl", "full", 1)
    tm.set("bowl", "half", 4)
    assert tm.get("bowl", 3) == "full" and tm.get("bowl", 5) == "half"
    assert tm.get("bowl", 0) == ""

    p, q = TreeNode(5), TreeNode(1)
    root = TreeNode(3, p, q)
    p.left, p.right = TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))
    assert diameter(root) == 4
    assert lca(root, p.right.right, p.left) is p
    assert level_order(root) == [[3], [5, 1], [6, 2], [7, 4]]

    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert min_obstacles_0_1_bfs([[0, 1, 1], [1, 1, 0], [1, 1, 0]]) == 2
    assert has_cycle_directed(3, [[0, 1], [1, 2], [2, 0]])
    assert not has_cycle_directed(3, [[0, 1], [0, 2], [1, 2]])
    assert (
        num_islands([list("11000"), list("11000"), list("00100"), list("00011")]) == 3
    )
    assert topo_sort(4, [[0, 1], [0, 2], [1, 3], [2, 3]]) == [0, 1, 2, 3]
    assert topo_sort(2, [[0, 1], [1, 0]]) == []
    dsu = DSU(5)
    assert dsu.union(0, 1) and dsu.union(1, 2) and not dsu.union(0, 2)
    assert dsu.components == 3
    assert dijkstra(4, [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1]], 0) == [0, 3, 1, 4]
    assert kruskal(4, [[0, 1, 1], [1, 2, 2], [0, 2, 3], [2, 3, 4]]) == 7

    assert len(subsets([1, 2, 3])) == 8
    assert sorted(permutations([1, 2, 3])) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert combination_sum2([10, 1, 2, 7, 6, 1, 5], 8) == [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6],
    ]

    assert rob([2, 7, 9, 3, 1]) == 12
    assert coin_change([1, 2, 5], 11) == 3 and coin_change([2], 3) == -1
    assert can_partition([1, 5, 11, 5]) and not can_partition([1, 2, 3, 5])
    assert lcs("abcde", "ace") == 3
    assert edit_distance("horse", "ros") == 3
    assert lis_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert matrix_chain([10, 30, 5, 60]) == 4500
    assert max_profit_with_fee([1, 3, 2, 8, 4, 9], 2) == 8
    assert min_assignment_cost([[9, 2, 7], [6, 4, 3], [5, 8, 1]]) == 9

    t = Trie()
    t.insert("apple")
    assert t.search("apple") and not t.search("app") and t.starts_with("app")
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert bit_tricks(8)["is_power_of_two"] and bit_tricks(12)["lowest_set_bit"] == 4
    assert count_smaller_after_self([5, 2, 6, 1]) == [2, 1, 1, 0]
    assert primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    sl = SortedListLite()
    for num in [5, 1, 4, 1]:
        sl.add(num)
    sl.remove(4)
    assert sl.a == [1, 1, 5] and sl.count_less(5) == 2
    lh = LazyMinHeap()
    for num in [3, 1, 2]:
        lh.push(num)
    lh.remove(1)
    assert lh.top() == 2

    print("all templates pass")
