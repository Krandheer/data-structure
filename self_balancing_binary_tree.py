class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


class sbbtree_node(Node):
    def __init__(self, value=None):
        self.root = value

    def get_height(self, node):
        if node:
            return node.height

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, curr_node):
        if curr_node and value < curr_node.value:
            if not curr_node.left:
                curr_node.left = Node(value)
                curr_node.height = curr_node.height + 1
            else:
                curr_node.height = curr_node.height + 1
                self._insert(value, curr_node.left)
        elif curr_node and value > curr_node.value:
            if not curr_node.right:
                curr_node.right = Node(value)
                curr_node.height = curr_node.height + 1
            else:
                curr_node.height = curr_node.height + 1
                self._insert(value, curr_node.right)

    # inorder traversal
    def print_tree(self):
        if not self.root:
            print(-1)
        else:
            self._print(self.root)

    def _print(self, curr_node):
        if curr_node:
            if curr_node.left:
                self._print(curr_node.left)
            print(curr_node.value, curr_node.height)
            if curr_node.right:
                self._print(curr_node.right)


sbb = sbbtree_node()
sbb.insert(40)
sbb.insert(35)
sbb.insert(45)
sbb.insert(30)

sbb.print_tree()
