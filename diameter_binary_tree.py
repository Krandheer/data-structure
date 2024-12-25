from typing import Optional

"""
Note: give an acyclic graph/tree, the farthest distance from any node is the one end of the diameter of the tree/graph.
and now when you find farthest distance from that node, the farthest distance from that node is the other end of the 
diameter of the tree/graph. to use this we need to convert tree to graph, basically adjacency list
and then find the diameter of the graph.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.root = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    d = 0

    def height(node):
        nonlocal d

        if not node:
            return -1

        left_h = height(node.left)
        right_h = height(node.right)

        d = max(d, left_h + right_h + 2)

        return max(left_h, right_h) + 1

    height(root)
    return d
