from typing import List


# clock wise reversal:
# first reverse whole arr, then part of them
# anticlock wise reversal:
# first reverse part of them, then whole of the array
def rotate(nums: List[int], k: int) -> None:
    def reverse(l, r) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    n = len(nums)
    k = k % n

    l, r = 0, n - 1
    reverse(l, r)

    l, r = 0, k - 1
    reverse(l, r)

    l, r = k, n - 1
    reverse(l, r)


arr = [1, 2, 3, 4, 5, 6, 7]
rotate(arr, 3)
print(arr)
