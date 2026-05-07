def monotonic_increasing(arr):
    stack = []  # will store indices
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        stack.append(i)
    return stack


# for next/prev smaller element maintain monotonic increasing stack
# for next/prev greater element maintain monotonic decreasing stack
def next_greater(arr):
    n = len(arr)
    res = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            res[stack.pop()] = arr[i]
        stack.append(i)

    return res


nums = [5, 2, 4, 1, 3]
print(next_greater(nums))
