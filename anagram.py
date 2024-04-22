from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_dict = Counter(s)
    t_dict = Counter(t)
    for key, val in s_dict.items():
        if key not in t_dict or t_dict[key] != val:
            return False
    return True


s1 = "a"
t1 = "ab"
print(isAnagram(s1, t1))
