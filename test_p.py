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


def fun(x, y):
    if x == 0:
        return y
    else:
        return fun(x - 1, x + y)


print(fun(5, 2))
