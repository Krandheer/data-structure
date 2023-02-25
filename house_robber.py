def rob(nums):
    if nums is None or len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[len(nums) - 1]


class Solution:
    def rob(self, nums) -> int:
        return self.rob2(len(nums) - 1, nums, [-1] * (len(nums)))

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
