import heapq
from typing import List


# a good problem, if you want min sum then use max-heap instead of min-heap
# most subsequence problem are about dp because we can't use window or two pointer
# but many time they could be solved using some trick like here.
def max_subsequence(nums: List[int], k: int):
    max_heap = [(x, i) for i, x in enumerate(nums[:k])]
    heapq.heapify(max_heap)
    total = sum(nums[:k])

    for i in range(k, len(nums)):
        heapq.heappush(max_heap, (nums[i], i))
        total += nums[i]
        total -= heapq.heappop(max_heap)[0]

    max_heap.sort(key=lambda x: x[1])

    def dp(ind):
        if ind == k:
            return 0
        if ind == len(nums):
            return float("-inf")
        skip = dp(ind + 1)
        take = nums[i] + dp(ind + 1)
        return max(skip, take)

    ans = dp(0)
    temp = [i for i, x in max_heap]
    return (ans, temp)


print(max_subsequence(nums=[2, 1, 3, 3], k=2))
