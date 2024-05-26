def mergeAlternately(word1, word2):
    merge = ""

    i, j = 1, 0
    merge += word1[0]
    while i < len(word1) and j < len(word2):
        if j < i:
            merge += word2[j]
            j += 1
        else:
            merge += word1[i]
            i += 1

    if i < len(word1):
        merge += word1[i:]

    if j < len(word2):
        merge += word2[j:]
    return merge


ans = mergeAlternately("abc", "pqr")
print(ans)
