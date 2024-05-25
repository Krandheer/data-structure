def maxArea(height) -> int:
    i, j = 0, len(height) - 1
    maxi = 0

    while i <= j:
        temp = (j - i) * min(height[i], height[j])
        maxi = max(temp, maxi)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return maxi


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
ans = maxArea(height)
print(ans)
