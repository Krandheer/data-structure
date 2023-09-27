from collections import defaultdict
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def vertical_order_traversal(root):
    if not root:
        return []

    # Create a dictionary to store nodes in each column
    column_map = defaultdict(list)

    # Create a queue to perform BFS
    queue = deque([(root, 0)])  # (node, column)

    # Perform BFS
    while queue:
        node, column = queue.popleft()

        # Add the node to the corresponding column
        column_map[column].append(node.value)

        # Enqueue left and right children with updated columns
        if node.left:
            queue.append((node.left, column - 1))
        if node.right:
            queue.append((node.right, column + 1))

    # Sort the columns by their column number
    sorted_columns = sorted(column_map.items(), key=lambda x: x[0])

    # Extract the values in sorted order
    result = [values for column, values in sorted_columns]

    # print(result)
    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Perform vertical order traversal
vertical_order = vertical_order_traversal(root)
for column in vertical_order:
    print(column)

# you use this same code for upper view of tree just take the first element of
# all column, and for bottom view just take the last elemnt from each column.

# for left and right view use level order traversal and store the element at each list in a
# dictionary with key as level and value of node in list. then first elemnt of each node will
# give left side view and last element will give right side view
