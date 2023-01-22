import pandas as pd

df = pd.DataFrame({"name": ["satish", 'arj' 'rahul', 'randheer', 'naman', 'sunita']})

name = df[df['name'].str[0] == 'r']
print(name)


def matmul(mat1, mat2):
    mat3 = [[], []]
    for index, j in enumerate(mat1):
        temp1 = 0
        temp2 = 0
        for index2, k in enumerate(j):
            for index3, l in enumerate(mat2):
                if index2 == index3:
                    temp1 = temp1 + k * l[0]
                    temp2 = temp2 + k * l[1]
        mat3[index].append(temp1)
        mat3[index].append(temp2)

    return mat3


mat1 = [[1, 2],
        [3, 4]]
mat2 = [[4, 5],
        [6, 7]]

print(matmul(mat1, mat2))
