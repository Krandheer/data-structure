from collections import defaultdict
from operator import le
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0
    temp = set()
    for num in nums:
        temp.add(num)

    start = set()
    for num in nums:
        if num - 1 not in temp:
            start.add(num)

    ans = 1
    for num in start:
        count = 1
        while num + 1 in temp:
            count += 1
            num += 1
        ans = max(ans, count)

    return ans


def lengthOfLongestSubstring(s: str) -> int:
    l, r = 0, 0
    temp = defaultdict(int)
    maxi = 0
    while l <= r < len(s):
        if s[r] not in temp:
            temp[s[r]] = r
            maxi = max(maxi, r - l + 1)
            r += 1
        else:
            l = temp[s[r]] + 1
            r = l
            temp = defaultdict(int)
    return maxi


# tags: leetcode: 424, quite good problem
def characterReplacement(s: str, k: int) -> int:
    temp = defaultdict(int)
    l, r = 0, 0
    ans = 0
    maxi = 0
    while r < len(s):
        m = r - l + 1
        temp[s[r]] += 1
        maxi = max(maxi, temp[s[r]])
        if m - maxi > k:
            temp[s[l]] -= 1
            l += 1
        ans = max(ans, r - l + 1)
        r += 1

    return ans


def checkInclusion(s1: str, s2: str) -> bool:
    s1_map = defaultdict(int)
    for i in s1:
        s1_map[i] += 1

    n = len(s1)

    l, r = 0, n
    while r <= len(s2):
        temp = defaultdict(int)
        for i in range(l, r):
            temp[s2[i]] += 1
        if temp == s1_map:
            return True
        l += 1
        r += 1
    return False


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    # monotonic stack, push element while maintaining monotonicity,
    # pop elements that voilate monotonocity
    stack = []
    for ind, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            idx = stack.pop()
            temperatures[idx] = ind - idx
        stack.append(ind)
    return temperatures
