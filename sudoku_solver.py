from collections import deque
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    for row in board:
        temp = set()
        for i in row:
            if i in temp:
                return False
            elif i != ".":
                temp.add(i)

    m, n = len(board), len(board[0])
    for i in range(m):
        temp = set()
        for j in range(n):
            if board[j][i] in temp:
                return False
            elif board[j][i] != ".":
                temp.add(board[j][i])

    start_end_row = [[0, 3], [3, 6], [6, 9]]
    start_end_col = [[0, 3], [3, 6], [6, 9]]

    for u, v in start_end_row:
        start_row = u
        end_row = v
        for s_col, e_col in start_end_col:
            start_col = s_col
            end_col = e_col
            temp = set()
            for i in range(start_row, end_row):
                for j in range(start_col, end_col):
                    if board[i][j] in temp:
                        return False
                    elif board[i][j] != ".":
                        temp.add(board[i][j])
    return True
