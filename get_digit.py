import math


def get_digit_in_number(number, base_of_number):
    """
    return number of digit in given base
    """
    ans = math.floor(math.log(number, base_of_number))+1
    return ans


print(get_digit_in_number(7, 2))