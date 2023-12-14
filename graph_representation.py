def adjancy_matrix_rep(graph):
    g = []
    for _ in range():
        temp = []
        for _ in range(6):
            temp.append(0)
        g.append(temp)

    for u, v in graph:
        g[u][v] = 1
        g[v][u] = 1
    return g


def adjancy_list_rep(graph, node):
    g = {}
    for i in range(node):
        g[i] = []

    for u, v in graph:
        g[u].append(v)
        g[v].append(u)

    return g


graph = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 3], [2, 3], [2, 4], [2, 5], [3, 5]]
# graph_1 = adjancy_matrix_rep(graph, 6)
# for i in graph_1:
#     print(i)
graph_1 = adjancy_list_rep(graph, 6)
for key, value in graph_1.items():
    print(key, "->", value)
