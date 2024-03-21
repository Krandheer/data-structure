from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    https://leetcode.com/problems/merge-intervals/editorial/
    """
    if len(intervals) <= 1:
        return intervals
    intervals = sorted(intervals)
    temp = [intervals[0]]
    for i in range(1, len(intervals)):
        x, y = temp.pop()
        u, v = intervals[i]
        if x <= u <= y:
            if v >= y:
                temp.append([x, v])
            else:
                temp.append([x, y])
        else:
            temp.append([x, y])
            temp.append([u, v])
    return temp


# interval = [[1, 3], [2, 6], [8, 10], [15, 18]]
interval = [[1, 4], [0, 2], [3, 5]]
print(merge(interval))
