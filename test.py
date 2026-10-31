from collections import Counter


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atmost(k):
            freq = Counter()
            l = r = ans = 0
            while r < len(nums):
                freq[nums[r]] += 1

                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1

                ans += r - l + 1
                r += 1
            return ans

        return atmost(k) - atmost(k - 1)
