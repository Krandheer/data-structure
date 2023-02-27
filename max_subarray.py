def maxSubArray(nums) -> int:
    if len(nums) < 1:
        return 0
    result = max(nums)

    temp = 0
    for i in range(len(nums)):
        temp += nums[i]
        if temp < 0:
            temp = 0
        else:
            result = max(temp, result)

    return result


print(maxSubArray([-2, -1]))
