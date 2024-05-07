def max_profit(prices) -> int:
    """leetcode solution day 7"""
    # better optimised
    if len(prices) < 2:
        return 0
    highest_profit = 0
    lowest_val = prices[0]
    if prices[1] > prices[0]:
        highest_profit = prices[1] - prices[0]

    for num in prices:
        if num < lowest_val:
            lowest_val = num
        highest_profit = max(highest_profit, num - lowest_val)

    return highest_profit

    # brute force
    # ans = 0
    # for index, num in enumerate(prices):
    #     for j in range(1, len(prices)):
    #         if index < j:
    #             ans = max(ans, prices[j] - num)
    # return ans


# two pointer approach
def pro(arr):
    i, j = 0, 1
    ans = 0
    while i <= j and j < len(arr):
        if arr[i] <= arr[j]:
            ans = max(ans, arr[j] - arr[i])
            j += 1
        else:
            i = j
            j += 1
    return ans


print(max_profit([7, 1, 5, 3, 6, 4]))
print(pro([7, 1, 5, 3, 6, 4]))
