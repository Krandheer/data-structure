import heapq
from typing import List


def minimum_time(grid: List[List[int]]) -> int:
    """leetcode: https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description/
    only catch here is that we can move back and forth. but we need to find minimum
    so we do our traversal using minheap instead of regular BFS.
    """
    if min(grid[0][1], grid[1][0]) > 1:
        return -1

    def is_valid(u, v, m, n):
        if 0 <= u < m and 0 <= v < n:
            return True
        return False

    def bfs(grid, start):
        x, y = start
        queue = []
        visited = set()
        visited.add(start)
        m, n = len(grid), len(grid[0])
        heapq.heappush(queue, (0, x, y))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while queue:
            level, x, y = heapq.heappop(queue)
            if (x, y) == (m - 1, n - 1):
                return level
            for dx, dy in directions:
                u, v = x + dx, y + dy
                if is_valid(u, v, m, n) and (u, v) not in visited:
                    visited.add((u, v))
                    wait = 0
                    if (grid[u][v] - level) % 2 == 0:
                        wait = 1
                    new_level = max(grid[u][v] + wait, level + 1)
                    heapq.heappush(queue, (new_level, u, v))
        return -1

    return bfs(grid, (0, 0))
