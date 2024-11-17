from typing import List


def shortest_subarray(nums: List[int], k: int) -> int:
    i = 0
    j = 0
    smallest_len = len(nums) + 1
    temp = 0
    n = len(nums)

    while j < n:
        temp += nums[j]

        while i <= j and temp >= k:
            smallest_len = min(smallest_len, j - i + 1)
            temp -= nums[i]
            i += 1

        j += 1

        if temp <= 0:
            temp = 0
            i = j

    return smallest_len if smallest_len <= n else -1

print(shortest_subarray([1,2], 4))
