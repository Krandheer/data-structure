def dfs_cycle(graph, node, visited, pathvisited, par):
    visited[node] = True
    pathvisited[node] = True
    for child in graph[node]:
        if not visited[child]:
            pathvisited[child] = True
            visited[child] = True
            if dfs_cycle(graph, child, visited, pathvisited, node):
                return True
        elif child != par and par != -1 and pathvisited[par]:
            return True
        pathvisited[child] = False
    return False


graph = {0: [1], 1: [], 2: [1, 3], 3: [4], 4: [0, 2]}

visited = {}
pathvisited = {}
for i in range(5):
    visited[i] = False
    pathvisited[i] = False

for i in graph:
    if not visited[i]:
        if dfs_cycle(graph, i, visited, pathvisited, -1):
            print(True)

