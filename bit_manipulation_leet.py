def minimizeXor(num1: int, num2: int) -> int:
    set_bits = 0
    while num2:
        num2 = num2 & (num2 - 1)
        set_bits += 1

    x = 0
    for i in reversed(range(32)):
        if num1 & (1 << i):
            x += 1 << i
            set_bits -= 1
            if set_bits == 0:
                return x

    for i in range(32):
        if (num1 & (1 << i)) == 0:
            set_bits -= 1
            x += 1 << i
            if set_bits == 0:
                return x

    return x
