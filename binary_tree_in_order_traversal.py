# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return root
        ans = []
        return self.helper(root, ans)

    def helper(self, root, ans=None):
        if ans is None:
            ans = []
        if root:
            self.helper(root.left, ans)
            ans.append(root.val)
            self.helper(root.right, ans)
        return ans
