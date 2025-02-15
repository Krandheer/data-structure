# 13 feb, 2025
# 1. Given a number, find the next greater number using same digits(or by rearranging the digits).
# For example,
# if the given number is 1234
# then next greater number would be 1243.
# If the input is 6918652
# then the output should be the number 6921568.
# For the input 1243,
# next greater number would be 1324.
# If there is no next greater number possible, then the program should return the same number. For example, for number 4321, same number 4321 would be returned.

# 6918652

# 6921568

# 1324
# 1243
# 1324

# ==========

# There is an array of balloons with varying heights on a straight line.
# Arrows can be launched towards the balloons from any height.
# Once an arrow hits a balloon, the arrow drops down to the next immediate height level (height - 1).
# How many arrows are needed to hit all the balloons in the given array.
# Input: Balloon array: [9,8,7,6,5,4]
# Output: 1
# Input: Balloon array: [3,4,1,2,2,6,1]
# Output: 5

# 3-0
# 4-1
# 1-1
# 2-1
# 6-1
# 1-1


from collections import defaultdict


def number_of_arrows(ballons):
    freq = defaultdict(int)
    for num in ballons:
        if num + 1 in freq and freq[num + 1] > 0:
            freq[num + 1] -= 1
        freq[num] += 1
    return sum(freq.values())


print(number_of_arrows([3, 4, 1, 2, 2, 6, 1]))


# 6969754
# 697 4569


def find_next_greater(nums):
    for i in range(len(nums) - 1, -1, -1):
        inflation_index = 0
        if nums[i] > nums[i - 1]:
            inflation_index = i - 1
            break
    swap_index = 0
    nums = nums[:i] + sorted(nums[inflation_index + 1 :])
    for i in range(inflation_index + 1, len(nums)):
        if nums[i] > nums[inflation_index]:
            swap_index = i
            break

    nums[inflation_index], nums[swap_index] = nums[swap_index], nums[inflation_index]
    return nums


print(find_next_greater([6, 9, 6, 9, 7, 5, 4]))
