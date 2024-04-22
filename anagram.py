from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = Counter(s)
        t_dict = Counter(t)
        for key, val in s_dict.items():
            if key not in t_dict or t_dict[key] != val:
                return False
        return True


sol = Solution()
s1 = "a"
t1 = "ab"
print(sol.isAnagram(s1, t1))
