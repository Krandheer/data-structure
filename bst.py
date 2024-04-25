"""
python implementation of binary tree: https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
https://www.youtube.com/watch?v=18YDhu9IFws&list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l&index=42&ab_channel=Amulya%27sAcademy
"""


class BST:
    def __init__(self, data):
        """
        first create the root node
        """
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        """
        if no root present then add at top means root
        """
        if not self.data:
            self.data = data

        if self.data == data:
            # avoid duplicate insertion
            return

        if self.data < data:
            # add to right subtree
            if self.right_child is None:
                self.right_child = BST(data)
            else:
                self.right_child.insert(data)
        else:
            # add to left subtree
            if self.left_child is None:
                self.left_child = BST(data)
            else:
                self.left_child.insert(data)

    def search(self, data):
        if self.data == data:
            print("found")
            return
        if self.data < data:
            if self.right_child is None:
                print("not found")
                return
            else:
                self.right_child.search(data)
        else:
            if self.left_child is None:
                print("not found")
                return
            else:
                self.left_child.search(data)

    def preorder(self):
        print(self.data)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.data)
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.data)

    def delete(self, data):
        """
        currently this doesn't work for root node, but that also can be easily achieved
        """
        if self.data is None:
            print("tree is empty")
            return
        if data < self.data:
            if self.left_child:
                self.left_child = self.left_child.delete(data)
            else:
                print("data is not present")
        elif data > self.data:
            if self.right_child:
                self.right_child = self.right_child.delete(data)
            else:
                print("data is not present")
        else:
            if self.left_child is None:
                temp = self.right_child
                self = None
                return temp
            if self.right_child is None:
                temp = self.left_child
                self = None
                return temp

            node = self.right_child
            while node.left_child:
                node = node.left_child
            self.data = node.data
            self.right_child = self.right_child.delete(node.data)
        return self
