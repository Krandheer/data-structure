class Solution:
    def numTrees(self, n: int) -> int:
        return self.fact(2 * n) // self.fact(n) // self.fact(n) // (n + 1)

    def fact(self, n):
        if n <= 1:
            return 1
        temp = 1
        for i in range(1, n + 1):
            temp = temp * i
        return temp


sol = Solution()
print(sol.fact(3))
