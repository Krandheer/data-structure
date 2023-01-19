"""
recursion solution to find the way to get the to the particular number on dice
"""


def dice(pat, target):
    if target == 0:
        print(pat)
    for i in range(1, target + 1):
        dice(pat + str(i), target - i)


def dice2(pat, target, result):
    if target == 0:
        result.append(pat)
    for i in range(1, target + 1):
        dice2(pat + str(i), target - i, result)
    return result


def dice3(pat, target, result):
    if target == 0:
        result.append(pat)
    for i in range(1, target + 1):
        dice3(pat + str(i), target - i, result)
    return len(result)


# dice("", 4)
print(dice2("", 4, []))
# print(dice3("", 4, []))
