from typing import List


def shortest_subarray(nums: List[int], k: int) -> int:
    # nums.sort()
    i, j = 0, 0
    if nums[0]==k:
        return 1

    smallest_len = 0
    temp = 0
    while j < len(nums):
        if temp <= k:
            temp+=nums[j]
            j+=1
        if temp >= k:
            temp-=nums[i]
            if smallest_len == 0:
                smallest_len =j-i
            else:
                smallest_len=min(smallest_len, j-i)
            i+=1

    if smallest_len>0:
        return smallest_len
    return -1

print(shortest_subarray([89,67,99,25,29], 166))
