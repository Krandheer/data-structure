import math
import time


def minimumTotal(triangle):
    # return helper_recursion(0, 0, matrix)

    dp_1 = [[-1 for j in range(len(triangle))] for i in range(len(triangle))]
    return helper_dp(0, 0, triangle, dp_1)


def helper_recursion(i, j, matrix):
    if i == len(matrix) - 1:
        return matrix[i][j]
    if i >= len(matrix):
        return math.inf
    right = matrix[i][j] + helper_recursion(i + 1, j + 1, matrix)
    down = matrix[i][j] + helper_recursion(i + 1, j, matrix)

    return min(right, down)


def helper_dp(i, j, matrix, dp):
    if i == len(matrix) - 1:
        return matrix[i][j]
    if i >= len(matrix):
        return math.inf
    if dp[i][j] != -1:
        return dp[i][j]
    right = matrix[i][j] + helper_dp(i + 1, j + 1, matrix, dp)
    down = matrix[i][j] + helper_dp(i + 1, j, matrix, dp)
    dp[i][j] = min(right, down)
    return dp[i][j]


start = time.perf_counter()
matrix = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(minimumTotal(matrix))
print(time.perf_counter() - start)
