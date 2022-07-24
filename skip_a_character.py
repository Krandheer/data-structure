"""
recursive function that skips a given character,
here that character is a,
"""


def skip(temp_up, temp_p):
    if len(temp_p) == 0:
        print(temp_up)
        return

    ch = temp_p[0]
    if ch == "a":
        skip(temp_up, temp_p[1:])
    else:
        skip(temp_up + ch, temp_p[1:])


# skip("", 'baccdab')

def skip2(temp_p):
    if len(temp_p) == 0:
        return ""

    ch = temp_p[0]
    if ch == "a":
        return skip2(temp_p[1:])
    else:
        return ch + skip2(temp_p[1:])


print(skip2('baccdab'))
