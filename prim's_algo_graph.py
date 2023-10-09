from heapq import *


def primes(graph, start, visited, distance, parent):
    bag = []
    heappush(bag, [0, start])
    visited[start] = 1
    distance[start] = 0
    parent[start] = -1
    while bag:
        d, n = heappop(bag)
        if not visited[n]:
            visited[n] = 1
        for cd, cn in graph[n]:
            if distance[cn] > cd:
                parent[cn] = n
                distance[cn] = cd
                heappush(bag, [cd, cn])
    print(distance)
    print(parent)


ipt = [[1, 2, 1], [2, 3, 4], [3, 4, 1], [4, 5, 2], [1, 5, 3], [2, 5, 2], [2, 4, 1]]
n = 5
graph = {}
distance = {}
parent = {}
visited = {}
for i in range(1, n + 1):
    graph[i] = []
    distance[i] = 10**8 + 1
    parent[i] = None
    visited[i] = 0
for u, v, i in ipt:
    graph[u].append([i, v])
    graph[v].append([i, u])

# print(graph)

primes(graph, 1, visited, distance, parent)
