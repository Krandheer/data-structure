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

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif self.head.next is None:
            self.head.next = new_node
            new_node.prev = self.head
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def delete_at_start(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

    def delete_at_end(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next.prev = None
            temp.next = None

    def delete_data(self, data):
        if self.head is None:
            pass
        elif self.head.next is None and self.head.data == data:
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                if temp.next.data == data:
                    temp.next.prev = None
                    temp.next.next.prev = temp
                    temp.next = temp.next.next
                    break
                temp = temp.next

    def search(self, data):
        if self.head is None:
            pass
        else:
            temp = self.head
            if temp.data == data:
                return True
            else:
                while temp.next:
                    if temp.data == data:
                        return True
                    temp = temp.next
        return False

    def __repr__(self) -> str:
        current = self.head
        nodes = []

        while current:
            nodes.append(f"{current.data}")
            current = current.next
        return "-><-".join(nodes)


dll = dll()
dll.insert_at_start(30)
dll.insert_at_start(20)
dll.insert_at_start(10)
dll.insert_at_end(40)
dll.insert_at_end(50)
print(dll)
# dll.delete_at_start()
# dll.delete_at_end()
# dll.delete_data(30)
print(dll.search(50))
print(dll)
