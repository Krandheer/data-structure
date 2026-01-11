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
