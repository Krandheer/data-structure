def canJump(nums):
    return helper(0, nums, [False] * (len(nums)))


def helper(i, nums, dp):
    if i == len(nums)-1:
        return True
    if dp[i]:
        return True
    for j in range(1, nums[i] + 1):
        if i+j <= len(nums):
            dp[i+j] = helper(i + j, nums, dp)

    if dp[len(nums)-1]:
        return True
    else:
        return False


def helper2(i, nums):
    if i == len(nums) - 1:
        return True
    for j in range(1, nums[i] + 1):
        val = helper2(i + j, nums)
        if val:
            return True

    return False


print(canJump([2, 0, 2]))
