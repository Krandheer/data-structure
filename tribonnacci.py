def helper_dp(self, n, dp):
    """
    leetcode dp question
    """
    if n == 1 or n == 0:
        return n
    elif n == 2:
        return 1
    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = self.helper_dp(n - 1, dp) + self.helper_dp(n - 2, dp) + self.helper_dp(n - 3, dp)
        return dp[n]
