def lis_recursion(index, prev_index, arr):
    if index == len(arr):
        return 0
    max_length = 0 + lis(index + 1, prev_index, arr)
    if prev_index == -1 or arr[prev_index] < arr[index]:
        max_length = max(max_length, 1 + lis(index + 1, index, arr))
    return max_length


def lis(index, prev_index, arr, dp):
    if index == len(arr):
        return 0
    if dp[index][prev_index + 1] != -1:
        return dp[index][prev_index]
    max_length = 0 + lis(index + 1, prev_index, arr, dp)
    if prev_index == -1 or arr[prev_index] < arr[index]:
        max_length = max(max_length, 1 + lis(index + 1, index, arr, dp))

    dp[index][prev_index + 1] = max_length
    return dp[index][prev_index + 1]


arr = [30, 40, 2, 5, 1, 7, 45, 50, 8]
dp = [[-1] * len(arr) for i in range(len(arr) + 1)]
print(lis(0, -1, arr, dp))
