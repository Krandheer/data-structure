# Given an array of size N-1 such that it only contains distinct
# integers in the range of 1 to N. Find the missing element.
# N = 5
# A[] = {1,2,3,5}
# Output: 4

from collections import Counter


def get_missing(N, arr):
    for i in range(1, N + 1):
        if i in arr:
            continue
        else:
            return i
    return -1


def get_missing2(N, arr):
    total_sum = (N * (N + 1)) / 2
    arr_sum = sum(arr)
    return int(total_sum - arr_sum)


def get_missing3(N, arr):
    d = Counter(arr)
    for i in range(1, N + 1):
        if i not in d.keys():
            return i


A = [1, 2, 3, 5]
N = 5

# print(get_missing2(N, A))
print(get_missing3(N, A))
print(get_missing(N, A))
