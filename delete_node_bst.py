# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        node = root

        # this will handle only root of the tree
        if root.val == key:
            return self.helper(root)

        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    # the node to be removed passed
                    root.left = self.helper(root.left)
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.helper(root.right)
                else:
                    root = root.right
        return node

    def helper(self, node):
        if not node.right:
            return node.left
        if not node.left:
            return node.right

        # if not returned by now that means root.left and root.right both there
        # take the right child and attach it to extreme right node of node.left subtree

        rightchild = node.right
        lastright = self.find_last_right(node.left)
        lastright.right = rightchild
        return node.left

    def find_last_right(self, node):
        while node.right:
            node = node.right
        return node
