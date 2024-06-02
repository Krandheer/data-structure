def findMaxAverage(nums, k):
    i = 0
    j = i + k - 1
    temp = 0
    for m in range(0, k):
        temp += nums[m]
    maxi = float("-inf")
    while j < len(nums):
        maxi = max(maxi, temp / k)
        temp -= nums[i]
        i += 1
        j += 1
        if j < len(nums):
            temp += nums[j]
        else:
            break
    return maxi


nums = [-1]
k = 1

ans = findMaxAverage(nums, k)
print(ans)
