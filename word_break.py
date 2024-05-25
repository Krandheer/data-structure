"""
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


def wordBreak(s: str, wordDict) -> bool:
    dp = [False for i in range(len(s) + 1)]
    dp[0] = True

    for i in range(len(s)):
        # start from string and then from that index check for words and if words found then last index of that word
        # becomes starting for next inner loop
        for j in range(i, len(s)):
            if not dp[i]:
                break
            if dp[i] and s[i : j + 1] in wordDict:
                dp[j + 1] = True

    return dp[-1]
