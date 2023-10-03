def print_sum(i, sum_n):
    if i < 1:
        # print(sum_n)
        return sum_n
    sum_n = sum_n + i
    return print_sum(i - 1, sum_n)


# print(print_sum(25, 0))


def print_sum2(i):
    if i < 0:
        return 0
    return i + print_sum2(i - 1)


# print(print_sum2(6))


def reverse_array(i, arr):
    if i >= len(arr) / 2:
        return
    arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
    reverse_array(i + 1, arr)


arr = [1, 2, 4, 3, 5]
# reverse_array(0, arr)
# print(arr)


def left_rotate_1(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]

    arr[len(arr) - 1] = temp
    return arr


# arr = [1, 2, 4, 3, 5]
# print(left_rotate_1(arr))


def shift_zero_to_end(arr):
    j = -1
    # find the first zero element index
    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
            break
    if j == -1:
        return arr
    # using two pointer method iterate and swap if non zero element and move forward zero index
    for i in range(j + 1, len(arr)):
        if i > j and arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr


temp = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
# print(shift_zero_to_end(temp))

# two pointers method can be used for union and intersection of two sorted array as well.
# prefix sum, two pointer method can be used for k-sum as well.
