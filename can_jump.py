def canJump(nums):
    return helper(nums)


def helper(nums):
    goal = len(nums) - 1
    # start from last and see if you can reach the next last or not and that's it.
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal == 0


def helper2(i, nums):
    if i == len(nums) - 1:
        return True
    for j in range(1, nums[i] + 1):
        val = helper2(i + j, nums)
        if val:
            return True

    return False


print(canJump([2, 0, 2]))
