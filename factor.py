# get all number that divides n
import math


def factor(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


# time complexity is reduced by square root of n
def factor2(n):
    factors = []
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
    return sorted(factors)


print(factor2(10))
print(factor(10))
