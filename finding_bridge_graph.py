def dfs(graph, start_node, intime, lowtime, par):
    global timer
    visited[start_node] = True
    intime[start_node] = timer
    lowtime[start_node] = timer

    timer = timer + 1
    for child in graph[start_node]:
        if not visited[child]:
            dfs(graph, child, intime, lowtime, start_node)
            if intime[start_node] < lowtime[child]:
                print('bridge ', start_node, "-", child)
            else:
                lowtime[start_node] = min(intime[child], lowtime[child])
        else:
            if child != par:
                lowtime[start_node] = min(intime[child], lowtime[child])


ipt = [[1, 2], [1, 3], [2, 4], [3, 4], [3, 5], [5, 6], [5, 7], [6, 7]]
timer = 1
"""
low time: current node stores the low value of the deepest parent, the parent which came first then all other of it's
parent, this makes sure that when we compare intime[node]<lowtime[child] then it is bridge as the node does not have
any deeper connection
"""
lowtime = {}
intime = {}
visited = {}
graph = {}
n = 7
for i in range(1, n + 1):
    graph[i] = []
    visited[i] = False
    intime[i] = None
    lowtime[i] = None
for u, v in ipt:
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, 1, intime, lowtime, -1)
