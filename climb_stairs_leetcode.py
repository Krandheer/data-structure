def climb_stair(n):
    if n == 1 or n == 2:
        return n
    else:
        return climb_stair(n - 1) + climb_stair(n - 2)


def climbstairs_leetcode(self, n, dp):
    """
    leetcode dp day 2 question
    """
    if n == 1 or n == 2:
        return n

    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = self.climbstairs_leetcode(n - 1, dp)
        +self.climbstairs_leetcode(n - 2, dp)
        return dp[n]
