ipt = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 3], [2, 3], [2, 4], [2, 5], [3, 5]]


def adjancy_list_rep(graph, node):
    g = {}
    for i in range(node):
        g[i] = []

    for i, j in ipt:
        g[i].append(j)
        g[j].append(i)
    return g


def dfs(graph, node, intime, outtime, visited=None):
    if not visited:
        visited = set()
    sm = 0
    print(node)
    visited.add(node)
    intime[node] = sm
    for child in graph[node]:
        if child not in visited:
            sm = sm + dfs(graph, child, intime, outtime, visited)
    sm = sm + 1
    outtime[node] = sm
    return intime, outtime


graph = adjancy_list_rep(ipt, 6)
print(dfs(graph, 0, {}, {}))
