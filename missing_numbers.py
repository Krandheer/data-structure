"""
Leetcode:
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

python len() function takes O(1) time
"""


def missing_number(nums):
    """find the missing number in given list"""
    # for i in range(len(nums) + 1):
    #     if i not in nums:
    #         return i

    # return (set(range(len(nums)+1)) - set(nums)).pop()

    n = len(nums)
    return (n * (n + 1)) // 2 - sum(nums)


a = [1, 2, 3, [3, 5, 6], 9]
for i in a:
    # if type(i)==int:
    #     print(i)
    if isinstance(i, int):
        print(i)
    else:
        for j in i:
            print(j)

        d = {}
        for ind, num in enumerate(nums):
            d[(num, ind)] = num

        d = sorted(d, key=lambda x: x[1])

        nums = [1, 3, 2, 3, 1]
