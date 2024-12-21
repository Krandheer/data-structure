def rob(nums):
    n = len(nums)
    if nums is None or n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[n - 1]


class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        return self.rob2(n - 1, nums, [-1] * n)

    # base recursion for dp
    def rob2(self, i, nums, dp):
        if i == 0:
            return nums[i]
        elif i < 0:
            return 0
        if dp[i] != -1:
            return dp[i]
        pick = nums[i] + self.rob2(i - 2, nums, dp)
        unpick = 0 + self.rob2(i - 1, nums, dp)
        dp[i] = max(pick, unpick)
        return dp[i]
