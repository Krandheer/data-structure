def is_valid(grid, visited, i, j):
    row, col = len(grid), len(grid[0])
    if 0 <= i < row and 0 <= j < col and visited[i][j] == 0:
        return True
    return False


def dfs(grid, visited, start_node):
    i, j = start_node[0], start_node[1]
    visited[i][j] = 1
    print(grid[i][j])
    for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        if is_valid(grid, visited, i + x, j + y):
            dfs(grid, visited, (i + x, j + y))


grid = [[3, 1, 5], [7, 8, 2], [14, 11, 9]]
row = len(grid)
col = len(grid[0])
visited = [[0] * col for _ in range(row)]
dfs(grid, visited, (0, 0))
