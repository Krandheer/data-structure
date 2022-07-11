# selection sort using the print star logic
def selection_sort(arr, r, c, max_index):
    if r == 0:
        return
    if c < r:
        if arr[c] > arr[max_index]:
            selection_sort(arr, r, c + 1, c)
        else:
            selection_sort(arr, r, c + 1, max_index)
    else:
        arr[max_index], arr[r - 1] = arr[r - 1], arr[max_index]
        selection_sort(arr, r - 1, 0, 0)


l = [5, 2, 7, 8, 1, 6]

selection_sort(l, len(l), 0, 0)
print(l)
