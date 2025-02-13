from collections import defaultdict
from typing import List

# tag: dp, leetcode_hard


def numWays(words: List[str], target: str):
    freq = {}
    n, m = len(words[0]), len(target)

    for i in range(n):
        temp = defaultdict(int)
        for word in words:
            temp[word[i]] += 1
        freq[i] = temp

    def solve(i, j, target):
        if j == m:
            return 1
        if i >= n:
            return 0
        take = 0
        not_take = 0
        if i < n and j < m and target[j] in freq[i]:
            take = freq[i][target[j]] * solve(i + 1, j + 1, target)
        if i < n and j < m:
            not_take = solve(i + 1, j, target)
        return (take + not_take) % (10**9 + 7)

    return solve(0, 0, target)


print(numWays(["acca", "bbbb", "caca"], "aba"))
