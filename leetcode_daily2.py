from typing import Optional


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


def monotonic_increasing(arr):
    stack = []
    for i in range(len(arr)):
        while stack and stack[-1] > arr[i]:
            stack.pop()
        stack.append(arr[i])
    return stack


arr = [5, 2, 4, 1, 3]
print(monotonic_increasing(arr))
