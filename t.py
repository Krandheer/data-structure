def check_sorted(arr, i):
    if i == len(arr):
        return True
    return arr[i] >= arr[i - 1] and check_sorted(arr, i + 1)


def linear_search(arr, i, target):
    if i == len(arr):
        return -1
    if arr[i] == target:
        return i
    return linear_search(arr, i + 1, target)


def linear_search2(arr, i, target):
    ans = []
    if i == len(arr):
        return ans
    if arr[i] == target:
        ans.append(i)
    temp = linear_search2(arr, i + 1, target)
    ans += temp
    return ans


def linear_search3(arr, i, target, ans):
    if i == len(arr):
        return ans
    if arr[i] == target:
        ans.append(i)
    return linear_search3(arr, i + 1, target, ans)


arr1 = [1, 2, 4, 4, 11, 9, 12]
# ans = check_sorted(arr, 1)
# ans = linear_search(arr, 0, 11)s
# ans = linear_search2(arr, 0, 4)
# ans = linear_search3(arr, 0, 4, [])
# print(ans)


def pattern(r, c):
    if not r:
        return

    if c < r:
        print("*", end=" ")
        pattern(r, c + 1)
    else:
        print()
        pattern(r - 1, 0)


# pattern(4, 0)


def pattern2(r, c):
    if not r:
        return

    if c < r:
        pattern2(r, c + 1)
        print("*", end=" ")
    else:
        pattern2(r - 1, 0)
        print()


# pattern2(4, 0)


def skip_char(up, to_skip):
    ans = ""
    if not up:
        return ans

    # take case
    ch = up[0]
    if ch != to_skip:
        ans = ans + ch
        temp = skip_char(up[1:], to_skip)
        ans = ans + temp
        return ans
    return skip_char(up[1:], to_skip)


# print(skip_char("bcacabd", "a"))


def skip_char2(p, up, to_skip):
    if not up:
        return p

    # take case
    ch = up[0]

    # not take case
    if ch != to_skip:
        return skip_char2(p + ch, up[1:], to_skip)
    return skip_char2(p, up[1:], to_skip)


print(skip_char2("", "bcacabd", "a"))
