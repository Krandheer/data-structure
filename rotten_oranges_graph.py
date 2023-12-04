"""
Problem Statement: Given a grid of dimension N x M where each cell in the grid can have values 0, 1, or 2 which has the
 following meaning:
0: Empty cell
1: Cells have fresh oranges
2: Cells have rotten oranges
We have to determine what is the minimum time required to rot all oranges. A rotten orange at index [i,j] can rot other
fresh oranges at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time.
immediately should strike breadth first traversal in such question.
"""

from collections import deque

ipt = [[2, 1, 1],
       [1, 1, 0],
       [0, 1, 1]]
row = len(ipt)
col = len(ipt[0])


def is_valid(visited, x, y):
    if x < 0 or y < 0 or x >= row or y >= col or visited[x][y] or ipt[x][y] != 1:
        return False
    return True


def rotten_orange():
    visited = []
    for _ in range(row):
        temp = []
        for _ in range(col):
            temp.append(0)
        visited.append(temp)

    queue = deque()
    fresh_count = 0
    # put all rotten in queue with initial level as 0 and count number of fresh as those are the one we need to turn
    # into rotten
    for i in range(row):
        for j in range(col):
            if ipt[i][j] == 2:
                visited[i][j] = 2
                queue.append((i, j, 0))
            else:
                visited[i][j] = 0
            if ipt[i][j] == 1:
                fresh_count += 1

    # dis_max keep track of max_level needed to make all rotten, perform bfs now
    made_rott = 0
    dis_max = 0
    while queue:
        i, j, d = queue.popleft()
        dis_max = max(d, dis_max)
        for a, b in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            if is_valid(visited, a+i, b+j):
                queue.append((a + i, b + j, d + 1))
                visited[a + i][b + j] = 2
                made_rott += 1

    if made_rott == fresh_count:
        return dis_max
    return -1


print(rotten_orange())
