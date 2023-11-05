class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"node: {self.data}"


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.next
        return count

    def insert_at_start(self, data):
        """
        adds new node containing data at head of linked list
        takes O(1) time
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def __repr__(self):
        current = self.head
        nodes = []

        while current:
            nodes.append(f"{current.data}")
            current = current.next

        return "->".join(nodes)

    def search(self, key):
        """
        return: True if the key is found otherwise False
        """
        current = self.head
        if current.data == key:
            return True
        while current:
            if current.next and current.next.data == key:
                return True
            current = current.next
        return False

    def insert(self, data, index):
        if index == 0:
            self.insert_at_start(data)

        if index > 0:
            position = index
            current = self.head
            new = Node(data)

            while position > 1:
                current = current.next
                position -= 1

            prev_node = current
            next_node = current.next
            prev_node.next = new
            new.next = next_node
