def increasing_triplet(nums):
    first = second = float("inf")
    for num in nums:
        if num < first:
            first = num

        if first < num < second:
            second = num

        if num > second:
            return True

    return False


print(increasing_triplet([2, 1, 5, 0, 4, 6]))
