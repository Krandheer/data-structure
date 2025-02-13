from collections import defaultdict
from typing import List


# tag: dp
def mincost_tickets(days: List[int], costs: List[int]):
    temp = defaultdict(int)
    for index, day in enumerate(days):
        temp[day] = index
    dp = {}

    def solve(i):
        if i in dp:
            return dp[i]
        if i > days[len(days) - 1]:
            return 0

        if i not in temp:
            return solve(i + 1)

        take_1 = costs[0] + solve(i + 1)
        take_7 = costs[1] + solve(i + 7)
        take_30 = costs[2] + solve(i + 30)

        dp[i] = min(take_1, take_7, take_30)

        return dp[i]

    return solve(1)
