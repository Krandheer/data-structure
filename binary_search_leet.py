def search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = end - (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
    return -1


# print(search([-1, 0, 3, 5, 9, 12], 9))


def searchInsert(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if mid and nums[mid] == target:
            return mid
        elif mid and nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if mide and nums[mid] > target:
        return mid
    else:
        return mid + 1


print(searchInsert([1, 3, 5, 6], 7))
