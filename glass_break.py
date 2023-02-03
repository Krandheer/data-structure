"""
script takes input as number of floor and floor number from which glass ball will break if thrown down,
and it returns the floor number if glass will break from that floor else return None
using python bisect library which uses binary search
"""

import bisect


def glass_break_floor(floors, glass_breaking_point):
    i = bisect.bisect_left(floors, glass_breaking_point)
    if i != len(floors) and floors[i] == glass_breaking_point:
        return i
    return None


total_floor_no = 7015
total_floor = [i for i in range(total_floor_no)]
print(glass_break_floor(total_floor, 31))
print(glass_break_floor(total_floor, 8000))
