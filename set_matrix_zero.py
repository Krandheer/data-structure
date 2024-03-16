from typing import *


def setZeroes(matrix: List[List[int]]) -> None:
    """
    dsa->1
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    col = len(matrix[0])
    zeros = []
    for i in range(rows):
        for j in range(col):
            if matrix[i][j] == 0:
                zeros.append((i, j))

    for i, j in zeros:
        for k in range(col):
            matrix[i][k] = 0

        for k in range(rows):
            matrix[k][j] = 0
    return matrix
    # print(rows, col)
    # return matrix


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

print(setZeroes(matrix))
