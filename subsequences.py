def sub_seqeunces(temp_p, temp_up, ans):
    if len(temp_up) == 0:
        ans.append(temp_p)
        return
    elem = temp_up[0]
    temp_p.append(elem)
    sub_seqeunces(temp_p[:], temp_up[1:], ans)
    temp_p.remove(elem)
    sub_seqeunces(temp_p[:], temp_up[1:], ans)
    return ans


# print(sub_array([], [5, 4, -1, ], []))


def subsequences(temp_p, temp_up):
    if len(temp_up) == 0:
        print(temp_p)
        return
    elem = temp_up[0]
    temp_p.append(elem)
    subsequences(temp_p, temp_up[1:])
    temp_p.remove(elem)
    subsequences(temp_p, temp_up[1:])


print(subsequences([], [-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def max_subsequence_sum(i, nums, dp):
    if i == 0:
        return nums[i]
    elif i < 0:
        return 0
    if dp[i] != -1:
        return dp[i]
    pick = nums[i] + max_subsequence_sum(i - 1, nums, dp)
    unpick = 0 + max_subsequence_sum(i - 1, nums, dp)
    dp[i] = max(pick, unpick)
    return dp[i]


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subsequence_sum(len(nums) - 1, nums, [-1] * (len(nums))))
