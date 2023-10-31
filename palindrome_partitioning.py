"""
given a string find the minimum number of partitions so that all partitions are palindrome.
solve using the concept of fron partitioning.
"""
import math

# ipt = "bababcbadcede"
ipt = "ABC"


def is_palindrome(i, j, str):
    while i <= j:
        if str[i] != str[j]:
            return False
        i = i + 1
        j = j - 1
    return True


def palindrome_partition(i, str):
    if i >= len(str):
        return 0
    min_cost = math.inf
    for j in range(i, len(str)):
        if is_palindrome(i, j, str):
            cost = 1 + palindrome_partition(j + 1, str)
            total_cost = min(min_cost, cost)
    return total_cost


print(palindrome_partition(0, ipt) - 1)
