class Solution_recursion:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        index1 = len(s) - 1
        index2 = len(t) - 1
        return self.helper(index1, index2, s, t)

    def helper(self, index1, index2, s, t):
        if index1 < 0 or index2 < 0:
            return 0

        if s[index1] == t[index2]:
            return 1 + self.helper(index1 - 1, index2 - 1, s, t)
        return max(
            self.helper(index1 - 1, index2, s, t), self.helper(index1, index2 - 1, s, t)
        )


class Solution_dp:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        index1 = len(s) - 1
        index2 = len(t) - 1
        dp = [[-1] * len(t) for _ in range(len(s))]
        return self.helper(index1, index2, s, t, dp)

    def helper(self, index1, index2, s, t, dp):
        if index1 < 0 or index2 < 0:
            return 0
        if dp[index1][index2] != -1:
            return dp[index1][index2]
        if s[index1] == t[index2]:
            dp[index1][index2] = 1 + self.helper(index1 - 1, index2 - 1, s, t, dp)
            return dp[index1][index2]
        dp[index1][index2] = max(
            self.helper(index1 - 1, index2, s, t, dp),
            self.helper(index1, index2 - 1, s, t, dp),
        )
        return dp[index1][index2]
