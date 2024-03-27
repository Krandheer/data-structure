from typing import List


def max_len(arr: List[str]):
    """
    Given an array of strings arr[] of length n representing non-negative integers,
    arrange them in a manner such that, after concatenating them in order,
    it results in the largest possible number. Since the result may be very large,
    return it as a string.
    Example 1:
    input =  []"3", "30", "34", "5", "9"]
    Output: "9534330"
    """
    # find the length of largest string in arr
    # make all of the string of same length
    # do the mapping of original string as value and this new arr as key
    # sort of basis of this key
    # and then combine using the values of hashset
    max_str = 0
    for i in arr:
        if len(i) > max_str:
            max_str = len(i)
    temp = []
    for i in arr:
        if len(i) < max_str:
            temp.append(i + str((max_str - len(i)) * 0))
        else:
            temp.append(i)
    hash_set = dict(zip(arr, temp))
    hash_set = {
        k: v for k, v in sorted(hash_set.items(), key=lambda x: x[1], reverse=True)
    }
    ans = ""
    for k in hash_set.keys():
        ans += k
    return ans


input_arr = ["3", "30", "34", "5", "9"]
print(max_len(input_arr))
