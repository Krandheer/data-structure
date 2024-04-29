from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # the sides where i can't go is the side that should be consider
        # in perimeter sum, rest are just for moving
        peri = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    p = 4
                    if i - 1 >= 0 and grid[i - 1][j]:
                        p -= 2
                    if j - 1 >= 0 and grid[i][j - 1]:
                        p -= 2
                    peri += p
        return peri
