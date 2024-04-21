class Solution:
    """leedcode 28th question, striver dsa sheet"""

    def krp(self, haystack: str, needle: str):
        needle_ord = self.get_ord(needle)
        index = -1
        if len(needle) == len(haystack):
            if needle == haystack:
                return 0
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            found = False
            curr = self.get_ord(haystack[i : i + len(needle)])
            if needle_ord == curr:
                found = True
                index = i
                temp = haystack[i : i + len(needle)]
                for i in range(len(temp)):
                    if needle[i] != temp[i]:
                        found = False
                        index = -1

            if found:
                break
        return index

    def get_ord(self, str1):
        temp = 0
        for i in str1:
            temp += ord(i)
        return temp

    def strStr(self, haystack: str, needle: str) -> int:
        return self.krp(haystack, needle)


haystack1 = "abc"
needle1 = "c"
sol = Solution()
print(sol.strStr(haystack1, needle1))
