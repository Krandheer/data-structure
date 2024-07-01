import math


def max_sum_subarray(nums):
    maxi = -math.inf
    i, j = 0, 0
    temp = 0
    start_sub = 0
    end_sub = 0
    while i <= j and i < len(nums) and j < len(nums):
        temp += nums[j]
        j += 1
        if temp < 0:
            i += 1
            temp = 0
            maxi = max(maxi, temp)
            continue
        if temp > maxi:
            maxi = temp
            start_sub = i
            end_sub = j
    print(maxi)
    return nums[start_sub + 1 : end_sub]


# inp1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(max_sum_subarray(inp1))
