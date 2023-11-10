class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.item_count = 0

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.item_count += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            raise IndexError("Empty stack")

    def peek(self):
        if not self.is_empty():
            data = self.head.data
            return data
        else:
            raise IndexError("empty stack")


s = Stack()
s.push(30)
s.push(20)
s.push(10)
print("pop: ", s.pop())
print("pop: ", s.pop())
print("peek: ", s.peek())
