import time


def fib1(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


fib1_time = time.time()
print(fib1(10))
print(f'fib1 time = {time.time() - fib1_time}')


def fib_dp(n, dp):
    if n == 0 or n == 1:
        return n
    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fib_dp(n - 1, dp) + fib_dp(n - 2, dp)
        return dp[n]


fib_dp_time = time.time()
print(fib_dp(10, [-1] * 11))
print(f"fib_dp_time = {time.time() - fib_dp_time}")
