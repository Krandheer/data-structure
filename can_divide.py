import math
from typing import List


def minimum_size(nums: List[int], max_operations: int) -> int:
    def can_distribute(m):
        ops = 0
        for num in nums:
            ops += math.ceil(num / m) - 1
            if ops > max_operations:
                return False
        return True

    left = 1
    right = max(nums)
    while left <= right:
        mid = (left + right) // 2
        # this basically tells if all elements can be made less than or equal to this.
        if can_distribute(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


print(minimum_size([9], 2))
