def check_sorted(arr, i):
    if i == len(arr):
        return True
    return arr[i] >= arr[i - 1] and check_sorted(arr, i + 1)


arr = [1, 2, 4, 11, 9, 12]
ans = check_sorted(arr, 1)
print(ans)
