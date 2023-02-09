def magic_number(n):
    ans = 0
    base = 5
    while n > 0:
        last = n & 1
        ans += last * base
        n = n >> 1
        base = base*5

    return ans


print(magic_number(5))
