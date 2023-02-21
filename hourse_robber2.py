class Solution:
    """leet code dp problem"""

    def rob(self, nums) -> int:
        N = len(nums)

        if N <= 1:
            return sum(nums)

        if N == 2:
            return max(nums[0], nums[1])

        dp1, nums1 = [0] * (N - 1), nums[:N - 1]
        dp2, nums2 = [0] * (N - 1), nums[1:]

        # base cases
        dp1[0], dp1[1] = nums1[0], max(nums1[0], nums1[1])
        dp2[0], dp2[1] = nums2[0], max(nums2[0], nums2[1])

        for i in range(2, N - 1):
            dp1[i] = max(dp1[i - 1], nums1[i] + dp1[i - 2])

        for i in range(2, N - 1):
            dp2[i] = max(dp2[i - 1], nums2[i] + dp2[i - 2])

        return max(dp1[N - 2], dp2[N - 2])