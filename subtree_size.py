def adjancy_list_rep(graph, node):
    g = {}
    for i in range(1, node):
        g[i] = []

    for u, v in graph:
        g[u].append(v)
        g[v].append(u)

    return g


def dfs(graph, node, distance, visited=None):
    if not visited:
        visited = set()
    visited.add(node)
    temp = 0
    for child in graph[node]:
        if child not in visited:
            t_temp, _ = dfs(graph, child, distance, visited)
            temp = temp + t_temp

    distance[node] = temp + 1
    return distance[node], distance


ipt = [[1, 2], [2, 4], [2, 5], [2, 6], [1, 3], [3, 7], [1, 8], [6, 10], [1, 9]]
graph = adjancy_list_rep(ipt, 11)

_, result = dfs(graph, 1, {})
print(result)
