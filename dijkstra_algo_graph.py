"""
Algo for sssp for directed graph, for undirected graph simple sssp with bfs using level order traversal works,
actually this will work for undirected as well, just use min heap instead of queue and then bfs will do job,
heap will make sure that you pop min element that minimise the distance.
"""
import math
from heapq import heappop, heappush


def dikshatra(graph, visited, distance, start):
    bag = []
    distance[start] = 0
    heappush(bag, [0, start])
    while bag:
        dist, node = heappop(bag)
        visited[node] = 1
        for cdist, cnode in graph[node]:
            if not visited[cnode] and cdist + dist < distance[cnode]:
                distance[cnode] = cdist + dist
                heappush(bag, [cdist + distance[node], cnode])


ipt = [
    [1, 3, 2],
    [1, 2, 1],
    [2, 3, 1],
    [2, 5, 1],
    [3, 4, 2],
    [5, 4, 5],
]

graph = {}
visited = {}
distance = {}
for i in range(1, 6):
    graph[i] = []
    visited[i] = 0
    distance[i] = math.inf


for u, v, d in ipt:
    graph[u].append((d, v))

dikshatra(graph, visited, distance, 1)
print(distance)
