import copy


def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    deep_copy = copy.deepcopy(nums)
    for idx in range(len(nums)):
        if idx + k < len(nums):
            nums[idx + k] = deep_copy[idx]
        else:
            temp = (idx + k) % len(nums)
            nums[temp] = deep_copy[idx]


a = [1, 2, 3, 4, 5, 6, 7]
rotate(a, 3)
print(a)
