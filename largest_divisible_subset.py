import math


def largest_divisible_subset(ipt, index, prev):
    if index == len(ipt):
        return 0
    take = -math.inf
    not_take = -math.inf
    if ipt[index] % ipt[prev] == 0 or prev == -1:
        take = 1 + largest_divisible_subset(ipt, index + 1, index)
    else:
        not_take = largest_divisible_subset(ipt, index + 1, prev)
    return max(take, not_take)


ipt = [1, 16, 7, 8, 4]
ipt = sorted(ipt)
print(largest_divisible_subset(ipt, 0, -1))
