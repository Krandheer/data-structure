from collections import deque, defaultdict

"""
preorder, postorder, inorder all of these methods are depth first searches.
level order is breadth first search for tree.
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_order(root):
    if not root:
        return
    result = {}

    queue = deque()
    queue.append((root, 0))

    while queue:
        node, level = queue.popleft()
        if level not in result:
            result[level] = [node.value]
        else:
            result[level].append(node.value)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return result


def level_order2(root):
    if not root:
        return
    result = []

    queue = deque()
    queue.append(root)

    while queue:
        size = len(queue)
        temp = []
        for i in range(size):
            node = queue.popleft()
            temp.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(temp)
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


# iierative preorder traversal
def preorder_traversal2(root):
    if not root:
        return
    stack = []
    result = []
    stack.append(root)

    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
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

print(preorder_traversal(root, []))
print(preorder_traversal2(root))
# print(level_order2(root))
# result = level_order(root)
# final_res = []
# for k, v in result.items():
#     final_res.append(v)
# print(final_res)


# TODO: lca ( least common ancestor) need to write code for this for bst and bt
