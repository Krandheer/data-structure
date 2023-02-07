def is_power_2(n):
    if n == 0:
        print("no")
    else:
        ans = n & (n - 1)
        if ans == 0:
            print("yes")
        else:
            print('no')


is_power_2(16)
