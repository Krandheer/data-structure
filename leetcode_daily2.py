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


print(minimumDifference([9, 4, 1, 7], 2))
