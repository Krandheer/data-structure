from typing import List


def process(i, j, temp, code, ans, is_negative):
    n = len(code)
    m = 1
    while m < n:
        temp -= code[i]
        if is_negative:
            j += 1
        if j >= n:
            j = j % n
        temp += code[j]
        ans[m] = temp
        i += 1
        if not is_negative:
            j += 1
        m += 1
    return ans


def decrypt(code: List[int], k: int) -> List[int]:
    n = len(code)
    ans = [0] * n
    if k == 0:
        return ans
    if k > 0:
        i, j = 1, k + 1
        temp = sum(code[i:j])
        ans[0] = temp
        ans = process(i, j, temp, code, ans, False)
    if k < 0:
        i, j = -1, k
        temp = sum(code[j:])
        ans[0] = temp
        ans = process(j, i, temp, code, ans, True)

    return ans


print(decrypt([2, 4, 9, 3], -2))
