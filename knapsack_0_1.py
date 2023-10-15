"""
0/1 knapsack uses the concept of pick and not pick of subsequence problems.
"""

import math

wt = [3, 2, 5]
val = [30, 40, 60]
bag_weight = 6


def knapsack(index, wt, val, bag_weight):
    if index == 0 and bag_weight < wt[0]:
        return 0
    elif index == 0:
        return val[0]
    not_picked = 0 + knapsack(index - 1, wt, val, bag_weight)
    picked = -math.inf

    if wt[index] <= bag_weight:
        picked = val[index] + knapsack(index - 1, wt, val, bag_weight - wt[index])
    return max(not_picked, picked)


print(knapsack(len(wt) - 1, wt, val, bag_weight))
