# Given an array of size N-1 such that it only contains distinct
# integers in the range of 1 to N. Find the missing element.
# N = 5
# A[] = {1,2,3,5}
# Output: 4

from collections import Counter
import asyncio


def get_missing(N, arr):
    for i in range(1, N + 1):
        if i in arr:
            continue
        else:
            return i
    return -1


def get_missing2(N, arr):
    total_sum = (N * (N + 1)) / 2
    arr_sum = sum(arr)
    return int(total_sum - arr_sum)


def get_missing3(N, arr):
    d = Counter(arr)
    for i in range(1, N + 1):
        if i not in d.keys():
            return i


A = [1, 2, 3, 5]
N = 5


# print(get_missing2(N, A))
# print(get_missing3(N, A))
# print(get_missing(N, A))


# texting async and await things in python, implementation and learning
async def foo(text):
    print(text)
    await asyncio.sleep(1)


async def main():
    print("inside main")
    # task is like creating event loop as in javascript
    # what it does is that it lets main thread run fast and then execute
    task = asyncio.create_task(foo("randheer"))
    # if stop the main thread even for a bit then task takes over and
    # then till it is not complete thread is not given to main function
    # await asyncio.sleep(2)
    print("finished")


# asyncio.run(main())
def remove_vowels(str1):
    a = ""
    for i in str1:
        if i.lower() not in ["a", "e", "i", "o", "u"]:
            a += i
    return a


# str1 = "sunitaalagi"
# print(remove_vowels(str1))


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


sq = Square(2)
print(sq.area())
print(sq.perimeter())
