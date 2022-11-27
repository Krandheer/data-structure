def ways_to_climb_stairs(p, target, ans):
    dict1 = {}
    for i in range(11):
        dict1[i] = 0
    if target == 0:
        ans.append(p)
        return
    ways_to_climb_stairs(p + str(1), target - 1, ans)
    if target >= 2:
        ways_to_climb_stairs(p + str(2), target - 2, ans)
    if target >= 3:
        ways_to_climb_stairs(p + str(3), target - 3, ans)
    return len(ans)


def ways_to_climb_stairs2(p, target):
    if target == 0:
        ans = [p]
        return ans

    ans1 = ways_to_climb_stairs2(p + str(1), target - 1)
    ans2 = []
    ans3 = []
    if target >= 2:
        ans2 = ways_to_climb_stairs2(p + str(2), target - 2)

    if target >= 3:
        ans3 = ways_to_climb_stairs2(p + str(3), target - 3)
    result = ans1 + ans2 + ans3
    return result


print(len(ways_to_climb_stairs2('', 10)))


def swap(arr):
    arr1 = []
    for i in range(len(arr) - 1, -1, -1):
        arr1.append(arr[i])
    return arr1


# print(swap([1, 1, 0, 0, 1]))

def horizontal_flip(mat):
    mat1 = []
    mat2 = []
    for row in mat:
        mat2.append([])
    for row in mat:
        temp = swap(row)
        mat1.append(temp)
    for index, row in enumerate(mat1):
        for i in row:
            if i == 0:
                i = 1
                mat2[index].append(i)
            elif i == 1:
                i = 0
                mat2[index].append(i)
    return mat2

# img = [[1, 1, 0, 0, 1],
#        [0, 0, 1, 0, 1],
#        [1, 1, 1, 0, 1]]
# print(horizontal_flip(img))

# img2 = [[1, 1, 0],
#         [1, 1, 1],
#         [0, 0, 1],
#         [1, 0, 1]]
# print(horizontal_flip(img2))
