def pascle_triangle(num):
    rows = [[0] * (i + 1) for i in range(num)]
    for i in range(0, num):
        rows[i][0] = rows[i][i] = 1
        for j in range(1, i):
            rows[i][j] = rows[i - 1][j - 1] + rows[i - 1][j]
    return rows


print(pascle_triangle(5))


def nth_row_pascle_triangle(n_row):
    # 4^C_0->n
    row = [0] * (n_row + 1)
    row[0] = row[-1] = 1
    denom = 1
    numer = 1
    for i in range(0, n_row - 1):
        numer *= n_row - i
        denom *= i + 1
        row[i + 1] = int(numer / denom)
    return row


print(nth_row_pascle_triangle(4))
