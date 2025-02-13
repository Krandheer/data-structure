# minimum insertion needed to convert given string to palindrome
def minimum_insertion_to_palindrome(index, ipt):
    def helper(index1, index2, ipt, ipt2):
        if index1 < 0 or index2 < 0:
            return 0
        if ipt[index1] == ipt2[index2]:
            return 1 + helper(index1 - 1, index2 - 1, ipt, ipt2)
        else:
            return max(
                helper(index1 - 1, index2, ipt, ipt2),
                helper(index1, index2 - 1, ipt, ipt2),
            )

    if ipt[::-1] == ipt:
        return 0
    ipt2 = ipt[::-1]
    helper_result = helper(index, index, ipt, ipt2)
    return len(ipt) - helper_result


ipt = "abcaa"
print(minimum_insertion_to_palindrome(len(ipt) - 1, ipt))
