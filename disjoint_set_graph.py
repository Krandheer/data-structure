def find(graph, node):
    if graph[node] < 0:
        return node
    else:
        return find(graph, graph[node])


def union(graph, u, v):
    a = find(graph, u)
    b = find(graph, v)

    if a == b:
        print(f"can't add, it's already part of the family,{u}, {v} ")
    else:
        if graph[a] == graph[b]:
            graph[b] = graph[a] + graph[b]
            graph[a] = b
        elif graph[a] < graph[b]:
            graph[a] = graph[a] + graph[b]
            graph[b] = a
        else:
            graph[b] = graph[a] + graph[b]
            graph[a] = b


n = 6
# # graph = {}
# for i in range(7):
#     graph[i] = -1
graph = [-1]*n
ipt = [[0, 1], [1, 2], [2, 3], [4, 5], [1, 3]]
for u, v in ipt:
    union(graph, u, v)

print(graph)
