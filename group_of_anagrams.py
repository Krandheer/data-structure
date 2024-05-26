from collections import defaultdict


def groupAnagrams(strs):
    d = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        d[key].append(word)
    return list(d.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = ["", ""]
ans = groupAnagrams(strs)
print(ans)
