"""
given a matrix, find its transpose without using inbuilt python function
i_q
"""


def transpose(matrix):
    transpose_mat = [[], [], []]
    for i in matrix:
        for j, k in enumerate(i):
            transpose_mat[j].append(k)
    return transpose_mat


matrix_input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix_input))
