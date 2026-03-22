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


def knapsack_dp(index, wt, val, bag_weight, dp):
    if index == 0 and bag_weight < wt[0]:
        return 0
    elif index == 0:
        return val[0]
    if dp[index][bag_weight] != -1:
        return dp[index][bag_weight]
    not_picked = knapsack_dp(index - 1, wt, val, bag_weight, dp)
    picked = -math.inf

    if wt[index] <= bag_weight:
        picked = val[index] + knapsack_dp(
            index - 1, wt, val, bag_weight - wt[index], dp
        )
    dp[index][bag_weight] = max(not_picked, picked)
    return dp[index][bag_weight]


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
dp = [[-1] * (bag_weight + 1) for _ in range(len(wt))]
print(knapsack(len(wt) - 1, wt, val, bag_weight))
print(knapsack_dp(len(wt) - 1, wt, val, bag_weight, dp))

# wt2 = [2, 4, 6]
# val2 = [5, 11, 13]
# bag_weight2 = 10
# print(unbounded_knapsack(len(wt2) - 1, wt2, val2, bag_weight2))


# given a two d board, and on board you can move max k step, and if you are on some cell you can move up down left right
# can you find how many given string could be formed, cell has character


def count_strings(board, word, max_steps):
    rows, cols = len(board), len(board[0])
    word_len = len(word)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y, index, steps):
        if steps > max_steps:
            return 0
        if index == word_len:
            return 1
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == word[index]:
                count += dfs(nx, ny, index + 1, steps + 1)
        return count

    total_count = 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:
                total_count += dfs(i, j, 1, 0)
    return total_count


# Example usage
board = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
word = "abc"
max_steps = 4
print(count_strings(board, word, max_steps))
