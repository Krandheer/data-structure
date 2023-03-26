def subsequence_sum_dp(i, nums, target, dp):
    if target == 0:
        return True
    elif i < 0:
        return False
    if dp[i][target] != -1:
        return dp[i][target]
    pick = False
    if target >= nums[i]:
        pick = subsequence_sum_dp(i - 1, nums, target - nums[i], dp)
    unpick = subsequence_sum_dp(i - 1, nums, target, dp)

    dp[i][target] = pick or unpick
    return dp[i][target]


def partition(arr):
    arr_sum = sum(arr)
    if arr_sum % 2 != 0:
        return False
    else:
        target = arr_sum // 2
        dp_1 = [[-1 for i in range(target + 1)] for j in range(len(nums))]
        return subsequence_sum_dp(len(arr) - 1, arr, target, dp_1)


nums = [2, 3, 3, 3, 4, 5]
print(partition(nums))
