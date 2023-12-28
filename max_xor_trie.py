class TrieNode:
    def __init__(self):
        self.links = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.links:
                node.links[bit] = TrieNode()
            node = node.links[bit]

    # def __repr__(self) -> str:
    #     return self._repr_helper(self.root, 0)

    # def _repr_helper(self, node, depth):
    #     if not node.links:
    #         return "end"
    #     else:
    #         lines = []
    #         for bit, child in node.links.items():
    #             lines.append("  " * depth + f"Bit {bit}:")
    #             lines.append(self._repr_helper(child, depth + 1))
    #         return "\n".join(lines)

    def prprint(self):
        node = self.root
        while node.links:
            for key, n in node.links.items():
                print(key)
            node = n


t = Trie()
t.insert(4)
# print(t.__repr__())
t.prprint()
