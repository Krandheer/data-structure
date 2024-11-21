from typing import List
from collections import deque


def count_unguarded(m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    # 0 <- free, 1 <- guards, 2 <- walls, 3 <- visited
    grid = [[0]*n for i in range(m)]
    for r, c in guards:
        grid[r][c]=1
    for r, c in walls:
        grid[r][c]=2
    def mark_visited(r, c):
        for i in range(r+1, m):
            if grid[i][c] in [1,2]:
                break
            grid[i][c]=3
        for i in reversed(range(0, r)):
            if grid[i][c] in [1,2]:
                break
            grid[i][c]=3

        for i in range(c+1, n):
            if grid[r][i] in [1,2]:
                break
            grid[r][i]=3

        for i in reversed(range(0, c)):
            if grid[r][i] in [1,2]:
                break
            grid[r][i]=3


    for r,c in guards:
        mark_visited(r,c)

    count = 0
    for row in grid:
        for n in row:
            if n == 0:
                count += 1

    return count
m = 8
n = 9
guards = [[5,8],[5,5],[4,6],[0,5],[6,5]]
walls =[[4,1]]
print(count_unguarded(m,n, guards, walls))
