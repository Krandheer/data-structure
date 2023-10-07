def isvisited(grid, visited, node):
    x, y = node
    row = len(grid)
    col = len(grid[0])

    if x < 0 or y < 0 or x >= row or y >= col or grid[x][y] == 1 or visited[x][y] == 1:
        return False
    return True


def dfs(grid, visited, start):
    i, j = start
    visited[i][j] = 1
    sm = 0
    for a, b in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if isvisited(grid, visited, (i + a, j + b)):
            sm += dfs(grid, visited, (i + a, j + b))
    return sm + 1


grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0],
]

visited = []
for i in range(len(grid)):
    temp = []
    for j in range(len(grid[0])):
        temp.append(0)
    visited.append(temp)


answer = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0 and visited[i][j] == 0:
            temp = dfs(grid, visited, (i, j))
            answer.append(temp)
print(answer)
