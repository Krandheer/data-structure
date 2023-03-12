import math


# recursion solution
def mat_chain_mul_recursion(i, j, arr):
    if i == j:
        return 0
    min_steps = math.inf
    # i = 0 to n-1, j = n-1 to 1, so for i == n and for j == n-1
    for k in range(i, j):
        steps = arr[i - 1] * arr[k] * arr[j] + mat_chain_mul_recursion(i, k, arr) + mat_chain_mul_recursion(k + 1, j,
                                                                                                            arr)
        if steps < min_steps:
            min_steps = steps
    return min_steps


# arr = [1, 2, 3, 4, 3]
arr = [10, 20, 30, 40, 50]
print(mat_chain_mul_recursion(1, len(arr) - 1, arr))


# dp topdown approach solution
def matrix_chain_mul_dp(i, j, arr, dp):
    if i == j:
        return 0
    min_steps = math.inf
    if dp[i][j] != -1:
        return dp[i][j]
    for k in range(i, j):
        steps = arr[i - 1] * arr[k] * arr[j] + matrix_chain_mul_dp(i, k, arr, dp) + matrix_chain_mul_dp(k + 1, j,
                                                                                                        arr, dp)
        if steps < min_steps:
            min_steps = steps
        dp[i][j] = min_steps
    return dp[i][j]


dp = [[-1 for j in range(len(arr))] for i in range(len(arr) - 1)]
print(matrix_chain_mul_dp(1, len(arr) - 1, arr, dp))
