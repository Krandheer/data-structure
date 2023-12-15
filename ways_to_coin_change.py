def total_num_ways(index, target, arr):
    if index == 0:
        if target % arr[index] == 0:
            return 1
        return 0

    not_take = total_num_ways(index - 1, target, arr)
    take = 0
    if arr[index] <= target:
        take = total_num_ways(index, target - arr[index], arr)

    return take + not_take


denom = [1, 2, 3]
target = 4

print(total_num_ways(2, target, denom))


def total_num_ways_dp(index, target, arr, dp):
    if index == 0:
        if target % arr[index] == 0:
            return 1
        return 0
    if dp[index][target] != -1:
        return dp[index][target]
    not_take = total_num_ways_dp(index - 1, target, arr, dp)
    take = 0
    if arr[index] <= target:
        take = total_num_ways_dp(index, target - arr[index], arr, dp)

    dp[index][target] = take + not_take
    return dp[index][target]


dp = [[-1 for _ in range(target + 1)] for _ in range(len(denom))]
print(total_num_ways_dp(2, target, denom, dp))
