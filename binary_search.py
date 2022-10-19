"""
using python bisect library to implement binary search on sorted list
"""
import bisect


def binary_search(sorted_list, x):
    i = bisect.bisect_left(sorted_list, x)
    if i != len(sorted_list) and sorted_list[i] == x:
        return i


"""
recursive binary search
"""


def recursive_binary_search(sorted_list, x):
    if len(sorted_list) == 0:
        return False

    else:
        midpoint = len(sorted_list) // 2
        if sorted_list[midpoint] == x:
            return True
        else:
            if sorted_list[midpoint] < x:
                return recursive_binary_search(sorted_list[midpoint + 1:], x)

            else:
                return recursive_binary_search(sorted_list[:midpoint], x)


a = [1, 2, 4, 6, 7, 12, 34, 39, 54]

print(binary_search(a, 54))
print(recursive_binary_search(a, 54))
