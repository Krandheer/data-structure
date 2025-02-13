from typing import List


def find_champion(n: int, edges: List[List[int]]) -> int:
    """leetcode 2924"""
    incoming = [0] * n
    for _, d in edges:
        incoming[d] += 1

    max_winners = []
    for i, v in enumerate(incoming):
        if v == 0:
            max_winners.append(i)

    if len(max_winners) > 1:
        return -1
    return max_winners[0]
