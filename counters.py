from collections import Counter
import numpy as np
from numpy import random

"""
#testing counter working
test = "randheer is good guy"
hash_map = Counter(test)
hash_map.pop(" ")
print(hash_map)"""

"""
#creating numpy array
arr = np.array([[1, 2], [3, 4]])
arr2 = np.array((1, 2, 3))
"""

"""print(arr.T)
print(arr)
print(arr.reshape(-1))"""

"""
#array traversal classical way
for x in arr:
    for y in x:
        print(y)
"""

"""
#array traversal numpy way
for x in np.nditer(arr):
    print(x)
"""

"""
#numpy array sorting
arr3 = np.array([0, 11, 2, 4, 6, 7, 8, 9])
print(np.sort(arr3))
"""

"""
#creating numpy array using random method
arr = random.randint(100, size=5)
arr2 = random.randint(100, size=(4,3))
print(arr2)
"""
