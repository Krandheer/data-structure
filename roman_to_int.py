class Solution:
    def romanToInt(self, s: str) -> int:
        d_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1:
                if d_map[s[i]] < d_map[s[i + 1]]:
                    ans -= d_map[s[i]]
                else:
                    ans += d_map[s[i]]
            else:
                ans += d_map[s[i]]
        return ans

    def intToRoman(self, num: int) -> str:
        map_d = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
        }
        ans = ""
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while n <= num:
                ans += map_d[n]
                num -= n
        return ans


sol = Solution()
ans = sol.intToRoman(58)
print(ans)
