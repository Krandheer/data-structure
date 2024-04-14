from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:
        n = len(obstacle_grid[0])
        m = len(obstacle_grid)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.helper(0, 0, obstacle_grid, dp)

    def helper(self, i, j, obstacle_grid, dp):
        n = len(obstacle_grid[0])
        m = len(obstacle_grid)
        if obstacle_grid[m - 1][n - 1] == 1:
            return 0
        if i == 0 and j == 0 and obstacle_grid[i][j] == 1:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        if i >= m or j >= n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        down = left = 0
        if i < m - 1 and obstacle_grid[i + 1][j] != 1:
            down = self.helper(i + 1, j, obstacle_grid, dp)
        if j < n - 1 and obstacle_grid[i][j + 1] != 1:
            left = self.helper(i, j + 1, obstacle_grid, dp)
        dp[i][j] = down + left
        return dp[i][j]


grid = [[1, 0]]
sol = Solution()
print(sol.uniquePathsWithObstacles(grid))
