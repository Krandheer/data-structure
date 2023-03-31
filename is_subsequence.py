class Solution_recursion:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind1 = len(s) - 1
        ind2 = len(t) - 1
        len_matched = 0
        return self.helper(ind1, ind2, s, t, len_matched)

    def helper(self, ind1, ind2, s, t, matched):
        if ind1 < 0 and matched == len(s):
            return True
        elif ind1 < 0 and matched != len(s):
            return False
        elif ind2 < 0 and matched != len(s):
            return False

        if s[ind1] == t[ind2]:
            return self.helper(ind1 - 1, ind2 - 1, s, t, matched + 1)
        else:
            left = self.helper(ind1 - 1, ind2, s, t, matched)
            right = self.helper(ind1, ind2 - 1, s, t, matched)
            return left or right


class Solution_dp:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind1 = len(s) - 1
        ind2 = len(t) - 1
        len_matched = 0
        dp = [[False] * len(t) for _ in range(len(s))]
        return self.helper(ind1, ind2, s, t, len_matched, dp)

    def helper(self, ind1, ind2, s, t, matched, dp):
        if ind1 < 0 and matched == len(s):
            return True
        elif ind1 < 0 and matched != len(s):
            return False
        elif ind2 < 0 and matched != len(s):
            return False
        if dp[ind1][ind2]:
            return True
        if s[ind1] == t[ind2]:
            dp[ind1][ind2] = self.helper(ind1 - 1, ind2 - 1, s, t, matched + 1, dp)
            return dp[ind1][ind2]
        else:
            left = self.helper(ind1 - 1, ind2, s, t, matched, dp)
            right = self.helper(ind1, ind2 - 1, s, t, matched, dp)
            if left:
                dp[ind1][ind2] = left
            else:
                dp[ind1][ind2] = right
            return dp[ind1][ind2]


def is_subsequence(s, t):
    if len(s) == 0:
        return True
    if len(s) > len(t):
        return False
    track = 0

    for i in range(len(t)):
        if track <= len(s) - 1:
            if s[track] == t[i]:
                track += 1
    return track == len(s)


t = "c"
s = "b"
sol = Solution_dp()

print(is_subsequence(s, t))
