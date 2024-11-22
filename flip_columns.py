from collections import defaultdict


def flip_columns(matrix):
    count = defaultdict(int)
    for row in matrix:
        if row[0]!=0:
            row = [0 if n else 1 for n in row]
        count[tuple(row)]+=1
    return max(count.values())


print(flip_columns([[0,1],[1,0]]))
