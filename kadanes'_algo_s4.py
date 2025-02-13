from typing import List


def maxSubArray(nums: List[int]) -> int:
    """
    find the subarray with maximum sum
    """
    if max(nums) < 0:
        return max(nums)
    maxi = 0
    temp = 0
    for i in nums:
        if i >= 0 or temp + i >= 0:
            temp += i
            maxi = max(maxi, temp)
        else:
            temp = 0
    return maxi


nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [-1, -2]
print(maxSubArray(nums1))
