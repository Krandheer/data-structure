import collections
import heapq
from collections import defaultdict
import math
from typing import List


def find_minimumTime(strength: List[int], K: int) -> int:
    x = 1
    energy = 0
    time = 0
    n = len(strength)
    strength.sort()
    i = 0
    temp = defaultdict(int)
    for ele in strength:
        temp[ele] += 1
    while n > 0:
        time += 1
        energy = energy + x

        if energy >= strength[i]:
            n = n - 1
            energy = 0
            x = x + K
            temp[strength[i]] -= 1
            i += 1
        elif energy in temp and temp[energy] > 0:
            n = n - 1
            x = x + K
            temp[energy] -= 1
            energy = 0
            i += 1

    return time


# print(find_minimumTime([20, 22, 16], 10))


def max_two_events(events: List[List[int]]):
    events.sort(key=lambda x: x[0])
    memo = {}

    def dp(index, prev_end, k):
        if index >= len(events):
            return 0

        if (index, prev_end) in memo:
            return memo[(index, prev_end)]

        start, end, val = events[index]
        not_take = dp(index + 1, prev_end, k)
        take = 0
        if start > prev_end and k < 2:
            take = val + dp(index + 1, end, k + 1)
        result = max(take, not_take)
        memo[(index, prev_end)] = result
        return result

    return dp(0, float("-inf"), 0)

    # print(max_two_events([[1, 3, 2], [4, 5, 2], [1, 5, 5]]))


def is_array_special(nums: List[int], queries: List[List[int]]) -> List[bool]:
    def found(start, end, voilating_index):
        left, right = 0, len(voilating_index) - 1
        while left <= right:
            mid = (left + right) // 2
            index = voilating_index[mid]
            if start < index <= end:
                return True
            elif index < start:
                left = mid + 1
            else:
                right = mid - 1
        return False

    voilating_index = []
    for i in range(1, len(nums)):
        if nums[i - 1] % 2 == nums[i] % 2:
            voilating_index.append(i)
    ans = []
    for q in queries:
        start, end = q
        if found(start, end, voilating_index):
            ans.append(False)
        else:
            ans.append(True)
    return ans


# print(is_array_special([4, 3, 1, 6], [[0, 2], [2, 3]]))


def pick_gifts(gifts: List[int], k: int) -> int:
    temp = [-num for num in gifts]
    heapq.heapify(temp)
    for _ in range(k):
        heapq.heappush(temp, -(math.isqrt(-heapq.heappop(temp))))
    return sum([-x for x in temp])


# print(pick_gifts([25, 64, 9, 4, 100], 4))


def find_score(nums: List[int]) -> int:
    marked = [False] * len(nums)
    ans = 0
    heap = []
    for i, num in enumerate(nums):
        heapq.heappush(heap, (num, i))
    while heap:
        num, i = heapq.heappop(heap)
        if not marked[i]:
            ans += num
            marked[i] = True
            if i - 1 >= 0:
                marked[i - 1] = True
            if i + 1 < len(nums):
                marked[i + 1] = True
    return ans


def continuous_subarrays(nums: List[int]) -> int:
    left, right, count = 0, 0, 0
    n = len(nums)
    temp = {}
    while right < n:
        temp[nums[right]] = temp.get(nums[right], 0) + 1
        while max(temp) - min(temp) > 2:
            temp[nums[left]] -= 1
            if temp[nums[left]] == 0:
                del temp[nums[left]]
            left += 1
        count += right - left + 1
        right += 1

    return count


# print(continuous_subarrays([5, 4, 2, 4]))


def max_average_ratio(classes: List[List[int]], extraStudents: int) -> float:
    # leetcode 1792. Maximum Average Pass Ratio
    heap = []
    for i, val in enumerate(classes):
        a, b = val
        j = (a / b) - (a + 1) / (b + 1)
        heapq.heappush(heap, (j, i))

    while extraStudents > 0:
        j, i = heapq.heappop(heap)
        a, b = classes[i]
        classes[i] = [a + 1, b + 1]
        j = ((a + 1) / (b + 1)) - ((a + 2) / (b + 2))
        heapq.heappush(heap, (j, i))
        extraStudents -= 1

    res = 0
    for i, val in enumerate(classes):
        a, b = val
        res += a / b

    res = res / len(classes)
    return res


print(max_average_ratio([[1, 2], [3, 5], [2, 2]], 2))
