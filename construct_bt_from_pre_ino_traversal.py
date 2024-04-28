from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return

        root_val = preorder[0]
        ind = inorder.index(root_val)
        node = TreeNode(root_val)
        node.left = self.buildTree(preorder[1 : ind + 1], inorder[: ind + 1])
        node.right = self.buildTree(preorder[ind + 1 :], inorder[ind + 1 :])
        return node
