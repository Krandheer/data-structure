def maxSubarraySumCircular(nums) -> int:
    if len(nums) < 1:
        return 0
    t = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            t = t + 1
    if t == 0:
        return max(nums)

    # kadane max
    result = max(nums)
    temp = 0
    for i in range(len(nums)):
        temp += nums[i]
        if temp < 0:
            temp = 0
        else:
            result = max(temp, result)

            # initialize array with negative of same values
    arr = [0] * (len(nums))
    for i in range(len(nums)):
        arr[i] = -nums[i]

    # perform kadane's algo
    result2 = max(arr)
    temp2 = 0
    for i in range(len(arr)):
        temp2 += arr[i]
        if temp2 < 0:
            temp2 = 0
        else:
            result2 = max(temp2, result2)

    # return max value
    return max(result, sum(nums) + result2)
