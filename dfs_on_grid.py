def is_valid(grid, visited, i, j):
    row, col = len(grid), len(grid[0])
    if i < 0 or j < 0 or i >= row or j >= col or visited[i][j] == 1:
        return False
    return True


def dfs(grid, visited, start_node):
    i, j = start_node[0], start_node[1]
    visited[i][j] = 1
    print(grid[i][j])
    if is_valid(grid, visited, i, j + 1):
        dfs(grid, visited, (i, j + 1))
    if is_valid(grid, visited, i, j - 1):
        dfs(grid, visited, (i, j - 1))
    if is_valid(grid, visited, i + 1, j):
        dfs(grid, visited, (i - 1, j))
    if is_valid(grid, visited, i + 1, j):
        dfs(grid, visited, (i + 1, j))


grid = [[3, 1, 5], [7, 8, 2], [14, 11, 9]]
row = len(grid)
col = len(grid[0])
visited = []
for i in range(row):
    temp = []
    for j in range(col):
        temp.append(0)
    visited.append(temp)

dfs(grid, visited, (0, 0))
