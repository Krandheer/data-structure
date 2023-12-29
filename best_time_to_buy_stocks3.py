def maxProfit(prices) -> int:
    """
    using dp take or not take logic, if buy then that means I am giving money and if bought then set buy to 1, so that
    it indicates that we can't buy till we sell and make buy to 1, and each time we sell and call function then
    we move two point ahead in index value for taking care of cooldown period.
    """
    dp = [[-1, -1] for _ in range(len(prices))]
    return helper(prices, 0, 0, dp)


def helper(prices, index, buy, dp):
    if index >= len(prices):
        return 0
    if dp[index][buy] != -1:
        return dp[index][buy]
    if not buy:
        dp[index][buy] = max(
            -prices[index] + helper(prices, index + 1, 1, dp),
            helper(prices, index + 1, 0, dp),
        )
    elif buy:
        dp[index][buy] = max(
            prices[index] + helper(prices, index + 2, 0, dp),
            helper(prices, index + 1, 1, dp),
        )
    return dp[index][buy]
