s1 = 'horse'
s2 = 'ros'
"""
you can perform insert, delete, replace operation, find minimum number of operation needed to convert 1 to 2.
"""


def minimum_op(index1, index2, s1, s2):
    if index1 < 0 and index2 < 0:
        return 0
    elif index1 < 0:
        return index2 + 1
    elif index2 < 0:
        return index1 + 1

    if s1[index1] == s2[index2]:
        return minimum_op(index1 - 1, index2 - 1, s1, s2)
    else:
        return 1 + min(minimum_op(index1 - 1, index2, s1, s2), minimum_op(index1, index2 - 1, s1, s2),
                       minimum_op(index1 - 1, index2 - 1, s1, s2))


print(minimum_op(len(s1) - 1, len(s2) - 1, s1, s2))


def minimum_op_dp(index1, index2, s1, s2, dp):
    if index1 < 0:
        return index2 + 1
    elif index2 < 0:
        return index1 + 1
    if dp[index1][index2] != -1:
        return dp[index1][index2]
    if s1[index1] == s2[index2]:
        dp[index1][index2] = minimum_op_dp(index1 - 1, index2 - 1, s1, s2, dp)
        return dp[index1][index2]
    else:
        dp[index1][index2] = 1 + min(minimum_op_dp(index1 - 1, index2, s1, s2, dp),
                                     minimum_op_dp(index1, index2 - 1, s1, s2, dp),
                                     minimum_op_dp(index1 - 1, index2 - 1, s1, s2, dp))
        return dp[index1][index2]


dp_1 = [[-1 for j in range(len(s2))] for i in range(len(s1))]
print(minimum_op_dp(len(s1) - 1, len(s2) - 1, s1, s2, dp_1))
