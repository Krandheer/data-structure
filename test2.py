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
# print(target_num(nums, 4, 0, []))


## very important concept returning list using declation in body
def target_num2(arr: List[int], target: int, index: int) -> List[int]:
    lis = []
    if index == len(arr):
        return lis

    # this will contain the answer for it's function call only
    if arr[index] == target:
        lis.append(index)

    ans_from_other_call = target_num2(arr, target, index + 1)
    lis.extend(ans_from_other_call)
    return lis


# print(target_num2(nums, 4, 0))


def delete_data(p, up, data):
    if len(up) == 0:
        return p
    if up[0] == data:
        return delete_data(p, up[1:], data)
    else:
        return delete_data(p + up[0], up[1:], data)


def delete_data2(up, data):
    p = ""
    if len(up) == 0:
        return p
    if up[0] == data:
        note_take = delete_data(p, up[1:], data)
        return note_take
    else:
        take = delete_data(p + up[0], up[1:], data)
        p = p + take
        return p


print(delete_data2("baccad", "a"))
