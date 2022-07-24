"""
recursive code to remove the duplicate letter from a given string
"""


def remove_duplicate(p, up, l):
    if len(up) == 0:
        print(p)
        return
    elem = up[0]
    if l[ord(elem) - ord('a')]:
        remove_duplicate(p, up[1:], l)
    else:
        l[ord(elem) - ord('a')] = True
        remove_duplicate(p + elem, up[1:], l)


list1 = []
for i in range(26):
    list1.append(False)
remove_duplicate("", "abbbcccdzzef", list1)
