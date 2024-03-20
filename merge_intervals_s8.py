from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    https://leetcode.com/problems/merge-intervals/editorial/
    """
    if len(intervals) == 1:
        return intervals
    temp = []
    for i in range(len(intervals) - 1):
        x, y = intervals[i]
        u, v = intervals[i + 1]
        if x <= u <= y and v >= y:
            temp.append([x, v])
        else:
            temp.append([u, v])
    return temp
