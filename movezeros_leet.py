def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    m = 0
    for i, n in enumerate(nums):
        if n != 0:
            nums[m] = n
            m = m + 1
    for i in range(m, len(nums)):
        print(i)
        nums[i] = 0


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
