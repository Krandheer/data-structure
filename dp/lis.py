def lis_recursion(index, prev_index, arr):
    """
    prev index to know if previous value was taken or not, if taken then compare that with current value,
    current value should be greater than previous value. start with minus one, as initially no value will be taken.
    prev index will be updated only when another value is taken that justify the condition of increasing sequence.
    and this happens for all values, so all subsequence is considered.
    """
    if index == len(arr):
        return 0
    max_length = lis_recursion(index + 1, prev_index, arr)
    if prev_index == -1 or arr[prev_index] < arr[index]:
        max_length = max(max_length, 1 + lis_recursion(index + 1, index, arr))
    return max_length


def lis(index, prev_index, arr, dp):
    if index == len(arr):
        return 0
    if dp[index][prev_index + 1] != -1:
        return dp[index][prev_index + 1]
    max_length = lis(index + 1, prev_index, arr, dp)
    if prev_index == -1 or arr[prev_index] < arr[index]:
        max_length = max(max_length, 1 + lis(index + 1, index, arr, dp))

    dp[index][prev_index + 1] = max_length
    return dp[index][prev_index + 1]


def list_bottom_up(nums):
    n = len(nums)
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for index in range(n - 1, -1, -1):
        for prev_index in range(index - 1, -2, -1):
            max_length = 0 + dp[index + 1][prev_index + 1]
            if prev_index == -1 or nums[prev_index] < nums[index]:
                max_length = max(max_length, 1 + dp[index + 1][index + 1])

            dp[index][prev_index + 1] = max_length
    return dp[0][0]


arr = [30, 2, 5, 7, 45, 8]
print(lis_recursion(0, -1, arr))
# dp = [[-1] * len(arr) for i in range(len(arr) + 1)]
# print(lis(0, -1, arr, dp))
# print(list_bottom_up(arr))
