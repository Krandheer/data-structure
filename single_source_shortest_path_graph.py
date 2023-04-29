from collections import deque


def bfs(graph, start):
    distance = {}
    visited = set()
    queue = deque([start])
    visited.add(start)
    distance[start] = 0

    while queue:
        node = queue.popleft()
        print(node)
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)
                distance[child] = distance[node]+1
    print(f"distance: {distance}")


ipt = [[1, 2], [2, 3], [1, 3], [1, 4], [1, 6], [3, 6], [1, 8], [1, 7], [8, 9], [7, 9], [3, 4], [3, 5], ]

graph = {}
for i in range(len(ipt) + 1):
    graph[i] = []
for u, v in ipt:
    graph[u].append(v)
    graph[v].append(u)

bfs(graph, 1)
