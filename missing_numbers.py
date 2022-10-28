"""
Leetcode:
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

python len() function takes O(1) time
"""


def missing_number(nums):
    # for i in range(len(nums) + 1):
    #     if i not in nums:
    #         return i

    # return (set(range(len(nums)+1)) - set(nums)).pop()

    n = len(nums)
    return (n * (n + 1)) // 2 - sum(nums)
