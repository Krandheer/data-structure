def get_xor_between_given_num(a, b):
    return get_xor(b) ^ get_xor(a - 1)


def get_xor(a):
    if a % 4 == 0:
        return a
    elif a % 4 == 1:
        return 1
    elif a % 4 == 2:
        return a + 1
    else:
        return 0


print(get_xor_between_given_num(3, 9))
