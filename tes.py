# nums1 = [-5, 4]
# nums2 = [1, 7, 8, 9]


# def find_median(nums1, nums2):
#     temp = []
#     i = 0
#     j = 0
#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] < nums2[j]:
#             temp.append(nums1[i])
#             i += 1
#         else:
#             temp.append(nums2[j])
#             j += 1

#     if j < len(nums2):
#         temp = temp + nums2[j:]
#     elif i < len(nums1):
#         temp = temp + nums1[1:]
#     return temp


# print(find_median(nums1, nums2)


# class Order:
#     def __init__(self) -> None:
#         self.order_item = {}
#         self.quantities = 0
#
#     def add_itmes(self, item, quantity, price):
#         self.quantities += quantity
#         self.order_item[item] = (quantity, price)
#
#     def total_price(self):
#         tot_pr = 0
#         for _, v in self.order_item.items():
#             tot_pr += v[1]
#         return tot_pr
#
#
# order = Order()
# order.add_itmes("keyboard", 21, 50)
# order.add_itmes("mouse", 20, 40)
# print(order.order_item)
# print(order.quantities)
# print(order.total_price())


# Given a string containing only three types of characters: '(', ')', and '*',
# write a function check_valid_string(s) that checks whether the input string is valid.
# The input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# A '*' can be treated as a wildcard character, which can represent either an open bracket
# '(' or a closing bracket ')' or nothing as well.
# Write a function check_valid_string(s) that takes a string s and returns True
# if the string is valid, and False otherwise.


def check_valid_string(s: str) -> bool:
    stack = []
    if "*" not in s:
        for i in s:
            if i == "(":
                stack.append("(")
            elif i == ")" and stack:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        return False

    if len(s) % 2 != 0:
        if s[len(s) // 2] != "*":
            return False

    for i in range(len(s) // 2):
        stack.append(s[i])

    j = len(s) // 2 + 1
    ch_flag = True
    while stack and j < len(s):
        ch = stack.pop()
        if not (ch in ("(", "*") and s[j] in ("*", ")")):
            ch_flag = False

    return ch_flag


assert check_valid_string("()") is True
assert check_valid_string("(*)") is True
assert check_valid_string(")(") is False
assert check_valid_string("(*))") is True
assert check_valid_string("(((**)") is True
