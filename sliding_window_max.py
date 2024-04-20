def sliding_window_max(nums, wind):
    """this take O(n^2) time complexity, it can be further optimised to O(n) by
    using dictionary and storing highest value in one k length window with
    value same and index different or something like that"""
    i = 0
    j = wind
    ans = []
    while j < len(nums) + 1:
        temp = max(nums[i:j])
        ans.append(temp)
        i += 1
        j += 1
    return ans


arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(arr, k))
