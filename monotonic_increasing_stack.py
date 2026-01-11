def monotonic_increasing(arr):
    stack = []  # will store indices
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        stack.append(i)
    return stack


# for next/prev smaller element maintain monotonic increasing stack
# for next/prev greater element maintain monotonic decreasing stack
def next_greater(nums):
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)

    return res


arr = [5, 2, 4, 1, 3]
print(next_greater(arr))
