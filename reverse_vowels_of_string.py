def reverseVowels(s):
    vow = ""
    for i in range(len(s)):
        if s[i] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            vow += s[i]
    vow = vow[::-1]
    j = 0
    temp = ""
    for i in range(len(s)):
        if s[i] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            temp += vow[j]
            j += 1
        else:
            temp += s[i]

    return temp


s = "aA"
ans = reverseVowels(s)
print(ans)
