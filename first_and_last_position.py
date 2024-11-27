from typing import List

ans = []
def binary_search(nums, target, start, end, search_direction_right):
    while start <= end:
        mid = end-(end-start)//2
        if nums[mid]==target:
            idx = mid
            ans.append(idx)
            if search_direction_right:
                start = mid+1
            else:
                end = mid-1

        elif nums[mid]>target:
            end = mid-1
        else:
            start = mid+1
def search_range(nums: List[int], target: int) -> List[int]:
    start = 0
    end = len(nums)-1
    binary_search(nums, target, start, end, True)
    binary_search(nums, target, start, end, False)
    return [-1,-1] if len(ans)==0 else [min(ans), max(ans)]

print(search_range([2,2], 2))
