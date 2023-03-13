import math


def min_cuts_to_cut_rode(i, j, cuts):
    if i > j:
        return 0
    min_cost = math.inf
    for index in range(i, j + 1):
        cost = cuts[j + 1] - cuts[i - 1] + min_cuts_to_cut_rode(i, index - 1, cuts) + min_cuts_to_cut_rode(index + 1, j,
                                                                                                           cuts)
        min_cost = min(min_cost, cost)
    return min_cost


cuts = [1, 3, 4, 5]
rod_len = 7
cuts.append(rod_len)
cuts.insert(0, 0)
# sorting so that we have independent sub problem after each cut we do
cuts.sort()
print(min_cuts_to_cut_rode(1, len(cuts) - 2, cuts))


def min_cuts_dp(i, j, cuts, dp):
    if i > j:
        return 0
    min_cost = math.inf
    if dp[i][j] != -1:
        return dp[i][j]
    for index in range(i, j + 1):
        cost = cuts[j + 1] - cuts[i - 1] + min_cuts_dp(i, index - 1, cuts, dp) + min_cuts_dp(index + 1, j, cuts, dp)
        min_cost = min(min_cost, cost)
        dp[i][j] = min_cost
    return dp[i][j]


dp = [[-1 for i in range(len(cuts))] for j in range(len(cuts))]
print(min_cuts_dp(1, len(cuts) - 2, cuts, dp))
print(dp)
