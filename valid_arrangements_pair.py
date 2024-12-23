from collections import defaultdict

# important conceptually


def valid_arrangement(pairs):
    adj = defaultdict(list)
    indegree = defaultdict(int)
    outdegree = defaultdict(int)
    for u, v in pairs:
        adj[u].append(v)
        indegree[v] += 1
        outdegree[u] += 1

    start_node = pairs[0][0]
    for key in adj:
        if outdegree[key] - indegree[key] == 1:
            start_node = key
            break
    if start_node == float("inf"):
        return pairs
    path = []

    def dfs(node):
        while len(adj[node]) > 0:
            next_node = adj[node][0]
            del adj[node][0]
            dfs(next_node)

        path.append(node)

    dfs(start_node)
    path = list(reversed(path))

    res = []
    for i in range(1, len(path)):
        res.append([path[i - 1], path[i]])
    return res


print(valid_arrangement([[1, 3], [3, 2], [2, 1]]))
