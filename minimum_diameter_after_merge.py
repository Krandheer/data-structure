import math
from collections import defaultdict, deque
from typing import List

"""
problem of the day, leet code
tag: hard, graph, diameter.
"""


def minimum_diameter_after_merge(
    edges1: List[List[int]], edges2: List[List[int]]
) -> int:
    graph1 = defaultdict(list)
    for u, v in edges1:
        graph1[u].append(v)
        graph1[v].append(u)
    graph2 = defaultdict(list)
    for u, v in edges2:
        graph2[u].append(v)
        graph2[v].append(u)

    def find_farthest_node(graph, node):
        q = deque([node])
        visited = set()
        visited.add(node)
        farthest_node = node
        while q:
            node = q.popleft()
            farthest_node = node
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    q.append(child)
        return farthest_node

    def find_diameter(graph, node):
        node = find_farthest_node(graph, node)
        q = deque([(node, 0)])
        visited = set()
        visited.add(node)
        diameter = 0
        while q:
            node, distance = q.popleft()
            diameter = distance
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    q.append((child, distance + 1))
        return diameter

    d1, d2 = 0, 0
    if edges1:
        d1 = find_diameter(graph1, edges1[0][0])
    if edges2:
        d2 = find_diameter(graph2, edges2[0][0])
    d3 = math.ceil(d1 / 2) + math.ceil(d2 / 2) + 1
    return max(d1, d2, d3)
