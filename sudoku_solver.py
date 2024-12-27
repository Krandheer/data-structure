from collections import Counter
from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    for row in board:
        temp = Counter(row)
        temp['.'] = 1
        if max(temp.values()) > 1:
            return False

    for i in range(len(board)):
        j = 0
        temp = {}
        while j < len(board):
            if board[j][i] not in temp:
                temp[board[j][i]] = 1
                j += 1
            elif board[j][i] == '.':
                j += 1
            else:
                return False

    def is_valid(board, x, y, m, n):
        temp = {}
        for i in range(x, m):
            for j in range(y, n):
                if board[i][j] not in temp:
                    temp[board[i][j]] = 1
                elif board[i][j] == '.':
                    continue
                else:
                    return False

    x, y = 0, 0
    m, n = 3, 3
    result = True
    for i in range(3):
        for j in range(3):
            x, y = x + i * 3, y + j * 3
            m, n = m + i * 3, n + j * 3
            result = is_valid(board, x, y, m, n)
            if result is not None and  result == False:
                return result
    return True


board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]
print(is_valid_sudoku(board))
