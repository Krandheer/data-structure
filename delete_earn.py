from collections import Counter

"""
covert the delete and earn problem to house robber problem and then use house robber concept to solve it
how to convert to house robber? use indices as place for same number, so indices 1 represents some of one 
and 2 sum of two if no 2 present then it is 0, so by default you will skip element before and after a index
and hence house robber problem.
now use pick unpick method, if picked then move two indices as you can pick adjacent next and if not then move
to adjacent next. and select max value between two that will get added to dp for that index.
"""


def delete_and_earn(nums):
    max_num = max(nums)
    x = Counter(nums)
    arr = [0] * (max_num + 1)
    for k, v in x.items():
        arr[k] = k * v

    return rob2(len(arr) - 1, arr, [-1] * (len(arr)))


def rob2(i, nums, dp):
    if i == 0:
        return nums[0]
    elif i < 0:
        return 0
    if dp[i] != -1:
        return dp[i]
    pick = nums[i] + rob2(i - 2, nums, dp)
    unpick = 0 + rob2(i - 1, nums, dp)
    dp[i] = max(pick, unpick)
    return dp[i]


print(delete_and_earn([3, 3, 3, 4, 2]))
