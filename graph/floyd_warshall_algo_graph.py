"""
this is used to find min distance from any node to any other node, 
usually used in matrix type representation of graph.
"""

import math

ipt = [[1, 3, 2], [1, 2, -1], [2, 3, 3], [3, 5, 2], [2, 5, 1], [3, 4, 1], [4, 5, 2]]
n = 5
row = n + 1
col = n + 1

graph = []
for _ in range(row):
    temp = []
    for _ in range(col):
        temp.append(math.inf)
    graph.append(temp)

for i in range(row):
    for j in range(col):
        if i == j:
            graph[i][j] = 0

for u, v, d in ipt:
    graph[u][v] = d

# reaching a node through another node, if that minimise the distance then update the distance, and that's it.
for k in range(1, n + 1):
    for i in range(1, row):
        for j in range(1, col):
            if i == j or i == k or j == k:
                pass
            elif graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# drop first row and first column from the graph
graph.pop(0)
graph[0].pop(0)
for item in graph:
    print(item)
