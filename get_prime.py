import math


# get all primes less than n
# time complexity n*sqrt(n)
def get_prime(n):
    primes = []
    for i in range(n):
        if is_prime(i):
            primes.append(i)
    return primes


# check if number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print(get_prime(40))
