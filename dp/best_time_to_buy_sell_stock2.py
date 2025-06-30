"""using dp take or not take logic, if buy then that means I am giving money and
if bought then set buy to 1, so that it indicates that we can't buy till we sell
and make buy to 0, and each time we call function we move one index"""

import time


def maxprofit_recursion(price, index, buy):
    """recursion for max profit"""
    if index >= len(price):
        return 0
    if buy:
        return max(
            -price[index] + maxprofit_recursion(price, index + 1, 0),
            maxprofit_recursion(price, index + 1, 1),
        )
    return max(
        +price[index] + maxprofit_recursion(price, index + 1, 1),
        maxprofit_recursion(price, index + 1, 0),
    )


def max_profit(prices) -> int:
    """returns max profit"""
    dp = [[-1, -1] for _ in range(len(prices))]
    return helper(prices, 0, 1, dp)


def helper(prices, index, buy, dp):
    if index >= len(prices):
        return 0
    if dp[index][buy] != -1:
        return dp[index][buy]
    if not buy:
        dp[index][buy] = max(
            prices[index] + helper(prices, index + 1, 1, dp),
            helper(prices, index + 1, 0, dp),
        )
    elif buy:
        dp[index][buy] = max(
            -prices[index] + helper(prices, index + 1, 0, dp),
            helper(prices, index + 1, 1, dp),
        )
    return dp[index][buy]


ipt = [7, 1, 5, 3, 6, 4]
# print(max_profit([4, 9, 0, 4, 10]))
now = time.time()
print(maxprofit_recursion(ipt, 0, 1))
print("Time taken for recursion:", time.time() - now)
now = time.time()
print(max_profit(ipt))
print("Time taken for dp:", time.time() - now)
