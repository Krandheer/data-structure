def maxProfit(prices):

    """
    leetcode buy sell stocks part II
    """
    ans = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            ans = ans + (prices[i + 1] - prices[i])
    return ans

