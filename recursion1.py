def print_n(n):
    if n == 0:
        return
    print(n)
    print_n(n - 1)
    print(n)


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(257))
print(factorial(5))
