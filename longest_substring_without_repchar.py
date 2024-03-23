def longest_substring_without_repeating_char(s: str) -> int:
    check = set()
    l, r = 0, 0
    total = 0
    while l <= r and r <= len(s) - 1:
        if s[r] not in check:
            total = max(total, r - l + 1)
            check.add(s[r])
            r += 1
        else:
            check.remove(s[l])
            l += 1
            total = max(total, r - l)
    if r == len(s):
        total = max(total, r - l)
    return total


# s = "au"
# s = "abcabcbb"
s = "tmmzuxt"
print(longest_substring_without_repeating_char(s))
