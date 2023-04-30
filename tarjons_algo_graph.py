"""
This is used to find the connected component in directed graph. for undirected graph we use disjoint set or
directed dfs as well.
"""


def tarjon(graph, visited, parent, node, intime, lowtime, lst, par):
    global timer
    visited[node] = 1
    parent[node] = par
    lst.append(node)
    intime[node] = timer
    lowtime[node] = timer
    timer += 1

    for child in graph[node]:
        if not visited[child]:
            tarjon(graph, visited, parent, child, intime, lowtime, lst, node)
            lowtime[node] = min(lowtime[node], lowtime[child])
        else:
            if child != par and child in lst:
                lowtime[node] = min(lowtime[node], intime[child])


ipt = [[1, 2], [2, 3], [3, 1], [2, 4], [5, 4]]

graph = {}
visited = {}
parent = {}
intime = {}
lowtime = {}
timer = 1
for i in range(1, len(ipt) + 1):
    graph[i] = []
    visited[i] = 0
    parent[i] = None
    intime[i] = None
    lowtime[i] = None

for u, v in ipt:
    graph[u].append(v)

for i in range(1, 6):
    if not visited[i]:
        lst = []
        tarjon(graph, visited, parent, i, intime, lowtime, lst, -1)

print(lowtime)
