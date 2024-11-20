def take_characters(s: str, k: int) -> int:
    total = {'a': 0, 'b':0, 'c':0}
    for ch in s:
        total[ch]+=1

    if min(total.values())<k: return -1

    window = {'a':0, 'b':0, 'c':0}

    i, j = 0, 0
    res = len(s)
    n = len(s)

    while j < n:
        window[s[j]]+=1
        total[s[j]]-=1
        while min(total.values())<k:
            total[s[i]]+=1
            i+=1
        res = min(res, n-(j-i+1))
        j+=1
    return res


print(take_characters("aabaaaacaabc", 2))
