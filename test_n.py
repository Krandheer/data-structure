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
    # make all the string of same length
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
    hash_set = dict(sorted(hash_set.items(), key=lambda x: x[1], reverse=True))
    ans = "".join(hash_set.keys())
    return ans


# input_arr = ["3", "30", "34", "5", "9"]
# print(max_len(input_arr))
def display_sorted_books(books_id, overdue_id):
    found = False
    def helper(temp_id):
        if temp_id in overdue_id:
            nonlocal found
            found = True
            return 0, temp_id
        return 1,temp_id
    books_id.sort(key=helper)
    return found

book_ids = [1,2,3,4,5,6,7,9]
overdue_ids = [1,3]
result = display_sorted_books(book_ids, overdue_ids)
print(result)
