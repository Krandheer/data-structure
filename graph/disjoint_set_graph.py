def find(graph, node):
    # this finds the root of the node
    if graph[node] < 0:
        return node
    else:
        return find(graph, graph[node])


def union(graph, u, v, ans):
    a = find(graph, u)
    b = find(graph, v)

    if a == b:
        print(f"can't add, it's already part of the family,{u}, {v} ")
        ans.append([u, v])
    else:
        if graph[a] == graph[b]:
            # b becomes parent and a points to b
            graph[b] = graph[a] + graph[b]
            graph[a] = b
        elif graph[a] < graph[b]:
            # a becomes parent and b points to a
            graph[a] = graph[a] + graph[b]
            graph[b] = a
        else:
            graph[b] = graph[a] + graph[b]
            graph[a] = b
    return ans


n = 6
# graph = {}
# for i in range(7):
#     graph[i] = -1
graph = [-1] * 6
# ipt = [[0, 1], [1, 2], [2, 3], [4, 5], [1, 3]]
ipt = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
ans = []
for u, v in ipt:
    ans = union(graph, u, v, ans)
print(ans)
# print(graph)
