def trap(height) -> int:
    left = [-1] * len(height)
    right = [-1] * len(height)
    left_max = height[0]
    right_max = height[-1]
    ans = 0
    for index, num in enumerate(height):
        left_max = max(left_max, num)
        left[index] = left_max

    for i in range(len(height) - 1, -1, -1):
        right_max = max(right_max, height[i])
        right[i] = right_max

    for i in range(len(height)):
        ans += min(left[i], right[i]) - height[i]
    return ans


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
