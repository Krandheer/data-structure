from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[-1 for j in range(n)] for i in range(m)]
        return self.helper(0, 0, obstacleGrid, dp)

    def helper(self, i, j, obstacleGrid, dp):
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        if i == 0 and j == 0 and obstacleGrid[i][j] == 1:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        if i >= m or j >= n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        down = left = 0
        if i < m - 1 and obstacleGrid[i + 1][j] != 1:
            down = self.helper(i + 1, j, obstacleGrid, dp)
        if j < n - 1 and obstacleGrid[i][j + 1] != 1:
            left = self.helper(i, j + 1, obstacleGrid, dp)
        dp[i][j] = down + left
        return dp[i][j]


grid = [[1, 0]]
sol = Solution()
print(sol.uniquePathsWithObstacles(grid))
