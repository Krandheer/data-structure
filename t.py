def check_sorted(arr, i):
    if i == len(arr):
        return True
    return arr[i] >= arr[i - 1] and check_sorted(arr, i + 1)


def linear_search(arr, i, target):
    if i == len(arr):
        return -1
    if arr[i] == target:
        return i
    return linear_search(arr, i + 1, target)


arr = [1, 2, 4, 11, 9, 12]
# ans = check_sorted(arr, 1)
ans = linear_search(arr, 0, 11)
print(ans)
