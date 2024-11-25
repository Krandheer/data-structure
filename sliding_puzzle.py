from collections import deque
from typing import List


def sliding_puzzle(self, board: List[List[int]]) -> int:
    """
    On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0.
    A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
    The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
    Given the puzzle board, return the least number of moves required so that the state of the board is solved.
    If it is impossible for the state of the board to be solved, return -1.
    """
    start = "".join([str(c) for row in board for c in row])
    visited = set()
    visited.add(start)
    queue = deque([(start.index('0'), start, 0)])
    adj_list = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4],
        4: [1, 3, 5],
        5: [4, 2]
    }
    ans = '123450'

    while queue:
        zero, state, level = queue.popleft()
        if state == ans:
            return level
        state_l = list(state)
        for i in adj_list[zero]:
            new_arr = state_l.copy()
            new_arr[i], new_arr[zero] = state_l[zero], state_l[i]
            new_arr_s = "".join(new_arr)
            if new_arr_s not in visited:
                visited.add(new_arr_s)
                queue.append((new_arr_s.index('0'), new_arr_s, level + 1))
    return -1
