def max_integer(banned, n, maxSum):
    visited = set()
    for elem in banned:
        visited.add(elem)

    temp = 0
    count = 0
    for i in range(1, n + 1):
        if i not in visited and temp + i <= maxSum:
            temp += i
            count += 1
        elif temp + i > maxSum:
            break
    return count


print(max_integer([1, 6, 5], 5, 6))
