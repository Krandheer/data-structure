"""
topological sorting exists only in DAG, directed acyclic graph, as otherwise it gets
in that cycle from which it could not come out.
print node in order of which they come in graph, means if there is edge between u and v
and u pointing to v then u should come first then v.
we can use indegree concept to do this, when in degree is 0 then take it in queue
and print it and traverse rest of its child
kahn algorithm uses this concept of indegree to do topological sorting.
"""
from collections import deque


def kahn(graph, visited, indegree):
    queue = deque()
    for key in indegree:
        if indegree[key] == 0:
            queue.append(key)
            visited[key] = True

    while queue:
        node = queue.popleft()
        print(node)
        for child in graph[node]:
            if not visited[child]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    visited[child] = True


ipt = [[1, 3], [1, 2], [1, 7], [2, 3], [4, 1], [4, 3], [5, 3], [6, 1], [6, 3], [8, 1], [9, 8], [9, 7]]

visited = {}
graph = {}
indegree = {}

for i in range(1, 10):
    graph[i] = []
    visited[i] = False
    indegree[i] = 0

for u, v in ipt:
    graph[u].append(v)
    indegree[v] += 1

kahn(graph, visited, indegree)
# print(graph)