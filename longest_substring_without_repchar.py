def longest_substring_without_repeating_char(s: str) -> int:
    check = set()
    i, j = 0, 0
    total = 0
    while i <= j and j <= len(s) - 1:
        if s[j] not in check:
            check.add(s[j])
            j += 1
        else:
            total = max(total, j - i)
            if s[i] != s[j]:
                i += 1
            else:
                j += 1
    if j == len(s):
        total = max(total, j - i)
    return total


s = "au"
s = "abcabcbb"
# s = "tmmzuxt"
print(longest_substring_without_repeating_char(s))
