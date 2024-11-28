from collections import deque


def bfs(grid):
    queue = deque()
    x, y = 0, 0
    m, n = len(grid), len(grid[0])
    visited = set()
    queue.append(( x, y, 0))
    visited.add((x, y))
    directions = [[1,0], [0,1], [-1,0], [0,-1]]
    while queue:
        x, y, level = queue.popleft()
        if x == m-1 and y == n-1:
            return level
        for dx, dy in directions:
            u, v = x+dx, y+dy
            if 0<=u<m and 0<= v < m and (u,v) not in visited:
                visited.add((u,v))
                if grid[u][v]==0:
                    queue.appendleft((u,v, level))
                else:
                    queue.append((u,v,level+1))
grid = [[0,1,1],[1,1,0],[1,1,0]]
print(bfs(grid))
