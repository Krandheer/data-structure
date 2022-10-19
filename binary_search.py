"""
using python bisect library to implement binary search on sorted list
"""
import bisect


def binary_search(sorted_list, x):
    i = bisect.bisect_left(sorted_list, x)
    if i != len(sorted_list) and sorted_list[i] == x:
        return i


a = [1, 2, 4, 6, 7, 12, 34, 39, 54]

print(binary_search(a, 54))
