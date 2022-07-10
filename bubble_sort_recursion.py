# using the trick we learnt in printing stars
def bubble_sort(arr, r, c):
    if r == 0:
        return

    # sort the current pair
    if c < r:
        if arr[c] > arr[c + 1]:
            arr[c], arr[c + 1] = arr[c + 1], arr[c]
        bubble_sort(arr, r, c + 1)
    else:
        # next pass for next pair starts
        bubble_sort(arr, r - 1, 0)


l = [4, 2, 3, 5, 1]

bubble_sort(l, len(l) - 1, 0)
print(l)
