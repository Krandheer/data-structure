from typing import List


def max_str_len(arr: List[str]):
    """
    Given an array of strings arr[] of length n representing non-negative integers,
    arrange them in a manner such that, after concatenating them in order,
    it results in the largest possible number. Since the result may be very large,
    return it as a string.
    Example 1:
    Input
    n = 5
    arr[] =  {"3", "30", "34", "5", "9"}   9534330
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
            max_str = int(i)
    temp = []
    for i in arr:
        if len(i) < max_str:
            temp.append(i + str((max_str - len(i)) * 0))
        else:
            temp.append(i)

    return temp


input_arr = ["3", "30", "34", "5", "9"]
print(max_str_len(input_arr))
