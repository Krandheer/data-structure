import math


def is_palindrome(i, j, str1):
    while i <= j:
        if str1[i] != str1[j]:
            return False
        i = i + 1
        j = j - 1
    return True


def palindrome_partition(i, str1):
    if i >= len(str1):
        return 0
    min_cost = math.inf
    for j in range(i, len(str1)):
        if is_palindrome(i, j, str1):
            cost = 1 + palindrome_partition(j + 1, str1)
            min_cost = min(min_cost, cost)
    return min_cost


ipt = "bababcbadcede"
# ipt = "aabb"
print(palindrome_partition(0, ipt) - 1)
