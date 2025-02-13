from typing import List


def generate(numRows: int) -> List[List[int]]:
    pascal = [[1]]
    if numRows == 2:
        pascal.append([1, 1])
    if numRows > 2:
        pascal.append([1, 1])
        for i in range(1, numRows - 1):
            temp = [1]
            for j in range(len(pascal[i]) - 1):
                temp.append(pascal[i][j] + pascal[i][j + 1])
            temp.append(1)
            pascal.append(temp)
    return pascal
