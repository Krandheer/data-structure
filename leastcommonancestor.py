class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Function to find the lowest common ancestor of two nodes in a binary tree
def lowest_common_ancestor(root, p, q):
    if not root:
        return None

    # If either p or q matches the current node, return the current node
    if root.value == p.value or root.value == q.value:
        return root

    # Recursively search for p and q in the left and right subtrees
    left_lca = lowest_common_ancestor(root.left, p, q)
    right_lca = lowest_common_ancestor(root.right, p, q)

    # If both left_lca and right_lca are not None, it means p and q are found
    # in both left and right subtrees, so the current node is the LCA.
    if left_lca and right_lca:
        return root

    # If either left_lca or right_lca is not None, return it as the LCA.
    return left_lca if left_lca else right_lca


# Example usage:
# Construct a binary tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = TreeNode(5)
q = TreeNode(1)

lca = lowest_common_ancestor(root, p, q)
print("Lowest Common Ancestor:", lca.value)
