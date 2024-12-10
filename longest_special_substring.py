from collections import defaultdict


def maximum_length(s: str) -> int:
    count = defaultdict(int)
    for start in range(len(s)):
        temp = ""
        for end in range(start, len(s)):
            if temp == "" or temp[-1] == s[end]:
                temp += s[end]
                count[temp] += 1
            else:
                break
    max_len = -1
    for k, v in count.items():
        if v >= 3:
            max_len = max(max_len, len(k))
    return max_len
