from typing import List


# leetcode biweekly contest
def minCost_contest(m: int, n: int, waitCost: List[List[int]]) -> int:
    dp = [[[-1] * 2 for _ in range(n)] for _ in range(m)]

    def grid_travel(i, j, time):
        if i == m - 1 and j == n - 1:
            return 0

        parity = time % 2
        if dp[i][j][parity] != -1:
            return dp[i][j][parity]

        # wait here if even time
        if parity == 0:
            dp[i][j][parity] = waitCost[i][j] + grid_travel(i, j, time + 1)

        # must move but in min cost direction
        else:
            res = float("inf")
            if i + 1 < m:
                entry_cost = (i + 2) * (j + 1)
                res = min(res, entry_cost + grid_travel(i + 1, j, time + 1))
            if j + 1 < n:
                entry_cost = (i + 1) * (j + 2)
                res = min(res, entry_cost + grid_travel(i, j + 1, time + 1))
            dp[i][j][parity] = res

        return dp[i][j][parity]

    return 1 + grid_travel(0, 0, 1)
