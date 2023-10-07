"""
minimum step needed to reach e from s
this works because it is using the single source shortest path concept of graph
using bfs
"""

from collections import deque

grid = [
    ["s", "n", "p", "p", "p"],
    ["p", "p", "p", "n", "p"],
    ["p", "n", "n", "n", "p"],
    ["p", "n", "e", "p", "p"],
]


def is_valid(graph, visited, x, y):
    row = len(graph)
    col = len(graph[0])
    if (
        x < 0
        or y < 0
        or x >= row
        or y >= col
        or visited[x][y] == 1
        or graph[x][y] == "n"
    ):
        return False
    return True


def bfs(graph, start_node, end_node, distance, visited):
    i, j = start_node[0], start_node[1]
    queue = deque()
    queue.append(start_node)
    distance[i][j] = 0
    visited[i][j] = 1
    while queue:
        k, l = queue.popleft()
        for u, v in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            if is_valid(graph, visited, k + u, l + v):
                queue.append((k + u, l + v))
                visited[k + u][l + v] = 1
                distance[k + u][l + v] = distance[k][l] + 1
    m, n = end[0], end[1]
    print(distance[m][n])


visited = []
distance = []
for i in range(len(grid)):
    temp = []
    dis = []
    for j in range(len(grid[0])):
        temp.append(0)
        dis.append(-1)
    visited.append(temp)
    distance.append(dis)

# find the starting node and ending node
start = ()
end = ()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "s":
            start = (i, j)
        if grid[i][j] == "e":
            end = (i, j)


bfs(grid, start, end, distance, visited)
