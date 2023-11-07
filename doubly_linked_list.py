class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class dll:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node

    def __repr__(self) -> str:
        current = self.head
        nodes = []

        while current:
            nodes.append(f"{current.data}")
            current = current.next
        return "-><-".join(nodes)


dll = dll()
dll.insert_at_start(20)
dll.insert_at_start(10)
dll.insert_at_start(30)
print(dll)
