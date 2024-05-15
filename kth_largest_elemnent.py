import heapq


def kth_largest_ele(nums, k):
    # find kth largest element in array without sorting it
    bag = []
    for i in nums:
        heapq.heappush(bag, i)

    ans = 0
    for i in range(len(nums) - k + 1):
        ans = heapq.heappop(bag)
    return ans


nums = [3, 2, 1, 5, 6, 4]
k = 2
