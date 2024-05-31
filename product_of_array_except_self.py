def productExceptSelf(nums):
    prefix = []
    suffix = [0] * len(nums)
    ans = []
    prefix.append(1)
    for i in range(1, len(nums)):
        prefix.append(prefix[i - 1] * nums[i - 1])
    suffix[-1] = 1
    for i in range(len(nums) - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    for i in range(len(nums)):
        ans.append(prefix[i] * suffix[i])
    return ans


nums = [1, 2, 3, 4]
ans = productExceptSelf(nums)
print(ans)
