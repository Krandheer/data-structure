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


# print(delete_data2("baccad", "a"))


def subset(p, up, answer):
    if len(up) == 0:
        answer.append(p)
        return answer
    take = up[0]
    subset(p + take, up[1:], answer)
    subset(p, up[1:], answer)
    return answer


def subset2(p, up):
    if len(up) == 0:
        answer = []
        answer.append(p)
        return answer
    ch = up[0]
    take = subset2(p + ch, up[1:])
    not_take = subset2(p, up[1:])
    if take:
        take.extend(not_take)
    return take


# print(subset2("", "abc"))


# matrix: no. of ways to reach the bottom right corner
def ways(i, j):
    if i == 0 and j == 0:
        return 1
    if i < 0 or j < 0:
        return 0
    return ways(i - 1, j) + ways(i, j - 1)


# 3 X 3 matrix
print(ways(2, 2))
