from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# this iterator works as inorder traversal,
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushAll(root, self.stack)

    def next(self) -> int:
        if self.stack:
            node = self.stack.pop()
            if node.right:
                self.pushAll(node.right, self.stack)
            return node.val
        return -1

    def pushAll(self, node, stack):
        if node:
            stack.append(node)
        if node.left:
            self.pushAll(node.left, stack)

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False
