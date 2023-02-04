def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        curr = my_list[i]
        for j in range(i, 0, -1):
            swap = False
            if curr < my_list[j - 1]:
                my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
                swap = True
            if not swap:
                break
    return my_list


b_list = [54, 62, 93, 17, 77, 31, 44, 55, 20]
print(insertion_sort(b_list))
