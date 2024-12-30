dp = {}


def helper(limit, num_zero, num_one, ans):
    state = (limit, ans)
    if state in dp:
        return dp[state]
    if ans == limit:
        return 1
    if ans > limit:
        return 0

    take_zero = helper(limit, num_zero, num_one, ans + num_zero)
    take_one = helper(limit, num_zero, num_one, ans + num_one)
    dp[state] = (take_zero + take_one) % (10**9 + 7)
    return dp[state]


ans = 0
low = 2
high = 3
zero = 1
one = 2
for i in range(low, high + 1):
    ans += helper(i, zero, one, "")
print(ans)
