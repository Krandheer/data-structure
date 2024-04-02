# alice book problem find the page first page of a book whose digit sum of two pages is S


# def sort_num(index, nums):
#     if index == len(nums) - 1:
#         return True
#     return nums[index] < nums[index + 1] and sort_num(index + 1, nums)


# nums = [1, 2, 3, 4, 11, 6, 7, 8, 9, 10]
# print(sort_num(0, nums))


from typing import List


def target_num(arr: List[int], target: int, index: int, lis: List[int]) -> List[int]:
    if index == len(arr) - 1:
        return lis
    if arr[index] == target:
        lis.append(index)

    return target_num(arr, target, index + 1, lis)


nums = [1, 2, 3, 4, 4, 5]
print(target_num(nums, 4, 0, []))
