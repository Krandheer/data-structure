import math


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

    def __repr__(self) -> str:
        return self._repr_helper(self.root, 0)

    def _repr_helper(self, node, depth):
        if not node.links:
            return "end"
        else:
            lines = []
            for bit, child in node.links.items():
                lines.append("  " * depth + f"Bit {bit}:")
                lines.append(self._repr_helper(child, depth + 1))
            return "\n".join(lines)

    # def prprint(self):
    #     node = self.root
    #     result = []
    #     count = 0
    #     while node.links:
    #         for key, n in node.links.items():
    #             result.append(" " * count + f"{key}")
    #             count += 1
    #         node = n
    #     print("\n".join(result))


def get_max_xor(nums):
    tri = Trie()
    for num in nums:
        tri.insert(num)
    max_xor = -math.inf
    for num in nums:
        node = tri.root
        current_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if (1 - bit) in node.links:
                current_xor += 1 << i
                node = node.links[1 - bit]
            else:
                node = node.links[bit]
        max_xor = max(max_xor, current_xor)
    return max_xor


t = Trie()
numbers = [3, 10, 5, 25, 2, 8]
# for num in numbers:
#     t.insert(num)
# t.insert(4)
# print(t.__repr__())
# t.prprint()
print(get_max_xor(numbers))
