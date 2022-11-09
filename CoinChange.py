"""
python program to find the minimum number of coin
need of given type of coin to find the change of
particular value of rupees.

"""

INF = 100000


def get_minimum(x, y):
    if x < y:
        return x
    else:
        return y


def min_coin_change(d, n, k):
    # d is the array of type of coin available
    # n is the rupees to be change with coins
    # k is the length of d
    m = [0] * (n + 1)  # list of length n+1

    for i in range(1, n + 1):
        minimum = INF

        for j in range(1, k):
            if i >= d[j]:
                minimum = get_minimum(minimum, 1 + m[i - d[j]])
        m[i] = minimum
    return m[n]


print(min_coin_change([1, 3, 5], 20, 3))  # to make 5. Number of denominations = 3
