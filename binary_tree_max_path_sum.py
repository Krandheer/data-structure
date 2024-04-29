from typing import Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.ans = -math.inf

        def helper(root):
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)
            left = max(0, left)
            right = max(0, right)
            temp = left + right + root.val
            self.ans = max(self.ans, temp)
            return max(left, right) + root.val

        helper(root)
        return self.ans
