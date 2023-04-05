import math
from typing import List
import time


class Solution_recursion:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        return self.helper(m, n, grid)

    def helper(self, m, n, grid):
        if m == 0 and n == 0:
            return grid[0][0]

        if m < 0 or n < 0:
            return 0
        left = up = math.inf
        if m > 0 and n > 0:
            left = grid[m][n] + self.helper(m, n - 1, grid)
            up = grid[m][n] + self.helper(m - 1, n, grid)
        if m == 0 and n > 0:
            left = grid[m][n] + self.helper(m, n - 1, grid)
        if m > 0 and n == 0:
            up = grid[m][n] + self.helper(m - 1, n, grid)
        return min(left, up)


class Solution_dp:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        return self.helper(m, n, grid, dp)

    def helper(self, m, n, grid, dp):
        if m == 0 and n == 0:
            return grid[0][0]

        if m < 0 or n < 0:
            return 0
        left = up = math.inf
        if dp[m][n] != -1:
            return dp[m][n]
        if m > 0 and n > 0:
            left = grid[m][n] + self.helper(m, n - 1, grid, dp)
            up = grid[m][n] + self.helper(m - 1, n, grid, dp)
        if m == 0 and n > 0:
            left = grid[m][n] + self.helper(m, n - 1, grid, dp)
        if m > 0 and n == 0:
            up = grid[m][n] + self.helper(m - 1, n, grid, dp)
        dp[m][n] = min(left, up)
        return dp[m][n]


sol = Solution_dp()
sol2 = Solution_recursion()
grid = [[1, 3, 1, 2, 3], [1, 5, 1, 4, 4], [4, 2, 1, 6, 9], [1, 2, 3, 4, 0], [5, 4, 3, 2, 1]]
start = time.perf_counter()
print(sol.minPathSum(grid))
print(f'dp solution time {time.perf_counter() - start}')
start2 = time.perf_counter()
print(sol2.minPathSum(grid))
print(f'recursion solution time: {time.perf_counter() - start2}')
