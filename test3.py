# Given an array of size N-1 such that it only contains distinct
# integers in the range of 1 to N. Find the missing element.
# N = 5
# A[] = {1,2,3,5}
# Output: 4

from collections import Counter
import asyncio
import time


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


# sq = Square(2)
# print(sq.area())
# print(sq.perimeter())

import asyncio


async def main():
    print("start")

    async def callback():
        print("callback")

    # Schedule the callback to be called after 5 seconds
    await asyncio.sleep(5)
    await callback()

    print("end")


# Run the event loop
# asyncio.run(main())

import asyncio


async def task_one():
    print("Task One: Start")
    await asyncio.sleep(3)  # Simulate an I/O operation
    i = 0
    for i in range(100000000):
        i = i + 1
    print(i)
    print("Task One: End")


async def task_two():
    print("Task Two: Start")
    await asyncio.sleep(3)  # Simulate another I/O operation
    print("Task Two: End")


async def main():
    # Start both tasks concurrently
    task1 = asyncio.create_task(task_one())
    task2 = asyncio.create_task(task_two())

    # Add another coroutine that doesn't involve I/O
    async def non_io_task():
        print("Non-I/O Task: Start")
        await asyncio.sleep(3)
        print("Non-I/O Task: End")

    # Schedule the non-I/O task to run concurrently
    task3 = asyncio.create_task(non_io_task())

    # Wait for all tasks to complete
    await asyncio.gather(task1, task2, task3)


# Run the event loop
# asyncio.run(main())
