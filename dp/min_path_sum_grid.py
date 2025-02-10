def minPathSum(grid):
    """minimum path sum in grid from top left to bottom right"""

    def helper(grid, row, col):
        if row < 0 or col < 0:
            return float("inf")
        if row == 0 and col == 0:
            return grid[0][0]

        left = grid[row][col] + helper(grid, row, col - 1)
        up = grid[row][col] + helper(grid, row - 1, col)
        return min(left, up)

    return helper(grid, len(grid) - 1, len(grid[0]) - 1)


# memoising it
def min_path_sum(grid, row, col, dp):
    if row < 0 or col < 0:
        return float("inf")
    if row == 0 and col == 0:
        return grid[row][col]

    if dp[row][col] != -1:
        return dp[row][col]
    left = grid[row][col] + min_path_sum(grid, row, col - 1, dp)
    up = grid[row][col] + min_path_sum(grid, row - 1, col, dp)
    dp[row][col] = min(left, up)
    return dp[row][col]


def minPathSum2(grid):

    def helper(grid, row, col, dp):
        if row < 0 or col < 0:
            return float("inf")
        if row == 0 and col == 0:
            return grid[row][col]

        if dp[row][col] != -1:
            return dp[row][col]
        dp[row][col] = grid[row][col] + min(
            helper(grid, row - 1, col, dp), helper(grid, row, col - 1, dp)
        )
        return dp[row][col]

    dp = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
    return helper(grid, len(grid) - 1, len(grid[0]) - 1, dp)


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
ans = minPathSum(grid)
print(ans)

dp = [[-1 for i in range(len(grid))] for j in range(len(grid[0]))]
ans2 = min_path_sum(grid, len(grid) - 1, len(grid[0]) - 1, dp)
print(ans2)
