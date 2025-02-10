import math


def minFallingPathSum(matrix):
    dp_1 = [[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    min_val = math.inf
    for j in range(len(matrix[0])):
        temp = helper_dp(len(matrix) - 1, j, matrix, dp_1)
        min_val = min(temp, min_val)
    return min_val

    # min_sum = math.inf
    # for j in range(len(matrix)):
    #     temp = helper_recursion(len(matrix) - 1, j, matrix)
    #     min_sum = min(min_sum, temp)
    #
    # return min_sum


def helper_recursion(i, j, matrix):
    if i == 0:
        return matrix[i][j]
    if i < 0 or i >= len(matrix) or j < 0 or j > len(matrix):
        return math.inf
    left = right = up = math.inf
    if i > 0 and j > 0:
        left = matrix[i][j] + helper_recursion(i - 1, j - 1, matrix)

    if i > 0 and j < len(matrix) - 1:
        right = matrix[i][j] + helper_recursion(i - 1, j + 1, matrix)

    if i > 0:
        up = matrix[i][j] + helper_recursion(i - 1, j, matrix)

    return min(left, right, up)


def helper_dp(i, j, matrix, dp):
    if i == 0:
        return matrix[i][j]
    if i < 0 or i >= len(matrix) or j < 0 or j > len(matrix):
        return math.inf
    left = right = up = math.inf
    if dp[i][j] != -1:
        return dp[i][j]
    if i > 0 and j > 0:
        left = matrix[i][j] + helper_dp(i - 1, j - 1, matrix, dp)

    if i > 0 and j < len(matrix) - 1:
        right = matrix[i][j] + helper_dp(i - 1, j + 1, matrix, dp)

    if i > 0:
        up = matrix[i][j] + helper_dp(i - 1, j, matrix, dp)

    dp[i][j] = min(left, right, up)
    return dp[i][j]


matrix = [[17, 82], [1, -44]]
print(minFallingPathSum(matrix))
