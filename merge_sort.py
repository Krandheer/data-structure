def merge_sort(unsorted_list):
    """
    sort the given list in ascending order and return the new sorted list
    divide and conquer type algo
    1. first divide the list from mid
    2. conquer the divided list, means sort them
    3. merge the sorted list
    O(nk log n) times
    """
    if len(unsorted_list) <= 1:
        return unsorted_list
    left_half, right_half = split(unsorted_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(a_list):
    """
    divide the list in two halves from midpoint and return both halves
    slicing operation of python takes O(k) times, where k is size of slice
    O(k log n) times
    """
    mid = len(a_list) // 2
    return a_list[:mid], a_list[mid:]


def merge(left, right):
    """merge two sorted list in one sorted list and return the sorted combined list"""
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i = i + 1
        else:
            l.append(right[j])
            j = j + 1

    while i < len(left):
        l.append(left[i])
        i = i+1

    while j < len(right):
        l.append(right[j])
        j = j+1
    return l


b_list = [54, 62, 93, 17, 77, 31, 44, 55, 20]

print(merge_sort(b_list))
