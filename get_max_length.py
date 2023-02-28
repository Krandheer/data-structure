def getMaxLen(nums) -> int:
    n = len(nums)
    pos = [0] * n  # (1)
    neg = [0] * n  # (2)

    if nums[0] > 0:
        pos[0] = 1
    else:
        pos[0] = 0
    if nums[0] < 0:
        neg[0] = 1
    else:
        neg[0] = 0

    for i in range(1, n):
        if nums[i] < 0:
            if neg[i - 1]:
                pos[i] = 1 + neg[i - 1]
            else:
                pos[i] = 0

            if pos[i - 1]:
                neg[i] = 1 + pos[i - 1]
            else:
                neg[i] = 1

        elif nums[i] > 0:
            if pos[i - 1]:
                pos[i] = 1 + pos[i - 1]
            else:
                pos[i] = 1
            if neg[i - 1]:
                neg[i] = 1 + neg[i - 1]
            else:
                neg[i] = 0

    return max(pos)


print(getMaxLen([-10000, -200000,]))
