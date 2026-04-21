from typing import List


def find(graph: List[int], node: int):
    """
    Finds the representative (or parent) of the set that a given node belongs to.
    This function implements the "find" operation in the Disjoint Set Union (DSU) or Union-Find data structure.
    It recursively traverses the graph to find the root parent of the given node. If the node is its own parent
    (indicated by a negative value in the graph), it returns the node itself.

    Args:
        graph (list[int]): The disjoint set data structure represented as a list, where each index represents a node.
                        A negative value at an index indicates the size of the set (as a negative number) and that
                        the node is a root parent.
        node (int): The node whose parent is to be found.

    Returns:
        int: The representative (or root parent) of the set that the node belongs to.
    """

    if graph[node] < 0:
        return node
    else:
        return find(graph, graph[node])


def union(graph: List[int], u: int, v: int, ans: List[List[int]]):
    a = find(graph, u)
    b = find(graph, v)

    if a == b:
        print(f"can't add, it's already part of the family,{u}, {v} ")
        ans.append([u, v])
    else:
        if graph[a] == graph[b]:
            # b becomes parent and a points to b
            graph[b] = graph[a] + graph[b]
            graph[a] = b
        elif graph[a] < graph[b]:
            # a becomes parent and b points to a
            graph[a] = graph[a] + graph[b]
            graph[b] = a
        else:
            graph[b] = graph[a] + graph[b]
            graph[a] = b
    return ans


n = 6
# graph = {}
# for i in range(7):
#     graph[i] = -1
graph = [-1] * 6
# ipt = [[0, 1], [1, 2], [2, 3], [4, 5], [1, 3]]
ipt = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
ans = []
for u, v in ipt:
    ans = union(graph, u, v, ans)
print(ans)
# print(graph)
