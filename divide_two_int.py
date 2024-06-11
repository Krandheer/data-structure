def divide(dividend, divisor):
    q = 0
    temp1 = abs(dividend)
    temp2 = abs(divisor)
    while temp1 < temp2:
        temp1 -= temp2
        q += 1

    if dividend < 0 or divisor < 0:
        return -q
    return q


dividend = 10
divisor = 3
ans = divide(dividend, divisor)
print(ans)
