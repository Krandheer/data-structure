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

    def search(self, data):
        if self.is_empty():
            return False
        elif self.tail.next == self.tail and self.tail.data == data:
            return True
        else:
            temp = self.tail.next
            while temp != self.tail:
                if temp.data == data:
                    return True
                temp = temp.next
            if self.tail.data == data:
                return True
        return False

    def delete_at_start(self):
        if self.is_empty():
            pass
        else:
            if self.tail.next == self.tail:
                self.tail = None
            else:
                self.tail.next = self.tail.next.next

    def delete_at_end(self):
        # find one before the tail
        if self.is_empty():
            pass
        else:
            if self.tail.next == self.tail:
                self.tail = None
            else:
                temp = self.tail.next
                while temp.next != self.tail:
                    temp = temp.next
                temp.next = self.tail.next
                self.tail = temp

    def delete_data(self, data):
        if self.is_empty():
            pass
        if self.tail.next == self.tail and self.tail.data == data:
            self.tail = None
        else:
            temp = self.tail.next
            if temp.data == data:
                self.tail.next = temp.next
            else:
                while temp != self.tail:
                    if temp.next.data == data and temp.next != self.tail:
                        temp.next = temp.next.next
                    elif temp.next.data == data and temp.next == self.tail:
                        temp.next = temp.next.next
                        self.tail = temp
                    temp = temp.next

    def __repr__(self) -> str:
        node = []
        if self.is_empty():
            pass
        else:
            head = self.tail.next
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

# mylist.delete_at_start()
# mylist.delete_at_end()
mylist.delete_data(10)
# print(mylist.search(60))
print(mylist)
