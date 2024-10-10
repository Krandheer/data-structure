from typing import List
from collections import Counter


def sort_colors(nums: List[int]) -> List:
    """
    dsa --> 5, day2
    Do not return anything, modify nums in-place instead.
    Given an array nums with n objects colored red, white, or blue, sort them in-place so that
    objects of the same color are adjacent, with the colors in the order red, white, and blue.
    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
    You must solve this problem without using the library's sort function.
    """
    maps = Counter(nums)
    track = 0
    for i in range(maps[0]):
        nums[i] = 0
        track += 1
    for j in range(track, maps[1] + track):
        nums[j] = 1
        track += 1
    for j in range(track, maps[2] + track):
        nums[j] = 2
        track += 1
    return nums


nums1 = [2, 0, 2, 1, 1, 0]

print(sort_colors(nums1))
