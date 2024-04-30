def get_permutations(p, up, ans):
    if up == "":
        ans.append(p)
        return ans
    ch = up[0]
    for i in range(len(p) + 1):
        get_permutations(p[0:i] + ch + p[i:], up[1:], ans)
    return ans


# print(get_permutations("", 'abc', []))


def get_permutations2(p, up):
    if up == "":
        print(p)
        return
    ch = up[0]
    for i in range(len(p) + 1):
        get_permutations2(p[0:i] + ch + p[i:], up[1:])


# print(get_permutations2("", 'abc'))


def get_permutations3(p, up):
    if up == "":
        return [p]
    ch = up[0]
    ans = []
    for i in range(len(p) + 1):
        ans += get_permutations3(p[0:i] + ch + p[i:], up[1:])
    return ans


print(get_permutations3("", "abc"))
