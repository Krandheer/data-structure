def bubble_sort(my_list):
    for i in range(len(my_list) - 1):
        swap = False
        for j in range(1, len(my_list)-i):
            if my_list[j] < my_list[j - 1]:
                my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
                swap = True
        if not swap:
            break
    return my_list


print(bubble_sort([4, 2, 3, 5, 1]))
