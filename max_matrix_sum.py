from collections import defaultdict
from typing import List


def max_matrix_sum(matrix: List[List[int]]) -> int:
    temp_count = 0
    mat_min = float("inf")
    temp_sum = 0
    for row in matrix:
        for n in row:
            temp_sum += abs(n)
            mat_min = min(mat_min, abs(n))
            if n < 0:
                temp_count +=1

    if temp_count & 1:
        temp_sum -= 2*mat_min
    return temp_sum


print(max_matrix_sum([[2,9,3],[5,4,-4],[1,7,1]]))
