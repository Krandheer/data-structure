from collections import Counter


def sort012(arr):
    """Given an array of size N containing only 0s, 1s, and 2s;
    sort the array in ascending order."""
    temp = Counter(arr)
    m = 0
    for _ in range(temp[0]):
        arr[m] = 0
        m += 1

    for _ in range(temp[1]):
        arr[m] = 1
        m += 1

    for _ in range(temp[2]):
        arr[m] = 2
        m += 1
    return arr


arr1 = [0, 2, 1, 2, 0]

result = sort012(arr1)
print(result)
