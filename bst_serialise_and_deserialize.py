# Definition for a binary tree node.
import json

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        def level_order(root):
            temp = {}
            if not root:
                return temp
            queue = deque()
            queue.append((root, 0))
            while queue:
                node, level = queue.popleft()
                if level not in temp:
                    temp[level] = [node.val]
                else:
                    temp[level].append(node.val)
                if node.left:
                    queue.append((node.left, level + 1))
                elif (level + 1) not in temp:
                    temp[level + 1] = ["#"]
                else:
                    temp[level + 1].append("#")
                if node.right:
                    queue.append((node.right, level + 1))
                elif (level + 1) not in temp:
                    temp[level + 1] = ["#"]
                else:
                    temp[level + 1].append("#")
            return temp

        temp = level_order(root)
        result = []
        for v in temp.values():
            result += v
        return json.dumps(result)

    def deserialize(self, data):
        data = eval(data)
        if not data:
            return
        queue = deque()
        root = TreeNode(data[0])
        queue.append((root, 0))
        while queue:
            node, index = queue.pop()
            if data[2 * index + 1] != "#":
                node.left = TreeNode(data[2 * index + 1])
                queue.append((node.left, index + 1))
            if data[2 * index + 2] != "#":
                node.right = TreeNode(data[2 * index + 2])
                queue.append((node.right, index + 2))
        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
sl = Codec()
data = sl.serialize(root)
print(data)
root = sl.deserialize(data)
print(sl.serialize(root))
