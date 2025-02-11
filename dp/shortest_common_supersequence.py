# return the shortest common supersequence containing both sequences
def shortest_common_supersequence(s1, s2):
    def lcs(index1, index2, s1, s2, dp):
        if index1 < 0 or index2 < 0:
            return 0

        if dp[index1][index2] != -1:
            return dp[index1][index2]
        if s1[index1] == s2[index2]:
            return 1 + lcs(index1 - 1, index2 - 1, s1, s2, dp)
        else:
            dp[index1][index2] = max(
                lcs(index1 - 1, index2, s1, s2, dp),
                lcs(index1, index2 - 1, s1, s2, dp),
            )
            return dp[index1][index2]

    index1 = len(s1) - 1
    index2 = len(s2) - 1
    dp = [[-1] * len(s2) for _ in range(len(s1))]
    temp = lcs(index1, index2, s1, s2, dp)
    return len(s1) + len(s2) - temp


s1 = "bleed"
s2 = "blue"
print(shortest_common_supersequence(s1, s2))
