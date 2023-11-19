class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # assuming the values are integer
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, curr_node):
        if curr_node and value < curr_node.value:
            if curr_node.left_child is None:
                curr_node.left_child = Node(value)
            else:
                self._insert(value, curr_node.left_child)
        elif curr_node and value > curr_node.value:
            if curr_node.right_child is None:
                curr_node.right_child = Node(value)
            else:
                self._insert(value, curr_node.right_child)
        else:
            print("value is already in tree, try any other value")

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, curr_node, curr_height):
        if curr_node is None:
            return curr_height
        left_height = self._height(curr_node.left_child, curr_height + 1)
        right_height = self._height(curr_node.right_child, curr_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            False

    def _search(self, value, curr_node):
        if value == curr_node.value:
            return True
        elif value < curr_node.value and curr_node.left_child is not None:
            self._search(value, curr_node.left_child)
        elif value > curr_node.value and curr_node.right_child is not None:
            self._search(value, curr_node.right_child)
        else:
            return False

    # printing tree in form of inorder traversal
    def print_tree(self):
        if self.root is None:
            print("tree is empty")
        else:
            self._print_tree(self.root)

    def _print_tree(self, curr_node):
        if curr_node:
            if curr_node.left_child:
                self._print_tree(curr_node.left_child)
            print(str(curr_node.value))
            if curr_node.right_child:
                self._print_tree(curr_node.right_child)


bst = BinarySearchTree()
bst.insert(40)
bst.insert(35)
bst.insert(45)
bst.insert(30)
bst.print_tree()
