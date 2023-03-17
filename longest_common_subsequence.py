s1 = 'adcbc'
s2 = 'dcadb'

"""
to get the longest common string convert the solution to bottom up, and start tracking from right bottom in table
as that is where you get the solution and then move back to left up and find if match then take otherwise move to
left or up whichever is highest as that is from where the current value must have come, and if match move diagonal
up.
for longest common substring start with n+1, m+1 table and fill if match with diagonal+1  or 0 and return max_val for table
"""


def lcs(index1, index2, string1, string2):
    if index1 < 0 or index2 < 0:
        return 0

    if string1[index1] == string2[index2]:
        return 1 + lcs(index1 - 1, index2 - 1, string1, string2)
    else:
        return max(lcs(index1 - 1, index2, string1, string2), lcs(index1, index2 - 1, string1, string2))


print(lcs(4, 4, s1, s2))


def lcs_dp(index1, index2, string1, string2, dp):
    if index1 < 0 or index2 < 0:
        return 0

    if dp[index1][index2] != -1:
        return dp[index1][index2]
    if string1[index1] == string2[index2]:
        dp[index1][index2] = 1 + lcs_dp(index1 - 1, index2 - 1, string1, string2, dp)
        return dp[index1][index2]
    else:
        dp[index1][index2] = max(lcs_dp(index1 - 1, index2, string1, string2, dp),
                                 lcs_dp(index1, index2 - 1, string1, string2, dp))
        return dp[index1][index2]


dp = [[-1 for j in range(len(s2))] for i in range(len(s1))]
print(lcs_dp(len(s1) - 1, len(s2) - 1, s1, s2, dp))
for i in dp:
    print(i)

