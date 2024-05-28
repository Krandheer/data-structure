import math


def gcdOfStlongest_str(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""

    gcd = math.gcd(len(str1), len(str2))
    return str2[:gcd]


str1 = "abcabc"
str2 = "abc"

ans = gcdOfStlongest_str(str1, str2)
print(ans)
