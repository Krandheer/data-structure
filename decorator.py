# import itertools


# for i in dir(itertools):
#     if not (i.startswith("__") or i.startswith("_")):
#         print(i)

# arr = [
#     1,
#     2,
#     3,
#     4,
# ]
# print(arr.index(3))
# print(arr.count(3))

from collections import defaultdict

# to use defaultdict behaviour need to pass the value type as
# argument otherwise it will throw error for unknow key
d = defaultdict(int)

from itertools import product

a = [1, 2, 3]
b = [3, 4]

# gives cartesian product of a and b
prod = product(a, b)

# for i in prod:
#     print(i)
# per = itertools.permutations(a)

# while handling the json in pthon i can pass indent = 4 arguments
# for better indentation, loads and dumps works in place, load and dupm work on file

# import secrets

# print(secrets.randbelow(10))
# print(secrets.token_hex())


## decorators are used to extend the functionality of the function on which it is used.


def start_end_decorator(func):
    def wrapper():
        print("start of function")
        func()
        print("end of function")

    return wrapper


@start_end_decorator
def print_name():
    print("randheer")


print_name()
