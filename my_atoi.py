def myAtoi(s) -> int:
    """leetcode problem 8"""

    def get_digit(s):
        temp = ""
        for ch in s:
            if ch.isnumeric():
                temp += ch
            else:
                break
        return temp

    s = s.strip()
    if s == "":
        return 0
    sign = ""
    if s[0] == "-" or s[0] == "+":
        sign = s[0]
        s = get_digit(s[1:])
    else:
        s = get_digit(s)
    if s == "":
        return 0
    n = int(s)
    if sign == "-":
        n = -n
    if n < (-(2**31)):
        n = -(2**31)
    if n > (2**31 - 1):
        n = 2**31 - 1
    return n


s = "+1"
print(myAtoi(s))
