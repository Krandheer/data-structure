from collections import deque


def is_valid(grid, visited, x, y):
    row = len(grid)
    col = len(grid[0])
    if 0 <= x < row and 0 <= y < col and not visited[x][y]:
        return True
    return False


def bfs(grid, visited, node):
    queue = deque()
    queue.append(node)
    i, j = node[0], node[1]
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        print(grid[x][y])
        for k, l in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            if is_valid(grid, visited, x + k, y + l):
                queue.append((x + k, y + l))
                visited[x + k][y + l] = 1


grid = [[3, 1, 5], [7, 8, 2], [14, 11, 9]]
row, col = len(grid), len(grid[0])
visited = [[False] * col for _ in range(row)]

bfs(grid, visited, (0, 0))
