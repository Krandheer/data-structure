import math


def min_falling_recursion(i, j, matrix):
    if i == len(matrix) - 1:
        return matrix[i][j]
    if i >= len(matrix):
        return math.inf
    right = matrix[i][j] + min_falling_recursion(i + 1, j + 1, matrix)
    down = matrix[i][j] + min_falling_recursion(i + 1, j, matrix)

    return max(right, down)


def min_falling_sum_dp(i, j, matrix, dp):
    if i == len(matrix) - 1:
        return matrix[i][j]
    if i >= len(matrix):
        return math.inf
    if dp[i][j] != -1:
        return dp[i][j]
    right = matrix[i][j] + min_falling_sum_dp(i + 1, j + 1, matrix, dp)
    down = matrix[i][j] + min_falling_sum_dp(i + 1, j, matrix, dp)
    dp[i][j] = min(right, down)
    return dp[i][j]


matrix = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
dp_1 = [[-1 for j in range(len(matrix))] for i in range(len(matrix))]
print(min_falling_sum_dp(0, 0, matrix, dp_1))
print(min_falling_recursion(0, 0, matrix))
