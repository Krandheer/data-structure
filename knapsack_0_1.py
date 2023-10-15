"""
0/1 knapsack uses the concept of pick and not pick of subsequence problems.
"""

import math


# 0/1 knapsack: can pick one element only once
def knapsack(index, wt, val, bag_weight):
    if index == 0 and bag_weight < wt[0]:
        return 0
    elif index == 0:
        return val[0]
    not_picked = knapsack(index - 1, wt, val, bag_weight)
    picked = -math.inf

    if wt[index] <= bag_weight:
        picked = val[index] + knapsack(index - 1, wt, val, bag_weight - wt[index])
    return max(not_picked, picked)


# knapsack where picking one element many times is allowed
def unbounded_knapsack(index, wt, val, bag_weight):
    if index == 0 and bag_weight < wt[0]:
        return 0
    elif index == 0:
        return val[0]
    not_picked = unbounded_knapsack(index - 1, wt, val, bag_weight)
    picked = -math.inf

    if wt[index] <= bag_weight:
        picked = val[index] + unbounded_knapsack(index, wt, val, bag_weight - wt[index])
    return max(not_picked, picked)


wt = [3, 2, 5]
val = [30, 40, 60]
bag_weight = 6
print(knapsack(len(wt) - 1, wt, val, bag_weight))

wt2 = [2, 4, 6]
val2 = [5, 11, 13]
bag_weight2 = 10
print(unbounded_knapsack(len(wt2) - 1, wt2, val2, bag_weight2))
