class Node:
	def __init__(self, value=None):
		self.value = None
		self.left_child = None
		self.right_child = None

class Binary_search_tree:
	def __init__(self):
		self.root = None

	#add element to binary search tree
	#assuming the values are integer
	def insert(self, value):
		if(self.root = None):
			self.root = Node(value)

		else:
			self._insert(value, self.root)

	def _insert(self, value, curr_node):
		if (value< curr_node.value):
			if(curr_node.left_child==None):
				curr_node.left_child=Node(value)
			else:
				self._insert(value, curr_node.left_child)
		elif(value>curr_node.value):
			if (curr_node.right_child==None):
				curr_node.right_child=Node(value)
			else:
				self._insert(value, curr_node.right_child)
		else:
			print("value is already in tree, try any other value")


	def height(self):
		if(self.root!=None):
			return self._height(self.root, 0)
		else:
			return 0
	def _height(self, curr_node, curr_height):
		if (curr_node == None):
			return curr_height
		left_height = self._height(curr_node.left_child, curr_height+1)
		right_height = self._height(curr_node.right_child, curr_height+1)
		return max(left_child, right_height)

	def search(self, value):
		if (self.root!=None):
			return self._search(value, self.root)
		else:
			False
	def _search(self, value, curr_node):
		if (value == curr_node.value):
			return True
		elif (value<curr_node.value and curr_node.left_child != None):
			self._search(value, curr_node.left_child)
		elif (value>curr_node.value and curr_node.right_child != None):
			self._search(value, curr_node.right_child)
		else:
			return False

	#printing tree in form of inorder traversal
	def print_tree(self):
		if (self.root==None):
			print("tree is empty")
		else:
			print(self._print_tree(self.root))

	def _print_tree(self, curr_node):
		if(curr_node!=None):
			self._print_tree(curr_node.left_child)
			print(str(curr_node.value))
			self._print_tree(curr_node.right_child)







