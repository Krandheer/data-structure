from collections import deque

"""
leetcode: 239
You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.
"""


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    dq = deque()
    ans = []
    for ind, num in enumerate(nums):
        if dq:
            # make sure that we are holding element of valid window
            while dq and dq[0] <= ind - k:
                dq.popleft()
            # keep deque in monotonic decreasing order
            while dq and nums[dq[-1]] < num:
                dq.pop()
        dq.append(ind)

        # if valid window exist start taking elements from it for answer
        if ind >= k - 1:
            ans.append(nums[dq[0]])

    return ans
