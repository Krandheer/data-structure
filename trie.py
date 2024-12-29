class Node:
    def __init__(self):
        self.links = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.links:
                node.links[ch] = Node()
            node = node.links[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        if node:
            for ch in word:
                if ch not in node.links:
                    return False
                node = node.links[ch]
        return node.is_end

    def matching_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.links:
                return False
            node = node.links[ch]
        return True

    def print_trie(self, node=None, prefix=""):
        if node is None:
            node = self.root

        for char, child in node.links.items():
            current_word = prefix + char
            # print(f"current word: {current_word} End of wordk: {child.is_end}")
            if child.is_end:
                print(current_word)
            self.print_trie(child, current_word)


tri = Trie()
words = ["apple", "apple", "app", "banana", "bat", "batman"]
for word in words:
    tri.insert(word)
tri.print_trie()
