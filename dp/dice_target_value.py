"""
Find the way to get the to the particular number on dice
"""


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


dice("", 4)
print(dice2("", 4, []))


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
