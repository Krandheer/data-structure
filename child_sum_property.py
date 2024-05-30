class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def child_sum_proeprty(root):
    if not root:
        return

    child = 0
    if root.left:
        child += root.left.val

    if root.right:
        child += root.right.val

    if child > root.val:
        root.val = child
    else:
        if root.left:
            root.left.val = root.val
        if root.right:
            root.right.val = root.val
    child_sum_proeprty(root.left)
    child_sum_proeprty(root.right)

    tot = 0
    if root.right:
        tot += root.right.val
    if root.left:
        tot += root.left.val

    if root.left or root.right:
        root.val = tot


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

child_sum_proeprty(root)
inorder(root)
