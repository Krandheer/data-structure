from typing import List


def binary_search(matrix, row, start_col, end_col, target):
    while start_col <= end_col:
        mid = end_col - (end_col - start_col) // 2
        if matrix[row][mid] == target:
            return True
        if matrix[row][mid] <= target:
            start_col = mid + 1
        else:
            end_col = mid - 1
    return False


def search(matrix: List[List[int]], target: int) -> bool:
    mid_col = len(matrix[0]) // 2
    start_row = 0
    end_row = len(matrix) - 1
    if end_row == 0:
        return binary_search(matrix, 0, 0, len(matrix[0]) - 1, target)
    while end_row - start_row > 1:
        mid_row = end_row - (end_row - start_row) // 2
        if matrix[mid_row][mid_col] == target:
            return True
        if matrix[mid_row][mid_col] < target:
            start_row = mid_row
        else:
            end_row = mid_row
    if matrix[start_row][mid_col] == target:
        return True
    if matrix[start_row + 1][mid_col] == target:
        return True

    if matrix[start_row][mid_col] <= target:
        if binary_search(matrix, start_row, mid_col, len(matrix[0]) - 1, target):
            return True
    if matrix[start_row][mid_col] >= target:
        if binary_search(matrix, start_row, 0, mid_col, target):
            return True

    if matrix[start_row + 1][mid_col] <= target:
        if binary_search(matrix, start_row + 1, mid_col, len(matrix[0]) - 1, target):
            return True
    if matrix[start_row + 1][mid_col] >= target:
        if binary_search(matrix, start_row + 1, 0, mid_col, target):
            return True
    return False


# matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
matrix1 = [[1]]
target1 = 0
print(search(matrix1, target1))
