def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    left_half, right_half = split(unsorted_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(a_list):
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
        i = i + 1

    while j < len(right):
        l.append(right[j])
        j = j + 1
    return l


b_list = [54, 62, 93, 17, 77, 31, 44, 55, 20]

print(merge_sort(b_list))
