from bisect import bisect_left
from collections import defaultdict
from functools import lru_cache
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def subtreeWithAllDeepest(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(node):
        if not node:
            return (0, None)

        left_depth, left_node = dfs(node.left)
        right_depth, right_node = dfs(node.right)

        if left_depth > right_depth:
            return (left_depth + 1, left_node)
        if right_depth > left_depth:
            return (right_depth + 1, right_node)
        return (left_depth + 1, node)

    return dfs(root)[1]


def minimumDeleteSum(s1: str, s2: str) -> int:
    def dfs(i, j):
        if i == len(s1):
            return sum(ord(char) for char in s2[j:])
        if j == len(s2):
            return sum(ord(char) for char in s1[i:])

        if s1[i] != s2[j]:
            return min(
                ord(s1[i]) + ord(s2[j]) + dfs(i + 1, j + 1),
                ord(s1[i]) + dfs(i + 1, j),
                ord(s2[j]) + dfs(i, j + 1),
            )
        else:
            return dfs(i + 1, j + 1)

    return dfs(0, 0)


def maximalRectangle(matrix: List[List[str]]) -> int:
    ans = 0
    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                heights[j] += 1
            else:
                heights[j] = 0

        stack = []
        for j in range(n + 1):
            curr_height = heights[j] if j < n else 0
            while stack and curr_height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = j if not stack else j - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(j)
    return ans


def maximizeSquareHoleArea(n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
    h_con = 1
    v_con = 1
    max_h = 1
    max_v = 1
    hBars.sort()
    vBars.sort()
    for ind in range(1, len(hBars)):
        if hBars[ind - 1] + 1 == hBars[ind]:
            h_con += 1
        else:
            h_con = 1
        max_h = max(max_h, h_con)

    for ind in range(1, len(vBars)):
        if vBars[ind - 1] + 1 == vBars[ind]:
            v_con += 1
        else:
            v_con = 1
        max_v = max(max_v, v_con)

    side = min(max_h, max_v) + 1
    return side * side


# print(maximizeSquareHoleArea(3, 2, [3, 2, 4], [3, 2]))


def minBitwiseArray(nums: List[int]) -> List[int]:
    ans = []
    for i in range(len(nums)):
        temp = -1
        for j in range(1001):
            if nums[i] == j | (j + 1):
                temp = j
                break
        ans.append(temp)
    return ans


def minimumDifference(nums: List[int], k: int) -> int:
    nums.sort()
    l, r = 0, k - 1
    ans = 0
    while r < len(nums):
        ans = min(ans, nums[r] - nums[l])
        l += 1
        r += 1

    return ans


class Solution:
    def minimumDistance(self, word: str) -> int:
        char_map = defaultdict(tuple)
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        k = 0
        for i in range(6):
            for j in range(6):
                char_map[chars[k]] = (i, j)
                k += 1
                if k == 26:
                    break
            if k == 26:
                break

        def calc_dist(c1, c2):
            x1, y1 = c1
            x2, y2 = c2
            return abs(x1 - x2) + abs(y1 - y2)

        @lru_cache(maxsize=None)
        def solve(ind: int, f1: str, f2: str) -> int:
            if ind >= len(word):
                return 0

            if f1 != "" and f2 != "":
                return min(
                    (
                        calc_dist(char_map[f1], char_map[word[ind]])
                        + solve(ind + 1, word[ind], f2)
                    ),
                    (
                        calc_dist(char_map[f2], char_map[word[ind]])
                        + solve(ind + 1, f1, word[ind])
                    ),
                )
            elif f1 != "" and f2 == "":
                return min(
                    (
                        calc_dist(char_map[f1], char_map[word[ind]])
                        + solve(ind + 1, word[ind], f2)
                    ),
                    solve(ind + 1, f1, word[ind]),
                )
            elif f1 == "" and f2 != "":
                return min(
                    (
                        calc_dist(char_map[f2], char_map[word[ind]])
                        + solve(ind + 1, f1, word[ind])
                    ),
                    solve(ind + 1, word[ind], f2),
                )
            else:
                return min(solve(ind + 1, word[ind], f2), solve(ind + 1, f1, word[ind]))

        return solve(0, "", "")


def minMirrorPairDistance(nums: List[int]) -> int:
    ans = 10**9
    seen = {}
    for ind, num in enumerate(nums):
        if num in seen:
            j = seen[num]
            ans = min(ans, abs(j - ind))

        mirror = 0
        while num >= 0:
            num, rem = divmod(num, 10)
            mirror = mirror * 10 + rem
        seen[mirror] = ind
    return ans if ans != 10**9 else -1


def mirrorDistance(n: int) -> int:
    mirror = 0
    temp = n
    while temp > 0:
        temp, rem = divmod(temp, 10)
        mirror = mirror * 10 + rem

    return abs(n - mirror)


def countAndSay(n: int) -> str:
    def rle(words: str) -> str:
        prev = words[0]
        ans = ""
        count = 0
        for ch in words:
            if ch != prev:
                ans = ans + f"{count}{prev}"
                count = 0
                prev = ch
            count += 1
        return ans + f"{count}{prev}"

    if n == 1:
        return "1"
    ans = "1"
    for i in range(2, n + 1):
        ans = rle(ans)
    return ans


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    ans = []

    def solve(ind, target, temp):
        if target == 0:
            # copy the array not reference to the array
            ans.append(temp[:])
            return
        if ind >= len(candidates) or target < 0:
            return

        # take case
        temp.append(candidates[ind])
        solve(ind, target - candidates[ind], temp)
        temp.pop()

        # skip case
        solve(ind + 1, target, temp)

    solve(0, target, [])
    return ans


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    ans = []
    candidates.sort()

    def solve(ind, target, temp):
        if target == 0:
            ans.append(temp[:])
            return
        for i in range(ind, len(candidates)):
            if i > ind and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                break
            # take case
            temp.append(candidates[i])
            solve(i + 1, target - candidates[i], temp)
            temp.pop()

    solve(0, target, [])
    return ans


def solveQueries(nums: List[int], queries: List[int]) -> List[int]:
    freq = defaultdict(list)
    for ind, num in enumerate(nums):
        freq[num].append(ind)
    n = len(nums)
    ans = []
    for q in queries:
        t = nums[q]
        lookup = freq[t]
        if len(lookup) == 1:
            ans.append(-1)
            continue

        pos = bisect_left(lookup, q)
        temp = float("inf")

        # Check next neighbor (with wrap-around)
        next_pos = (pos + 1) % len(lookup)
        d = abs(lookup[next_pos] - q)
        temp = min(temp, d, n - d)

        # Check prev neighbor (with wrap-around)
        prev_pos = (pos - 1) % len(lookup)
        d = abs(lookup[prev_pos] - q)
        temp = min(temp, d, n - d)

        ans.append(temp)
    return ans


print(solveQueries([1, 3, 1, 4, 1, 3, 2], [0, 3, 5]))
