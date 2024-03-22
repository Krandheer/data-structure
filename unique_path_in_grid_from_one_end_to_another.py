# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[-1 for j in range(n)] for i in range(m)]
#         return self.helper(m - 1, n - 1, dp)

#     def helper(self, i, j, dp):
#         if i == 0 and j == 0:
#             return 1
#         if i < 0 or j < 0:
#             return 0
#         if dp[i][j] != -1:
#             return dp[i][j]

#         dp[i][j] = self.helper(i - 1, j, dp) + self.helper(i, j - 1, dp)
#         return dp[i][j]


def paths(m, n, dp):
    if m == 0 or n == 0:
        return 1
    elif m < 0 or n < 0:
        return 0
    if dp[m][n] != -1:
        return dp[m][n]
    dp[m][n] = paths(m - 1, n, dp) + paths(m, n - 1, dp)
    return dp[m][n]


def uniquePaths(m: int, n: int) -> int:
    dp = [[-1] * n for j in range(m)]
    return paths(m - 1, n - 1, dp)


print(uniquePaths(3, 7))
