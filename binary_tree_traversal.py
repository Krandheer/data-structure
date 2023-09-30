from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_order(root):
    if not root:
        return
    result = []

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def inorder_traversal(root, result):
    if not root:
        return
    inorder_traversal(root.left, result)
    result.append(root.value)
    inorder_traversal(root.right, result)
    return result


def preorder_traversal(root, result):
    if not root:
        return
    result.append(root.value)
    preorder_traversal(root.left, result)
    preorder_traversal(root.right, result)
    return result


def postorder_traversal(root, result):
    if not root:
        return
    postorder_traversal(root.left, result)
    postorder_traversal(root.right, result)
    result.append(root.value)
    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Level order traversal:")
# print(level_order(root))

print(inorder_traversal(root, []))

# TODO: lca ( least common ancestor) need to write code for this for bst and bt
