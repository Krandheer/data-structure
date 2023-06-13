# import collections
#
# Card = collections.namedtuple('Card', ['rank', 'suit'])
#
#
# class FrenchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()
#
#     def __init__(self):
#         self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, position): return self._cards[position]
#
#
# a = FrenchDeck()
# print(len(a))

"""
a variable defined outside the scope of function can be accessed inside the function but can't be modified without
 declaring it as global inside the function you trying to modifying it.
"""


def fun(x, y):
    if x == 0:
        return y
    else:
        return fun(x - 1, x + y)


# print(fun(5, 2))


# import asyncio
#
#
# async def your_coroutine(delay_in_seconds):
#     print(f'This coroutine will pause for {delay_in_seconds} seconds')
#     await asyncio.sleep(delay_in_seconds)
#     print(f'Finished awaiting {delay_in_seconds} seconds')
#
#
# async def main():
#     await asyncio.gather(*[your_coroutine(i) for i in range(5)])
#
#
# asyncio.run(main())

def isValid(s):
    # code here
    ipv4 = s.split(".")
    is_ok = True
    temp = 0

    if len(ipv4) == 4:
        for i in ipv4:
            if int(i) == 0:
                temp = temp + 1
            if temp == 4:
                is_ok = False
            if not is_ok:
                return 0
            if not (0 <= int(i) <= 255):
                return 0
    return 1


print(isValid("0.0.0.0"))
