class Solution:
    def letterCombinations(self, digits: str):
        self.map_d = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        def helper(p, up, ans):
            if not up:
                ans.append(p)
                return
            n = up[0]
            ch = self.map_d[int(n)]
            for _, ch in enumerate(ch):
                helper(p + ch, up[1:], ans)
            return ans

        return helper("", digits, [])


sol = Solution()
ans = sol.letterCombinations("234")
print(ans)
