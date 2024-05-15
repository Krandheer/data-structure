def reverseWords(s):
    """reverse word in a string"""
    s = s.strip()
    temp_s = s.split(" ")
    s = []
    temp = []
    for i in temp_s:
        if i:
            s.append(i)

    for i in range(len(s) - 1, -1, -1):
        temp.append(s[i])

    result = " ".join(temp)
    return result


ans = reverseWords("a good   example")
print(ans)
