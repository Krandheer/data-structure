def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()

    visited.add(start_node)
    print(start_node)

    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph_1 = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}


# dfs(graph_1, "A")
graph_2 = [
    [1, 2],
    [1, 5],
    [2, 3],
    [2, 4],
    [2, 5],
    [3, 4],
    [3, 6],
    [4, 5],
    [4, 6],
    [5, 6],
]


def adjancy_list_rep(graph, node):
    g = {}
    for i in range(node):
        g[i] = []

    for u, v in graph:
        g[u].append(v)
        g[v].append(u)

    return g


graph_2 = adjancy_list_rep(graph_2, 7)
# dfs(graph_2, 1)
# for key, value in graph_2.items():
#     print(key, "->", value)

# ipt = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 3], [2, 3], [2, 4], [2, 5], [3, 5]]
# graph = adjancy_list_rep(ipt, 6)
# dfs(graph, 0)
