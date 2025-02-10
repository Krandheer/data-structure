from typing import List


class Solution:
    """
    leetcode problem
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(
            self.help(0, cost, [-1] * (len(cost) + 1)),
            self.help(1, cost, [-1] * (len(cost) + 1)),
        )

    def help(self, start, cost, dp):
        if start >= len(cost):
            return 0
        if dp[start] != -1:
            return dp[start]
        dp[start] = (
            min(self.help(start + 1, cost, dp), self.help(start + 2, cost, dp))
            + cost[start]
        )
        return dp[start]
