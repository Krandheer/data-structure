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


print(solve(15))
