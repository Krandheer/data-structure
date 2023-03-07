class Solution:
    def nthUglyNumber(self, n: int) -> int:
        naug = []
        k = 1
        while len(naug) < n:
            if self.is_prime(k):
                naug.append(k)
            k = k + 1
        return naug[-1]

    @staticmethod
    def is_prime(n):
        c = 2
        factors = []
        while n > 1:
            if n % c == 0:
                factors.append(c)
                n = n // c
            else:
                c = c + 1

        for num in factors:
            if num not in [2, 3, 5]:
                return False
        else:
            return True


obj = Solution()
print(obj.nthUglyNumber(10))
