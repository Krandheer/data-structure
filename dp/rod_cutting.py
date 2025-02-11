import math
import sys

cost = [2, 5, 7, 8, 10]

"""
cost is the market price for length of rod, for length 1 price 2, length 2 price 5 and so on...
index+1 = rod length
think like collecting rod length of different sizes till you reach the rod length.
And while doing so keep maximazing the cost.
"""


def max_cost(index, rod, cost_arr):
    if index == 0:
        return rod * cost_arr[index]

    not_take = 0 + max_cost(index - 1, rod, cost_arr)
    take = -math.inf
    # below if condition makes sure that we pick valid length.
    rod_length = index + 1
    if rod_length <= rod:
        take = cost_arr[index] + max_cost(index, rod - rod_length, cost_arr)
    return max(not_take, take)


print(max_cost(len(cost) - 1, len(cost), cost))


# something is going phishy in this dp
def max_cost_dp(index, rod, cost_arr, dp):
    if index == 0:
        return rod * cost_arr[0]

    if dp[index][rod] != -1:
        return dp[index][rod]
    not_take = 0 + max_cost_dp(index - 1, rod, cost_arr, dp)
    take = -sys.maxsize
    rod_length = index + 1
    if rod_length <= rod:
        take = cost_arr[index] + max_cost_dp(index, rod - rod_length, cost_arr, dp)
    dp[index][rod] = max(not_take, take)
    return dp[index][rod]


dp = [[-1 for j in range(len(cost) + 1)] for i in range(len(cost))]
print(max_cost_dp(4, 5, cost, dp))
