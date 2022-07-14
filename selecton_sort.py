def selection_sort(alist):
    for num_pass in range(len(alist) - 1, 0, -1):
        position_of_max = 0
        for i in range(1, num_pass + 1):
            if alist[i] > alist[position_of_max]:
                position_of_max = i

        alist[num_pass], alist[position_of_max] = alist[position_of_max], alist[num_pass]

    return alist
