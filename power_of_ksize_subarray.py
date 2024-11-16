from typing import List


def results_array(nums: List[int], k: int) -> List[int]:
    i = 0
    j = k-1
    ans = []

    while j < len(nums):
        window = nums[i:j+1]
        is_strictly_increasing = True
        for x in range(1, len(window)):
            if window[x] != window[x-1] + 1:
                is_strictly_increasing = False
                break
        if is_strictly_increasing:
            ans.append(window[-1])
            i += 1
            j += 1
        else:
            ans.append(-1)
            i += 1
            j += 1
    return ans
