def binary_search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = end - (end - start) // 2
        if nums[mid] == target:
            return mid

        # check if left half is sorted
        if nums[mid] > nums[start]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1
