from typing import List


# tag: dp
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        subarray_sum = []
        i, j, temp = 0, 0, 0

        while i <= j < len(nums):
            temp += nums[j]
            if j - i + 1 == k:
                subarray_sum.append(temp)
                temp -= nums[i]
                i += 1
            j += 1

        help = {}

        def helper(i, count):
            state = (i, count)
            if state in help:
                return help[state]
            if count == 0:
                return 0
            if i + k - 1 >= len(nums):
                return float("-inf")
            take = subarray_sum[i] + helper(i + k, count - 1)
            not_take = helper(i + 1, count)
            help[state] = max(take, not_take)
            return help[state]

        def solve(start_index, count, nums):
            if count == 0:
                return
            if start_index + k - 1 >= len(nums):
                return

            take = subarray_sum[start_index] + helper(start_index + k, count - 1)
            not_take = helper(start_index + 1, count)

            # this makes sure that we take lexicographically smallest index
            if take >= not_take:
                ans.append(start_index)
                solve(start_index + k, count - 1, nums)
            else:
                solve(start_index + 1, count, nums)

        ans = []
        solve(0, 3, nums)
        return ans
