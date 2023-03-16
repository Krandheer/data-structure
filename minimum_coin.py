import math


def minimum_coin_to_target(index, target, arr_coin):
    """
    return minimum number of coin to make the target
    """
    if index == 0:
        if target % arr_coin[0] == 0:
            return target // arr_coin[0]
        return math.inf
    not_take = 0 + minimum_coin_to_target(index - 1, target, arr_coin)
    take = math.inf
    if arr_coin[index] <= target:
        take = 1 + minimum_coin_to_target(index, target - arr_coin[index], arr_coin)
    return min(not_take, take)


coin_denom = [1, 2, 3]
target = 7
print(minimum_coin_to_target(2, target, coin_denom))


def minimum_coin_dp(index, target, arr_coin, dp):
    """
    return minimum number of coin to make the target
    """
    if index == 0:
        if target % arr_coin[0] == 0:
            return target // arr_coin[0]
        return math.inf
    if dp[index][target] != -1:
        return dp[index][target]
    not_take = 0 + minimum_coin_dp(index - 1, target, arr_coin, dp)
    take = math.inf
    if arr_coin[index] <= target:
        take = 1 + minimum_coin_dp(index, target - arr_coin[index], arr_coin, dp)
    dp[index][target] = min(not_take, take)
    return dp[index][target]


dp_1 = [[-1 for i in range(target+1)] for j in range(len(coin_denom))]
print(minimum_coin_dp(2, target, coin_denom, dp_1))
