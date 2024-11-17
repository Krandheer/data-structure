from typing import List


def shortest_subarray(nums: List[int], k: int) -> int:
    i, j = 0, 0
    if nums[0]==k:
        return 1

    smallest_len = len(nums)+1
    temp = 0

    while j < len(nums):
        if temp <= k:
            temp+=nums[j]
            j+=1
        if temp >= k:
            temp-=nums[i]
            smallest_len=min(smallest_len, j-i)
            i+=1

    if smallest_len>len(nums):
        return -1
    return smallest_len

print(shortest_subarray([1,2], 4))
