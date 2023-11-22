class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


class sbbtree_node(Node):
    def __init__(self, value=None):
        self.root = value
