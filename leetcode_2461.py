from typing import List


def maximum_subarray_sum(nums: List[int], k: int) -> int:
    n = len(nums)
    elements = set()
    current_sum = 0
    max_sum = 0
    l, r = 0, 0

    while r < n:
        if nums[r] not in elements:
            current_sum += nums[r]
            elements.add(nums[r])

            if r - l + 1 == k:
                if current_sum > max_sum:
                    max_sum = current_sum

                current_sum -= nums[l]
                elements.remove(nums[l])
                # shift window ahead
                l += 1
        # change window with latest duplicate value in window
        else:
            while nums[l] != nums[r]:
                current_sum -= nums[l]
                elements.remove(nums[l])
                l += 1
            l += 1
        r += 1

    return max_sum

print(maximum_subarray_sum([5,3,3,1,1], 3))
