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


print(lengthOfLongestSubstring("abcabcbb"))
