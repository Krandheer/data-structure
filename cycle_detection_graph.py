"""
cycle detection in undirected graph, this same can be done using dfs as well.
the concept is that when you fall on visited not then it should not parent and if so then there is cycle.
"""

from collections import deque

ipt = [[1, 2], [1, 3], [2, 3], [2, 4], [4, 5], [5, 1]]
n = 5
graph = {}
visited = {}

for i in range(1, n + 1):
    graph[i] = []
    visited[i] = False
for u, v in ipt:
    graph[u].append(v)
    graph[v].append(u)


def bfs_cycle(graph, node, visited, par):
    queue = deque()
    queue.append((node, par))
    visited[node] = True

    while queue:
        node, par = queue.popleft()
        for child in graph[node]:
            if not visited[child]:
                queue.append((child, node))  # Append a tuple (child, node)
                visited[child] = True
            else:
                if child != par:
                    return True
    return False


def dfs_cycle(graph, node, visited, par):
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            if dfs_cycle(graph, child, visited, node):
                return True
        elif child != par:
            return True
    return False


print(dfs_cycle(graph, 1, visited, -1))
print(bfs_cycle(graph, 1, visited, -1))
