def quicksort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    left_of_pivot = []
    right_of_pivot = []
    pivot = unsorted_list[0]
    for value in unsorted_list[1:]:
        if value < pivot:
            left_of_pivot.append(value)
        else:
            right_of_pivot.append(value)

    return quicksort(left_of_pivot) + [pivot] + quicksort(right_of_pivot)


b_list = [54, 62, 93, 17, 77, 31, 44, 55, 20]

print(quicksort(b_list))
