def minPathSum(grid):
    """minimum path sum in grid from top left to bottom right"""

    def helper(grid, row, col):
        if row < 0:
            return float("inf")
        if col < 0:
            return float("inf")
        if row == 0 and col == 0:
            return grid[0][0]

        return grid[row][col] + min(
            helper(grid, row - 1, col),
            helper(grid, row, col - 1),
        )

    return helper(grid, len(grid) - 1, len(grid[0]) - 1)


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
ans = minPathSum(grid)
print(ans)
