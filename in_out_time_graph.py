ipt = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 3], [2, 3], [2, 4], [2, 5], [3, 5]]


def adjancy_list_rep(node):
    g = {i: [] for i in range(node)}

    for i, j in ipt:
        g[i].append(j)
        g[j].append(i)
    return g


def dfs(graph, node, intime, outtime, timer=1, visited=None):
    if not visited:
        visited = set()
    # global timer
    # print(node)
    visited.add(node)
    intime[node] = timer
    timer += 1
    for child in graph[node]:
        if child not in visited:
            intime, outtime, timer = dfs(graph, child, intime, outtime, timer, visited)
    outtime[node] = timer
    timer += 1
    return intime, outtime, timer


graph = adjancy_list_rep(6)
intime, outime = {}, {}
# timer = 1
# print("graph", graph)
dfs(graph, 0, intime, outime)
print(intime, outime)
