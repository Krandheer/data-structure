from collections import deque

moves = [[2, 1], [-2, 1], [2, -1], [-2, -1], [-1, -2], [-1, 2], [1, -2], [1, 2]]


def is_valid(grid, visited, x, y):
    row = len(grid)
    col = len(grid[0])
    if x < 0 or y < 0 or x >= row or y >= col or visited[x][y] == 1:
        return False
    return True


def bfs(grid, start, end, distance, visited):
    i, j = start[0], start[1]
    queue = deque()
    queue.append(start)
    distance[i][j] = 0
    visited[i][j] = 1
    while queue:
        k, l = queue.popleft()
        for u, v in moves:
            if is_valid(grid, visited, k + u, l + v):
                visited[k + u][l + v] = 1
                distance[k + u][l + v] = distance[k][l] + 1
                queue.append((k + u, l + v))

    print(distance[end[0]][end[1]])


grid = [["", "B", "", ""], ["", "", "", ""], ["", "A", "", ""], ["", "", "", ""]]
row = len(grid)
col = len(grid[0])
visited = []
distance = []
for i in range(row):
    temp = []
    dist = []
    for j in range(col):
        temp.append(0)
        dist.append(-1)
    visited.append(temp)
    distance.append(dist)

start = ()
end = ()
for i in range(row):
    for j in range(col):
        if grid[i][j] == "A":
            start = (i, j)
        if grid[i][j] == "B":
            end = (i, j)
# print(start, end)
bfs(grid, start, end, distance, visited)
# for item in distance:
#     print(item)
