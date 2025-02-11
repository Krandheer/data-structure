def sub_seqeunces(temp_p, temp_up, ans):
    """
    we can use this code to check longest increasing subsequence in brute force approach,
    just before adding in answer check if it is increasing sequence if yes add it
    and have a variable to store the length and keep modifying the length if any
    longer length found.
    and since it is recursion we can optimise it using memoization technique
    """

    if len(temp_up) == 0:
        ans.append(temp_p)
        return
    elem = temp_up[0]
    temp_p.append(elem)
    sub_seqeunces(temp_p[:], temp_up[1:], ans)
    temp_p.remove(elem)
    sub_seqeunces(temp_p[:], temp_up[1:], ans)
    return ans


# unprocess = [5, 4, -1]
# print(sub_seqeunces([], unprocess, []))


def subsequences(temp_p, temp_up):
    if len(temp_up) == 0:
        print(temp_p)
        return
    elem = temp_up[0]
    temp_p.append(elem)
    subsequences(temp_p, temp_up[1:])
    temp_p.remove(elem)
    subsequences(temp_p, temp_up[1:])


# print(subsequences([], [-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def max_subsequence_sum(i, nums, dp):
    if i == 0:
        return nums[i]
    if i < 0:
        return 0
    if dp[i] != -1:
        return dp[i]
    pick = nums[i] + max_subsequence_sum(i - 1, nums, dp)
    unpick = 0 + max_subsequence_sum(i - 1, nums, dp)
    dp[i] = max(pick, unpick)
    return dp[i]


# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# dp_1 = [-1]*len(nums)
# print(max_subsequence_sum(len(nums) - 1, nums, dp_1))
# print(dp_1)


def subsequence_sum(i, nums, target):
    if target == 0:
        return True
    if i < 0:
        return False
    pick = False
    if target >= nums[i]:
        pick = subsequence_sum(i - 1, nums, target - nums[i])
    unpick = subsequence_sum(i - 1, nums, target)

    return pick or unpick


# nums = [1, 2, 3, 4]
# target = 4
# print(subsequence_sum(len(nums) - 1, nums, target))


def subsequence_sum_dp(i, nums, target, dp):
    if target == 0:
        return True
    if i < 0:
        return False
    if dp[i][target] != -1:
        return dp[i][target]
    pick = False
    if target >= nums[i]:
        pick = subsequence_sum_dp(i - 1, nums, target - nums[i], dp)
    unpick = subsequence_sum_dp(i - 1, nums, target, dp)

    dp[i][target] = pick or unpick
    return dp[i][target]


#
# nums = [1, 2, 3, 4]
# target = 4
# dp_1 = [[-1 for _ in range(target + 1)] for _ in range(len(nums))]
# print(subsequence_sum_dp(len(nums) - 1, nums, target, dp_1))


def subsequence_sum_count(i, nums, target):
    """
    find number of subsequence of nums that have sum equal to target.
    """
    if target == 0:
        return 1
    if i == 0:
        if target == 0 and nums[0] == 0:
            return 2
        if target in (0, nums[0]):
            return 1

        return 0

    unpick = subsequence_sum_count(i - 1, nums, target)
    pick = 0
    if target >= nums[i]:
        pick = subsequence_sum_count(i - 1, nums, target - nums[i])

    return pick + unpick


# nums = [1, 2, 3, 4, 0]
# target = 3
# print(subsequence_sum_count(len(nums) - 1, nums, target))
