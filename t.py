def check_sorted(arr, i):
    if i == len(arr):
        return True
    if arr[i] <= arr[i - 1]:
        return False
    return check_sorted(arr, i + 1)


arr = [1, 2, 4, 10, 9, 12]
ans = check_sorted(arr, 1)
print(ans)
