def is_valid(i, j, grid, visited):
    row, col = len(grid), len(grid[0])
    if 0 <= i < row and 0 <= j < col and not visited[i][j]:
        return True
    return False


def dfs(grid, visited, start_node):
    i, j = start_node[0], start_node[1]
    visited[i][j] = True
    print(grid[i][j])
    for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        if is_valid(i + x, j + y, grid, visited):
            dfs(grid, visited, (i + x, j + y))


grid = [[3, 1, 5], [7, 8, 2], [14, 11, 9]]
row, col = len(grid), len(grid[0])
visited = [[False] * col for _ in range(row)]

dfs(grid, visited, (0, 0))
