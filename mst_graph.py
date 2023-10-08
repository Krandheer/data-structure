# krushkal algorithm for minimum spanning tree using disjoint set concept
ipt = [
    [1, 2, 1],
    [3, 6, 2],
    [6, 7, 2],
    [3, 4, 1],
    [1, 3, 3],
    [4, 5, 5],
    [6, 5, 6],
    [2, 6, 4],
    [7, 5, 7],
]


# this returns the head of the family
def find(graph, node):
    if graph[node] < 0:
        return node
    else:
        return find(graph, graph[node])


def union(graph, u, v, answer):
    a = find(graph, u)
    b = find(graph, v)

    # this check helps to avoid the formation of cycle
    if a != b:
        # answer storing the mst
        answer.append([u, v])

        # making the disjoint set form of graph to avoid the formation of cycle
        if graph[a] == graph[b]:
            graph[b] = graph[a] + graph[b]
            graph[a] = b
        elif graph[a] < graph[b]:
            graph[a] = graph[a] + graph[b]
            graph[b] = a
        else:
            graph[b] = graph[a] + graph[b]
            graph[a] = b


# sorting on basis of weight to get mst
ipt = sorted(ipt, key=lambda x: x[2])
n = 7
answer = []
graph = [-1] * (n + 1)
for (
    u,
    v,
    _,
) in ipt:
    union(graph, u, v, answer)
# print(graph)
print(answer)


# ipt2 = [
#     [1, 2, 3],
#     [1, 3, 2],
#     [2, 3, 2],
#     [2, 5, 1],
#     [3, 4, 4],
#     [4, 5, 8],
#     [3, 7, 4],
#     [4, 7, 5],
#     [5, 6, 6],
#     [7, 6, 2],
#     [7, 8, 1],
#     [7, 9, 2],
#     [6, 9, 1],
# ]

# graph2 = {}
# for i in range(1, 10):
#     graph2[i] = []
# for u, v, w in ipt2:
#     graph2[u].append([w, v])
#     graph2[v].append([w, u])

# print(graph2)
