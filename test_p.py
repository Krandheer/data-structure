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


def factorial(n, a=1):
    if n <= 1:
        return a
    else:
        return factorial(n - 1, a * n)



print(factorial(5))
