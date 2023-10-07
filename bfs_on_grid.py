from collections import deque


def is_valid(grid, visited, x, y):
    row = len(grid)
    col = len(grid[0])
    if x < 0 or y < 0 or x >= row or y >= col or visited[x][y] == 1:
        return False
    return True


def bfs(grid, visited, node):
    queue = deque()
    queue.append(node)
    i, j = node[0], node[1]
    visited[i][j] = 1
    while queue:
        x, y = queue.popleft()
        print(grid[x][y])
        for k, l in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            if is_valid(grid, visited, x + k, y + l):
                queue.append((x + k, y + l))
                visited[x + k][y + l] = 1


grid = [[3, 1, 5], [7, 8, 2], [14, 11, 9]]
row = len(grid)
col = len(grid[0])
visited = []
for i in range(row):
    temp = []
    for j in range(col):
        temp.append(0)
    visited.append(temp)

bfs(grid, visited, (0, 0))
