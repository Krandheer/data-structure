from collections import deque
from typing import List


def shortest_subarray(nums: List[int], k: int) -> int:
    n = len(nums)
    pre = [0] * (n + 1)
    q = deque()
    min_len = n + 1
    for i in range(n):
        pre[i + 1] = pre[i] + nums[i]

    for i in range(n + 1):
        while q and pre[i] - pre[q[0]] >= k:
            min_len = min(min_len, i - q.popleft())

        while q and pre[i] <= pre[q[-1]]:
            q.pop()
        q.append(i)
    return min_len if min_len <= n else -1


print(shortest_subarray([84, -37, 32, 40, 95], 167))
