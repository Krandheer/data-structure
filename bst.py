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
            print('found')
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

