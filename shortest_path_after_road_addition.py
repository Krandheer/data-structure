from collections import deque
from typing import List


def bfs(n, graph, start):
    ans = 0
    visited = set()
    q = deque([(start, 0)])

    while q:
        ele, level = q.popleft()
        if ele == n-1:
            ans =  level
            break
        for j in graph[ele]:
            if j not in visited:
                visited.add(j)
                q.append((j, level+1))
    return ans
def shortest_distance_after_queries(n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        in_adj_li = {}
        for i in range(n-1):
            in_adj_li[i]=[i+1]
        for s, d in queries:
            in_adj_li[s].append(d)
            ans.append(bfs(n, in_adj_li, 0))
        return ans

print(shortest_distance_after_queries(5, [[2,4],[0,2],[0,4]]))
