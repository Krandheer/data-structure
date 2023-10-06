from collections import deque


def bfs(graph, start, visited=None):
    if not visited:
        visited = set()
    visited.add(start)
    queue = deque([start])
    distance = {}
    distance[start] = 0

    while queue:
        node = queue.popleft()
        # print(node)
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)
                distance[child] = distance[node] + 1
    print(f"distance: {distance}")


def adjancy_list_rep(graph, node):
    g = {}
    for i in range(node):
        g[i] = []

    for u, v in graph:
        g[u].append(v)
        g[v].append(u)

    return g


ipt = [
    [1, 2],
    [2, 3],
    [1, 3],
    [1, 4],
    [1, 6],
    [3, 6],
    [1, 8],
    [1, 7],
    [8, 9],
    [7, 9],
    [3, 4],
    [3, 5],
]


graph = adjancy_list_rep(ipt, 10)
bfs(graph, 9)
