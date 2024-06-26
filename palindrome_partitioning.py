import math


def is_palindrome(i, j, str1):
    while i <= j:
        if str1[i] != str1[j]:
            return False
        i = i + 1
        j = j - 1
    return True


def palindrome_partition(i, str1):
    if i >= len(str1):
        return 0
    min_cost = math.inf
    for j in range(i, len(str1)):
        if is_palindrome(i, j, str1):
            cost = 1 + palindrome_partition(j + 1, str1)
            min_cost = min(min_cost, cost)
    return min_cost


def palindrome_partition_dp(i, str1, dp):
    if i >= len(str1):
        return 0
    min_cost = math.inf
    if dp[i] != -1:
        return dp[i]
    for j in range(i, len(str1)):
        if is_palindrome(i, j, str1):
            cost = 1 + palindrome_partition(j + 1, str1)
            min_cost = min(min_cost, cost)
            dp[i] = min_cost
    return dp[i]


def palidrome_partition2(index, s, ans, path):
    if index >= len(s):
        ans.append(path[:])
        return ans

    for j in range(index, len(s)):
        if is_palindrome(index, j, s):
            path.append(s[index : j + 1])
            palidrome_partition2(j + 1, s, ans, path)
            path.pop()
    return ans


# ipt = "aabb"
ipt = "bababcbadcede"
dp = [-1 for i in range(len(ipt))]
print(palindrome_partition_dp(0, ipt, dp))
print(palindrome_partition(0, ipt))
# print(palidrome_partition2(0, ipt, [], []))
