def compress(chars):
    i, j = 0, 0
    while i <= j < len(chars) - 1:
        if chars[i] == chars[j + 1]:
            j += 1
        else:
            if j - i + 1 > 1 and j - i + 1 < 10:
                chars[i : j + 1] = [chars[i], str(j - i + 1)]
                i = i + 2
                j = i
            elif j - i + 1 >= 10:
                temp = []
                temp.append(chars[i])
                temp_str = str(j - i + 1)
                for d in temp_str:
                    temp.append(d)
                chars[i : j + 1] = temp
                i = i + len(temp_str) + 1
                j = i
            elif j - i + 1 == 1:
                chars[i : j + 1] = chars[i]
                i = i + 1
                j = i
    if i <= j:
        if j - i + 1 > 1 and j - i + 1 < 10:
            chars[i : j + 1] = [chars[i], str(j - i + 1)]
            i = i + 2
            j = i + 1
        elif j - i + 1 >= 10:
            temp = []
            temp.append(chars[i])
            temp_str = str(j - i + 1)
            for d in temp_str:
                temp.append(d)
            chars[i : j + 1] = temp
            i = i + len(temp_str) + 1
            j = i
        elif j - i + 1 == 1:
            chars[i : j + 1] = chars[i]
            i = i + 2
            j = i + 1
    print(chars)
    return len("".join(chars))


chars = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]
ans = compress(chars)
print(ans)
