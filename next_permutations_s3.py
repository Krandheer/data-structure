from typing import List


def nextPermutation(nums: List[int]) -> None:
    """
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


nums = [2, 3, 1]
nextPermutation(nums)
print(nums)
