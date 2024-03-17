from typing import *
from collections import Counter


def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    Given an array nums with n objects colored red, white, or blue, sort them in-place
    so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
    You must solve this problem without using the library's sort function.
    """
    map = Counter(nums)
    track = 0
    for i in range(map[0]):
        nums[i] = 0
        track += 1
    for j in range(track, map[1] + track):
        nums[j] = 1
        track += 1
    for j in range(track, map[2] + track):
        nums[j] = 2
        track += 1
    return nums


nums = [2, 0, 2, 1, 1, 0]

print(sortColors(nums))
