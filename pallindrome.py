"""
checking if pallindrome using recursion
"""


def is_pallindrome(i, str1):
    if i >= len(str1) // 2:
        return True
    if str1[i] != str1[len(str1) - i - 1]:
        return False
    else:
        return is_pallindrome(i + 1, str1)


print(is_pallindrome(0, 'madam'))
