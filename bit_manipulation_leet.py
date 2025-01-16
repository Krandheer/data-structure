from collections import defaultdict
from typing import List


def minimizeXor(num1: int, num2: int) -> int:
    set_bits = 0
    while num2:
        num2 = num2 & (num2 - 1)
        set_bits += 1

    x = 0
    for i in reversed(range(32)):
        if num1 & (1 << i):
            x += 1 << i
            set_bits -= 1
            if set_bits == 0:
                return x

    for i in range(32):
        if (num1 & (1 << i)) == 0:
            set_bits -= 1
            x += 1 << i
            if set_bits == 0:
                return x

    return x


def xorAllNums(nums1: List[int], nums2: List[int]) -> int:
    ans = 0
    freq = defaultdict(int)
    len1, len2 = len(nums1), len(nums2)
    for num in nums1:
        freq[num] = freq.get(num, 0) + len2

    for num in nums2:
        freq[num] = freq.get(num, 0) + len1

    for k, v in freq.items():
        if v & 1:
            ans ^= k

    return ans
