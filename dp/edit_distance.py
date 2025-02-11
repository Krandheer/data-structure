import math


def compare_string(index1, index2, word1, word2):
    if index1 <= 0:
        return index2 + 1
    if index2 <= 0:
        return index1 + 1

    if word1[index1] == word2[index2]:
        return compare_string(index1 - 1, index2 - 1, word1, word2)
    else:
        replace = 1 + compare_string(index1 - 1, index2 - 1, word1, word2)
        delete = 1 + compare_string(index1 - 1, index2, word1, word2)
        insert = 1 + compare_string(index1, index2 - 1, word1, word2)
        return min(replace, delete, insert)


def recur(word1, word2, i, j, dp):
    if i < 0:
        return j + 1
    if j < 0:
        return i + 1
    if dp[i][j] != -1:
        return dp[i][j]

    if word1[i] == word2[j]:
        dp[i][j] = recur(word1, word2, i - 1, j - 1, dp)
        return dp[i][j]
    else:
        replace = 1 + compare_string(i - 1, j - 1, word1, word2)
        delete = 1 + compare_string(i - 1, j, word1, word2)
        insert = 1 + compare_string(i, j - 1, word1, word2)
        dp[i][j] = min(replace, delete, insert)
        return dp[i][j]


word1 = "intention"
word2 = "execution"
dp = [[-1] * len(word2) for _ in range(len(word1))]
res = recur(word1, word2, len(word1) - 1, len(word2) - 1, dp)
print(res)
print(compare_string(len(word1) - 1, len(word2) - 1, word1, word2))
