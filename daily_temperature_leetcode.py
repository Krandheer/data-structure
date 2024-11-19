from typing import List


def daily_temperature(temperatures: List[int]) -> List[int]:
    res = [0]*(len(temperatures))
    stack = []
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            temp, ind = stack.pop()
            res[ind]= i-ind
        stack.append((t, i))
    return res




print(daily_temperature([73,74,75,71,69,72,76,73]))
