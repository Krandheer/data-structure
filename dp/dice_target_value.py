"""
Find the way to get the to the particular number on dice
"""

# recursion
import time


def dice_rolls(target):
    if target == 0:
        return 1
    if target < 0:
        return 0

    total_ways = 0
    for i in range(1, 7):
        total_ways += dice_rolls(target - i)
    return total_ways


# memoization
def dice_rolls_memo(target, memo):
    if target == 0:
        return 1
    if target < 0:
        return 0
    if memo[target] != -1:
        return memo[target]

    total_ways = 0
    for i in range(1, 7):
        total_ways += dice_rolls_memo(target - i, memo)

    memo[target] = total_ways
    return total_ways


# bottom up dp
def dice_rolls_dp(target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for j in range(1, 7):
            if i - j >= 0:
                dp[i] += dp[i - j]
    return dp[target]


now = time.time()
print(dice_rolls(25))
print("Time taken (recursion):", time.time() - now)
now = time.time()
memo = [-1] * 26
print(dice_rolls_memo(25, memo))
print("Time taken (memoization):", time.time() - now)
now = time.time()
print(dice_rolls_dp(25))
print("Time taken (bottom up dp):", time.time() - now)


# Recursion
def dice(pat, target):
    if target == 0:
        print(pat)
    for i in range(1, target + 1):
        dice(pat + str(i), target - i)


def dice2(pat, target, result=[]):
    if target == 0:
        result.append(pat)
    for i in range(1, target + 1):
        dice2(pat + str(i), target - i, result)
    return result


# dice("", 4)
# print(dice2("", 4, []))


def coin_sum(coins, index, target):
    if index == 0:
        if target % coins[index] == 0:
            return 1
        else:
            return 0

    unpick = coin_sum(coins, index - 1, target)
    pick = 0
    if target >= coins[index]:
        pick = 1 + coin_sum(coins, index, target - coins[index])
    return pick + unpick


def coin_sum_dp(coins, index, target, dp):
    if index == 0:
        if target % coins[index] == 0:
            return 1
        else:
            return 0
    if dp[index][target] != -1:
        return dp[index][target]

    unpick = coin_sum_dp(coins, index - 1, target, dp)
    pick = 0
    if target >= coins[index]:
        pick = 1 + coin_sum_dp(coins, index, target - coins[index], dp)
    dp[index][target] = pick + unpick
    return dp[index][target]


# coins = [1, 2, 3]
# target = 4
# # 1111, 112, 121, 13, 211, 22, 31
# dp = [[-1] * (target + 1) for _ in range(len(coins))]
# print(coin_sum(coins, len(coins) - 1, target))
# print(coin_sum_dp(coins, len(coins) - 1, target, dp))
