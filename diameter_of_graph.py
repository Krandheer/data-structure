def adjancy_list_rep(graph, node):
    """adjacency list representation of graph"""
    g = {}
    for j in range(1, node):
        g[j] = []

    for u, v in graph:
        g[u].append(v)
        g[v].append(u)

    return g


def dfs(graph, node, visited=None):
    """this function calculates the diameter of graph using dfs method"""
    if not visited:
        visited = set()
    visited.add(node)
    temp = 0
    for child in graph[node]:
        if child not in visited:
            temp = max(temp, dfs(graph, child, visited))

    return temp + 1


ipt = [[1, 2], [2, 4], [2, 5], [2, 6], [1, 3], [3, 7], [1, 8], [6, 10], [1, 9]]
graph = adjancy_list_rep(ipt, 11)
# result = dfs(graph_1, 3, {})
# print(result)

# find the diameter by iterating on all node.
"""
Instead of doing below things, we could just take any random node, find the farthest distance node using bfs
and then using that node find the next end of diameter which will also give the diameter of the graph.
"""
max_r = 0
for i in range(1, 11):
    result = dfs(graph, i, set())
    if result > max_r:
        max_r = result
print(max_r)
