# krushkal algorithm for minimum spanning tree using disjoint set concept

"""
it's like greedy algo, just that here edges are sorted first and then taken out one by one.
while in prime's algo we take nodes one by one. but there also we remain by keeping a  min heap.
mst: minimum spanning tree, no cycle in graph.
"""
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
    return find(graph, graph[node])


def union(graph, u, v, answer):
    a = find(graph, u)  # will return the head node of the family
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
N = 7
answer = []
graph = [-1] * (N + 1)
for u, v, _ in ipt:
    union(graph, u, v, answer)
print(answer)
