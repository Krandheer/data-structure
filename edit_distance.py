import math


def compare_string(index1, index2, word1, word2, mini):
    if index1 <= 0:
        return index2 + 1
    if index2 <= 0:
        return index1 + 1
    if word1[index1] == word2[index2]:
        return min(mini, compare_string(index1 - 1, index2 - 1, word1, word2, mini))
    else:
        return 1 + min(
            mini,
            compare_string(index1 - 1, index2 - 1, word1, word2, mini),
            compare_string(index1 - 1, index2, word1, word2, mini),
            compare_string(index1, index2 - 1, word1, word2, mini),
        )


def recur(word1, word2, i, j, dp, mini):
    if i < 0:
        return j + 1
    if j < 0:
        return i + 1
    if dp[i][j] != -1:
        return dp[i][j]

    # not take case
    if word1[i] == word2[j]:
        mini = min(mini, recur(word1, word2, i - 1, j - 1, dp, mini))
    else:
        mini = 1 + min(
            mini,
            recur(word1, word2, i - 1, j, dp, mini),
            recur(word1, word2, i, j - 1, dp, mini),
            recur(word1, word2, i - 1, j - 1, dp, mini),
        )
    dp[i][j] = mini
    return dp[i][j]


word1 = "intention"
word2 = "execution"
dp = [[-1] * len(word2) for _ in range(len(word1))]
res = recur(word1, word2, len(word1) - 1, len(word2) - 1, dp, math.inf)
print(res)
print(compare_string(len(word1) - 1, len(word2) - 1, word1, word2, math.inf))
