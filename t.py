from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(i, col):
            if i != j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(row):
        matrix[i].reverse()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix))
