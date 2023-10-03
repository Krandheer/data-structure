"""
cycle detection in undirected graph, this same can be done using dfs as well.
the concept is that when you fall on visited node then it should not be parent and if so then there is cycle.
"""

from collections import deque

ipt = [[1, 2], [1, 3], [2, 3], [2, 4], [4, 5], [5, 1]]
n = 5


def adjancy_list_rep(graph, node):
    g = {}
    for i in range(node):
        g[i] = []

    for u, v in graph:
        g[u].append(v)
        g[v].append(u)

    return g


graph = adjancy_list_rep(ipt, n + 1)


def bfs_cycle(graph, node, par, visited=None):
    queue = deque()
    queue.append((node, par))
    if not visited:
        visited = set()
    visited.add(node)

    while queue:
        node, par = queue.popleft()
        for child in graph[node]:
            if child not in visited:
                queue.append((child, node))  # Append a tuple (child, node)
                visited.add(child)
            else:
                if child != par:
                    return True
    return False


def dfs_cycle(graph, node, par, visited=None):
    if not visited:
        visited = set()
    visited.add(node)

    for child in graph[node]:
        if child in visited:
            return dfs_cycle(graph, child, node, visited)
        elif child != par:
            return True
    return False


print(dfs_cycle(graph, 1, -1))
print(bfs_cycle(graph, 1, -1))
