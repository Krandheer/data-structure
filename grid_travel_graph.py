"""
finding unique paths for given grid using graph traversal algorithm.
"""


def grid_travel(m, n, i, j, visited):
    if i == m - 1 or j == n - 1:
        return 1
    if i >= m or j >= n or visited[i][j]:
        return 0
    visited[i][j] = 1
    down = grid_travel(m, n, i, j + 1, visited)
    right = grid_travel(m, n, i + 1, j, visited)
    visited[i][j] = 0
    return down + right


visited = []
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(0)
    visited.append(temp)

result = grid_travel(3, 3, 0, 0, visited)
print(result)
