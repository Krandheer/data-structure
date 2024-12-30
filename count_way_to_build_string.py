def helper(limit, num_zero, num_one, ans):
    if len(ans) == limit:
        return 1
    if len(ans) > limit:
        return 0

    take_zero = helper(limit, num_zero, num_one, ans + "0" * num_zero)
    take_one = helper(limit, num_zero, num_one, ans + "1" * num_one)
    return take_zero + take_one


ans = 0
low = 2
high = 3
zero = 1
one = 2
for i in range(low, high + 1):
    ans += helper(i, zero, one, "")
print(ans)
