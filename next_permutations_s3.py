from typing import *


def nextPermutation(nums: List[int]) -> None:
    """
    dsa ->3, day2
    Do not return anything, modify nums in-place instead.
    """
    is_modified = False
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            for j in range(len(nums) - 1, i - 1, -1):
                if nums[j] > nums[i - 1]:
                    nums[i - 1], nums[j] = nums[j], nums[i - 1]
                    break
            nums[i:] = reversed(nums[i:])
            is_modified = True
            break
    if not is_modified:
        nums.reverse()


nums = [3, 2, 1]
print(nextPermutation(nums))
