def dfs_cycle(graph, node, visited, current_path, par):
    """
    simple as undirected graph but here we need to check whether the current
    node is already present in the path or not. For that we are using current_path map
    """
    visited[node] = True
    current_path[node] = True
    for child in graph[node]:
        if not visited[child]:
            current_path[child] = True
            visited[child] = True
            if dfs_cycle(graph, child, visited, current_path, node):
                return True
        elif child != par and par != -1 and current_path[par]:
            return True
        current_path[child] = False
    return False


graph = {0: [1], 1: [], 2: [1, 3], 3: [4], 4: [0, 2]}

visited = {}
current_path = {}
for i in range(5):
    visited[i] = False
    current_path[i] = False

for i in graph:
    if not visited[i]:
        if dfs_cycle(graph, i, visited, current_path, -1):
            print(True)
