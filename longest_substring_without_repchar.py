def longest_substring_without_repeating_char(s: str) -> int:
    """
    striver sheet 24th problem
    """
    check = {}
    l, r = 0, 0
    max_len = r - l + 1
    while l <= r <= len(s) - 1:
        if s[r] not in check:
            check[s[r]] = r
            max_len = max(max_len, r - l + 1)
            r += 1
        else:
            p = check[s[r]]
            if l <= p:
                l = p + 1
            check.pop(s[r])
    return max_len


sr = ["au", "abcabcbb", "tmmzux"]
for st in sr:
    print(longest_substring_without_repeating_char(st))
# st = "tmmzuxt"
# print(longest_substring_without_repeating_char(st))
