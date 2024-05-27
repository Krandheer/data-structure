from collections import Counter
import heapq


def topKFrequent(nums, k):
    d = Counter(nums)
    min_heap = []
    for num, freq in d.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    ans = [num for _, num in min_heap]

    return ans


nums = [1, 1, 1, 2, 2, 3]

ans = topKFrequent(nums, 2)
print(ans)
