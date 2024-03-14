from typing import List


def kids_with_candies(candies: List[int], extra_candies: int) -> List[bool]:
    """There are n kids with candies. You are given an integer array candies,
    where each candies[i] represents the number of candies the ith kid has,
    and an integer extraCandies, denoting the number of extra candies that you have.
    Return a boolean array result of length n, where result[i] is true if,
    after giving the ith kid all the extraCandies, they will have the greatest number
    of candies among all the kids, or false otherwise.

    Note that multiple kids can have the greatest number of candies.
    """
    maxi = max(candies)
    temp = [False] * len(candies)
    for index, n in enumerate(candies):
        if n + extra_candies >= maxi:
            temp[index] = True
    return temp
