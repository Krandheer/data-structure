class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2 = 0
        p3 = 0
        p5 = 0
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[p5]*5 == dp[i]:
                p5 += 1
        return dp[-1]

    #     naug = []
    #     k = 1
    #     while len(naug) < n:
    #         if self.is_prime(k):
    #             naug.append(k)
    #         k = k + 1
    #     return naug[-1]
    #
    # @staticmethod
    # def is_prime(n):
    #     c = 2
    #     factors = []
    #     while n > 1:
    #         if n % c == 0:
    #             factors.append(c)
    #             n = n // c
    #         else:
    #             c = c + 1
    #
    #     for num in factors:
    #         if num not in [2, 3, 5]:
    #             return False
    #     else:
    #         return True


obj = Solution()
print(obj.nthUglyNumber(11))
