# count = 0
#
#
# def get_zeros(n):
#     global count
#     if n == 0:
#         return 1
#     if n % 10 == 0:
#         count = count + 1
#         get_zeros(n // 10)
#     else:
#         get_zeros(n // 10)
#
#
# get_zeros(40304)
# print(count)

def get_zeros(n, count):
    if n == 0:
        return count
    if n % 10 == 0:
        return get_zeros(n // 10, count + 1)
    else:
        return get_zeros(n // 10, count)


print(get_zeros(40304040, 0))