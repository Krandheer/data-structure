# alice book problem find the page first page of a book whose digit sum of two pages is S


def solve(S):
    if S == 1:
        return 1

    for i in range(1, S + 2):
        if i < 10 and i % 2 == 0:
            if 2 * i + 1 == S:
                return i
        if i > 10 and i % 2 == 0:
            temp = 0
            a = i
            while a > 10:
                temp = temp + a % 10
                a = a // 10
                if a < 10:
                    temp = temp + a

            if temp * 2 + 1 == S:
                return i


# print(solve(15))


def sum_natural(n, temp):
    if n == 1:
        return 1
    temp = n + sum_natural(n - 1, temp)
    return temp


print(sum_natural(5, 0))


# def getItems(entries):
#     # Write your code here
#     n = len(entries)
#     items = []
#     temp = 0
#     view = 0
#     result = []
#     index = 0
#     for i in range(n):
#         a = entries[i]
#         if a[0] == "INSERT"
#             if not items:
#                 items.append(a)
#             for j in range(len(items)):
#                 b = int(a[2])
#                 if int(items[j][2]) > b:
#                     index = j
#             items.insert(index, a)
#             temp = temp+1
#         if a[0] == "VIEW":
#             result.append(items[view])
#             view = view+1
#     for i in range(len(result)):
#         return result[i][1]
