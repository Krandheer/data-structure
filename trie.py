class Node:
    def __init__(self):
        self.links = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for i in word:
            if word not in node.links:
                node.links[i] = Node()
            node = node.links[i]
        node.is_end = True

    def search(self, word):
        node = self.root
        if node:
            for i in word:
                if i not in node.links:
                    return False
                node = node.links[i]
        return node.is_end

    def print_trie(self, node=None, prefix=""):
        if node is None:
            node = self.root

        for char, child in node.links.items():
            current_word = prefix + char
            print(f"current word: {current_word} End of wordk: {child.is_end}")
            if child.is_end:
                print(current_word)
            self.print_trie(child, current_word)


tri = Trie()
tri.insert("tty")
print(tri.search("tty"))
# tri.print_trie()
