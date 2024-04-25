def long_inc_subarr(arr):
    """finding the longest incrasing subarray in given array"""
    i, j = 0, 1
    maxi = 0
    prev_max = 0
    j_till = 0
    while i <= j and j < len(arr):
        if arr[j] >= arr[j - 1]:
            prev_max = max
            maxi = max(maxi, j - i + 1)
            j += 1
            if prev_max != maxi:
                j_till = j
        else:
            i = j
            j += 1
    return arr[j_till - maxi : j_till], maxi


arr = [1, 3, 5, 2, 9, 3, 11, 13]

ans = long_inc_subarr(arr)
print(ans)
