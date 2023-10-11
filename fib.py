import time


def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


# fib1_time = time.time()
# print(fib1(40))
# print(f"fib1 time = {time.time() - fib1_time}")


def fib_dp(n, dp):
    if n <= 1:
        return n
    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fib_dp(n - 1, dp) + fib_dp(n - 2, dp)
        return dp[n]


# fib_dp_time = time.time()
# print(fib_dp(40, [-1] * 41))
# print(f"fib_dp_time = {time.time() - fib_dp_time}")


def fib_iterative(n, dp):
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


print(fib_iterative(6, [-1] * 7))


def fib_space_otpimised(n):
    prev_2nd = 0
    prev = 1
    for i in range(2, n + 1):
        ans = prev_2nd + prev
        prev_2nd = prev
        prev = ans
    return ans


print(fib_space_otpimised(6))
