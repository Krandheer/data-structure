def numberOfArithmeticSlices(nums) -> int:
    # count = 0
    # for i in range(len(nums) - 2):
    #     diff = nums[i + 1] - nums[i]
    #     for j in range(i + 2, len(nums)):
    #         if nums[j] - nums[j - 1] == diff:
    #             count += 1
    #         else:
    #             break
    # return count

    n = len(nums)
    dp = [0] * n
    ans = 0
    for i in range(2, n):
        if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
            dp[i] = dp[i - 1] + 1
        ans += dp[i]
    return ans


print(numberOfArithmeticSlices([1, 2, 3, 4]))
