from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.root = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0

        def height(node):
            nonlocal d
            if not node:
                return 0
            left_h = height(node.left)
            right_h = height(node.right)

            d = max(d, left_h + right_h + 1)

            return max(left_h, right_h) + 1

        height(root)
        return d - 1
