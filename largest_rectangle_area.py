from typing import List

"""
This problem uses the concept of Monotonic Stack to find the largest rectangle area in a histogram.
The idea is to maintain a stack that keeps track of the indices of the histogram bars in increasing
order of their heights. When we encounter a bar that is shorter than the bar at the index stored at the top of the stack,
we pop the stack and calculate the area of the rectangle that can be formed with the popped bar as the shortest bar.
"""


def largestRectangleArea(heights: List[int]) -> int:
    heights.append(0)
    # this stack will help in finding the lowest height in
    # right and left of current height
    stack = []
    ans = 0
    for ind, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
            curr_h = heights[stack.pop()]
            w = ind
            if stack:
                w = w - stack[-1] - 1
            ans = max(ans, w * curr_h)
        stack.append(ind)
    return ans


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
