"""
you are given list of coordinates as list of list and number of restaurant to be returned as input
return the nearest restaurant to the customer.
!!! Amazon coding screening question !!!
"""


def findRestaurants(allLocations, numRestaurants):
    # Write your code here
    if allLocations is None or numRestaurants is None:
        return [[]]
    result = []
    for j in range(numRestaurants):
        d_min = (allLocations[0][0]) ** 2 + (allLocations[0][1]) ** 2
        temp = 0
        for i in range(len(allLocations)):
            if d_min > (allLocations[i][0]) ** 2 + (allLocations[i][1]) ** 2:
                d_min = (allLocations[i][0]) ** 2 + (allLocations[i][1]) ** 2
                temp = i
        result.append(allLocations[temp])
        allLocations.remove(allLocations[temp])
    return result


print(findRestaurants([[1, 2], [3, 4], [1, -1]], 2))
