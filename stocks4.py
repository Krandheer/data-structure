def maxProfit(prices, fee):
    """
    same as third one except that here one complete transaction has some fee and cool down period is not needed.
    """
    dp = [[-1, -1] for i in range(len(prices))]
    return helper(prices, 0, 0, dp, fee)


def helper(prices, index, buy, dp, fee):
    if index >= len(prices):
        return 0
    if dp[index][buy] != -1:
        return dp[index][buy]
    if not buy:
        dp[index][buy] = max(
            -prices[index] + helper(prices, index + 1, 1, dp, fee),
            helper(prices, index + 1, 0, dp, fee),
        )
    elif buy:
        dp[index][buy] = max(
            prices[index] - fee + helper(prices, index + 2, 0, dp, fee),
            helper(prices, index + 1, 1, dp, fee),
        )
    return dp[index][buy]
