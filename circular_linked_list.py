class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Cll:
    def __init__(self):
        self.tail = None

    def is_empty(self):
        return self.tail is None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def __repr__(self) -> str:
        if self.is_empty():
            pass
        else:
            head = self.tail.next
            node = []
            while head != self.tail:
                node.append(f"{head.data}")
                head = head.next
            node.append(f"{self.tail.data}")
        return "->".join(node)


mylist = Cll()
mylist.insert_at_start(30)
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_end(40)
mylist.insert_at_end(50)
print(mylist)
