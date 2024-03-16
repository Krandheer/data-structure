from typing import List


def is_valid(start, board):
    row = start[0]
    column = start[1]
    if (
        (0 <= row < len(board))
        and (0 <= column < len(board[0]))
        and board[row][column] == "O"
    ):
        return True
    return False


def dfs(start, visited, board):
    row = start[0]
    column = start[1]
    if not visited[row][column]:
        visited[row][column] = 1
        dir1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i, j in dir1:
            if is_valid((row + i, column + j), board):
                dfs((row + i, column + j), visited, board)


def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    visited = []
    for _ in range(len(board)):
        temp = []
        for _ in range(len(board[0])):
            temp.append(0)
        visited.append(temp)

    # traversion first row
    for j in range(len(board[0])):
        if board[0][j] == "O":
            start = (0, j)
            dfs(start, visited, board)

    for j in range(len(board[0])):
        if board[len(board) - 1][j] == "O":
            start = (len(board) - 1, j)
            dfs(start, visited, board)

    # traversing columns
    for j in range(len(board)):
        if board[j][0] == "O":
            start = (j, 0)
            dfs(start, visited, board)

    for j in range(len(board)):
        if board[j][len(board[0]) - 1] == "O":
            start = (j, len(board[0]) - 1)
            dfs(start, visited, board)

    # converting O to X, final stepp of the solution
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if not visited[i][j]:
                board[i][j] = "X"
    return board


board1 = [
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
]
print(solve(board1))
