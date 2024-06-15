from collections import Counter


def sort012(arr):
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


# arr = [0, 2, 1, 2, 0]
# ans = sort012(arr)
# print(ans)
