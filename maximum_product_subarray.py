def maxProduct(nums) -> int:
    """
    maintain curMax and curMin to handle the case in which product of -ve and -ve becomes positive.
    """
    curMax, curMin = 1, 1
    res = max(nums)

    for n in nums:
        if n == 0:
            curMax, curMin = 1, 1
        vals = (n, n * curMax, n * curMin)
        curMax, curMin = max(vals), min(vals)

        res = max(res, curMax)

    return res
