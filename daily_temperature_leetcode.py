from typing import List


def daily_temperature(temperatures: List[int]) -> List[int]:
    res = [0] * (len(temperatures))
    stack = []
    for ind, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            _, i = stack.pop()
            res[ind] = ind - i
        stack.append((temp, ind))
    return res


print(daily_temperature([73, 74, 75, 71, 69, 72, 76, 73]))
