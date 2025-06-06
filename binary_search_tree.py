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
        if not self.root:
            return -1
        return self._height(self.root)

    def _height(self, curr_node):
        if curr_node is None:
            return -1
        left_height = self._height(curr_node.left_child)
        right_height = self._height(curr_node.right_child)
        return max(left_height, right_height) + 1

    def search(self, value):
        if self.root:
            return self._search(value, self.root)
        return False

    def _search(self, value, curr_node):
        if value == curr_node.value:
            return True
        if value < curr_node.value and curr_node.left_child:
            self._search(value, curr_node.left_child)
        elif value > curr_node.value and curr_node.right_child:
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
print(bst.height())
# bst.print_tree()
