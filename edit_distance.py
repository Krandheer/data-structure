ipt1 = "randheer"
ipt2 = "kumar"


def compare_string(index1, index2, string1, string2):
    if index1 <= 0:
        return index2 + 1
    if index2 <= 0:
        return index1 + 1
    if index1 <= 0 and index2 <= 0:
        return 0
    if string1[index1] == string2[index2]:
        index1 = index1 - 1
        index2 = index2 - 1

    return 1 + min(
        compare_string(index1 - 1, index2 - 1, string1, string2),
        compare_string(index1 - 1, index2, string1, string2),
        compare_string(index1, index2 - 1, string1, string2),
    )


print(compare_string(len(ipt1) - 1, len(ipt2) - 1, ipt1, ipt2))
