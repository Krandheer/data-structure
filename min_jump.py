def jump(nums):
    """
    trying to find the farthest distance from a range of indices, where r is the highest end of range
    and l is the lowest end of range, and number of jump to reach a range is one as we will consider on
    index out of those range in final path.
    """

    res = 0
    l, r = 0, 0

    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])

        l = r + 1
        r = farthest
        res += 1
    return res
