def longest_substring_without_repeating_char(s: str) -> int:
    """
    striver sheet 24th problem
    """
    check = set()
    l, r = 0, 0
    max_len = r - l + 1
    while l <= r <= len(s) - 1:
        if s[r] not in check:
            check.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1
        else:
            check.remove(s[r])
            l += 1
    return max_len


sr = ["au", "abcabcbb", "tmmzuxt"]
for st in sr:
    print(longest_substring_without_repeating_char(st))
