ipt = [[1, 1, 0], [1, 1, 1], [1, 1, 0]]


def count_squares(ipt, dp):
    for row in range(len(dp)):
        dp[row][0] = ipt[row][0]
    for col in range(len(dp[0])):
        dp[0][col] = ipt[0][col]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if ipt[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    print(dp)
    dp_sum = 0
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j] != -1:
                dp_sum = dp_sum + dp[i][j]
    return dp_sum


dp = []
for i in range(len(ipt)):
    temp = []
    for j in range(len(ipt[0])):
        temp.append(-1)
    dp.append(temp)
print(count_squares(ipt, dp))
