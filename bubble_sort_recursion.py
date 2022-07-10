def star_pattern(arr, r, c):
    if r == 0:
        return
    if c < r:
        if arr[c] > arr[c + 1]:
            arr[c], arr[c + 1] = arr[c + 1], arr[c]
        star_pattern(arr, r, c + 1)
    else:
        star_pattern(arr, r - 1, 0)


l = [4, 2, 3, 5, 1]

star_pattern(l, len(l) - 1, 0)
print(l)
