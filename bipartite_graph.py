graph = {
    1: [3],
    2: [1, 3, 6],
    3: [2, 4],
    4: [3, 7, 5],
    5: [4, 6],
    6: [2, 5],
    7: [4, 8],
    8: [7],
}

color = []
for i in range(9):
    color.append(-1)


# if graph has no cycle then it will always be bipartite, if graph has cycle
# and cycle length is odd then it will not be bipartite
def dfs(graph, node, col, color):
    color[node] = col

    for child in graph[node]:
        if color[child] == -1:
            if not dfs(graph, child, 1 - col, color):
                return False
        elif color[child] == color[node]:
            return False
    return True


print(dfs(graph, 1, 0, color))
