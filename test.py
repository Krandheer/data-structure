def print_sum(i, sum_n):
    if i < 1:
        # print(sum_n)
        return sum_n
    sum_n = sum_n + i
    return print_sum(i - 1, sum_n)


print(print_sum(5, 0))


def print_sum2(i):
    if i < 0:
        return 0
    return i + print_sum2(i - 1)


print(print_sum2(6))