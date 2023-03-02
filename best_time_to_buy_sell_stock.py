def maxProfit(prices) -> int:
    """
    leetcode solution day 7
    """
    # better optimised
    if len(prices) < 2:
        return 0
    max_profit = 0
    lowest_val = prices[0]
    if prices[1] > prices[0]:
        max_profit = prices[1] - prices[0]

    for num in prices:
        if num < lowest_val:
            lowest_val = num
        max_profit = max(max_profit, num - lowest_val)

    return max_profit

    # brute force
    # ans = 0
    # for index, num in enumerate(prices):
    #     for j in range(1, len(prices)):
    #         if index < j:
    #             ans = max(ans, prices[j] - num)
    # return ans


print(maxProfit([7, 1, 5, 3, 6, 4]))
