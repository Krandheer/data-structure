"""
this is similar to fibonacci, so to reduce the space complexity
we can use pre and prev2 here and current variable and remove the dp
array from the code below
"""


def climb_stair(n):
    if n == 1 or n == 2:
        return n
    else:
        return climb_stair(n - 1) + climb_stair(n - 2)


def climbstairs_leetcode(n, dp):
    """
    leetcode dp day 2 question
    """
    if n == 1 or n == 2:
        return n

    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = climbstairs_leetcode(n - 1, dp) + climbstairs_leetcode(n - 2, dp)
        return dp[n]


print(climb_stair(5))
print(climbstairs_leetcode(5, [-1] * 6))
