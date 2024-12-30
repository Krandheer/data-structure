def helper(low, high, num_zero, num_one, ans):
    if low <= len(ans) <= high:
        return 1
    if len(ans) > high:
        return 0

    take_zero = helper(low, high, num_zero, num_one, ans + "0" * num_zero)
    take_one = helper(low, high, num_zero, num_one, ans + "1" * num_one)
    return take_zero + take_one


print(helper(2, 3, 1, 2, ""))
